import requests
URL = "http://localhost:8000/calc"
payload = {
    "attacker": {
        "ATTACK": 1,
        "SKILL": 3,
        "STRENGTH": 4,
        "ARMOR_PENETRATION": 1,
        "FLAT_DAMAGE": 2,
        "D3_DAMAGE": 0,
        "D6_DAMAGE": 0,
        "BLAST": 0,
        "HEAVY": 0,
        "LETHAL_HITS": 0,
        "SUSTAINED_HITS": 0,
        "TWIN_LINKED": 0,
        "REROLL_TO_HIT": 0,
        "REROLL_TO_WOUND": 0
    },
    "defender": {
        "TOUGHNESS": 4,
        "ARMOR_SAVE": 3,
        "N_MODELS": 1,
        "INVULNERABLE_SAVE": 0,
        "FEEL_NO_PAIN": 0
    }
}
response = requests.post(URL, json=payload, timeout=10)
print(response.json())