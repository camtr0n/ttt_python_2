__author__ = 'Camtr0n'


def is_valid(num, valid):
    try:
        if int(num) in valid:
            return True
    except:
        pass
    return False


def tuple_replace(replacement, position, original):
        new = original[:position] + (replacement,)
        if position < len(original) - 1:
            new += original[position + 1:]
        return new
