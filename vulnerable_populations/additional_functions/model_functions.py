import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score

def to_evaluate_optimal_components(dataframe: pd.DataFrame, components: {int, float}, cluster_algorithm: str, clusters: np.ndarray):
    """При фиксированном числе компонент алгоритма PCA функция перебирает число кластеров для алгоритма кластеризации.
    Для каждого числа кластеров вычисляются коэффициент силуэта и индекс Дэвиса-Болдина. Функция возвращает максимальный коэффициент силуэта,
    минимальный индекс Дэвиса-Болдина и число кластеров при этих метриках.

    Args:
        dataframe (pd.DataFrame): датафрейм, по которому проводятся расчёты.
        components (int, float): число главных компонент алгоритма PCA.
        cluster_algorithm (str): алгоритм кластеризации, который хотим применить. Допустимые значения: 'KMeans', 'GaussianMixture' и
        'AgglomerativeClustering'.

    Returns:
        tuple: множество, состоящее из числа компонент, пары максимального коэффициента силуэта и чисел кластеров, при которых получается
        такой коэффициент, и пары минимального индекса Дэвиса-Болдина и чисел кластеров, при которых получается такой индекс.
    """
    
    # применяем алгоритм понижения размерности
    pca = PCA(n_components=components, random_state=42)
    pca.fit(dataframe)
    dataframe_reducted = pca.transform(dataframe)
    dataframe_reducted = pd.DataFrame(data=dataframe_reducted, index=dataframe.index)
    
    silhouettes = []
    db_scores = []
    
    # применяем кластеризацию
    if cluster_algorithm == "KMeans":
        for cluster in clusters:
            kmeans = KMeans(n_clusters=cluster, random_state=42, n_init=10)
            kmeans.fit(dataframe_reducted)
            silhouettes.append(np.round(silhouette_score(dataframe_reducted, kmeans.labels_), 6))
            db_scores.append(np.round(davies_bouldin_score(dataframe_reducted, kmeans.labels_), 6))
    elif cluster_algorithm == "GaussianMixture":
        for cluster in clusters:
            gm = GaussianMixture(n_components=cluster, random_state=42)
            gm.fit(dataframe_reducted)
            silhouettes.append(np.round(silhouette_score(dataframe_reducted, gm.predict(dataframe_reducted)), 6))
            db_scores.append(np.round(davies_bouldin_score(dataframe_reducted, gm.predict(dataframe_reducted)), 6))
    elif cluster_algorithm == "AgglomerativeClustering":
        for cluster in clusters:
            agglomerative = AgglomerativeClustering(n_clusters=cluster)
            agglomerative.fit(dataframe_reducted)
            silhouettes.append(np.round(silhouette_score(dataframe_reducted, agglomerative.labels_), 6))
            db_scores.append(np.round(davies_bouldin_score(dataframe_reducted, agglomerative.labels_), 6))
    else:
        print("Некорректный ввод для алгоритма кластеризации. Допустимые значения: 'KMeans', 'GaussianMixture' и 'AgglomerativeClustering'.")
        return
    
    # выбираем число кластеров, при которых наблюдается максимальный коэффициент силуэта
    max_silhouette = np.max(silhouettes)
    clusters_silhouette = []
    try:
        while silhouettes.index(max_silhouette) > -1:
            clusters_silhouette.append(clusters[silhouettes.index(max_silhouette)])
            silhouettes.remove(max_silhouette)
    except ValueError:
        pass
    
    # выбираем число кластеров, при которых наблюдается минимальный индекс Дэвиса-Болдина
    min_db_score = np.min(db_scores)
    clusters_db_score = []
    try:
        while db_scores.index(min_db_score) > -1:
            clusters_db_score.append(clusters[db_scores.index(min_db_score)])
            silhouettes.remove(min_db_score)
    except ValueError:
        pass
    
    return (components, (max_silhouette, clusters_silhouette), (min_db_score, clusters_db_score))


def to_evaluate_optimal_metrics(dataframe: pd.DataFrame, array_components: np.ndarray, cluster_algorithm: str, clusters: np.ndarray):
    """По заданному алгоритму кластеризации, а также по заданному диапазону значений кластеров считает коэффициенты
    силуэта и индекс Дэвиса-Болдина и выводит параметры, при которых наблюдаются оптимальные коэффициент и индекс.

    Args:
        dataframe (pd.DataFrame): датафрейм, по которому проводятся расчёты.
        components (int, float): число главных компонент алгоритма понижения размерности.
        cluster_algorithm (str): алгоритм кластеризации, который хотим применить. Допустимые значения: 'KMeans', 'GaussianMixture' и
        'AgglomerativeClustering'.
    """
    metrics = []
    for n_components in array_components:
        metrics.append(to_evaluate_optimal_components(
            dataframe=dataframe,
            components=n_components,
            cluster_algorithm=cluster_algorithm,
            clusters=clusters)
                       )
    
    # выводим параметры, при которых получается максимальный коэффициент силуэта
    metrics.sort(key=lambda metric: metric[1][0], reverse=True)
    silhouette_opt = metrics[0]
    print(f"Максимальный коэффициент силуэта, равный {silhouette_opt[1][0]}, получается при {silhouette_opt[0]} главных компонентах.")
    print(f"Число кластеров при максимальном коэффициенте силуэта - {silhouette_opt[1][1]}.")
    # на тот случай, если комбинаций параметров, при которых получается максимальный коэффициент силуэта, не одна
    i = 1
    while metrics[i][1][0] == silhouette_opt[1][0]:
        print(f"Максимальный коэффициент силуэта также получается при {metrics[i][0]} главных компонентах.")
        print(f"Число кластеров - {metrics[i][1][1]}.")
    
    # и то же самое делаем для минимального индекса Дэвиса-Болдина
    metrics.sort(key=lambda metric: metric[2][0])
    db_score_opt = metrics[0]
    print(f"Минимальный индекс Дэвиса-Болдина, равный {db_score_opt[2][0]}, получается при {db_score_opt[0]} главных компонентах.")
    print(f"Число кластеров при минимальном индексе Дэвиса-Болдина - {db_score_opt[2][1]}.")
    # на тот случай, если комбинаций параметров, при которых получается минимальный индекс Дэвиса-Болдина, не одна
    i = 1
    while metrics[i][2][0] == db_score_opt[2][0]:
        print(f"Максимальный коэффициент силуэта также получается при {metrics[i][0]} главных компонентах.")
        print(f"Число кластеров - {metrics[i][2][1]}.")