# Project-5. New York City Taxi Trip Duration

## Содержание
[1. Описание задачи](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Deskription-of-task)
[2. Какую проблему решаем?](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#What-problem-are-we-solving?)
[3. Краткая информация о данных](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Short-information-about-data)
[4. Этапы работы над задачей](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Stages-of-work-on-the-task)
[5. Результат](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Result)
[6. Выводы](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Conclusions)

### Описание задачи
Построить модель МО, которая будет на основе предложенных характеристик предсказывать общую продолжительность поездки такси в Нью-Йорке.

:arrow_up:[to Содержание](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Contents)

### Какую проблему решаем?
Предсказать общую продолжительность поездки такси, то есть решить задачу регрессии.

**Что практикуем?**
Отрабатываем навыки работы с несколькими источниками данных, генерации признаков, разведывательного анализа и визуализации данных, отбора признаков и, конечно же, построения моделей машинного обучения!

### Краткая информация о данных
- New York City Taxi Trip Duration.ipynb - файл-ноутбук с готовым решением;
- holiday_data.csv - исходный файл с праздничными датами (https://lms.skillfactory.ru/assets/courseware/v1/33bd8d5f6f2ba8d00e2ce66ed0a9f510/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/holiday_data.csv);
- osrm_data_test.csv - файл с данными из OSRM API для тестовой выборки (https://drive.google.com/file/d/1wCoS-yOaKFhd1h7gZ84KL9UwpSvtDoIA/view?usp=sharing);
- osrm_data_train.csv - файл с данными из OSRM для поездок из тренировочной таблицы (https://drive.google.com/file/d/1ecWjor7Tn3HP7LEAm5a0B_wrIfdcVGwR/view?usp=sharing);
- test.csv - файл с тестовой выборкой (https://drive.google.com/file/d/1C2N2mfONpCVrH95xHJjMcueXvvh_-XYN/view?usp=sharing);
- train.csv - тренировочный датасет (https://drive.google.com/file/d/1X_EJEfERiXki0SKtbnCL9JDv49Go14lF/view?usp=sharing);
- weather_data.csv - набор данных, содержащий информацию о погодных условиях в Нью-Йорке в 2016 году (https://lms.skillfactory.ru/assets/courseware/v1/0f6abf84673975634c33b0689851e8cc/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/weather_data.zip)

:arrow_up:[to Содержание](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Contents)

### Этапы работы над задачей
- формирование набора данных на основе нескольких источников информации;
- проектирование новых признаков с помощью Feature Engineering и выявление наиболее значимых при построении модели;
- исследование предоставленных данных и выявление закономерностей;
- построение нескольких моделей и выбор из них наилучшей по заданной метрике;
- проектирование процесса предсказания времени длительности поездки для новых данных

:arrow_up:[to Содержание](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Contents)

### Результат
Для решения задачи были построены несколько моделей МО:
- модель линейной регрессии,
- модель полиномиальной регрессии 2-ой степени,
- модель полиномиальной регрессии 2-ой степени с L2-регуляризацией,
- модель дерева решений,
- модель случайного леса,
- модель градиентного бустинга над решающими деревьями,
- модель экстремального градиентного бустинга.
После обучения этих моделей на тренировочном наборе данных и проверке их качества стало понятно, что самыми эффективными моделями среди построенных моделей оказались модели градиентного бустинга. Их ошибка предсказания (в качестве метрики качества использовалась метрика RMSLE (Root Mean Squared Log Error)) составила примерно 0.39. А медианная абсолютная ошибка (MeAE) модели градиентного бустинга над решающими деревьями составила 1.8 секунды.

:arrow_up:[to Содержание](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Contents)

### Выводы
Мы справились с настоящим проектом, решив важную и актуальную задачу. Теперь мы можем решить полноценную задачу регрессии, начиная от предобработки данных и заканчивая оценкой качества построенных моделей и отбора наиболее значимых факторов.

:arrow_up:[to Содержание](https://github.com/Odomari/homework_sf_data_science/tree/master/Project-5/README.md#Contents)