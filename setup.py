from setuptools import setup,find_packages

classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha"
]


setup(
    name="virva",
    version="0.0.5",
    description="Virva is the simplest synthetic dataframe generator ",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/charleslf2/virva",
    project_urls={
        "Bug Tracker":"https://github.com/charleslf2/virva/issues",
        "Docs":"https://charleslf2.github.io/virva/"
    },
    author="Charles TCHANAKE",
    author_email="datadevfernolf@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["Synthetic data generator", "fake data generator", 
    "csv generator", "dataframe generator"],
    packages=find_packages(),
    install_requires=["pandas", "rich"]
)