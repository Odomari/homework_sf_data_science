import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from functools import singledispatch
from scipy.stats import normaltest

# список с шаблонами для работы с библиотекой re (библиотека для работы с регулярными выражениями) по каждому региону РФ.
templates = ['\s*Белгородская.+', '\s*Брянская.+', '\s*Владимирская.+', '\s*Воронежская.+', '\s*Ивановская.+', '\s*Калужская.+',
       '\s*Костромская.+', '\s*Курская.+', '\s*Липецкая.+', '\s*Московская.+', '\s*Орловская.+', '\s*Рязанская.+',
       '\s*Смоленская.+', '\s*Тамбовская.+', '\s*Тверская.+', '\s*Тульская.+', '\s*Ярославская.+', '.*Москва.*',
       '[\w|\s]*\\bКарел[\w|\s]+', '[\w|\s]*\\bКоми', '\s*Ненецкий.+|НАО', '\s*Вологодская.+', '\s*Калининградская.+',
       '\s*Ленинградская.+', '\s*Мурманская.+', '\s*Новгородская.+', '\s*Псковская.+', '.*Санкт-Петербург.*', '[\w|\s|\(|-]*\\bАдыгея\)?',
       '[\w|\s]*\\bКалмык[\w|\s]+', '[\w|\s]*\\bКрым[\w|\s]*', '\s*Краснодарский.+', '\s*Астраханская.+', '\s*Волгоградская.+', '\s*Ростовская.+',
       '.*Севастополь.*', '[\w|\s]*\\bДагестан[\w|\s]*', '[\w|\s]*\\bИнгуш[\w|\s]+',
       '[\w|\s]*\\bКабардино-Балкар[\w|\s]+', '[\w|\s]*\\bКарачаево-Черкес[\w|\s]+', '[\w|\s|\(|-]*\\bАлания[\w|\s]*\)?',
       '[\w|\s]*\\bЧеч[\w|\s]+', '\s*Ставропольский.+', '[\w|\s]*\\bБашк[\w|\s]+',
       '[\w|\s]*\\bМарий[\w|\s]+', '[\w|\s]*\\bМордов[\w|\s]+', '[\w|\s|\(|-]*\\bТатар[\w|\s]*\)?',
       '[\w|\s]*\\bУдмурт[\w|\s]+', '[\w|\s|\(|-]*\\bЧуваш[\w|\s]*\)?', '[\w|\s]*\\bПермский[\w|\s]+', '\s*Кировская.+', '\s*Нижегородская.+', '\s*Оренбургская.+',
       '\s*Пензенская.+', '\s*Самарская.+', '\s*Саратовская.+', '\s*Ульяновская.+', '\s*Курганская.+', '\s*Свердловская.+',
       '\s*Хант.+|\s*ХМАО|\s*Югра', '\s*Ямал.+|\s*ЯНАО', '\s*Челябинская.+', '\s*Респ.+Алтай|\s*Алтай.+респ.+', '[\w|\s]*\\bТ[ы|у]в[\w|\s]+',
       '[\w|\s]*\\bХакас[\w|\s]+', '\s*Алтайский.+', '[\w|\s]*\\bКрасноярский[\w|\s]+', '\s*Иркутская.+', '\s*Кемеровская.+', '\s*Новосибирская.+',
       '\s*Омская.+', '\s*Томская.+', '\s*Респ.+Бурят.+|\s*Бурят.+респ.+', '[\w|\s|\(|-]*\\bЯкут[\w|\s]*\)?', '\s*Забайкальский.+', '[\w|\s]*\\bКамчатский[\w|\s]+',
       '\s*Приморский.+', '\s*Хабаровский.+', '\s*Амурская.+', '\s*Магаданская.+', '\s*Сахалинская.+', '\s*Еврейская.+|\s*ЕАО', '\s*Чукотский.+|\s*ЧАО']

# отдельный список шаблонов для Архангельской и Тюменской областей.
templates_specials = ['\s*Архангельская.+', '\s*Тюменская.+']

