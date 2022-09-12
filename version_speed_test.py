
import random
import time
import argparse


def estimate_pi(num_points: int, show_estimate: bool) -> None:
    """
    Simple Monte Carlo Pi estimation calculation.

    Args:
        num_points (int):
            Number of random numbers used to for estimation.
        show_estimate (bool):
            If True, will show the estimation of Pi, otherwise
            will not output anything.
    """
    within_circle = 0

    for _ in range(num_points):
        x, y = (random.uniform(-1, 1) for v in range(2))
        radius_squared = x**2 + y**2

        if radius_squared <= 1:
            within_circle += 1

    pi_estimate = 4 * within_circle / num_points

    if not show_estimate:
        print("Final Estimation of Pi=", pi_estimate)


def run_test(num_points: int, num_repeats: int, only_time: bool) -> None:
    """
    Perform the tests and measure required time.

    Args:
        num_points (int): 
            Number of random numbers used to for estimation.
        num_repeats (int): 
            Number of times the test is repeated.
        only_time (bool):
            If True will only print the time, otherwise
            will also show the Pi estimate and a neat formatted
            time.
    """
    start_time = time.time()

    for _ in range(num_repeats):
        estimate_pi(num_points, only_time)

    time_taken = (time.time() - start_time) / num_repeats

    if only_time:
        print(f"{time_taken:.4f}")
    else:
        print(f"Estimating pi took {time_taken:.4f} seconds per run.")


def positive_integer(value: str) -> int:
    """Check for positive integer in arg_parse."""
    int_value = int(value)

    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")

    return int_value


def main(arguments=None):
    """Main loop in arg parser."""
    parser = argparse.ArgumentParser()

    parser.add_argument("-p",
                        "--num_points",
                        help="Number of random points to use for estimating Pi.",
                        type=positive_integer,
                        default=1_000_000)

    parser.add_argument("-r", 
                        "--num_repeats", 
                        help="Number of times to repeat the calculation.", 
                        type=positive_integer, 
                        default=5)
                        
    parser.add_argument("--only-time", action='store_true', default=False)

    args = parser.parse_args()

    run_test(args.num_points, args.num_repeats, args.only_time)


if __name__ == "__main__":
    main()

