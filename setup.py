import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zimfarm",
    version="0.0.9",
    author="Chris Li",
    author_email="chris@kiwix.com",
    description="Zimfarm Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openzim/zimfarm-client",
    install_requires=["requests>=2.21.0"],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['zimfarm=zimfarm.commands:main'],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
)
