from setuptools import find_packages, setup

install_requires = []
with open("requirements.txt") as f:
    for module in f:
        install_requires.append(module.strip())

setup(
    name="graphql-client",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/jaswanth098/graphql-client",
    install_requires=install_requires,
    author="jaswanth098",
    package_dir={"graphql-client": "graphql_client"},
    author_email="jaswanth_dbz1992@yahoo.com",
    description="Grapqhl Client to make query, mutation and subscriptions",
    keywords=["graphql", "graphql-client"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "License :: MIT License",
    ],
)
