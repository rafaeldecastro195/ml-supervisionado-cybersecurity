import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.manifold import TSNE

# Funções relativas à geração de gráficos de histograma, curva de distribuição normal e kde

def gerar_curva_normal(df, nome_col, cor_cn='k', xy_cn=False, legenda=False, largura_linha=2):
    '''Função que gera uma Curva de Distribuição Normal a ser usada, preferencialmente, compondo outros gráficos'''
    try:
        # Determina os valores da Curva de Distribuíção Normal
        mu = np.mean(df[nome_col])
        sigma = np.std(df[nome_col])
        x = np.linspace(df[nome_col].min(), df[nome_col].max(), 100)

        # Cria a Curva de Distribuição Normal
        curva_normal = plt.plot(x, norm.pdf(x, mu, sigma), color=cor_cn, lw=largura_linha, label='Curva de Distribuição Normal')

        # Legenda mostrando a Curva de Distribuição Normal
        if legenda:
            plt.legend(loc='upper right')
        return curva_normal

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def gerar_kde(df, nome_col, cor_kde='#6D0EEB', legenda=False, xy_kde=True):
    '''Função que gera KDE (Estimativa de Densidade de Kernel)'''
    try:
        # Cria o KDE
        kde = sns.kdeplot(data=df[nome_col], color=cor_kde, label='KDE')

        # Legenda mostrando o KDE
        if legenda:
            plt.legend(loc='upper right')
        return kde

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def determinar_limite_x(df, nome_col):
    '''Função que determina o limite do Eixo X de um histograma, baseado nos Limites Superior e Inferior e IQR'''
    try:
        q1 = df[nome_col].quantile(0.25)
        q3 = df[nome_col].quantile(0.75)
        iqr = q3 - q1
        minimo = q1 - (1.5 * iqr)
        maximo = q3 + (1.5 * iqr)
        
        return plt.xlim(minimo, maximo)
    
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def gerar_histograma(df, nome_col, largura=12, altura=4, legenda=False, curva_normal=False, kde=False, cor='#E6B75C', stat='density', largura_linha=2, limite_x=False):
    '''Função que gera histograma com a possibilidade de gerar Curva de Distribuição Normal e KDE sobrepostos'''
    try:
        # Determina o tamanho da figura
        plt.figure(figsize=(largura, altura))
        # Cria o gráfico de histograma
        grafico = sns.histplot(df[nome_col], color=cor, stat=stat, line_kws={'lw':largura_linha})
            
        if curva_normal:
            gerar_curva_normal(df, nome_col)

        if kde:
            gerar_kde(df, nome_col)

        if legenda:
            plt.legend(loc='upper right')

        if limite_x:
            determinar_limite_x(df, nome_col)
            
        plt.title(f'Distribuição do atributo {nome_col}, usando a estatística de {stat}')
        plt.xlabel(nome_col)
        plt.ylabel(stat)
        plt.show()
        plt.close()
        return grafico

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

#============================================================================================================================================================================================================================================

# Funções para geração de gráficos boxplot

def gerar_boxplot(df, nome_col, altura=4, largura=12, cor='#8B56FC', showfliers=True):
    '''Essa função gera um gráfico do tipo Boxplot'''
    try:
        plt.figure(figsize=(largura, altura))

        grafico = sns.boxplot(x=df[nome_col], color=cor, legend=False, showfliers=showfliers)

        plt.title(f'Boxplot do atributo {nome_col}')
        plt.xlabel(nome_col)

        plt.show()
        plt.close()

        print('\n\n')

        return grafico

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None

    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None

    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        return None

#============================================================================================================================================================================================================================================

# Funções para geração de gráficos scatterplot, t-SNE, regressão logística
   
def gerar_tsne_2d(df, nome_col, num_componentes=2, taxa_aprendizado='auto', inicio='random', perplexidade=30):
    '''Essa função gera um algoritmo de TSNE '''
    try: 
        # Define o array relacionado à feature
        X = df[[nome_col]] # Coloca-se o nome do atributo em lista, para que seja visto como duas dimensões, o que é necessário para o TSNE
    
        # Cria instância da classe TSNE
        X_incorporado = TSNE(n_components=num_componentes, learning_rate=taxa_aprendizado, init=inicio, perplexity=perplexidade, random_state=42).fit_transform(X)

        return X, X_incorporado
        
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None
        
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None

    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        return None, None

def gerar_visualizacao_regressao_logística(df, nome_col, target):
    '''Essa função gera uma visualização dos dados para Regressão Logística em relação ao alvo'''
    try:
        fig, ax = plt.subplots()

        plt.scatter(X_treino, y_treino)

        plt.set(y_ticks=(0,1))

        plt.show()

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
        
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None

    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        return None

def gerar_sigmoid(df, nome_col):
    '''Essa função gera o resultado da função sigmoid'''
    try:
        funcao_sigmoid = 1/(1 + np.exp(- df[nome_col]))
        return funcao_sigmoid
    
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
        
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None

    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        return None
    
def gerar_scatterplot(df, nome_col, largura=12, altura=4, x=None, y=None, tsne2d=False, visualizacao_rl=False, alpha=0.5):
    '''Essa função gera um Scatterplot com possibilidade de visualização de TSNE 2D'''
    try: 

        plt.figure(figsize=(largura, altura))

        if not tsne2d:
            x = x if x is not None else df.index
            y = y if y is not None else df[nome_col]
            grafico = sns.scatterplot(data=df, x=x, y=y, hue=df[nome_col], alpha=alpha)
            plt.title(f'Scatterplot do atributo {nome_col}')
        if tsne2d:
            X, X_incorporado = gerar_tsne_2d(df, nome_col)
            grafico = sns.scatterplot(x=X_incorporado[:, 0],
                                     y=X_incorporado[:,1],
                                     hue=df[nome_col],
                                     alpha=alpha)
            plt.title(f'Scatterplot, com t-SNE 2D, do atributo {nome_col}')
    
        plt.show()
        plt.close()
    
        print('\n\n')
    
        return grafico

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
        
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None

    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        return None