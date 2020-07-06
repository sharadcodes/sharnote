from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sharnote',
    version='0.0.4',
    author="Sharad Raj Singh Maurya",
    author_email="iamsharadrah@gmail.com",
    url="https://github.com/sharadcodes/sharnote",
    description='A command line note taking utility developed in Python that saves notes in JSON format',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['sharnote'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points={ "console_scripts": ['sharnote=sharnote:main'] }
)
