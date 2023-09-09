from solution_1.data_etl import Datasource_A, Datasource_B

def transform_data(dtasource_name):
    if dtasource_name == 'datasource_a':
        transformer = Datasource_A()
    elif dtasource_name == 'datasource_b':
        transformer = Datasource_B()

    transformer.transform()

