# Ini adalah simple repository untuk tugas 4 wrangling

import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "cars_data_prediction",
    version = "0.0.1",
    author = "Shofi",
    autor_email = "kudefajri@gmail.com",
    description = "simple repo for task 4 wrangling",
    long_description = "long_description",
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    classifier = ["Programming Language :: Python :: 3"],
    install_requires = [
        "numpy",
        "pandas == 1.1.4",
        "scikit-learn == 0.22", #(>= 3.5)
    ],
    python_requires = ">=3.7"
)
