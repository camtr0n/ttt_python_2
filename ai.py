__author__ = 'Camtr0n'

import player

class Score(object):
    def __init__(self, val, move, depth):
        self.value = val
        self.move = move
        self.depth = depth

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return (self.value > other.value) or (self.value == self.depth and self.depth < other.depth)


def score_game(player, initiator, depth):
    if player is initiator:
        return Score(500, None, depth)
    elif player:
        return Score(-500, None, depth)
    else:
        return Score(0, None, depth)


def get_move_ranks(board, active_player, initiator, multiplier):
    moves = board.available
    candidates = [board.copy.apply_move(move, active_player) for move in moves]
    inactive_player = player.opposite_symbol(active_player)
    ranks = [negamax(candidate, inactive_player, initiator) for candidate in candidates]
    for rank in ranks:
        rank.value *= multiplier
    return zip(moves, ranks)


def best_score(board, active, initiator):
    best = Score(-1000, None, board.depth)
    multiplier = 1 if active is initiator else -1
    for move, rank in get_move_ranks(board, active, initiator, multiplier):
        best = Score(rank.value, move, rank.depth) if rank > best else best
    best.value *= multiplier
    return best


def negamax(board, active, initiator):
    winner = board.winner
    if not winner and not board.tied:
        if board.center not in board.available:
            best = best_score(board, active, initiator)
        else:
            best = Score(1000, board.center, board.depth)
    else:
        best = score_game(winner, initiator, board.depth)
    return best
