import matplotlib.pyplot as plt


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def do_primes(n):
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
        plt.scatter(i, dists[i], s=2)
    plt.savefig(str(n) + "_x=number" + ".svg")
    plt.clf()

    for i in range(1, len(primes) - 1):
        plt.scatter(primes[i], dists[i], s=2)
    plt.savefig(str(n) + "_x=value" + ".svg")
    plt.clf()
    # plt.show()


do_primes(100)
do_primes(1000)
do_primes(10000)
do_primes(100000)
do_primes(1000000)
do_primes(10000000)
