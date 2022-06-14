from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="csv-linter",
    description="lint csv files",
    packages = find_packages(),
    author = "Ayodeji Yekeen",
    entry_points = """
    [console_scripts]
    csv-linter=csv_linter:main
    """,
    install_requires = ["click==8.1.3","pandas==1.4.2"],
    vaersion = "0.0.1",
    url = "https://github.com/Deji01/CLI-Tool"
)