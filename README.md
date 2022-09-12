# Speed test for Python 3.11
This is a simple speed test to compare Python 3.11 to previous python version from 3.5 to 3.10.

## Blog post
This is the code which belongs to a blog post you can find here.

## Requirements
- Python environment to run the tester
- Docker to download each Python Env.

## Usage:
```shell
python run_main_all_versions_test.py
```

## Monte Carlo Pi estimation
For this I us a Pi estimation. Not sure if this is the best workload but it is at least Python heavy.

## Result
```stdout
The new Python 3.11 took 4.891 seconds per run.

Python 3.5 took 7.089 seconds per run. (Python 3.11 is 44.9% faster)
Python 3.6 took 7.0434 seconds per run. (Python 3.11 is 44.0% faster)
Python 3.7 took 7.1027 seconds per run. (Python 3.11 is 45.2% faster)
Python 3.8 took 7.579 seconds per run. (Python 3.11 is 55.0% faster)
Python 3.9 took 7.0289 seconds per run. (Python 3.11 is 43.7% faster)s
Python 3.10 took 6.0265 seconds per run. (Python 3.11 is 23.2% faster)
```

## Result for C++
Build instructions in the folder.

```stdout
Pi is approximately 3.14227 and took 0.25728 seconds to calculate.
Pi is approximately 3.14164 and took 0.25558 seconds to calculate.
Pi is approximately 3.1423 and took 0.25740 seconds to calculate.
Pi is approximately 3.14108 and took 0.25737 seconds to calculate.
Pi is approximately 3.14261 and took 0.25664 seconds to calculate.

Each loop took on average 0.25685 seconds to calculate.
```