# Словарь, ключами которого являются шаблоны из списков выше, а значениями - полные названия регионов. Дело в том, что в разных
# файлах с данными регионы РФ могут называться по разному, например, Чувашия или Чувашская Республика и пр. Этот словарь будет
# использоваться для переименования изначальных названий регионов в те, которые мы считаем удобными для нас, чтобы затем в процессе
# объединения данных в один датафрейм, у нас не возникло конфликтов из-за разного названия регионов.
dictionary = {
       '\s*Белгородская.+': 'Белгородская область', '\s*Брянская.+': 'Брянская область', '\s*Владимирская.+': 'Владимирская область',
       '\s*Воронежская.+': 'Воронежская область', '\s*Ивановская.+': 'Ивановская область', '\s*Калужская.+': 'Калужская область',
       '\s*Костромская.+': 'Костромская область', '\s*Курская.+': 'Курская область', '\s*Липецкая.+': 'Липецкая область',
       '\s*Московская.+': 'Московская область', '\s*Орловская.+': 'Орловская область', '\s*Рязанская.+': 'Рязанская область',
       '\s*Смоленская.+': 'Смоленская область', '\s*Тамбовская.+': 'Тамбовская область', '\s*Тверская.+': 'Тверская область',
       '\s*Тульская.+': 'Тульская область', '\s*Ярославская.+': 'Ярославская область', '.*Москва.*': 'Москва',
       '[\w|\s]*\\bКарел[\w|\s]+': 'Республка Карелия', '[\w|\s]*\\bКоми': 'Республика Коми', '\s*Ненецкий.+|НАО': 'Ненецкий автономный округ',
       '\s*Архангельская.+': 'Архангельская область', '\s*Вологодская.+': 'Вологодская область', '\s*Калининградская.+': 'Калининградская область',
       '\s*Ленинградская.+': 'Ленинградская область', '\s*Мурманская.+': 'Мурманская область', '\s*Новгородская.+': 'Новгородская область',
       '\s*Псковская.+': 'Псковская область', '.*Санкт-Петербург.*': 'Санкт-Петербург', '[\w|\s|\(|-]*\\bАдыгея\)?': 'Республика Адыгея',
       '[\w|\s]*\\bКалмык[\w|\s]+': 'Республика Калмыкия', '[\w|\s]*\\bКрым[\w|\s]*': 'Республика Крым', '\s*Краснодарский.+': 'Краснодарский край',
       '\s*Астраханская.+': 'Астраханская область', '\s*Волгоградская.+': 'Волгоградская область', '\s*Ростовская.+': 'Ростовская область',
       '.*Севастополь.*': 'Севастополь', '[\w|\s]*\\bДагестан[\w|\s]*': 'Республика Дагестан', '[\w|\s]*\\bИнгуш[\w|\s]+': 'Республика Ингушетия',
       '[\w|\s]*\\bКабардино-Балкар[\w|\s]+': 'Республика Кабардино-Балкария', '[\w|\s]*\\bКарачаево-Черкес[\w|\s]+': 'Республика Карачаево-Черкессия',
       '[\w|\s|\(|-]*\\bАлания[\w|\s]*\)?': 'Республика Северная Осетия-Алания', '[\w|\s]*\\bЧеч[\w|\s]+': 'Республика Чечня', '\s*Ставропольский.+': 'Ставропольский край',
       '[\w|\s]*\\bБашк[\w|\s]+': 'Республика Башкортостан', '[\w|\s]*\\bМарий[\w|\s]+': 'Республика Марий Эл', '[\w|\s]*\\bМордов[\w|\s]+': 'Республика Мордовия',
       '[\w|\s|\(|-]*\\bТатар[\w|\s]*\)?': 'Республика Татарстан', '[\w|\s]*\\bУдмурт[\w|\s]+': 'Республика Удмуртия', '[\w|\s|\(|-]*\\bЧуваш[\w|\s]*\)?': 'Республика Чувашия',
       '[\w|\s]*\\bПермский[\w|\s]+': 'Пермский край', '\s*Кировская.+': 'Кировская область', '\s*Нижегородская.+': 'Нижегородская область',
       '\s*Оренбургская.+': 'Оренбургская область', '\s*Пензенская.+': 'Пензенская область', '\s*Самарская.+': 'Самарская область',
       '\s*Саратовская.+': 'Саратовская область', '\s*Ульяновская.+': 'Ульяновская область', '\s*Курганская.+': 'Курганская область',
       '\s*Свердловская.+': 'Свердловская область', '\s*Хант.+|\s*ХМАО|\s*Югра': 'Ханты-Мансийский автономный округ - Югра',
       '\s*Ямал.+|\s*ЯНАО': 'Ямало-Ненецкий автономный округ', '\s*Тюменская.+': 'Тюменская область',
       '\s*Челябинская.+': 'Челябинская область', '\s*Респ.+Алтай|\s*Алтай.+респ.+': 'Республика Алтай', '[\w|\s]*\\bТ[ы|у]в[\w|\s]+': 'Республика Тыва',
       '[\w|\s]*\\bХакас[\w|\s]+': 'Республика Хакасия', '\s*Алтайский.+': 'Алтайский край', '[\w|\s]*\\bКрасноярский[\w|\s]+': 'Красноярский край',
       '\s*Иркутская.+': 'Иркутская область', '\s*Кемеровская.+': 'Кемеровская область', '\s*Новосибирская.+': 'Новосибирская область',
       '\s*Омская.+': 'Омская область', '\s*Томская.+': 'Томская область', '\s*Респ.+Бурят.+|\s*Бурят.+респ.+': 'Республика Бурятия',
       '[\w|\s|\(|-]*\\bЯкут[\w|\s]*\)?': 'Республика Саха - Якутия', '\s*Забайкальский.+': 'Забайкальский край', '[\w|\s]*\\bКамчатский[\w|\s]+': 'Камчатский край',
       '\s*Приморский.+': 'Приморский край', '\s*Хабаровский.+': 'Хабаровский край', '\s*Амурская.+': 'Амурская область',
       '\s*Магаданская.+': 'Магаданская область', '\s*Сахалинская.+': 'Сахалинская область', '\s*Еврейская.+|\s*ЕАО': 'Еврейская автономная область',
       '\s*Чукотский.+|\s*ЧАО': 'Чукотский автономный округ'
}


