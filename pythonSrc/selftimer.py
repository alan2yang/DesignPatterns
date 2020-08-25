import cProfile
import pstats
from io import StringIO


def mytimer(func):
    pr = cProfile.Profile()

    def innerwrap(*args, **kwargs):
        pr.enable()
        func(*args, **kwargs)
        pr.disable()
        s = StringIO()
        sortby = 'tottime'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    return innerwrap


@mytimer
def loop(count):
    result = []
    for i in range(count):
        result.append(i)


if __name__ == '__main__':
    loop(1000000)
