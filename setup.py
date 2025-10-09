from setuptools import find_packages, setup

setup(
    name="pmgr",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pmgr=pmgr.__main__:main",
        ]
    },
)
