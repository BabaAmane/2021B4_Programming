import numpy as np
from nlp import task15
from nlp import task16
import task12

docs = task12.docs
terms = task12.terms
tf_idf = task15.tf_idf(terms, docs)
len_docs = len(docs)
array = np.zeros((len_docs,len_docs))

for i in range(len(tf_idf)):
    for j in range(len(tf_idf)):
        array[i][j] = task16.cosine_sim(tf_idf[i], tf_idf[j])

print(array)


