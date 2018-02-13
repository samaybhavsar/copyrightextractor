#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

copyright_str = ['&copy;','©','Copyright','&#169;']

def extract(html):
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all("i", class_="fa-copyright");
    if res:
        return res[0].parent.text.strip()
    res = soup.find_all("i", class_="glyphicon-copyright-mark");
    if res:
        return res[0].parent.text.strip()
    for crstr in copyright_str:
        res = soup.find_all(text=re.compile(crstr))
        if res:
            return res[0].parent.text.strip()
    return "Copyright not found"
