"""
Coin Flip by cuZz
"""
from random import randint
coin_sides = ['tails', 'heads']


def flip_times():
    while True:
        try:
            how_many = int(input("How many flips bro?\n"))
        except ValueError:
            print("\n" * 100)
            print("That's not a number")
            continue
        else:
            return how_many


def coin_flip(times, tails=0, heads=0):
    for number in range(0, times):
        selector = randint(0, 1)
        print(coin_sides[selector])
        if selector == 0:
            tails += 1
        else:
            heads += 1

    print("\n")
    print(f"Total number of tails: {tails}")
    print(f"Total number of heads: {heads}")


times = flip_times()
coin_flip(times)
