import random
import statistics


def how_many_before_collisions(buckets, loops=1):
    """
    roll random hashes into 'buckets' and print
    how rolls before a hash collision.

    Run 'loops' number of times
    """
    for i in range(loops):
        tries = 0
        tried = set()

        results = []

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets

            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break
        result = tries / buckets * 100
        results.append(result)

        print(f'{buckets} buckets, {tries} hashes before collisions. ({result:.1f}%)')

    print(statistics.mean(results))


how_many_before_collisions(32, 10)