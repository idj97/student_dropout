_unknown = set([90,99])
_student = set([0])
_lowskilled = set([9, 191, 192, 193, 182])
_service = set([5,151,152,153,194,195, 114])
_agricultural = set([6, 163])
_skilled = set([7,8,171,173,175, 172, 181, 183])
_military = set([10, 101, 102, 103, 154])
_administrative = set([4,141,143,144, 123, 112])
_midlevel_pros = set([3,131, 122,132,134, 135, 174])
_highlevel_pros = set([1,2,125, 124])

def map_occupation(occupation):
    if occupation in _unknown:
        return 0
    elif occupation in _student:
        return 1
    elif occupation in _lowskilled:
        return 2
    elif occupation in _service:
        return 3
    elif occupation in _agricultural:
        return 4
    elif occupation in _skilled:
        return 5
    elif occupation in _military:
        return 6
    elif occupation in _administrative:
        return 7
    elif occupation in _midlevel_pros:
        return 8
    elif occupation in _highlevel_pros:
        return 9
    else:
        raise Exception("Unsupported qualification " + str(occupation))
    