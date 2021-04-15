import numpy as np
import task13
import task14

def tf_idf(terms, docs):
    tf = []
    idf = []

    for i in range(len(terms)):
        idf.append(task14.idf(terms[i], docs))
    
    for i in range(len(terms)):
        tf_s = []
        for j in range(len(docs)):
            tf_s.append(task13.tf(terms[j], docs[i]))
        tf.append(tf_s)

    idf_array = np.array(idf)
    tf_array = np.array(tf)

    return idf_array * tf_array

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

print(tf_idf(terms, docs))
