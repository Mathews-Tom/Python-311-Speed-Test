import subprocess
import os


def speed_test_version(image: str) -> float:
    """
    Run single_test on Python Docker image.

    Args:
        image (str):
            full name of the the docker hub Python image.

    Returns:
        run_time (float):
            runtime in seconds per test loop.
    """
    docker_cmd = ["docker", "run", "-it", "--rm", "-v", 
                  f"{cwd}/{SCRIPT}:/{SCRIPT}", image, "python", f"/{SCRIPT}",
                  "--num_points", str(NUM_POINTS), "--num_repeats", 
                  str(NUM_REPEATS), "--only-time"]

    output = subprocess.run(docker_cmd,
                            capture_output=True,
                            text=True)

    avg_time = float(output.stdout.strip())

    return avg_time


if __name__ == "__main__":
    BASE_IMAGE = {"name": "Python 3.11", "image": "python:3.11-rc-slim"}

    TEST_IMAGES = [{"name": "Python 3.5", "image": "python:3.7-slim"},
                {"name": "Python 3.6", "image": "python:3.7-slim"},
                {"name": "Python 3.7", "image": "python:3.7-slim"},
                {"name": "Python 3.8", "image": "python:3.8-slim"},
                {"name": "Python 3.9", "image": "python:3.9-slim"},
                {"name": "Python 3.10", "image": "python:3.10-slim"}]

    NUM_POINTS = 10_000_000  # Number of points used to estimate Pi.
    NUM_REPEATS = 5  # Number of times to repeat the test loop.

    SCRIPT = "version_speed_test.py"

    cwd = os.getcwd()

    # Get test time for current Python version
    base_time = speed_test_version(BASE_IMAGE["image"])
    print(f"The new {BASE_IMAGE['name']} took {base_time} seconds per run.\n")

    # Create a dictionary containing the time taken to run the test for further analysis.
    execution_times = {}
    execution_times[BASE_IMAGE['name'].split(" ")[1]] = base_time

    # Compare to previous Python versions
    for item in TEST_IMAGES:
        total_time = speed_test_version(item["image"])
        execution_times[item['name'].split(" ")[1]] = total_time
        print(f"{item['name']} took {total_time} seconds per run. " \
            f"({BASE_IMAGE['name']} is {(total_time / base_time) - 1:.1%} faster)")

