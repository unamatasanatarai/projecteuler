# Python

use python3

```
virtualenv -p python3 venv
```

Running all tasks is easy:
```
./run
```

Running one task is easy:
```
./run 007_10001st_prime
```

Watching is easy (with entr):
```
./run watch
./run watch task_file_name.py
```

Benchmarking?
```
./run bench task_file_name
./run bench task_file_name 500
```

Testing libs is easy:
```
python -m unittest discover -p "*_test.py"
```

