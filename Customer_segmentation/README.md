# ЗАДАЧА. Сегментация клиентов

## Содержание
[1. Описание задачи](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Описание-задачи)
[2. Какую проблему решаем?](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Какую-проблему-решаем?)
[3. Краткая информация о данных](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Краткая-информация-о-данных)
[4. Этапы работы](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Этапы-работы)
[5. Результаты](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Результаты)
[6. Заключения](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Заключения)

### Описание задачи
Произвести сегментацию клиентов на основе их покупательской способности, частоты совершения заказов и срока давности последнего заказа, а также определить оптимальную стратегию взаимодействия с ними.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Содержание)

### Какую проблему решаем?
Построить модель кластеризации клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров.

**Что мы практикуем**
- применение алгоритмов кластеризации;
- применение алгоритмов снижения размерности.

### Краткая информация о данных
- customer_segmentation.ipynb - файл-ноутбук, содержащий решение задачи;
- customer_segmentation_project.csv - исходный набор данных о клиентах;
- customer_segmentation_project_cleaned.csv - очищенный от выбросов набор данных.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Содержание)

### Этапы работы
- Произвести предобработку набора данных.
- Провести разведывательный анализ данных и выявить основные закономерности.
- Сформировать категории товаров и клиентов. 
- Построить несколько моделей машинного обучения, решающих задачу кластеризации клиентов, определить количество кластеров и проинтерпретировать их.
- Спроектировать процесс предсказания категории интересов клиента и протестировать модель на новых клиентах.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Содержание)

### Результаты
Была произведена сегментация клиентов на 3 кластера алгоритмом KMeans на основе 2-ух признаков, полученных снижением размерности методом главных компонент (PCA). Также произведена сегментация на 7 кластеров тем же алгоритмом KMeans на 2-ух признаках, полученных снижением размерности методом t-SNE.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Содержание)

### Заключения
- получен опыт в применении алгоритмов кластеризации;
- получен опыт в применении алгоритмов снижения размерности;
- произведена сегментация клиентов;
- составлено описание каждого кластера, на основе которого можно применять разные стратегии по удержанию либо привлечению клиентов.

:arrow_up:[to contents](https://github.com/Odomari/homework_sf_data_science/tree/master/LinearAlgebraInLinearMethods/README.md#Содержание)