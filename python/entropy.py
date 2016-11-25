import nltk
import math
import string
import argparse
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

#################add help document and argument here#################
parser = argparse.ArgumentParser(description='I really want to write a clear discription of this program to help users, but you know what, this is a HELP DOCUMENT!!!! If anyone can understand the documentation of software without going to any forums, then that must be bullshit. So, lets talk about how to use this command: #$%^&*(*&^%$#$%^&*(&^%$#$%^&*(&^%$ ')
parser.add_argument('dir',help=' Directory of training texts',type=str)
parser.add_argument('dirT',help=' Directroy of testing texts',type=str)
parser.add_argument('train',help='Number of documents in training sets',type=int)
parser.add_argument('test',help='Number of documents in testing sets',type=int)
args = parser.parse_args()


####################################################################
print args.dir, args.dirT, args.train, args.test

numOfTrain =args.train
numOfTest = args.test

def get_tokens(i,dirc):
    with open(dirc + str(i),'r') as shakes:
         text = shakes.read()
         tokens = nltk.word_tokenize(text)
         return tokens
def get_corpus(i,dirc):
    with open(dirc + str(i),'r') as corpus:
         text = corpus.read()
         return text

def tf_idf(word,docidx):
    length = np.zeros((1,numOfTrain+20))
    occur = np.zeros((1,numOfTrain+20))        
    P = np.zeros((1,numOfTrain+20))
    PLOGP = np.zeros((1,numOfTrain+20))
    for i in range(docidx-1,docidx +20):
        tokens = get_tokens(i+1,str(args.dir)+'/')
        length[0,i] = len(tokens)
        occur[0,i] = tokens.count(word)
        P[0,i] = (occur[0,i]+1)/(length[0,i] + numOfTrain)
        PLOGP[0,i] = P[0,i]*np.log2(P[0,i])
    entropy = -np.tanh(PLOGP.sum())
    print word
    print entropy
        
        
        

filted = []
tokenList = []
tokenTupleList = ()
print('Gathering terms, please wait......')


for i in range(1,numOfTrain + 1):
    tokens = get_tokens(i,str(args.dir)+'/')
    listTemp = list(enumerate(tokens))
    for term in listTemp:
        if term[1] not in tokenList and len(term[1])>2:
           entropy = tf_idf(term[1],i)
           tokenList.append(term[1])
           if entropy < 0.4:
              filted.append(term[1])

print('Writing keywords to file')
with open('keys','w') as fKey:
     for i in range(1,len(filted)):
         fKey.write(str(filted[i])+'\t')

