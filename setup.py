from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata7", # the name that you will install via pip
    version="1.1",
    author="Charlie May",
    author_email="your@email.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/charlie-may86/lambdata7.git",
    #keywords="",
    packages=find_packages(), # ["my_lambdata"]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)