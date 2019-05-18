import matplotlib.pyplot as plt


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def do_prime(n, ty):
    primes = []
    dists = []
    for i in range(1, n, 2):
        if is_prime(i):
            primes.append(i)
            print(i)
    for i in range(1, len(primes)):
        dists.append(primes[i] - primes[i - 1])
    print(len(primes))
    print(primes)
    print(len(dists))
    print(dists)
    for i in range(1, len(primes) - 1):
        if ty == 1:
            x = i # primes[i]
        else:
            x = primes[i]
        y = dists[i]
        plt.scatter(x, y, s=2)
    name = str(n) + "_x="
    if ty == 1:
        name = name + "number"
    else:
        name = name + "value"
    print(name)
    plt.savefig(name + ".svg")
    plt.show()


do_prime(100, 0)
do_prime(100, 1)
do_prime(1000, 0)
do_prime(1000, 1)
do_prime(10000, 0)
do_prime(10000, 1)
do_prime(100000, 0)
do_prime(100000, 1)
do_prime(1000000, 0)
do_prime(1000000, 1)
do_prime(10000000, 0)
do_prime(10000000, 1)