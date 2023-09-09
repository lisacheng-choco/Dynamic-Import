# Dynamic-Import
Learn how to dynamically import modules and classes in Python

## Project Introduction
### Background

In data processing pipelines, I had different data sources and transformation methods.

In the beginning, I developed many `class` and use conditional statements to switch between different `class` to adopt correct data transformation method. Here is the code.

```python


# data_etl.py
class Datasource_A:
    def transform(self):
        print("Complete to transform Datasource_A")

class Datasource_B:
    def transform(self):
        print("Complete to transform Datasource_B")


# main.py
def transform_data(dtasource_name):
    if dtasource_name == 'datasource_a':
        transformer = Datasource_A()
    elif dtasource_name == 'datasource_b':
        transformer = Datasource_B()

    transformer.transform()

```

However, It becomes a challenge while the new data source and transformation method are introduced. The impacts are:

1. Need to modify `data_etl.py` and may impact existing code.
2. As the number of data sources grows, the conditional statements in the `main` function become unwieldy and harder to maintain.

### Solution
1. Adopt dynamic import modules by using `__import__` and `getattr`.
2. Separate different datasource classes into seperate modules, `data_etl/datasource_a.py` and `data_etl/datasource_b.py`.

Here is the code
```python

# data_etl/datasource_a.py
class Datasource_A:
    def transform(self):
        print("Complete to transform Datasource_A")


# data_etl/datasource_b.py
class Datasource_B:
    def transform(self):
        print("Complete to transform Datasource_B")


# main.py
module_json = {
    "datasource_a": "data_etl.datasource_a.Datasource_A",
    "datasource_b": "data_etl.datasource_b.Datasource_B"
}

def _get_etl_by_datasource_name(datasource_name): 
    solution_name, dir_name, module_name, class_name  = module_json[datasource_name].rsplit('.', 3)
    module_path = ".".join([solution_name, dir_name, module_name])
    module = __import__(module_path, fromlist=[class_name])
    klass = getattr(module, class_name)
        
    return klass


def transform_data(datasource_name):
    klass = _get_etl_by_datasource_name(datasource_name)
    transformer = klass()

    transformer.transform()

```

1. **Extensibility**: You can easily add support for new data source by creating a new class in a separate module and updating the `module_json` dictionary. No changes are required in the `transform_data` function or the main application code.
2. **Maintainability**: The conditional statements in the `transform_data` function are eliminated, making the code more maintainable as you add more media format support.
3. **Organization**: Data source transormation methods are organized into separate modules (`data_etl/datasource_a.py`, `data_etl/datasource_b.py`), enhancing code organization and separation of concerns.
4. **Flexibility**: You can swap out or update specific data transformer independently without affecting other parts of the application

## Requirements
Python 3.10 or above

## Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/lisacheng-choco/Dynamic-Import.git
```

Then navigate to the directory:

```bash
cd Dynamic-Import
```

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

There are two solutions:
1. `solution_1`: without dynamic import modules
2. `solution_2`: with dynamic import modules

There are two existing data source:
1. `datasource_a`
2. `datasource_b`

To specify solution and data source, you can use the `--solution` and `--datasource_name` options:

```bash
python main.py --solution solution_1 --datasource_name datasource_a
```
```bash
python main.py --solution solution_1 --datasource_name datasource_b
```
```bash
python main.py --solution solution_2 --datasource_name datasource_a
```
```bash
python main.py --solution solution_2 --datasource_name datasource_b
```

