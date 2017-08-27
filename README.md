## Description

title2bib is a module of [bibcure](https://github.com/bibcure/bibcure)and [scihub2pdf](https://github.com/bibcure/scihub2pdf)


## Install

```
$ sudo pip install title2bib
```

or if you want the full version

```
$ sudo pip install bibcure
```

## Features and how to use


Given a title...

```
$ title2bib An useful paper
```

Given a file of titles or ids

```
$ title2bib -i  titles.txt -o refs.bib
```

* search papers related and return the bibs


### bibcure

```
$ bibcure -i input.bib -o output.bib
```

Given a bib file...

* check sure the Arxiv items have been published, then update them

* complete all fields(url, journal, etc) of all bib items using DOI number

* find and create DOI number associated with each bib item which has not
DOI field

* abbreviate jorunals names

```
$ doitobib 10.1038/s41524-017-0032-0
```

Given a DOI number...

* get bib item given a doi



```
$ arxivcheck 1601.02785
```

Given a arxiv id...

* given an arixiv id, check if has been published, and then returns the updated bib
