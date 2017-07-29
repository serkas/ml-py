from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=2)

"""
with PdfPages('multipage_pdf.pdf') as pdf:
    fig, ax = plt.subplots(3, 3, figsize=(15, 15))
    plt.suptitle("iris_pairplot")

    for i in range(3):
        for j in range(3):
            ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=60)
            ax[i, j].set_xticks(())
            ax[i, j].set_yticks(())
            if i == 2:
                ax[i, j].set_xlabel(iris['feature_names'][j])
            if j == 0:
                ax[i, j].set_ylabel(iris['feature_names'][i + 1])
            if j > i:
                ax[i, j].set_visible(False)

    pdf.savefig()  # saves the current figure into a pdf page
"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])

acc = knn.score(X_test, y_test)

print(acc)