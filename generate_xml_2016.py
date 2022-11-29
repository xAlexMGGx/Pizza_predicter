import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom


def extract():
    pizzas = pd.read_csv('ORIGINALS/pizzas.csv')
    pizza_types = pd.read_csv('ORIGINALS/pizza_types.csv', encoding='latin-1')
    orders = pd.read_csv('ORIGINALS/orders_2016.csv', sep=';')
    order_details = pd.read_csv('ORIGINALS/order_details_2016.csv', sep=';', encoding='latin-1')
    data_dictionary = pd.read_csv('ORIGINALS/data_dictionary.csv')
    return pizzas, pizza_types, orders, order_details, data_dictionary

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def main():
    pizzas, pizza_types, orders, order_details, data_dictionary = extract()
    data = {}
    dfs = [pizzas, pizza_types, orders, order_details, data_dictionary]
    df_names = ['pizzas', 'pizza_types', 'orders', 'order_details', 'data_dictionary']
    for idx, df in enumerate(dfs):
        data[df_names[idx]] = {}
        data[df_names[idx]]['length'] = df.shape[0]
        data[df_names[idx]]['columns'] = {}
        for column in df.columns:
            data[df_names[idx]]['columns'][column] = {}
            data[df_names[idx]]['columns'][column]['dtype'] = df[column].dtype
            data[df_names[idx]]['columns'][column]['unique'] = df[column].nunique()
            data[df_names[idx]]['columns'][column]['nulls'] = df[column].isnull().sum()
    root1 = ET.Element('data')
    for df_name in df_names:
        df = ET.SubElement(root1, df_name)
        ET.SubElement(df, 'length').text = str(data[df_name]['length'])
        columns = ET.SubElement(df, 'columns')
        for column in data[df_name]['columns']:
            col = ET.SubElement(columns, column)
            for key in data[df_name]['columns'][column]:
                ET.SubElement(col, key).text = str(data[df_name]['columns'][column][key])

    with open('data_report_2016.xml', 'w') as f:
        f.write(prettify(root1))