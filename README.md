# Python

use python3

```
virtualenv -p python3 venv
```

Running all tasks is easy:
```
python run.py
```

Running one task is easy:
```
python run.py 00016
```

Running HOT is easy (with entr):
```
ls *.py | entr -c python run.py
```

Testing libs is easy:
```
python -m unittest discover -p "*_test.py"
```

