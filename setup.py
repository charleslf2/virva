from setuptools import setup,find_packages

classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Development Status :: 4 - Beta"
]


setup(
    name="virva",
    version="0.1.9",
    description="Virva is the simplest  fake dataframe generator ",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/charleslf2/virva",
    project_urls={
        "Bug Tracker":"https://github.com/charleslf2/virva/issues",
    },
    author="Charles TCHANAKE",
    author_email="datadevfernolf@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["data generator", "fake data generator", 
    "csv generator", "dataframe generator"],
    packages=find_packages(),
    install_requires=["pandas", "rich"]
)