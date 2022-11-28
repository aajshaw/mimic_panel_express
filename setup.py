import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="mimic_panel_express",
    version="0.1.0",
    author="Anthony Shaw",
    author_email="tony@adshaw.uk",
    description="Simple mimic panel development",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="model railway control panel",
    url="https://github.com/aajshaw/mimic_panel_express",
    packages=setuptools.find_packages(),
    install_requires=['pysimplegui',],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: BSD 3-Clause :: BSD 3-Clause License",
        "Topic :: SOFTWARE DEVELOPMENT :: LIBRARIES :: PYTHON_MODULES",
        "Operating System :: OS Independent"
    ),
    zip_safe=True,
)