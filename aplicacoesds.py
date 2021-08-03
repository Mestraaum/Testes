import streamlit as st
import pandas as pd
import numpy as np

dados = pd.read_csv("Planilha - APLICAÇÕES DS - Página1.csv")
#===============================================================================================================


# ESTRUTURAÇÃO DA SIDEBAR

paginas = dados['CATEGORIA'].unique()
paginas = paginas[:-1]


# paginas = dados['CATEGORIA'].drop_duplicates()

st.sidebar.image('bannerflai.jpg', use_column_width = 'always')
pagina = st.sidebar.radio('Selecione a área do seu interesse', paginas)


titulo = "Aplicações de Data Science para a seguinte área:" # Para o tírulo de todas as páginas
saplicacao = "Selecione a aplicação abaixo " # Para a caixa de seleção de aplicações
explore = "Para explorá-las, selecione a do seu interesse na barra abaixo:" # Texto que fica ao lado da quantidade de utilizações

suj = pd.DataFrame({'col1':['Conhece mais alguma área?']})

sujestao = st.sidebar.checkbox("Deixe sua sujestão!")

#===============================================================================================================


# CÓDIGO PARA AUTOMATIZAR A LEITURA DAS PESSOAS

	
def geral(pagina):
	aero = dados[dados['CATEGORIA'] ==  pagina]['APLICACAO']


	st.title(titulo, pagina) #Título 1 tá na aba 1
	st.title(pagina)

	st.write("Para a área acima, nós temos atualmente uma amostra de ", (str(len(aero))),"utilizações. ",explore)
	
	aplic = st.selectbox("",aero)


	imagem = dados[dados['APLICACAO'] ==  aplic]['IMAGEM']
	st.image(imagem.loc[imagem.index[0]], use_column_width = 'always')

	st.header(aplic)


	resumo = dados[dados['APLICACAO'] ==  aplic]['RESUMO']
	
	st.write(resumo.loc[resumo.index[0]])

	links = dados[dados['APLICACAO'] == aplic]['REFERENCIA']

	'''

	'''

	st.write("Referência:")
	st.write(links[links.index[0]])



def sujest(sujestao):
	st.image('bannerflai.jpg', use_column_width = 'always')

	st.title("Nos ajude com sua sujestão!")

	st.write('Além destas aplicações de Inteligência Artificial, nós da FLAI sabemos que ainda existem muitas outras áreas de atuação das quais as mesmas ainda não adicionameos neste webapp.')

	st.write('Sabendo disso nós deixamos uma aba especialmente para as pessoas que desejarem nos ajudar com áreas de atuação que não foram postas aqui.')

	st.write('Para nos auxiliar a adicionarmos mais áreas de atuação, temos o link abaixo para sua interação (via GOOGLE FORMS)')

	'''
	### [Link do formulário](https://forms.gle/Z7GEwrsZTYfLqoNJ7)
	'''

	st.write("")

	st.write('Agradecemos pelo seu apoio! 😉')


#===============================================================================================================


# TEXTO DA PÁGINA PRINCIPAL


if pagina == paginas[[0]] and sujestao == False:
	'''
	# Aplicações e áreas de atuação da inteligência artificial
	'''
	st.image('imagem1.png', use_column_width = 'always')

	'A tecnologia hoje já está presente em praticamente todos os setores existentes. Podemos dizer o mesmo para ciência de dados, e para facilitar sua busca por suas inúmeras aplicações, nós da equipe FLAI desenvolvemos esse web app para que você consiga encontrar com uma maior facilidade alguma aplicação em uma área de seu interesse.'
	
	'Nosso principal objetivo com esse web app é auxiliar a comunidade interessada na área de Ciência de Dados a entender o quão vastos são as oportunidades de emprego.'

	'Vale salientar que além destas aplicações que nós temos aqui, existem mais inúmeras aplicações em inúmeras áreas. Com isso, deixamos em aberto uma ultima aba chamada "Suas Aplicações", no qual VOCÊ, usuário deste web app, poderá compartilhar aplicações das quais você sentiu falta por aqui.'


	'Neste web app, temos', str(len(dados)-1), 'aplicações distribuidas entre ', str(len(paginas[1:len(paginas)])), 'áreas de atuação. Essas áreas são:'
	
	'''
	
	'''

	for i in paginas[1:len(paginas)]:
			st.subheader(i)

	'''

	'''

	'''
	E para facilitar a sua navegação, você pode selecionar a área do seu interesse apenas selecionando alguma das áreas na aba a esquerda.
	'''

#===============================================================================================================

# Layout geral de abas para o webapp das aplicações:

for i in range(len(paginas)):
	if paginas[[i]] == pagina:
		if pagina != paginas[[0]] and sujestao == False:
			geral(pagina)
		if pagina != paginas[[0]] and sujestao != False or pagina == paginas[[0]] and sujestao != False:
			sujest(sujestao)


#===============================================================================================================

# Layout para a área de sujestões


