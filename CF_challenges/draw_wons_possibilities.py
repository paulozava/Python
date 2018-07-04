def draws_and_wins(teams, points):
    result = []
    for draws in range(teams):
        for wins in range(0, points - draws + 1, 3):
            obtained_points = draws + wins
            if obtained_points == points:
                result.append([draws, wins])
        if draws + 3 > points:
            break
    return result