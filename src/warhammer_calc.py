"""
Módulo de cálculo de dano médio para Warhammer 40k.

Fornece a classe WarHammerCalc, que executa todas as etapas do cálculo de dano esperado,
incluindo acerto, ferida, salvaguarda e redução de dano, além de simular regras especiais.
"""
DICE_SIDES = 6
DICE_MAX = DICE_SIDES + 1

class WarHammerCalc:
    """
    Classe responsável por calcular o dano médio esperado em ataques de Warhammer 40k,
    considerando todas as etapas do processo: acerto (hit), ferida (wound), salvaguarda (save)
    e redução de dano (Feel No Pain).

    Permite simular as principais regras do sistema, como rerolls, Sustained Hits, Lethal Hits,
    Blast, Twin-Linked, modificadores de armadura, saves invulneráveis e dados de dano variáveis (D3, D6).

    Os parâmetros de atacante e defensor devem ser fornecidos como dicionários, permitindo flexibilidade
    para diferentes perfis de unidades e armas.

    Métodos principais:
        - calc_hit_roll: Calcula acertos médios.
        - calc_wound_roll: Calcula feridas médias.
        - calc_save_roll: Calcula saves falhos médios.
        - calc_damage: Calcula dano médio final.
        - run_calc: Executa toda a sequência e retorna um resumo dos resultados.

    Exemplos de uso:
        attacker = {...}
        defender = {...}
        calc = WarHammerCalc(attacker, defender)
        resultado = calc.run_calc()
    """
    def __init__(
        self,
        attacker_kwargs: dict,
        defender_kwargs: dict
    ):
        self.attacker_kwargs = attacker_kwargs
        self.defender_kwargs = defender_kwargs
        self.hit_result = 0
        self.auto_wound = 0
        self.wound_result = 0
        self.save_result = 0
        self.damage_result = 0


    def roll_to_hit(
        self,
        skill: int,
        reroll_value: int
    ) -> float:
        """
        Calcula a probabilidade média de um ataque acertar (hit) em um D6, considerando rerolls.

        Args:
            skill (int): Valor mínimo necessário no dado para acertar (ex: 3 para 3+).
            reroll_value (int): Valor do dado que pode ser rerrolado (0 se não houver reroll).

        Returns:
            float: Probabilidade média de acerto para um ataque.
        """
        if skill <= 0:
            skill = 1
        p_success = (DICE_MAX - skill) / DICE_SIDES
        if reroll_value == 0:
            return p_success            
        p_reroll = reroll_value / DICE_SIDES
        return p_success + p_reroll * p_success


    def blast(
            self,
            blast: int,
            n_models: int
    ) -> int:
        """
        Calcula o bônus de ataques concedido pela regra Blast.

        Para cada 5 modelos na unidade alvo (arredondando para baixo), adiciona 1 ataque extra.
        Retorna 0 se o valor de blast for menor ou igual a zero.

        Args:
            blast (int): Valor indicando se a arma possui a regra Blast (>0 ativa o bônus).
            n_models (int): Número de modelos na unidade alvo.

        Returns:
            int: Número de ataques extras concedidos pela regra Blast.
        """
        if blast <= 0:
            return 0
        return n_models // 5


    def sustained_hits(
        self,
        attacks: int,
        add_hits: int
    ) -> float:
        """
        Calcula o número médio de ataques considerando a regra de Sustained Hits.

        Para cada ataque realizado, existe uma chance de gerar ataques adicionais (add_hits)
        caso um valor específico seja rolado no dado (normalmente 6+).

        Args:
            attacks (int): Número inicial de ataques.
            add_hits (int): Número de ataques extras gerados por cada sucesso de Sustained Hits.

        Returns:
            float: Número médio total de ataques após aplicar Sustained Hits.
        """
        p_success = (DICE_MAX - DICE_SIDES) / DICE_SIDES
        return attacks + (attacks * add_hits * p_success)


    def lethal_hits(
        self,
        attacks: int
    ) -> float:
        """
        Calcula o número médio de ataques que causam feridas automáticas (auto-wounds) devido à regra Lethal Hits.

        Para cada ataque realizado, existe uma chance de gerar uma ferida automática caso um valor específico
        seja rolado no dado (normalmente 6+).

        Args:
            attacks (int): Número de ataques realizados.

        Returns:
            float: Número médio de ataques que causam feridas automáticas após aplicar Lethal Hits.
        """
        p_success = (DICE_MAX - DICE_SIDES) / DICE_SIDES
        return attacks * p_success


    def get_wound_roll(
        self,
        strength: int,
        toughness: int
    ) -> int:
        """
        Determina o valor mínimo necessário no D6 para causar uma ferida (wound) com base na força do atacante e na resistência do defensor,
        seguindo as regras do Warhammer 40k.

        Args:
            strength (int): Força do ataque.
            toughness (int): Resistência do alvo.

        Returns:
            int: Valor mínimo no D6 necessário para causar uma ferida (2, 3, 4, 5 ou 6).
        """
        match True:
            case _ if strength >= 2 * toughness:
                return 2
            case _ if strength > toughness:
                return 3
            case _ if strength == toughness:
                return 4
            case _ if strength * 2 <= toughness:
                return 6
            case _:
                return 5


    def roll_to_wound(
        self,
        wound_roll: int,
        reroll_value: int
    ) -> float:
        """
        Calcula a probabilidade média de causar uma ferida (wound) em um D6, considerando rerolls.

        Args:
            wound_roll (int): Valor mínimo necessário no dado para causar a ferida (ex: 4 para 4+).
            reroll_value (int): Valor do dado que pode ser rerrolado (0 se não houver reroll).

        Returns:
            float: Probabilidade média de causar uma ferida para um ataque.
        """
        if wound_roll <= 0:
            wound_roll = 1
        p_success = (DICE_MAX - wound_roll) / DICE_SIDES
        if reroll_value == 0:
            return p_success
        p_reroll = reroll_value / DICE_SIDES
        return p_success + p_reroll * p_success


    def calc_damage_die(
        self,
        damage_dice: int,
        n_dice: int
    ) -> float:
        """
        Calcula o valor médio inteiro de dano para um tipo de dado (ex: D3, D6) multiplicado pela quantidade de dados.

        Args:
            damage_dice (int): Número de lados do dado de dano (ex: 3 para D3, 6 para D6).
            n_dice (int): Quantidade de dados a serem rolados.

        Returns:
            float: Valor médio total de dano causado pelos dados.
        """
        if n_dice <= 0:
            return 0
        result = ((1 + damage_dice) / 2) * n_dice
        return result


    def roll_to_save(
        self,
        save_roll: int
    ) -> float:
        """
        Calcula a probabilidade média de sucesso em um teste de salvaguarda (save) em um D6.

        Args:
            save_roll (int): Valor mínimo necessário no dado para passar no save (ex: 3 para 3+).

        Returns:
            float: Probabilidade média de sucesso no save.
        """
        if save_roll >= DICE_SIDES:
            save_roll = DICE_SIDES
        p_success = (DICE_MAX - save_roll) / DICE_SIDES
        return p_success


    def roll_to_feel_no_pain(
        self,
        result: float,
        feel_no_pain: int
    ) -> float:
        """
        Calcula o valor médio de dano restante após aplicar a regra de Feel No Pain.

        Args:
            result (float): Dano total antes do Feel No Pain.
            feel_no_pain (int): Valor mínimo necessário no dado para ignorar o dano (ex: 5 para 5+). Use 0 se não houver FNP.

        Returns:
            float: Dano médio restante após aplicar Feel No Pain.
        """
        if feel_no_pain > 0:
            result *= (1 - feel_no_pain / DICE_SIDES)
        return result


    def calc_hit_roll(self):
        """
        Calcula o número médio de ataques bem-sucedidos (hits) após considerar modificadores, rerolls,
        Sustained Hits e Lethal Hits.

        Utiliza os valores de ATTACK, BLAST, SKILL, HEAVY, REROLL_TO_HIT, SUSTAINED_HITS e LETHAL_HITS do atacante.
        Atualiza o atributo self.hit_result com o resultado e self.auto_wound se Lethal Hits for aplicado.

        Returns:
            self: A própria instância, permitindo encadeamento de métodos.
        """
        attacks = self.attacker_kwargs["ATTACK"] + (
            self.blast(
                self.attacker_kwargs["BLAST"],
                self.defender_kwargs["N_MODELS"]
            ) if self.attacker_kwargs["BLAST"] > 0 else 0
        )
        skill = (
            self.attacker_kwargs["SKILL"] - self.attacker_kwargs["HEAVY"]
        )
        reroll_value = self.attacker_kwargs["REROLL_TO_HIT"]
        if self.attacker_kwargs["SUSTAINED_HITS"] > 0:
            attacks = self.sustained_hits(
                attacks,
                self.attacker_kwargs["SUSTAINED_HITS"]
            )
        if self.attacker_kwargs["LETHAL_HITS"] > 0:
            self.auto_wound = self.lethal_hits(attacks)
        result = attacks * (
            self.roll_to_hit(
                skill,
                reroll_value
            )
        )
        self.hit_result = result
        return self


    def calc_wound_roll(self):
        """
        Calcula o número médio de feridas (wounds) causadas após considerar força, resistência, rerolls,
        habilidades especiais (como Twin-Linked) e feridas automáticas (auto-wounds).

        Utiliza os valores de STRENGTH, TOUGHNESS, REROLL_TO_WOUND, TWIN_LINKED e auto_wound.
        Atualiza o atributo self.wound_result com o resultado.

        Returns:
            self: A própria instância, permitindo encadeamento de métodos.
        """
        strength = self.attacker_kwargs["STRENGTH"]
        toughness = self.defender_kwargs["TOUGHNESS"]
        wound_roll = self.get_wound_roll(
            strength,
            toughness
        )
        reroll_value = (
            wound_roll - 1
        ) if self.attacker_kwargs["TWIN_LINKED"] > 0 else self.attacker_kwargs["REROLL_TO_WOUND"]
        result = (
            self.hit_result * self.roll_to_wound(
                wound_roll,
                reroll_value
            )
        ) + self.auto_wound
        self.wound_result = result
        return self


    def calc_save_roll(self):
        """
        Calcula o número médio de feridas (wounds) que não foram salvas após considerar o valor de salvaguarda (save)
        e o save invulnerável do defensor.

        Utiliza os valores de ARMOR_SAVE, ARMOR_PENETRATION, INVULNERABLE_SAVE do defensor e atacante,
        além do resultado de wounds.

        Atualiza o atributo self.save_result com o resultado.

        Returns:
            self: A própria instância, permitindo encadeamento de métodos.
        """
        save_roll = self.defender_kwargs["ARMOR_SAVE"] + self.attacker_kwargs["ARMOR_PENETRATION"]
        invulnerable_save = self.defender_kwargs["INVULNERABLE_SAVE"]
        final_save = invulnerable_save if invulnerable_save < save_roll else save_roll
        p_fail = 1 - self.roll_to_save(final_save)
        result = p_fail * self.wound_result
        self.save_result = result
        return self


    def calc_damage(self):
        """
        Calcula o dano médio causado após considerar o dano base da arma, dados de dano (D3, D6)
        e a quantidade de feridas que passaram pelo save e pelo Feel No Pain.

        Utiliza os valores de FLAT_DAMAGE, D3_DAMAGE, D6_DAMAGE do atacante, além do resultado de wounds e saves.
        Aplica a redução de dano do Feel No Pain, se houver.

        Atualiza o atributo self.damage_result com o resultado.

        Returns:
            self: A própria instância, permitindo encadeamento de métodos.
        """
        damage = (
            self.attacker_kwargs["FLAT_DAMAGE"] +
            self.calc_damage_die(
                3,
                self.attacker_kwargs["D3_DAMAGE"]
            ) +
            self.calc_damage_die(
                6,
                self.attacker_kwargs["D6_DAMAGE"]
            )
        )
        result = (
            self.wound_result - self.save_result
        ) * damage
        result = self.roll_to_feel_no_pain(
            result,
            self.defender_kwargs["FEEL_NO_PAIN"]
        )
        self.damage_result = result
        return self


    def run_calc(self) -> dict:
        """
        Executa toda a sequência de cálculo de dano do Warhammer 40k, incluindo acerto (hit), ferida (wound),
        salvaguarda (save) e dano final, atualizando os atributos correspondentes.

        Chama internamente os métodos:
            - calc_hit_roll
            - calc_wound_roll
            - calc_save_roll
            - calc_damage

        Returns:
            dict: Um dicionário com os resultados médios de cada etapa do cálculo:
                - "hit_result": Número médio de acertos.
                - "wound_result": Número médio de feridas.
                - "save_result": Número médio de feridas salvas.
                - "damage_result": Dano médio final causado.
        """
        self.calc_hit_roll()
        self.calc_wound_roll()
        self.calc_save_roll()
        self.calc_damage()
        return {
            "hit_result": self.hit_result,
            "wound_result": self.wound_result,
            "save_result": self.save_result,
            "damage_result": self.damage_result
        }