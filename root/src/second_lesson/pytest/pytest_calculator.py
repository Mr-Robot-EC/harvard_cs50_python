from root.src.second_lesson.unit_tests.calculator import square

# pytest
"""
docs.pytest.org
pip install pytest
pytest pytest_calculator.py
"""

# run tests
"""
### Running the Tests
To execute the tests, use the following command from the 
C:\\Users\Dell\Desktop\Projects\harvard_cs50_python\ directory:

python -m pytest root\src\second_lesson\pytest\pytest_calculator.py

Python was raising an error because it couldn’t recognize the directories 
as importable packages. 

To resolve this, I created an empty `__init__.py` file in each directory. 
This tells the Python interpreter that the directories are packages, 
allowing me to access and import the `calculator` module from `unit_tests` 
to run the tests successfully.
"""

def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4
    assert square(-3) == 9