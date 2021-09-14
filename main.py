# pandas
# openpyxl
# twilio

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC42eb6a65b0f4d72c2ac0dfd8e1f0c965"
# Your Auth Token from twilio.com/console
auth_token  = "b0c6b8db333efec726cea92979204389"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel
Lista_meses = ['Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in Lista_meses:
    Tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(Tabela_vendas['Vendas'] > 55000).any():
        vendedor = Tabela_vendas.loc[Tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = Tabela_vendas.loc[Tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        message = client.messages.create(
            to="+5581982320634",
            from_="+14155270455",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum na coluna vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada

