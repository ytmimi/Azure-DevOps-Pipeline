from setuptools import find_packages, setup

with open("README.md", encoding="utf-8", mode="r") as f:
    long_description = f.read()


test_requires = ["pytest-cov"]
docs_requires = ["sphinx", "sphinx_rtd_theme"]
dev_requires = test_requires + docs_requires + ["flake8", "black", "pre-commit"]

setup(
    name="Azure-DevOps-Pipeline",
    version="0.1.0",
    author="Yacin Tmimi",
    author_email="yacintmimi@gmail.com",
    description="Used to test setting up Azure Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytmimi/Azure-DevOps-Pipeline",
    packages=find_packages(exclude=["test*"]),
    extras_require={"test": test_requires, "docs": docs_requires, "dev": dev_requires},
    python_requires=">=3.6",
)
