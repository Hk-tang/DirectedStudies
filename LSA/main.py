import os

import pandas as pd
from nltk.corpus import stopwords
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def pre_process(documents):
    news_df = pd.DataFrame({'document': documents})

    # removing everything except alphabets`
    news_df['clean_doc'] = news_df['document'].str.replace("[^a-zA-Z#]", " ")

    # removing short words
    news_df['clean_doc'] = news_df['clean_doc'].apply(
        lambda x: ' '.join([w for w in x.split() if len(w) > 3]))

    # make all text lowercase
    news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())

    return news_df


def remove_stopwords(dataframe):
    stop_words = stopwords.words('english')

    # tokenization
    tokenized_doc = dataframe['clean_doc'].apply(lambda x: x.split())

    # remove stop-words
    tokenized_doc = tokenized_doc.apply(
        lambda x: [item for item in x if item not in stop_words])

    # de-tokenization
    detokenized_doc = []
    for i in range(len(dataframe)):
        t = ' '.join(tokenized_doc[i])
        detokenized_doc.append(t)

    dataframe['clean_doc'] = detokenized_doc

    return dataframe


def create_document_term_matrix(dataframe):
    vectorizer = TfidfVectorizer(stop_words='english',
                                 max_features=None,  # keep top 1000 terms
                                 max_df=0.5,
                                 smooth_idf=True)

    X = vectorizer.fit_transform(dataframe['clean_doc'])

    # print(X.shape)  # check shape of the document-term matrix

    return vectorizer, X


def create_svd(matrix, num_topics):
    # SVD represent documents and terms in vectors
    model = TruncatedSVD(n_components=num_topics, algorithm='randomized',
                             n_iter=100, random_state=122)

    model.fit(matrix)

    # print(len(model.components_))

    return model


def read_data(directory):
    data = []
    for filename in os.listdir(directory):
        with open(os.path.normpath(os.path.join(directory, filename)), "r") as file:
            data.append(file.read())
    return data


if __name__ == '__main__':
    pd.set_option("display.max_colwidth", 200)
    # dataset = fetch_20newsgroups(shuffle=True, random_state=1,
    #                              remove=('headers', 'footers', 'quotes'))
    # # data is a list where each element is a document as one string
    # data = dataset.data
    data = read_data(os.path.normpath("data/hc.apache.org"))
    # print(len(data))
    data = pre_process(data)
    data = remove_stopwords(data)
    vectorizer, matrix = create_document_term_matrix(data)

    # for j in range(1, 21):
    svd_model = create_svd(matrix, 30)

    terms = vectorizer.get_feature_names()

    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:7]
        items = []
        for t in sorted_terms:
            items.append(t[0])
        print("Topic " + str(i + 1) + ": ", ", ".join(items))
