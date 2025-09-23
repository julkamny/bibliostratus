
# coding: utf-8

version = 1.37
version_suffix = "1"   # contenu : "RC1", "RC2", "RC3", etc.
lastupdate = "25/08/2025"
programID = "bibliostratus"


import codecs
import os
import json
import re
# import smc.bibencodings
import SPARQLWrapper
#from pkg_resources import py2_warn
import tkinter as tk
import webbrowser
from tkinter import filedialog
from urllib import error, request
import pymarc
import ssl

from joblib import Parallel, delayed
import multiprocessing

from unidecode import unidecode

import bibliostratus.main as main
import bibliostratus.marc2tables as marc2tables
import bibliostratus.bib2id as bib2id
import bibliostratus.aut2id as aut2id
import bibliostratus.ark2records as ark2records
import bibliostratus.funcs as funcs
import bibliostratus.forms as forms

import bibliostratus.mapping_number_letters as mapping_number_letters
import bibliostratus.sru as sru
import bibliostratus.udecode as udecode

