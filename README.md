# Python

use python3

```
virtualenv -p python3 venv
```

Running all tasks is easy:
```
./run
python run.py
```

Running one task is easy:
```
./run 0016
python run.py 0016
```

Running HOT is easy (with entr):
```
ls *.py | entr -c ./run
ls *.py | entr -c python run.py
```

Testing libs is easy:
```
python -m unittest discover -p "*_test.py"
```

