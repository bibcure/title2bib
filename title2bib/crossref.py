
from __future__ import unicode_literals, print_function, absolute_import
import requests
from builtins import input
import difflib
from doi2bib.crossref import get_bib_from_doi
from unidecode import unidecode
from arxivcheck.arxiv import get_arxiv_info, generate_bib_from_arxiv
bare_url = "http://api.crossref.org/"


def find_cross_info(params):
    url = bare_url+"works"
    requested = requests.get(url, params=params)
    return requested


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\t It is >>'{}' article?\n y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            unidecode(item["title"]), unidecode(title)))
        if w == "y":
            found = True
            result = item
            break
        if w == "q":
            break
    return found, result


def sort_items_by_title(items, title):
    return sorted(
        items,
        key=lambda x: difflib.SequenceMatcher(
            None,
            x["title"],
            title
        ).ratio(),
        reverse=True
    )


def get_from_title(title, get_first=False):
    found = False
    params = {"query.bibliographic": title, "rows": 20}
    r = find_cross_info(params)
    items = r.json()["message"]["items"]
    for i, item in enumerate(items):
        title_item = item["title"][0]
        try:
            title_item = title_item.decode("utf-8")
        except:
            pass

        item["title"] = title_item
        item["is_crossref"] = True

        if title_item == title:
            return True, item
        
        items[i] = item

    if len(items) == 0:
        found_arxiv,  arxiv_items = get_arxiv_info(title, field="ti")
        for arxiv_item in arxiv_items:
            arxiv_item["is_crossref"] = False
            items.append(arxiv_item)

    if r.status_code == 200 and len(items) > 0:
        items = sort_items_by_title(items, title)
        if get_first:
            found = True
            item = items[0]
        else:
            found, item = ask_which_is(title, items)

    return found, item


def get_bib_from_title(title, get_first=False, abbrev_journal=False):
    found = False
    bib = ""
    found, item = get_from_title(title, get_first)
    if found:
        if item["is_crossref"]:
            if "DOI" in item:
                doi = item["DOI"]
                found, bib = get_bib_from_doi(doi)

        else:
            if "arxiv_doi" in item:
                doi = item["arxiv_doi"]
                published, bib = get_bib_from_doi(doi, abbrev_journal)
            else:
                bib = generate_bib_from_arxiv(item, title, field="ti")

            # if "short-container-title" in item:
            # abbreviated_journal = item["short-container-title"][0]##aqui pode acontecer de realizar a chamada para

    return found, bib
