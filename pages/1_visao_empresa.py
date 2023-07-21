# bibliotecas necessárias
import pandas as pd
import re
import folium
import streamlit as st

from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

from streamlit_folium import folium_static

st.set_page_config( page_title='Vião Empresa', page_icon='📈', layout='wide' )
#------------------------------------------------------------------------------
# Funções
#------------------------------------------------------------------------------

def country_maps( df1 ):
    df_aux = ( df1.loc[:, ['City', 'Road_traffic_density', 'Delivery_location_latitude', 'Delivery_location_longitude']]
                      .groupby( ['City', 'Road_traffic_density'])
                      .median()
                      .reset_index() )
        
    map_ = folium.Map( zoom_start=11 )
    for index, location_info in df_aux.iterrows():
        folium.Marker( [location_info['Delivery_location_latitude'],
                        location_info['Delivery_location_longitude']],
                        popup=location_info[['City', 'Road_traffic_density']] ).add_to( map_ )
        
    folium_static( map_, width=1024, height=600 )

def order_share_by_week( df1 ):
    df_aux1 = df1.loc[:, ['ID', 'week_of_year']].groupby( 'week_of_year' ).count().reset_index()
    df_aux2 = ( df1.loc[:, ['Delivery_person_ID', 'week_of_year']]
                   .groupby( 'week_of_year')
                   .nunique()
                   .reset_index() )
    df_aux = pd.merge( df_aux1, df_aux2, how='inner', on='week_of_year' )
    df_aux['order_by_delivery'] = df_aux['ID'] / df_aux['Delivery_person_ID']
    fig = px.line( df_aux, x='week_of_year', y='order_by_delivery' )
            
    return fig

def order_by_week( df1 ):
    # Quantidade de pedidos por Semana
    df1['week_of_year'] = df1['Order_Date'].dt.strftime( "%U" )
    df_aux = df1.loc[:, ['ID', 'week_of_year']].groupby( 'week_of_year' ).count().reset_index()
    fig = px.line( df_aux, x='week_of_year', y='ID' )
           
    return fig

def traffic_order_city( df1 ):
    df_aux = ( df1.loc[:, ['ID', 'City', 'Road_traffic_density']]
                  .groupby(['City','Road_traffic_density'])
                  .count()
                  .reset_index() )
           
    fig = px.scatter( df_aux, x='City', y='Road_traffic_density', size='ID',color='City')
           
    return fig

def traffic_order_share( df1 ):
    df_aux = ( df1.loc[:, ['ID', 'Road_traffic_density']]
                  .groupby( 'Road_traffic_density' )
                  .count()
                  .reset_index() )
    df_aux = df_aux.loc[df_aux['Road_traffic_density'] != "NaN", :]
    df_aux['perc_ID'] =  df_aux['ID'] / df_aux['ID'].sum()
    # gráfico
    fig = px.pie( df_aux, values='perc_ID', names='Road_traffic_density' )
                
    return fig

def order_metric( df1 ):
    cols = ['ID', 'Order_Date']
    # selecao de linhas
    df_aux = df1.loc[:, cols].groupby( 'Order_Date' ).count().reset_index()
            
    #desenhar com Plotly o grafico de linhas
    fig = px.bar( df_aux, x='Order_Date', y='ID' )
            
    return fig

