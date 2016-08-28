import pickle

f = open('myfile', 'r')
s = f.read()
pickle.load(s)
eval(s)
