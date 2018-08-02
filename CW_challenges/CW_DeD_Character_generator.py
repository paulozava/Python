def char_attribute(score):
    modifier = score//2 - 5
    if score == 0:
        modifier = 0

    if score < 10:
        max_spell_level = -1
    elif 10 <= score <= 27:
        max_spell_level = (score - 10) // 2
    else:
        max_spell_level = 9

    spf = lambda sc, spl: 1 + (sc - 12 - 2*spl)//8
    spells = [spf(score, spell_level) for spell_level in range(9) if spf(score, spell_level) > 0]

    return {"modifier": modifier, "maximum_spell_level": max_spell_level, "extra_spells": spells}

def psion_power_points(level, score):
    ability_mod = (score - 10) // 2
    psi = int(level * ability_mod * 0.5)
    return psi

def carrying_capacity(score, size, quadrupede=False):
    score, size, quadrupede = 12, 'medium', False
    p = [3, 6, 10, 13, 16, 20, 23, 26, 30, 33, 38, 43, 50, 58, 66, 76, 86, 100, 116, 133, 153, 173, 200, 233, 266, 306, 346, 400, 466]

    if quadrupede:
        mod = {'fine': 1/4, 'diminutive': 1/2, 'tiny': 3/4, 'small': 1, 'medium': 1.5, 'large': 3, 'huge': 6, 'gargantuan': 12, 'colossal': 24}
    else:
        mod = {'fine': 1/8, 'diminutive': 1/4, 'tiny': 1/2, 'small': 3/4, 'medium': 1, 'large': 2, 'huge': 4, 'gargantuan': 8, 'colossal': 16}

    if score <= 29:
        max_light_load = p[score - 1]
    else:
        max_light_load = 466 + 466 * 4 * ((score - 29)//10)

    min_medium_load = max_light_load + 1
    max_medium_load = min_medium_load + max_light_load
    min_heavy_load = max_medium_load + 1
    max_heavy_load = min_heavy_load + max_light_load
    max_lift_load = max_heavy_load
    max_push_load = max_heavy_load * 5

    basic_capacity = [max_light_load, min_medium_load, max_medium_load, min_heavy_load, max_heavy_load, max_lift_load, max_push_load]
    ajusted_capacity = list(map(lambda x, y=mod[size]: x * y, basic_capacity))
    return ajusted_capacity