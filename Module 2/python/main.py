# Importando as bibliotecas necessária 
from sqlalchemy import create_engine
import pandas as pd

# Usando a classe create_engine da biblioteca sqlalchemy vamos armazena a string de conexão usando Psycopg2
engine = create_engine('postgresql+psycopg2://postgres:HnlZ6R59jk7LGOI0p20GXj7Up@localhost/postgres')

# Para testar vamos utilizar um select simples
sql = 'select * from "Billboard" as TBB limit 10;'

# E usando o select vamos armazenar o resultado na variavel df(dataframe) usando o pandas
df = pd.read_sql_query(sql,engine)

# Pronto tabela sendo retornada em um dataframe
print(df)