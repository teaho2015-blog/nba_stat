import urllib.request
import urllib.parse
from urllib.request import urlopen
import json

from src.table import *

json_losangle_url = 'https://www.google.com/publicdata/query?session=z4VmSe5t6Ls&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2231080%22%5D%7D%5D%7D'
json_atlanta_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2212060%22%5D%7D%5D%7D'
json_Charlotte_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2216740%22%5D%7D%5D%7D'
json_Miami_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2233100%22%5D%7D%5D%7D'
json_Orlando_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2236740%22%5D%7D%5D%7D'
json_Washington_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2247900%22%5D%7D%5D%7D'
json_Boston_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2214460%22%5D%7D%5D%7D'
json_NewYork_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2235620%22%5D%7D%5D%7D'
json_Philadelphia_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2237980%22%5D%7D%5D%7D'
json_Chicago_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2216980%22%5D%7D%5D%7D'
json_Cleveland_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2217460%22%5D%7D%5D%7D'
json_Detroit_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2219820%22%5D%7D%5D%7D'
json_Indianapolis_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2226900%22%5D%7D%5D%7D'
json_Milwaukee_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2233340%22%5D%7D%5D%7D'
json_Dallas_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2219100%22%5D%7D%5D%7D'
json_Houston_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2226420%22%5D%7D%5D%7D'
json_Memphis_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2232820%22%5D%7D%5D%7D'
json_NewOrleans_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2235380%22%5D%7D%5D%7D'
json_SanAntonio_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2241700%22%5D%7D%5D%7D'
json_Denver_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2219740%22%5D%7D%5D%7D'
json_Minneapolis_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2233460%22%5D%7D%5D%7D'
json_OklahomaCity_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2236420%22%5D%7D%5D%7D'
json_Portland_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2238900%22%5D%7D%5D%7D'
json_Utah_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2241620%22%5D%7D%5D%7D'
json_GoldenState_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2241860%22%5D%7D%5D%7D'
json_LosAngeles_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2231080%22%5D%7D%5D%7D'
json_Phoenix_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2238060%22%5D%7D%5D%7D'
json_Sacramento_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2240900%22%5D%7D%5D%7D'
json_Seattle_url = 'https://www.google.com/publicdata/query?session=fDnuBUFzelI&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2242660%22%5D%7D%5D%7D'
json_Trenton_url = 'https://www.google.com/publicdata/query?session=KukhXSOkxJg&jsq=%7B%22apiVersion%22%3A%221.0%22%2C+%22queries%22%3A%5B%7B%22qt%22%3A%22sliceDataByConcept%22%2C+%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gdp_metro%22%2C+%22ms%22%3A%7B%22fd%22%3A%5B%5D%2C+%22m%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22gross_domestic_product%22%7D%7D%2C+%22limit%22%3A1501%2C+%22pdim%22%3A%7B%22dsid%22%3A%22r2gb7qq0m55r_%22%2C+%22v%22%3A11%2C+%22id%22%3A%22metro%22%7D%2C+%22pid%22%3A%5B%2245940%22%5D%7D%5D%7D'

json_test_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

req = urllib.request.Request(json_Trenton_url)
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
req.add_header("Cookie",
               "__utmc=173272373; __utmz=173272373.1606589774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=173272373.1886659557.1606589774.1606589774.1606672714.2; SEARCH_SAMESITE=CgQInpAB; HSID=A9Vbk0t5x_P2NLyci; SSID=ADYQoPjLLlIx1KLwy; APISID=PvXj7lEI91tZj4l9/AViOVEWm7ItI3Ijmd; SAPISID=YRvXZ--To1Rcw7H9/AiqCrbohhxn8dX66r; __Secure-3PAPISID=YRvXZ--To1Rcw7H9/AiqCrbohhxn8dX66r; SID=3wf5ZwBkrtkaFL7d1jmcwYDN6dhO4rgacjBPWeSySLTxcT43oYE8MVLomGQTSZqHHzkxNA.; __Secure-3PSID=3wf5ZwBkrtkaFL7d1jmcwYDN6dhO4rgacjBPWeSySLTxcT43kCJ7B5CeR5p59T28X5X0Jw.; 1P_JAR=2020-11-29-18; NID=204=LXnIUbDuTLxh4klpLabwuMhnNDMoW6hFA-U5yEYjpJxO6LF8RBBUWxF5_vbs36W8-v_as17ktsJyfnSERgmgpdTKFAb96c6335249o263EzpWVGfrestbhhSI7f5Ozb4g1DDPDm3mx3yHDUjO7zdo8aRhmYpIGdTUBsYByagyKOKwltDpdmWZ_bwm4wP-Uqnxw9N9ZCqGU5OmlryklbDqMW-kgiy5Tp8RY06FFG64XLsFqxIr9VYTfomqBTYpfRE3h6ncc42QDxlea0nwjCtsYQITqokpJQnIpQPu8b_o9O5UavKlXnuPw; SIDCC=AJi4QfEMBWuty08kqV3cTyWPq4d35--rXVg80suVXqZ0_T9bXTuaY6xXv6f56dZbVm91kv1LRw; __Secure-3PSIDCC=AJi4QfHZYr3MveZmiEmCuOtuznD1GB7Rlizxk-wz-tCRCPtOmQpazm9wSEIgPt-iSgsc7NZgfzY")
req.add_header("Host", "www.google.com")
req.add_header("X-Client-Data", "CJO2yQEIorbJAQjBtskBCKmdygEImbXKAQisx8oBCPXHygEI6cjKAQi0y8oBCNzVygEIl5rLARiKwcoB")
req.add_header("Accept",
               "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")

with urllib.request.urlopen(req) as res:
    print(res.getheaders())
    json_str = res.read().decode('utf-8')
    jsondata = json.loads(json_str)
    print(jsondata)

    year_list = jsondata['results'][0]['t']
    gdp_list = jsondata['results'][0]['v'][0]['m'][0]
    for i, year_item in enumerate(year_list):
        print(i, year_list[i], gdp_list[i])
        stmt = t_city_gdp.insert(values=dict(city_id=34, year=year_list[i], gdp= gdp_list[i] ))
        stmt.execute()