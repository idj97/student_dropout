_unknown = set([0,34])
_basic = set([15,9, 37,38,19,29,30,26,11,10,35,36,12,14])
_secondary = set([1,27,13, 25])
_frequency=set([6,18,33,31])
_specialized = set([22,20,39,41,42])
_bachelor = set([2,3,40])
_master = set([4,43])
_doctorate = set([5,44])

def map_qualification(qualification):
    if qualification in _unknown:
        return 0
    elif qualification in _basic:
        return 1
    elif qualification in _secondary:
        return 2
    elif qualification in _frequency:
        return 3
    elif qualification in _bachelor:
        return 4
    elif qualification in _master:
        return 5
    elif qualification in _specialized:
        return 6
    elif qualification in _doctorate:
        return 7
    else:
        raise Exception("Unsupported qualification " + str(qualification))
