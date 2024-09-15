import nltk
from nltk.parse.generate import generate
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP | NP
    NP -> Det N PP | Det N
    VP -> V NP | V PP
    PP -> P NP
    Det -> 'the'
    N -> 'king' | 'north'
    V -> 'is'
    P -> 'in'
""")
parser=nltk.ChartParser(grammar)
sentence="the king in the north"
tokens=sentence.split()
for tree in parser.parse(tokens):
    tree.pretty_print()