def to_modify_dataframe(dataframe: pd.DataFrame, drop=True):
    """Функция переименовывает регионы России под наши требования, чтобы в датафреймах регионы назывались одинаково.
       Кроме того, для простоты функция удаляет столбцы, в которых есть хотя бы одно пропущенное значение. На самом деле,
       это даже логично, поскольку нам предлагается среди прочих проанализировать Республику Крым и город Севастополь, по которым
       данных до 2015 год, нет.

    Args:
        dataframe (pd.DataFrame): датафрейм, в котором происходят преобразования.
        drop: булевый параметр. Если значение равно True, то будем удалять столбцы с пропущенными значениями. Если же значение
        параметра равно False, то удалять не нужно. По умолчанию равен True.

    Returns:
        pd.DataFrame: преобразованный датасет.
    """
    regions = dataframe.index.to_list()
    templates_self = templates.copy()
    templates_specials_self = templates_specials.copy()
    dataframe_mod = {}
    
    # Проходя по каждому региону РФ, ищем соответствующий ему шаблон. Если такое совпадение нашлось, то записываем регион
    # в том виде, в каком он задан в словаре (dictionary) выше.
    for region in regions:
        for template in templates_self:
            if re.fullmatch(template, region, flags=re.DOTALL):
                dataframe_mod[dictionary[template]] = dataframe.loc[region]
                templates_self.remove(template)
                break
    
    # почему Архангельская и Тюменская области рассматриваются отдельно? Потому что есть другие регионы РФ, в названиях которых
    # в исходных excel или csv-таблицах, могут быть написаны Архангельская либо Тюменская область. Таким образом, шаблону, например,
    # для Архангельской области будут соответствовать несколько записей из исходных таблиц.
    # Такая запись происходит потому, что, например, Ненецкий автономный округ (НАО) раньше входил в состав Архангельской области,
    # но сейчас является самостоятельным регионом. Поэтому в исходных таблицах очень часто можно встретить записи "Архангельская
    # область", "Ненецкий автономный округ" и "Архангельская область (без автномного округа)". Соотвественно в первой записи
    # записаны данные, когда два региона были одним, что для нас уже не актуально. Но если проводить поиск по Архангельской
    # области так же, как и по всем другим, то на один шаблон, найдётся два, а иногда и три. Поэтому Архангельскую область
    # обрабатываем так, как написано ниже.
    # Выше сказанное справедливо и для Тюменской области, когда-то включавшей в себя Ханты-Мансийский автномный округ (ХМАО) и
    # Ямало-Ненецкий автономный округ (ЯНАО).
    for template in templates_specials_self:
        match_list = []
        for region in regions:
            if re.fullmatch(template, region, re.DOTALL):
                match_list.append(region)
        max_len = len(match_list[0])
        index_max_len = -1
        for i, region in enumerate(match_list):
            if len(region) > max_len:
                index_max_len = i
        dataframe_mod[dictionary[template]] = dataframe.loc[match_list[index_max_len]]
    
    dataframe_mod = pd.DataFrame(index=dataframe_mod.keys(), columns=dataframe.columns, data=dataframe_mod.values())
    
    # удаляем столбцы, где есть есть пропущенные значения.
    if drop:
        dataframe_mod = dataframe_mod.dropna(axis=1)
    
    # после преобразований будем выводить итоговое число регионов России, которых должно быть 85. Это своеобразная проверка на то,
    # что в ходе преобразований я не потерял никакой из нужных регионов.
    print(f'Число регионов России - {len(dataframe_mod.index)}.')
    
    """columns = dataframe_mod.columns
    for column in columns:
        try:
            words = column.split(' ')
            for word in words:
                if word.isdigit():
                    if int(word) < 2015:
                        columns = columns.drop(column)
        except AttributeError:
            if column < 2015:
                columns = columns.drop(column)
    dataframe_mod = dataframe_mod[columns]"""
    
    return dataframe_mod


