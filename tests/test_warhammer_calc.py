from .test_utils import (
    init_base_test,
    init_strength_gt_tough_test,
    init_strength_twice_gt_tough_test,
    init_tough_gt_strength_test,
    init_tough_twice_gt_strength_test,
    init_d3_damage_test,
    init_d6_damage_test,
    init_blast_test,
    init_heavy_test,
    init_lethal_hits_test,
    init_sustained_hits_test,
    init_twin_linked_test,
    init_reroll_to_hit_test,
    init_reroll_to_wound_test,
    init_invulnerable_save_test,
    init_feel_no_pain_test
)
import pytest
from warhammer_calc import WarHammerCalc


@pytest.mark.parametrize(
    "test_data",
    [
        init_base_test(),
        init_strength_gt_tough_test(),
        init_strength_twice_gt_tough_test(),
        init_tough_gt_strength_test(),
        init_tough_twice_gt_strength_test(),
        init_d3_damage_test(),
        init_d6_damage_test(),
        init_blast_test(),
        init_heavy_test(),
        init_lethal_hits_test(),
        init_sustained_hits_test(),
        init_twin_linked_test(),
        init_reroll_to_hit_test(),
        init_reroll_to_wound_test(),
        init_invulnerable_save_test(),
        init_feel_no_pain_test()
    ]
)
def test_warhammer_calc(test_data):
    test_input, test_assert = test_data
    attacker_kwargs, defender_kwargs = test_input["attacker_kwargs"], test_input["defender_kwargs"]
    calc = WarHammerCalc(attacker_kwargs, defender_kwargs)
    results = calc.run_calc()
    assert results == test_assert