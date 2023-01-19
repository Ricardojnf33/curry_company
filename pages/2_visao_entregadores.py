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

st.set_page_config( page_title='Vião Entregadores', page_icon='🚚', layout='wide' )

#------------------------------------------------------------------------------
# Funções
#------------------------------------------------------------------------------

def top_delivers( df1, top_asc ):
    df2 = ( df1.loc[ :, ['Delivery_person_ID', 'City', 'Time_taken(min)'] ]
               .groupby( ['City', 'Delivery_person_ID' ] )
               .max()
               .sort_values(['City', 'Time_taken(min)'], ascending=False ).reset_index() )
    
    df_aux01 = df2.loc[df2['City'] == 'Metropolitian', :].head(10)
    df_aux02 = df2.loc[df2['City'] == 'Urban', :].head(10)
    df_aux03 = df2.loc[df2['City'] == 'Semi-Urban', :].head(10)

    df3 = pd.concat( [df_aux01, df_aux02, df_aux03] ).reset_index( drop=True )
                    
    return df3

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

# Import dataset
df = pd.read_csv('Data/train.csv')

#  
df1 = clean_code( df )

#=======================================================
             # SIDEBAR
#=======================================================

st.header( 'Marketplace - Visão Entregadores' )

st.sidebar.markdown( '# Curry Company' )
st.sidebar.markdown( '### Fastest Delivery in Town' )
st.sidebar.markdown( """___""" )

st.sidebar.markdown( '## Selecione uma data limite' )
date_slider = st.sidebar.slider( 
    'Até qual valor?',
    value=pd.datetime( 2022, 4, 13 ),
    min_value=pd.datetime(2022, 2, 11),
    max_value=pd.datetime(2022, 4, 6),
    format='DD-MM-YYYY' )

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


#=======================================================
             #LAYOUT DO STREAMLIT
#=======================================================

tab1, tab2, tab3 = st.tabs( ['Visão Gerencial', 'Visão Tática', 'Visão_Geográfica'] )

with tab1:
    with st.container():
        st.title( 'Overall Metrics' )
        
    col1, col2, col3, col4 = st.columns( 4, gap='large' )
    with col1:
        # A maior idade dos entregadores
        maior_idade = df1.loc[:, 'Delivery_person_Age'].max()
        col1.metric( 'Maior de idade', maior_idade )
        
    with col2:            
        # A menor idade dos entregadores
        menor_idade = df1.loc[:, 'Delivery_person_Age'].min() 
        col2.metric( 'Menor de idade', menor_idade )
        
    with col3:            
        # A melhor condicao de veiculos
        Melhor_condicao = df1.loc[:, 'Vehicle_condition'].max()
        col3.metric( 'Melhor condicao', Melhor_condicao )
        
    with col4:            
        # A pior condicao de veiculos
        Pior_condicao = df1.loc[:, 'Vehicle_condition'].min()
        col4.metric( 'Pior condicao', Pior_condicao )
            
    with st.container():
        st.markdown( """---""" )
        st.title( 'Avaliacoes' )
        
        col1, col2 = st.columns( 2 )
        with col1:
            st.markdown( '##### Avaliacoes medias por Entregador' )
            df_avg_per_delivery = df1.loc[:, ['Delivery_person_ID','Delivery_person_Ratings']].groupby( 'Delivery_person_ID' ).mean().reset_index()
            st.dataframe( df_avg_per_delivery )
        with col2:
            st.markdown( '##### Avalicao media por transito' )
            
            df1_avg_std_rating_by_traffic = df1.loc[ :, ['Delivery_person_Ratings','Road_traffic_density']].groupby('Road_traffic_density').agg( {'Delivery_person_Ratings': ['mean', 'std']} )
            # mudanças das colunas
            df1_avg_std_rating_by_traffic.columns = ['Delivery_mean', 'Delivery_std']

            # reset do index
            df1_avg_std_rating_by_traffic = df1_avg_std_rating_by_traffic.reset_index()
            df1_avg_std_rating_by_traffic
            
            
            st.markdown( '##### Avaliacao media por clima' )
            
            # Avaliação média por condições climáticas
            df1_avg_std_rating_by_Weatherconditions = ( df1.loc[ :, ['Delivery_person_Ratings','Weatherconditions']].groupby('Weatherconditions')
                                .agg({'Delivery_person_Ratings':['mean','std']}) )
            # mudanças das colunas
            df1_avg_std_rating_by_Weatherconditions.columns = ['Delivery_mean', 'Delivery_std']

            # reset do index
            df1_avg_std_rating_by_Weatherconditions = df1_avg_std_rating_by_Weatherconditions.reset_index()
            df1_avg_std_rating_by_Weatherconditions
            
            
    
    with st.container():
            st.markdown("""---""")
            st.title( 'Velocidade de Entrega' )
            
            col1, col2 = st.columns( 2)
            with col1:
                st.subheader( 'Top Entregadores mais rapidos' )
                df3 = top_delivers( df1, top_asc=True )
                st.dataframe( df3 )
                
                
            with col2:
                st.markdown( '##### Top Entregadores mais lentos' )
                df3 = top_delivers( df1, top_asc=False )                
                st.dataframe( df3 )
    
    