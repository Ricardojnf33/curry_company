import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎲",
    layout='wide'
)

st.sidebar.markdown( '# Curry Company' )
st.sidebar.markdown( '## Fastest Delivery in Town' )
st.sidebar.markdown( """---""" )

#image_path = '/home/ricardo/repos/Pergunta_de_negocio_FTC/' 
image = Image.open( 'cheetah_data_science.png' )
st.sidebar.image( image, width=120 )

st.sidebar.markdown( '### Powered by Cheetah Data Science' )

st.write( "# Curry Company Growth Dashboard" )

st.markdown(
    """
    
    Growth Dashboard foi construído para acommpanhar as métricas de crescimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes
    ### Ask for Help
    - Time de Data Science no Email
        - ricardo.jnf1@gmail.com
""")
        
