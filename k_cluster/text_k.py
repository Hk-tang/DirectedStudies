import os
import argparse

import matplotlib.pyplot as plt
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


def elbow(Y_sklearn, documentname):
    number_clusters = range(1, 7)

    kmeans = [KMeans(n_clusters=i, max_iter=600) for i in number_clusters]

    score = [kmeans[i].fit(Y_sklearn).score(Y_sklearn) for i in range(len(kmeans))]
    score = [i * -1 for i in score]

    plt.plot(number_clusters, score)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title(documentname.split("/")[-1])
    if not os.path.exists("results/" + documentname.split("/")[0]):
        os.makedirs("results/" + documentname.split("/")[0])
    plt.savefig("results/" + documentname)
    # plt.show()


def transform(dataframe):
    data = dataframe['contents']
    # data.head()

    tf_idf_vectorizor = TfidfVectorizer(stop_words='english',  # tokenizer = tokenize_and_stem,
                                        max_features=5000)
    tf_idf = tf_idf_vectorizor.fit_transform(data)
    tf_idf_norm = normalize(tf_idf)
    tf_idf_array = tf_idf_norm.toarray()
    # print(pd.DataFrame(tf_idf_array, columns=tf_idf_vectorizor.get_feature_names()).head())

    return tf_idf_array


# Read all files within a directory
def read_data(directory):
    file_contents = {
        "filenames": [],
        "contents": []
    }
    for root, _, files in os.walk(directory):
        for file in files:
            with open(os.path.normpath(os.path.join(root, file)), "r") as f:
                file_contents["filenames"].append(file)
                file_contents["contents"].append(f.read())
    return file_contents


def plot(data, documentname):
    elbow(data, documentname)

    # This code is if you want to see the clusterings themselves
    # kmeans = KMeans(n_clusters=1, max_iter=600, algorithm='auto')
    # fitted = kmeans.fit(data)
    # prediction = kmeans.predict(data)
    #
    # plt.scatter(data[:, 0], data[:, 1], c=prediction, s=50, cmap='viridis')
    #
    # plt.show()
    #
    # centers2 = fitted.cluster_centers_
    # plt.scatter(centers2[:, 0], centers2[:, 1], c='black', s=300, alpha=0.6);
    #
    # plt.show()


if __name__ == '__main__':
    plt.style.use('classic')
    base_path = "data/"  # e.g., data/apache
    for root, libs, _ in os.walk(base_path):
        for lib in libs:
            for lib_root, docs, files in os.walk(os.path.normpath(root + "/" + lib)):
                for doc in docs:
                    raw_data = read_data(os.path.normpath(lib_root + "/" + doc))

                    df = pd.DataFrame.from_dict(raw_data)
                    tf_idf_array = transform(df)

                    sklearn_pca = PCA(n_components=2)
                    Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

                    plot(Y_sklearn, lib + "/" + doc.capitalize())

