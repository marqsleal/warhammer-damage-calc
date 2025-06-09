"""
Módulo utilitário para validação de dicionários de entrada (JSON) utilizados no cálculo de dano do Warhammer 40k.

Fornece a classe JsonValidator, que garante a presença de todos os campos obrigatórios, 
a tipagem correta (inteiros) e a validade dos valores (incluindo campos binários e valores de D6) 
para os atributos de atacante e defensor.

Exemplo de uso:
    from json_validator import JsonValidator

    JsonValidator.validate_attacker(attacker_kwargs)
    JsonValidator.validate_defender(defender_kwargs)
"""
class JsonValidator:
    """
    Classe utilitária para validar dicionários de entrada (JSON) usados no cálculo de dano Warhammer 40k.
    Garante que todos os campos obrigatórios estejam presentes e que os valores estejam dentro dos limites esperados.
    """
    REQUIRED_ATTACKER_FIELDS = [
        "ATTACK",
        "SKILL",
        "STRENGTH",
        "ARMOR_PENETRATION",
        "FLAT_DAMAGE",
        "D3_DAMAGE",
        "D6_DAMAGE",
        "BLAST",
        "HEAVY",
        "LETHAL_HITS",
        "SUSTAINED_HITS",
        "TWIN_LINKED",
        "REROLL_TO_HIT",
        "REROLL_TO_WOUND"
    ]


    REQUIRED_DEFENDER_FIELDS = [
        "TOUGHNESS",
        "ARMOR_SAVE",
        "N_MODELS",
        "INVULNERABLE_SAVE",
        "FEEL_NO_PAIN"
    ]


    BINARY_ATTACKER_FIELDS = [
        "BLAST",
        "HEAVY",
        "LETHAL_HITS",
        "TWIN_LINKED",
        "REROLL_TO_HIT",
        "REROLL_TO_WOUND"
    ]


    D6_DEFENDER_FIELDS = [
        "ARMOR_SAVE",
        "INVULNERABLE_SAVE",
        "FEEL_NO_PAIN"
    ]


    @staticmethod
    def validate_attacker(data: dict) -> None:
        """
        Valida o dicionário de atributos do atacante para o cálculo de dano.

        Verifica se todos os campos obrigatórios estão presentes, se todos os valores são inteiros
        e se os campos binários possuem apenas os valores 0 ou 1.

        Args:
            data (dict): Dicionário contendo os atributos do atacante.

        Raises:
            ValueError: Se faltar algum campo obrigatório ou se algum campo binário não for 0 ou 1.
            TypeError: Se algum campo obrigatório não for inteiro.
        """
        missing = [field for field in JsonValidator.REQUIRED_ATTACKER_FIELDS if field not in data]
        if missing:
            raise ValueError(f"Campos obrigatórios ausentes no atacante: {missing}")
        not_int = [field for field in JsonValidator.REQUIRED_ATTACKER_FIELDS if not isinstance(data[field], int)]
        if not_int:
            raise TypeError(f"Os seguintes campos do atacante não são inteiros: {not_int}")
        not_binary = [
            field for field in JsonValidator.BINARY_ATTACKER_FIELDS
            if data[field] not in (0, 1)
        ]
        if not_binary:
            raise ValueError(f"Os seguintes campos do atacante devem ser 0 ou 1: {not_binary}")


    @staticmethod
    def validate_defender(data: dict) -> None:
        """
        Valida o dicionário de atributos do defensor para o cálculo de dano.

        Verifica se todos os campos obrigatórios estão presentes, se todos os valores são inteiros
        e se os campos relacionados a D6 possuem valores entre 1 e 6.

        Args:
            data (dict): Dicionário contendo os atributos do defensor.

        Raises:
            ValueError: Se faltar algum campo obrigatório ou se algum campo D6 não estiver entre 1 e 6.
            TypeError: Se algum campo obrigatório não for inteiro.
        """
        missing = [field for field in JsonValidator.REQUIRED_DEFENDER_FIELDS if field not in data]
        if missing:
            raise ValueError(f"Campos obrigatórios ausentes no defensor: {missing}")
        not_int = [field for field in JsonValidator.REQUIRED_DEFENDER_FIELDS if not isinstance(data[field], int)]
        if not_int:
            raise TypeError(f"Os seguintes campos do defensor não são inteiros: {not_int}")
        not_d6 = [
            field for field in JsonValidator.D6_DEFENDER_FIELDS
            if not (0 <= data[field] <= 6)
        ]
        if not_d6:
            raise ValueError(f"Os seguintes campos do defensor devem estar entre 0 e 6: {not_d6}")