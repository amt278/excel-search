import flet as ft
import pandas as pd


def read_table(path):
    data = pd.read_excel(path)
    return data


def update_table(data):
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text(column_name)) for column_name in data.columns
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]) for row in data.values.tolist()
        ],
    )
    return table


def filter_table(data: pd.DataFrame, key, query):
    print(data[key].dtype)
    if data[key].dtype == 'int64':
        data = data[data[key] == int(query)]
    else:
        data = data[data[key].str.contains(query)]
    print(f'filtered data: {data}')
    table = update_table(data)
    return table
