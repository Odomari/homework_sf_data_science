# Vulnerable_populations

## Содержание
[1. Описание задачи](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Deskription-of-task)
[2. Краткая информация о данных](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Short-information-about-data)
[3. Этапы работы](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Stages-of-work-on-the-task)
[4. Результаты](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Result)
[5. Заключения](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Conclusions)

### Описание задачи
Кластеризовать регионы России и определить, какие из них наиболее остро нуждаются в помощи малообеспеченным/неблагополучным слоям населения.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Contents)

### Краткая информация о данных
- additional_functions - папка с файлами .py, содержащими дополнительные функции для работы с данными.
- datasets_mod - папка с обработанными данными из исходных файлов, помещённые в отдельные файлы.
- read_data - папка с ноутбук-файлами .ipynb, содержащие в себе чтение каждого из исходных файлов, обработку данных и сохранение модифицированных данных в отдельные файлы с сохранением с папке read_data.
- social_russia_data - папка с исходными данными, с которыми необходимо работать.
- cleaned_clusterization_and_classification.ipynb - файл с проведением кластеризации на очищенных данных и классификацией тех регионов, которые оказались выбросами.
- merge_data.ipynb - файл, в котором все модифицированные данные из папки datasets_mod объединяются в один датафрейм с сохранением в файле merged_data.csv.
- non_cleaned_clusterization.ipynb - кластеризация всех регионов сразу.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Contents)

### Этапы работы
- чтение каждого из входных файлов (входные данные - в папке social_russia_data), анализ признаков, их преобразование и сохранение преобрзованных данных в файлы в папку datasets_mod. Большое внимание уделялось корреляции между признаками. Если признаки сильно коррелировали между собой, рассматривались разницы между соседними признаками. Корреляции между получавшимися признаками практически отсутствовали.
- объединение всех модифицированных данных в один датафрейм (файл merge_data.ipynb) с сохранением в один файл (файл merged_data.csv). Отбор признаков в зависимости от корреляции: остались только те признаки, корреляция у которых с другими прзнаками составляла не более, чем 0.9 по абсолютной величине.
- кластеризация всех регионов России сразу с приминением алгоритмов KMeans, EM-алгоритма и агломеративной кластеризации. Для отбора признаков и понижения размерности применялся алгоритм PCA.
- кластеризация на очищенном наборе данных. В кластеризации принимали участие только регионы, не попавшие в выбросы. Для определения того, к какому кластеру принадлежат регионы-выбросы, строилась модель классификации.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Contents)

### Результаты
Кластеризация проводилась на 2 признаках, полученных в результате работы алгоритма PCA на 70 признаках, что позволило сократить время кластеризации, а также визуализировать результаты.
На неочищенном наборе данных лучшим показал себя алгоритм KMeans с разбиением регионов на 3 кластера с коэффициентом силуэта, равным 0.59.
На очищенном наборе регионов (туда не вошли 9 из 85 регионов) самым лучшим оказалась агломеративная кластеризация с разбиением на 2 кластера и коэффициентом силуэта, равным 0.62.
Для определения регионов-выбросов рассматривались модели логистическая регрессия и дерево решений. Обе модели показали значение F1-меры в 0.67.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Contents)

### Conclusions
В итоге провели кластеризацию регионов России на 2 кластера. Регионами, которым необходимо выделение помощи, стали Республика Дагестан, Республика Ингушетия, Республика Кабардино-Балкария, Республика Карачаево-Черкессия, Республика Чечня и Республика Алтай.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/vulnerable_populations/README.md#Contents)