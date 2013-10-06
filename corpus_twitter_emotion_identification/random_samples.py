from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat,spatial
from math import *
from pprint import pprint
import numpy as np
import scipy
import sys
import random


foa = open(sys.argv[1], "r")
fof = open("d2", "r")
fom = open("d3", "r")
fot = open("d4", "r")

def rantxt(txt):
	tt=[]
	for n in txt.readlines():
		tt.append(n)
	ar=[]
	for r in range(1000):
		ar.append(r)

	samples=[]
	for nn in range(20):
		random.shuffle(ar)
		samples.append(random.choice(ar))

	for i in  samples:
		print tt[i],	

rantxt(foa)
