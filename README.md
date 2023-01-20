# Painel Gerencial para a Curry Company.
   
Este projeto tem como objetivo desenvolver um painel gerencial para acompanhar as métricas-chave da Curry Company, uma empresa de tecnologia que criou um aplicativo de entrega de comida. Com a utilização de Python, Jupyter Lab, Terminal, Streamlit, Streamlit Cloud e Github, foi possível desenvolver um painel que pode ser acessado por qualquer dispositivo conectado à internet, mostrando informações importantes como o número de entregas realizadas, renda gerada, avaliações dos entregadores e outras métricas-chave.
     
# Requisitos e Dependências:

      1. streamlit==1.15.1
      2. plotly==5.10.0
      3. pandas==1.4.3
      4. numpy==1.23.1
      5. folium==0.13.0
      6. matplotlib==3.5.3
      7. matplotlib-inline==0.1.6
      8. haversine==2.7.0
      9. streamlit-folium==0.7.0
      10.Pillow==9.2.0

# Instalação e Execução
   1. Faça o clone do repositório do projeto usando 'git clone https://github.com/Ricardojnf33/curry_company.git'
   2. Entre na pasta do projeto com 'cd curry_company'
   3. Instale as dependências com 'pip install -r requirements.txt'
   4. Execute o projeto com 'streamlit run Home.py'

# Exemplos de Uso
O painel gerencial pode ser usado para visualizar informações sobre:

   * Número de entregas realizadas por dia, semana e mês
   * Renda gerada por dia, semana e mês
   * Avaliação dos entregadores
   * E outras métricas-chave

# Screenshots
![newplot.png](https://github.com/Ricardojnf33/curry_company/blob/main/newplot.png)
![newplot.png](https://github.com/Ricardojnf33/curry_company/blob/main/newplot2.png)


## Introdução
Este conjunto de dados é sobre o serviço de entrega de comida, onde um restaurante, loja ou empresa de entrega de comida independente entrega comida a um cliente. Um pedido é geralmente feito através do site ou aplicativo móvel de um restaurante ou mercado, ou através de uma empresa de pedidos de comida. Os itens entregues podem incluir pratos principais, acompanhamentos, bebidas, sobremesas ou itens de mercearia e geralmente são entregues em caixas ou sacolas. A pessoa que faz a entrega normalmente dirige um carro, mas em cidades maiores onde as residências e os restaurantes estão mais próximos, eles podem usar bikes ou scooters motorizados.

Este conjunto de dados inclui informações sobre os pedidos realizados, como os itens pedidos, os clientes que fizeram os pedidos, os restaurantes ou lojas dos quais os itens foram comprados e os entregadores que entregaram os itens. Também pode incluir informações sobre a entrega em si, como a data e hora em que o pedido foi feito, a data e hora em que o pedido foi entregue e a distância entre o restaurante ou loja e o local de entrega. Outros pontos de dados potenciais podem incluir o método de pagamento usado, o custo do pedido e quaisquer instruções ou solicitações especiais feitas pelo cliente.

# 1. Problema de negócio

A Curry Company é uma empresa de tecnologia que criou um aplicativo que conecta restaurantes, entregadores e pessoas.

Através desse aplicativo, é possível realizar o pedido de uma refeição, em qualquer restaurante cadastrado, e recebê-lo no conforto de sua casa por um entregador também cadastrado no aplicativo da Curry Company.

A empresa realiza negócios entre reastaurantes, entregadores e pessoas, e gera muitos dados sobre entregas, tipos de pedidos, condições climáticas, avaliação dos entregadores e etc. Apesar da entrega estar crescendo, em termos de entregas, o CEO não tem visibilidade completa dos KPI's de crescimento da empresa.

Você foi contratado como Cientistas de Dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um dos principais KPIs estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes.

A Curry Company possui um modelo negócio chamado Marletplace, que fazer o intermédio do negócio entre três clientes principais: Restaurantes, entregaddorese pessoas compradoras. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento.

1. Do lado da empresa

   1. Quantidade de pedidos por dia.
   2. Quantidade de pedidos por semana.
   3. Distribuição dos pedidos por tipo de tráfego.
   4. Comparação do volume de pedidos por cidade e tipo de tráfego.
   5. A quantidade de pedidos por entregador por semana.
   6. A localização central de cada cidade por tipo de tráfego 

2. Do lado do entregador:

   1. A menor e maior idade dos entregadores.
   2. A pior e a melhor condição de veículos.
   3. A avaliação média por entregador.
   4. A avaliação média e o desvio padrão por tipo de tráfego.
   5. A avaliação média e o desvio padrão por condições climáticas.
   6. Os 10 entregadores mais rápidos por cidade.
   7. Os 10 entregadores mais lentos por cidade.

3. Do lado do restaurante:

    1. Quantidade de entregadores únicos.
    2. A distância média dos restaurantes e dos locais de entrega.
    3. O tempo médio e o desvio padrão de entrega por cidade.
    4. O tempo médio e o desvio padrão de entrega por cidade e tipo de pedido.
    5. O tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego.
    6. O tempo médio de entrega durante os festivais.

O objetivo desse projeto pe criar um conjunto de gráficos e tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 2. Premissas assumidas para a análise
 
  * A nálise foi realizada com dados entre 11/02/2022 e 06/04/2022.
  * Marketplace foi o modelo de negocio assumido.
  * Os 3 principais visões do negócio foram: Visão transaçãode pedidos, visão restaurante e visão entregadores
  
# 3. Estratégia da solução
  
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:

 1.0 Visão da empresa
 2.0 Visão do entregador
 3.0 Visão do restaurante

# 4. Top 3 Insights de dados
  
  1. A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximidamente 10% do número de pedidos em dia sequenciais.
  2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.
  3. As maiores variaçõess no tempo de entregam acontecem durante o clima ensolarado.

# 5. O produto final do projeto

Painel online, hospedado em uma Cloud e disponível para acesso em qualquer dispositivo conectado à internet

O painel pode ser acessado através do link: https://cheetahds-curry-company.streamlit.app/

# 6. Conclusão
  
O objetivo desse projeto é criar um conjunto de gráficos ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão da Empresa, podemos concluir que o número de pedidos cresceu entre a semana 06 e a semana 13 do ano de 2022.

# 7. Próximos passos
  
1. Reduzir o número de métricas
2. Criar novos filtros.
3. Adicionar novas visões de negócio.

   ## Automatização com IA

Para melhorar a experiência de usuário e a eficiência dos processos deste projeto, como próximos passos, também incluiremos automatização com IA. Algumas das funcionalidades incluem:

1. Utilização de algoritmos de aprendizado de máquina para analisar dados do conjunto de dados e gerar insights automatizados para incluir no painel gerencial. Isso pode incluir previsões de vendas, análise de sentimentos dos clientes, e outras métricas.

2. Implementação de uma interface de chatbot para permitir que os usuários interajam com o painel gerencial de forma mais intuitiva e conversacional.

3. Utilização de técnicas de reconhecimento de imagem para processar imagens dos entregadores ou dos pedidos, para melhorar a segurança e eficiência do processo de entrega.

4. Adição de uma funcionalidade de reconhecimento de voz para permitir que os usuários façam pedidos ou acessar as informações do painel gerencial de forma mais natural, usando comandos de voz.

5. Utilização de técnicas de processamento de linguagem natural para analisar dados de texto, como comentários dos clientes, para gerar insights automatizados.
