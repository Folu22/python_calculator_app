import os
from pathlib import Path


file_name = [
    "tests/__init__.py",
    "tests/test_add.py",
    "tests/test_subtract.py",
    "tests/test_multiply.py",
    "tests/test_divide.py",
    "tests/test_complex_math.py",
    "__init__.py",
    "add.py",
    "subtract.py",
    "multiply.py",
    "divide.py",
    "complex_math.py",
    "requirement.txt",
    "main.py"
    
]

for files in file_name:
    filepath = Path(files)
    filedir = filepath.parent

    if (not os.path.exists(filedir)) or os.path.getsize(filedir) == 0:
        os.makedirs(filedir, exist_ok=True)
        print(f"Directory {filedir} created")

    else:
        print(f"Directory {filedir} already exists")

    with open(filepath, "w") as fp:
        pass