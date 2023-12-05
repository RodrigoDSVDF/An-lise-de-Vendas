#!/usr/bin/env python
# coding: utf-8

# In[126]:


pip install dash


# In[127]:


# Importar as bibliotecas
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Ler os dados em Excel
df = pd.read_excel(r'C:\Users\Rodrigo_df\Downloads\Vendas.xlsx')



# In[128]:


df.head()


# In[129]:


df.columns


# In[130]:


print(df.dtypes)


# 

# In[174]:


from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

# Supondo que você já tenha o DataFrame df
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])

# Agrupar por 'Data da Venda' e calcular a quantidade total de vendas
df_total = df.groupby('Data da Venda')['Qtd. Vendida'].sum().reset_index()

app.layout = html.Div([
    html.H4('Quantidade de Vendas ao Longo do Tempo'),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("graph", "id")])  # O gráfico será atualizado quando a página for carregada
def update_line_chart(id):
    fig = px.line(df_total, 
        x="Data da Venda", y='Qtd. Vendida', title='Quantidade de Vendas ao Longo do Tempo')
    return fig

app.run_server(debug=True)


# In[136]:


contagem = df['Produto'].value_counts()

print(contagem)


# In[138]:


contagem = df.groupby('Produto')['Qtd. Vendida'].sum().sort_values(ascending=False)
print(contagem)


# In[149]:


print(df['Preco Unitario'])


# In[151]:


import plotly.express as px

# Agrupar por 'Produto' e calcular a quantidade total de vendas
df_total = df.groupby('Produto')['Qtd. Vendida'].sum().reset_index()

# Ordenar o resultado em ordem decrescente
df_total = df_total.sort_values('Qtd. Vendida', ascending=False)

# Criar o gráfico de barras interativo
fig = px.bar(df_total, x='Produto', y='Qtd. Vendida', 
             labels={'Qtd. Vendida':'Quantidade Vendida', 'Produto':'Produto'},
             title='Quantidade Vendida por Produto')

fig.show()



# In[80]:


df.columns


# In[107]:


import matplotlib.pyplot as plt



plt.barh(df['Produto'], df['Preco Unitario'])
plt.xlabel('Preço Unitario')
plt.ylabel('Produto')
plt.title('Gráfico de Barras Horizontais: Produto vs Preço Unitário')
plt.show()



# In[103]:


df_numericas = df.select_dtypes(include='number')

# Calcular a matriz de correlação
matriz_correlacao = df_numericas.corr()

# Plotar o mapa de calor
plt.rcParams["figure.figsize"] = (16, 6)
ax = sns.heatmap(matriz_correlacao, annot=True)


# In[171]:


# Definindo a paleta de cores
palette = sns.color_palette("husl", 8)

# Criando o gráfico
g = sns.lmplot(x="Faturamento", y="Preco Unitario", data=df, palette=palette, height=5, aspect=1.5)

# Adicionando um título
plt.title('Relação entre o preço Unitário e Faturamento', fontsize=15)

# Rotulando os eixos
g.set_axis_labels('Fraturamento', 'Preço Unitário', fontsize=12)

# Ajustando a legenda
plt.legend(title='Legenda', title_fontsize='13', loc='upper right')

# Mostrando o gráfico
plt.show()


# In[168]:


# Definindo a paleta de cores
palette = sns.color_palette("husl", 8)

# Criando o gráfico
g = sns.lmplot(x="Faturamento", y="Qtd. Vendida", data=df, palette=palette, height=5, aspect=1.5)

# Adicionando um título
plt.title('Relação entre o Faturamento e a Qtd. Vendida', fontsize=15)

# Rotulando os eixos
g.set_axis_labels('Faturamento', 'Qtd. Vendida', fontsize=12)

# Ajustando a legenda
plt.legend(title='Legenda', title_fontsize='13', loc='upper right')

# Mostrando o gráfico
plt.show()


# In[ ]:




