import gmpy2

# Each RESET we apply a 64× “phase reset”
RESET = 67520

def get_prime_and_harmony(n: int):
    """
    Walk through the integers, detect primes,
    step the harmonic multiplier cycle, and
    stop when we've seen n primes.
    Returns a tuple: (prime, harmony_sequence_value).
    """
    count = 0
    gs = 2       # geometric/harmonic sequence value
    cycle = 0    # 0→×4, 1→×16, 2→×64, 3→×256
    i = 2        # current integer to test

    while True:
        if gmpy2.is_prime(i):
            count += 1

            # For the very first prime (2), gs stays at 2
            if count == 1:
                prime = i
                harmony = gs
            else:
                # Advance the harmonic sequence
                if cycle == 0:
                    gs *= 4
                elif cycle == 1:
                    gs *= 16
                elif cycle == 2:
                    gs *= 64
                else:
                    gs *= 256

                cycle = (cycle + 1) % 4
                prime = i
                harmony = gs

            # Once we've reached the n-th prime, return both values
            if count == n:
                return prime, harmony

        i += 1

