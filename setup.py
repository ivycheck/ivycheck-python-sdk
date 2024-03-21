import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

setuptools.setup(
    name="ivycheck",
    version="0.9.0",
    author="IvyCheck",
    description="IvyCheck Python Client SDK",
    author_email="founders@ivycheck.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    extras_require={
        "dev": [
            "pylint==2.16.2",
        ],
    },
    package_dir={"": "src"},
    python_requires=">=3.8",
    package_data={"ivycheck": ["py.typed"]},
)
