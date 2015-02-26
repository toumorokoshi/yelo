# this is how much weight the match has
# on the ratings. 30 is a good standard.
WEIGHT_CONSTANT = 30


def play_match(winner, loser):
    # R_n = R_0 + K * (W - W_e)
    winner_win_expectancy = _calculate_win_expectancy(winner - loser)
    winner_new = winner + WEIGHT_CONSTANT * (1 - winner_win_expectancy)

    loser_win_expectancy = _calculate_win_expectancy(loser - winner)
    loser_new = loser + WEIGHT_CONSTANT * (0 - loser_win_expectancy)

    return winner_new, loser_new


def _calculate_win_expectancy(rating_difference):
    return 1 / (10 ** (-rating_difference / 400.0) + 1)
