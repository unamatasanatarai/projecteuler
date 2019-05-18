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

Running HOT is easy (with entr):
```
ls *.py | entr -c ./run
ls *.py | entr -c python run.py
```

Benchmarking?
```
./bench 017_number_letter_counts.py 400
```

Testing libs is easy:
```
python -m unittest discover -p "*_test.py"
```

