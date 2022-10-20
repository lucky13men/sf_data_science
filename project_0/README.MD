# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)  
[6. Выводы](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)


### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под "угадать" имеется в виду "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрика качества**  
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем**  
- Учимся писать хороший код на *Python*.
- Учимся работать с *IDE*.
- Учимся работать с *GitHub*.


### Краткая информация о данных
....

:arrow_up:[к оглавлению](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Этапы работы над проектом
- За основу был взят файл *game_v2.py*.
- Выбран способ поиска числа при помощи метода Бинарный поиск.
- Доработана функция *random_predict* с учётом применения вышеуказанного метода поиска числа.

:arrow_up:[к оглавлению](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Результат
Написанный алгоритм угадывает число в среднем за 6 попыток, что соответствует заданным условиям проекта. Информация о версиях используемых библиотек и Python приведена в файлах requirements.txt и game_v3.ipynb.

:arrow_up:[к оглавлению](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Выводы
- Освоил написание корректного кода на *Python*.
- Освоил работу с *IDE*.
- Освоил работу с *GitHub*.
- Написал алгоритм поиска загаданного компьютером числа за минимальное минимальное число попыток с учётом всех условий соревнования.
- Оформил проект по PEP-8.
- Выложил проект в собственный учебный репозиторий на *GitHub*.

:arrow_up:[к оглавлению](https://github.com/lucky13men/sf_data_science/blob/main/project_0/README.MD#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)