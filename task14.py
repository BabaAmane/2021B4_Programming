import numpy as np

def idf(term, docs):
    df = 0
    N = len(docs)
    for doc in docs:
        df += term in doc
    return np.log10(N / df) + 1

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

for term in terms:
    print("idf(", term, ")=", idf(term, docs))