@singledispatch
def print_hist_and_box(dataframe: pd.DataFrame):
    """Функция выводит распределение всех признаков из dataframe в виде гистограммы и коробчатой диаграммы.

    Args:
        dataframe (pd.DataFrame): датафрейм, признаки которого необходимо посмотреть.
    """
    axes = plt.subplots(nrows=dataframe.shape[1], ncols=2, figsize=(10, 30))[1]
    for i, column in enumerate(dataframe.columns):
        sns.histplot(data=dataframe[column], ax=axes[i][0]);
        sns.boxplot(x=dataframe[column], ax=axes[i][1]);


@print_hist_and_box.register
def _(feature: pd.Series):
    """Функция выводит распределение признака в виде гистограммы и коробчатой диаграммы.

    Args:
        feature (pd.Series): признак, который необходимо посмотреть.
    """
    axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))[1]
    sns.histplot(data=feature, ax=axes[0]);
    sns.boxplot(data=feature, ax=axes[1], orient='h');


# start_year: int, end_year: int, feature: str,
def transform_to_changes(dataframe: pd.DataFrame, shift=1, not_percent=True):
    """Функция считает разность между признаками, находящимися на расстоянии shift.

    Args:
        dataframe (pd.DataFrame): датафрейм, в котором происходят преобразования.
        shift (int, optional): Число, показывающее, на каком расстоянии находятся признаки (столбцы), между которыми нужно считать
        разность. По умолчанию берутся соседние столбцы, то есть равно 1.
        is_percent (bool, optional): Индикатор того, являются ли изначальные значения в признаках процентами или нет. Если это -
        проценты, то их просто вычитаем. В противном случае, считается отношение разности между признаками к вычитаемому признаку,
        и полученное отношение умножается на 100 (для счёта в процентах). По умолчанию исходные признаки - не проценты, то есть
        аргумент равен True.

    Returns:
        pd.DataFrame: преобразованный датафрейм.
    """
    changes = list()
    if not_percent:
        for index in dataframe.index:
            values = dataframe.loc[index].values
            changes_index = list()
            for i in range(shift, len(values)):
                changes_index.append(round((values[i] - values[i - shift]) / values[i - shift] * 100, 6))
            changes.append(changes_index)
        changes = np.array(changes)
    else:
        for index in dataframe.index:
            values = dataframe.loc[index].values
            changes_index = list()
            for i in range(shift, len(values)):
                changes_index.append(values[i] - values[i - shift])
            changes.append(changes_index)
        changes = np.array(changes)
    return pd.DataFrame(
        changes,
        index=dataframe.index.to_list(),
        columns=dataframe.columns[shift:]
        #[f'Динамика {feature} на {i} г., в %' for i in range(start_year, end_year)]
        #dataframe.columns.delete(0)
    )


def to_evaluate_corr_pairs(dataframe: pd.DataFrame, limit: float):
    """Функция вычисляет все пары признаков, корреляция между которыми не менее заданного порога по абсолютной величине.

    Args:
        dataframe (pd.DataFrame): исходный датафрейм.
        limit (float): заданное пороговое значение для корреляции.

    Returns:
        list: список с парами коррелированных признаков.
    """
    corr_tab = dataframe.corr()
    corr_pairs = []
    for i in range(len(corr_tab.columns)):
        for j in range(0, len(corr_tab.index)):
            if i >= j:
                continue
            if (np.abs(corr_tab[corr_tab.columns[i]].iloc[j]) >= limit) and (corr_tab.columns[i] != corr_tab.index[j]):
                corr_pairs.append([corr_tab.columns[i], corr_tab.index[j]])
    return corr_pairs


def outliers_z_score(data: pd.DataFrame, feature: str):
    """Функция находит выбросы по заданному признаку.

    Args:
        data (pd.DataFrame): исходный датасет.
        feature (str): рассматриаемый признак.

    Returns:
        pd.DataFrame: найденные выбросы.
    """
    mu = data[feature].mean()
    sigma = data[feature].std()
    lower_bound = mu - 3 * sigma
    upper_bound = mu + 3 * sigma
    outliers = data[(data[feature] < lower_bound) | (data[feature] > upper_bound)]
    return outliers


def stat_test(data: pd.Series):
    """Функция проводит тест на нормальность Д'Агостино.

    Args:
        data (pd.Series): данные для теста.

    Returns:
        bool: True, если данные распределены нормально, False - иначе.
    """
    # Пусть H0 - гипотеза о том, что данные распределены нормально, а Ha - альтернативняа гипотеза.

    alpha = 0.05

    _, p = normaltest(data)
    if p > alpha/2:
        # приниамем гипотезу H0, то есть данные распределены нормально
        return True
    else:
        # отвергаем гипотезу H0
        return False