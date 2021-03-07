import random
from typing import Sequence

def get_ps_number_range(lo, hi) -> Sequence[int]:
    ps_number_range = range(lo, hi+1)
    #return random.sample(ps_number_range, min(len(ps_number_range), 10))
    #ps_range = range(lo, hi+1)
    return ps_number_range if len(ps_number_range) <= 10 else random.sample(ps_number_range, 10)
    #if len(ps_range) <= 10:
    #    return ps_range
    #else:
    #    return random.sample(ps_range, 10)
#print(*get_ps_number_range(1, 5))
the_range = get_ps_number_range(100, 111)
print(*the_range)
print(len(the_range))

print(*range(100, 111))