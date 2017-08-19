from setuptools import setup, find_packages

readme = open('README.md','r')
README_TEXT = readme.read()
readme.close()

setup(
    name="titletobib",
    version="0.2.2",
    packages = find_packages(exclude=["build",]),
    scripts=["titletobib/bin/titletobib"],
    long_description = README_TEXT,
    install_requires=["requests", "future", "doitobib"],
    include_package_data=True,
    license="GPLv3",
    description="Generate a bibtex given a title",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/titletobib/archive/0.2.2.tar.gz",
    keywords=["bibtex", "science","scientific-journals"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/bibcure/titletobib"
)
