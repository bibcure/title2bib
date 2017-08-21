from setuptools import setup, find_packages

readme = open('README','r')
README_TEXT = readme.read()
readme.close()

setup(
    name="title2bib",
    version="0.2.5",
    packages = find_packages(exclude=["build",]),
    scripts=["title2bib/bin/title2bib"],
    long_description = README_TEXT,
    install_requires=["requests", "future", "doi2bib","arxivcheck"],
    include_package_data=True,
    license="GPLv3",
    description="Generate a bibtex given a title",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/title2bib/archive/0.2.5.tar.gz",
    keywords=["bibtex", "science","scientific-journals"],

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/bibcure/title2bib"
)
