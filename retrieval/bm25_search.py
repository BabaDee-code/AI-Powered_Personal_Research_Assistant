from rank_bm25 import BM25Okapi

def bm25_search(query, corpus):
    bm25 = BM25Okapi(corpus)
    tokenized_query = query.split()
    return bm25.get_top_n(tokenized_query, corpus, n=5)
