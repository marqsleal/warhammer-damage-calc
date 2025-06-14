def init_base_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        "hit_result": 6.666666666666666,
        "wound_result": 3.333333333333333,
        "save_result": -0.5555555555555558,
        "damage_result": 7.777777777777778
    }
    return test_input, test_assert


def init_strength_gt_tough_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 5,
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
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 4.444444444444444,
        'save_result': -0.7407407407407409,
        'damage_result': 10.37037037037037
    }
    return test_input, test_assert


def init_strength_twice_gt_tough_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 8,
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
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 5.555555555555555,
        'save_result': -0.9259259259259263,
        'damage_result': 12.962962962962964
    }
    return test_input, test_assert


def init_tough_gt_strength_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
        "defender_kwargs": {
            "TOUGHNESS" : 5,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 2.222222222222222,
        'save_result': -0.37037037037037046,
        'damage_result': 5.185185185185185
    }
    return test_input, test_assert


def init_tough_twice_gt_strength_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
        "defender_kwargs": {
            "TOUGHNESS" : 8,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 1.111111111111111,
        'save_result': -0.18518518518518523,
        'damage_result': 2.5925925925925926
    }
    return test_input, test_assert


def init_d3_damage_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 1,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 3.333333333333333,
        'save_result': -0.5555555555555558,
        'damage_result': 15.555555555555555
    }
    return test_input, test_assert


def init_d6_damage_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 1,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 3.333333333333333,
        'save_result': -0.5555555555555558,
        'damage_result': 21.38888888888889
    }
    return test_input, test_assert


def init_blast_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 1,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 10,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 8.0,
        'wound_result': 4.0,
        'save_result': -0.666666666666667,
        'damage_result': 9.333333333333334
    }
    return test_input, test_assert


def init_heavy_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 1,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 8.333333333333334,
        'wound_result': 4.166666666666667,
        'save_result': -0.6944444444444448,
        'damage_result': 9.722222222222223
    }
    return test_input, test_assert


def init_lethal_hits_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 1,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 5.0,
        'save_result': -0.8333333333333337,
        'damage_result': 11.666666666666668
    }
    return test_input, test_assert


def init_sustained_hits_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 1,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 7.777777777777777,
        'wound_result': 3.8888888888888884,
        'save_result': -0.6481481481481484,
        'damage_result': 9.074074074074073
    }
    return test_input, test_assert


def init_twin_linked_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 1,
            "REROLL_TO_HIT": 0,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 5.0,
        'save_result': -0.8333333333333337,
        'damage_result': 11.666666666666668
    }
    return test_input, test_assert


def init_reroll_to_hit_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
            "ARMOR_PENETRATION": 1,
            "FLAT_DAMAGE": 2,
            "D3_DAMAGE": 0,
            "D6_DAMAGE": 0,
            "BLAST": 0,
            "HEAVY": 0,
            "LETHAL_HITS": 0,
            "SUSTAINED_HITS": 0,
            "TWIN_LINKED": 0,
            "REROLL_TO_HIT": 1,
            "REROLL_TO_WOUND": 0
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 7.777777777777777,
        'wound_result': 3.8888888888888884,
        'save_result': -0.6481481481481484,
        'damage_result': 9.074074074074073
    }
    return test_input, test_assert


def init_reroll_to_wound_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
            "REROLL_TO_WOUND": 1
        },
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 3.888888888888889,
        'save_result': -0.6481481481481485,
        'damage_result': 9.074074074074074
    }
    return test_input, test_assert


def init_invulnerable_save_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 3,
            "FEEL_NO_PAIN": 0
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 3.333333333333333,
        'save_result': 1.1111111111111112,
        'damage_result': 4.444444444444444
    }
    return test_input, test_assert


def init_feel_no_pain_test() -> tuple:
    test_input = {
        "attacker_kwargs": {
            "ATTACK" : 10,
            "SKILL" : 3,
            "STRENGTH" : 4,
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
        "defender_kwargs": {
            "TOUGHNESS" : 4,
            "ARMOR_SAVE" : 3,
            "N_MODELS": 1,
            "INVULNERABLE_SAVE": 0,
            "FEEL_NO_PAIN": 3
        }
    }
    test_assert = {
        'hit_result': 6.666666666666666,
        'wound_result': 3.333333333333333,
        'save_result': -0.5555555555555558,
        'damage_result': 2.5925925925925926
    }
    return test_input, test_assert