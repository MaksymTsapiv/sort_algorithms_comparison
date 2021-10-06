"""Sort algorithms comparison"""

import json
import random
import timeit

import matplotlib.pyplot as plt

from sort_algorithms import merge_sort, \
    shell_sort, insertion_sort, selection_sort


timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""


class Tester:

    def __init__(self):

        self.results = {}
        self.experiments = [self.random_sample, self.ordered_sample, self.reversed_sample, self.random_multiset123]
        self.methods = [selection_sort, insertion_sort, shell_sort, merge_sort]
        self.sizes = [2**i for i in range(7, 16)]

    def __str__(self):
        with open('result.json', 'w') as fp:
            json.dump(self.results, fp, indent=4)
        return 'go to results.json'

    def run(self):
        experiments = {}
        for exp in self.experiments:
            number = {}
            for size in self.sizes:
                approaches = {}
                arr = exp(size)
                for method in self.methods:
                    carr = arr.copy()
                    approaches[method.__name__] = dict(
                        zip(['seconds', 'comparisons'], list(timeit.Timer(lambda: method(carr)).timeit(number=1))))
                number[size] = approaches
            experiments[exp.__name__] = number
        self.results = experiments

    @staticmethod
    def random_sample(n):
        return random.sample(range(1, n + 1), n)

    @staticmethod
    def ordered_sample(n):
        return list(range(1, n + 1))

    @staticmethod
    def reversed_sample(n):
        return list(reversed(Tester.ordered_sample(n)))

    @staticmethod
    def random_multiset123(n):
        arr = [i for i in range(1, 4)] * (n // 3)
        random.shuffle(arr)
        return arr

    def build_graphs(self, path):
        with open(path, 'r') as fp:
            results = json.load(fp)

        for exp in results:
            s = []
            c = []
            for sizes in results[exp]:
                for sorts in results[exp][sizes]:
                    s.append(results[exp][sizes][sorts]['seconds'])
                    c.append(results[exp][sizes][sorts]['comparisons'])
            plt.figure(exp)
            plt.plot(self.sizes, s[::4], 'b-',
                     label='selection sort')
            plt.plot(self.sizes, s[1::4], 'r--',
                     label='insertion sort')
            plt.plot(self.sizes, s[2::4], 'y-',
                     label='shell sort')
            plt.plot(self.sizes, s[3::4], 'g--',
                     label='merge sort')
            plt.legend()
            plt.xscale('log', base=2)
            plt.xticks([2**i for i in range(7, 16)])
            plt.title(f'{exp}')
            plt.xlabel("Size of input (n)")
            plt.ylabel("Number of seconds")
            plt.savefig(f'./graphs/sec_{exp}.png')

            plt.figure(exp+'2')
            plt.plot(self.sizes, c[::4], 'b-',
                     label='selection sort')
            plt.plot(self.sizes, c[1::4], 'r--',
                     label='insertion sort')
            plt.plot(self.sizes, c[2::4], 'y-',
                     label='shell sort')
            plt.plot(self.sizes, c[3::4], 'g--',
                     label='merge sort')
            plt.legend()
            plt.xscale('log', base=2)
            plt.xticks([2 ** i for i in range(7, 16)])
            plt.title(f'{exp}')
            plt.xlabel("Size of input (n)")
            plt.ylabel("Number of comparisons")
            plt.savefig(f'./graphs/com_{exp}.png')


if __name__ == '__main__':
    t = Tester()
    # t.run()
    # print(t)
    t.build_graphs('result.json')
