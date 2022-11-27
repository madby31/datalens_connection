#!/usr/bin/env python
# coding: utf-8
# ver 1.1
import pandas as pd

def func_build_url(doc_id, sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid={sheet_id}'

def func_input(message):
    while True:
        data = input("Введите "+message+":\n")
        if data:
            break
    return data

doc_id = func_input('id документа') # Можете вместо функции сразу записать id
sheet_id_one = func_input('id первого листа') # Можете вместо функции сразу записать id
sheet_id_two = func_input('id второго листа') # Можете вместо функции сразу записать id
col_name_one = func_input('название 1 колонки') # Можете вместо функции сразу записать название
col_name_two = func_input('название 2 колонки') # Можете вместо функции сразу записать название
df_one = pd.read_csv(func_build_url(doc_id, sheet_id_one))
df_two = pd.read_csv(func_build_url(doc_id, sheet_id_two))
df = df_one.merge(df_two, left_on=col_name_one, right_on=col_name_two, how='left')
df.to_csv('data.csv', header=True, sep=";", encoding="cp1251", decimal=".", index=False)
print('Done!')