def clean_code( df1 ):
    """ Esta funao tem a responsabilidade de limpar o dataframe
    
        Tipos de limpeza:
        1. Remoção de dados NAN
        2. Mudança do tipo da coluna de dados
        3. Remoção dos espaços da variáveis de texto
        4. Formatação da coluna de datas
        5. Limpeza da coluna de tempo ( remoção do texto da variável numérica )
        
        Input: Dataframe
        Output: Dataframe
    
    
    """
    # 1. convertendo a coluna Age de texto para numero
    linhas_vazias = df1['Delivery_person_Age'] != 'NaN '
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = df1['Road_traffic_density'] != 'NaN '
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = df1['City'] != 'NaN '
    df1 = df1.loc[linhas_vazias, :].copy()

    #linhas_vazias = df1['Time_taken(min)'] != 'NaN '
    #df1 = df1.loc[linhas_vazias, :].copy()

    #linhas_vazias = df1['Type_of_order'] != 'NaN '
    #df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = df1['Festival'] != 'NaN '
    df1 = df1.loc[linhas_vazias, :].copy()

    df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype( int )
    df1.shape

    # 2. convertendo a coluna Ratings de texto para numero decimal ( float )
    df1['Delivery_person_Ratings'] = df1['Delivery_person_Ratings'].astype( float )

    # 3. convertendo a coluna order_date de texto para data
    df1['Order_Date'] = pd.to_datetime( df1['Order_Date'], format='%d-%m-%Y' )

    # 4. convertendo multiple_deliveries de texto para numero inteiro ( int )
    linhas_vazias = df1['multiple_deliveries'] != 'NaN '
    df1 = df1.loc[linhas_vazias, :].copy()
    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype( int )

    # 5. removendo o espacos dentro de strings
    df1.loc[:, 'ID'] = df1.loc[:,'ID'].str.strip()
    df1.loc[:, 'Road_traffic_density'] = df1.loc[:,'Road_traffic_density'].str.strip()
    df1.loc[:, 'Type_of_order'] = df1.loc[:,'Type_of_order'].str.strip()
    df1.loc[:, 'Type_of_vehicle'] = df1.loc[:,'Type_of_vehicle'].str.strip()
    df1.loc[:, 'City'] = df1.loc[:,'City'].str.strip()
    df1.loc[:, 'Festival'] = df1.loc[:,'Festival'].str.strip()

    # 6. limpando a coluna de Time_taken(min)
    df1['Time_taken(min)'] = df1['Time_taken(min)'].apply( lambda x: x.split( '(min) ')[1] )
    df1['Time_taken(min)'] = df1['Time_taken(min)'].astype( int )
    
    return df1
#----------------------------------Inicio da Estrutura lógica do código---------------------------------
#-------------------------------------------------------------------------------------------------------
# Import dataset
#------------------------------------------------------------------------------
df = pd.read_csv('Data/train.csv')

#------------------------------------------------------------------------------
# Limpando os dados
#------------------------------------------------------------------------------
df1 = clean_code( df )

#=======================================================
             # SIDEBAR
#=======================================================

st.header( 'Marketplace - Visão Cliente' )

st.sidebar.markdown( '# Curry Company' )
st.sidebar.markdown( '### Fastest Delivery in Town' )
st.sidebar.markdown( """___""" )


st.sidebar.markdown('## Selecione uma data limite')
date_slider = st.sidebar.slider(
    'Até qual valor?',
    value=pd.Timestamp(2022, 4, 13),
    min_value=pd.Timestamp(2022, 2, 11),
    max_value=pd.Timestamp(2022, 4, 6),
    format='DD-MM-YYYY'
)


st.header( date_slider )
st.sidebar.markdown( """___""" )

traffic_options = st.sidebar.multiselect(
    'Quais as condições do trânsito',
    ['Low', 'Medium', 'High', 'Jam'],
    default=['Low','Medium', 'High', 'Jam'] )

st.sidebar.markdown( """___""" )

#image_path = '/home/ricardo/repos/Pergunta_de_negocio_FTC/' 
image = Image.open( 'cheetah_data_science.png' )
st.sidebar.image( image, width=120 )

st.sidebar.markdown( '### Powered by Cheetah Data Science' )

# Filtro de data
linhas_selecionadas = df1['Order_Date'] < date_slider
df1 = df1.loc[linhas_selecionadas, :]

# Filtro de data
linhas_selecionadas = df1['Road_traffic_density'].isin( traffic_options )
df1 = df1.loc[linhas_selecionadas, :]

#=======================================================
             #LAYOUT DO STREAMLIT
#=======================================================

tab1, tab2, tab3 = st.tabs( ['Visão Gerencial', 'Visão Tática', 'Visão Geográfica'] )

with tab1:
    with st.container():
        # Order Metric
        fig = order_metric( df1 )
        st.markdown( '# Orders by Day' )
        st.plotly_chart(fig, use_container_width=True)
            
    with st.container():
        cols1, cols2 = st.columns( 2 )
        
        with cols1:
            fig = traffic_order_share( df1 )
            st.markdown( '# Traffic Order Share' )
            st.plotly_chart ( fig, use_container_width=True )
                                          
        with cols2:
            fig = traffic_order_city ( df1 )
            st.markdown( '# Traffic Order City' )
            st.plotly_chart( fig, use_container_width=True )
                    
            
with tab2:
    with st.container():
        st.markdown( "# Order by Week" )
        fig = order_by_week( df1 )
        st.plotly_chart( fig, use_container_width=True )
                
    with st.container():
        st.markdown( "# Order Share by Week" )
        fig = order_share_by_week( df1 )
        st.plotly_chart( fig, use_container_width=True )
        
with tab3:
    st.markdown( "# Country Maps" )
    country_maps( df1 )
    
