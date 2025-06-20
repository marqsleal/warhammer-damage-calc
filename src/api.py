"""
API FastAPI para cálculo de dano médio em Warhammer 40k.

Este módulo expõe um endpoint `/calc` que recebe os atributos do atacante e do defensor,
valida os dados recebidos e retorna os resultados do cálculo de dano utilizando a classe WarHammerCalc.

Modelos Pydantic garantem a validação automática dos dados de entrada.
O módulo também utiliza JsonValidator para validações adicionais de regras de negócio.

Exemplo de uso:
    - Envie uma requisição POST para /calc com os dados do atacante e do defensor em JSON.
    - Receba como resposta um dicionário com os resultados do cálculo (hit_result, wound_result, save_result, damage_result).
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from warhammer_calc import WarHammerCalc # pylint: disable=import-error
from json_validator import JsonValidator # pylint: disable=import-error

app = FastAPI(title="Warhammer 40k Damage Calculator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AttackerModel(BaseModel):
    """
    Modelo Pydantic que representa os atributos necessários de um atacante para o cálculo de dano no Warhammer 40k.

    Todos os campos são inteiros e obrigatórios, correspondendo aos parâmetros esperados pelo WarHammerCalc e pelo validador.

    Campos:
        ATTACK (int): Número de ataques.
        SKILL (int): Valor de habilidade de acerto.
        STRENGTH (int): Força do ataque.
        ARMOR_PENETRATION (int): Penetração de armadura.
        FLAT_DAMAGE (int): Dano fixo por ataque.
        D3_DAMAGE (int): Quantidade de dados D3 de dano.
        D6_DAMAGE (int): Quantidade de dados D6 de dano.
        BLAST (int): Indica se a arma possui a regra Blast (0 ou 1).
        HEAVY (int): Indica se a arma possui a regra Heavy (0 ou 1).
        LETHAL_HITS (int): Indica se a arma possui a regra Lethal Hits (0 ou 1).
        SUSTAINED_HITS (int): Indica se a arma possui a regra Sustained Hits (0 ou 1).
        TWIN_LINKED (int): Indica se a arma possui a regra Twin-Linked (0 ou 1).
        REROLL_TO_HIT (int): Valor de reroll para acerto (0 ou 1).
        REROLL_TO_WOUND (int): Valor de reroll para ferida (0 ou 1).
    """
    ATTACK: int
    SKILL: int
    STRENGTH: int
    ARMOR_PENETRATION: int = 0
    FLAT_DAMAGE: int = 0
    D3_DAMAGE: int = 0
    D6_DAMAGE: int = 0
    BLAST: int = 0
    HEAVY: int = 0
    LETHAL_HITS: int = 0
    SUSTAINED_HITS: int = 0
    TWIN_LINKED: int = 0
    REROLL_TO_HIT: int = 0
    REROLL_TO_WOUND: int = 0

class DefenderModel(BaseModel):
    """
    Modelo Pydantic que representa os atributos necessários de um defensor para o cálculo de dano no Warhammer 40k.

    Todos os campos são inteiros e obrigatórios, correspondendo aos parâmetros esperados pelo WarHammerCalc e pelo validador.

    Campos:
        TOUGHNESS (int): Resistência do alvo.
        ARMOR_SAVE (int): Valor de salvaguarda de armadura.
        N_MODELS (int): Número de modelos na unidade alvo.
        INVULNERABLE_SAVE (int): Valor de salvaguarda invulnerável.
        FEEL_NO_PAIN (int): Valor de Feel No Pain (0 se não houver).
    """
    TOUGHNESS: int
    ARMOR_SAVE: int
    N_MODELS: int
    INVULNERABLE_SAVE: int = 0
    FEEL_NO_PAIN: int = 0

class CalcRequest(BaseModel):
    """
    Modelo Pydantic que representa o corpo da requisição para o endpoint de cálculo de dano.

    Contém dois campos obrigatórios:
        attacker (AttackerModel): Dados do atacante.
        defender (DefenderModel): Dados do defensor.

    Ambos os campos devem seguir os modelos definidos para atacante e defensor, garantindo a validação automática dos dados recebidos pela API.
    """
    attacker: AttackerModel
    defender: DefenderModel

@app.post("/calc")
async def calculate_damage(payload: CalcRequest):
    """
    Endpoint da API responsável por calcular o dano médio esperado em um ataque de Warhammer 40k.

    Recebe um corpo de requisição contendo os dados do atacante e do defensor, valida os dados recebidos,
    executa o cálculo de dano utilizando o WarHammerCalc e retorna os resultados.

    Args:
        payload (CalcRequest): Corpo da requisição contendo os atributos do atacante e do defensor.

    Returns:
        dict: Dicionário com os resultados do cálculo (hit_result, wound_result, save_result, damage_result).

    Raises:
        HTTPException 400: Se os dados de entrada forem inválidos ou não seguirem as regras de validação.
    """
    attacker = payload.attacker.model_dump()
    defender = payload.defender.model_dump()
    try:
        JsonValidator.validate_attacker(attacker)
        JsonValidator.validate_defender(defender)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    calc = WarHammerCalc(attacker, defender)
    result = calc.run_calc()
    return result