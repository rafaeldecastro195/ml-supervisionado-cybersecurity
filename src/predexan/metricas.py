def gerar_analise_basica(df, nome_col):
    '''Essa função gera valores de Análise Básica de um ou mais atributos'''
    try:   
        contagem = df[nome_col].count()
        nulas = df[nome_col].isna().sum()
        duplicadas = df[nome_col].size - df[nome_col].nunique()
        valores_unicos = df[nome_col].nunique()
        total_valores = df[nome_col].value_counts()[0]
    
        return contagem, nulas, duplicadas, valores_unicos, total_valores
    
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None, None, None
        
def imprimir_analise_basica(df, nome_col):
    '''Função que mostra os valores das Análises Básicas de um ou mais atributos'''
    try:
        contagem, nulas, duplicadas, valores_unicos, total_valores = gerar_analise_basica(df, nome_col)

        print(f'\n\n Análise Básica do atributo {nome_col}:')
        print(f'\n - No total, há {contagem} células e destas, {nulas} são nulas, {duplicadas} estão repetidas e o total de valores unicos são {valores_unicos}.')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None

def gerar_tendencia_central(df, nome_col):
    '''Função que gera valores de Medidas de Tendência Central de um ou mais atributos'''
    try:
        media = df[nome_col].mean()
        mediana = df[nome_col].median()
        moda = df[nome_col].mode()[0]

        return media, mediana, moda
    
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None
        
def imprimir_tendencia_central(df, nome_col):
    '''Função que imprime os valores das Medidas de Tendência Central de cada atributo'''
    try:
        media, mediana, moda = gerar_tendencia_central(df, nome_col)

        print(f'\n\n Medidas de Tendência Central do atributo {nome_col}: ')
        print(f'\n - A média aritmética de seus valores é, aproximadamente, {media:.2f};')
        print(f'\n - A mediana é, aproximadamente, {mediana:.2f};')
        print(f'\n - A moda é, aproximadamente, {moda:.2f};')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None

def gerar_dispersao(df, nome_col):
    '''Função que gera valores de  Medidas de Dispersão e Amplitude de um ou mais atributos'''
    try:
        media = df[nome_col].mean()
        valor_min = df[nome_col].min()
        valor_max = df[nome_col].max()
        faixa = valor_max - valor_min
        desvio_padrao = df[nome_col].std()
        coeficiente_variacao = (desvio_padrao/media) if media != 0 else 0

        return media, valor_min, valor_max, desvio_padrao, coeficiente_variacao, faixa

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None, None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None, None, None, None
        
def imprimir_dispersao(df, nome_col):
    '''Imprime Medidas de Dispersão e Amplitude com interpretação estatística'''
    try:
        media, valor_min, valor_max, desvio_padrao, coeficiente_variacao, faixa = gerar_dispersao(df, nome_col)
        
        print('\n\n Medidas de Dispersão e Amplitude')
        print(f'\n - Amplitude: de {valor_min:.2f} até {valor_max:.2f}. Variam em uma faixa de {faixa:.2f}')
        print(f'\n - Desvio Padrão: {desvio_padrao:.2f}')
        print(f'\n - Coeficiente de Variação: {(coeficiente_variacao):.2f} (Valores > 1 indicam alta dispersão)')
        
        if desvio_padrao > media:
             print(f'Nota: O desvio padrão é superior à média, confirmando a presença de outliers e assimetria.')
        else:
             print(f'Os valores concentram-se num intervalo de {media-desvio_padrao:.2f} a {media+desvio_padrao:.2f} (em caso de normalidade).')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def gerar_quartis(df, nome_col):
    '''Função que gera valores de  Medidas de Dispersão e Amplitude de um ou mais atributos'''
    try:
        quartil_25 = df[nome_col].quantile(0.25)
        quartil_50 = df[nome_col].quantile(0.50)
        quartil_75 = df[nome_col].quantile(0.75)

        return quartil_25, quartil_50, quartil_75
        
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None
        
def imprimir_quartis(df, nome_col):
    '''Função que imprime os valores dos quartis de 25%, 50% e 75% de cada atributo'''
    try:
        quartil_25, quartil_50, quartil_75 = gerar_quartis(df, nome_col)

        print(f'\n\n Medidas de Posição (Quartis) do atributo {nome_col}:')
        print(f'\n - O valor do quartil de 25% é {quartil_25:.2f}. Isto significa que 25% dos dados da amostra do atributo {nome_col} são menores ou iguais a esse valor;')
        print(f'\n - O valor do quartil de 50% é {quartil_50:.2f}. Isto significa que 50% dos dados da amostra do atributo {nome_col} são menores ou iguais a esse valor. Equivale à mediana;')
        print(f'\n - O valor do quartil de 75% é {quartil_75:.2f}. Isto significa que 75% dos dados da amostra do atributo {nome_col} são menores ou iguais a esse valor;')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def gerar_valor_outliers(df, nome_col):
    '''Função que gera valores de análises de Outliers de um ou mais atributos'''
    try:
        quartil_25 = df[nome_col].quantile(0.25)
        quartil_50 = df[nome_col].quantile(0.50)
        quartil_75 = df[nome_col].quantile(0.75)
        limite_inferior = quartil_25 - (1.5 * (quartil_75 - quartil_25))
        limite_superior = quartil_75 + (1.5 * (quartil_75 - quartil_25))
        outlier_inferior = df[df[nome_col] < limite_inferior].shape[0]
        percentual_outlier_inferior = (outlier_inferior/df[nome_col].shape[0]) * 100
        outlier_superior = df[df[nome_col] > limite_superior].shape[0]
        percentual_outlier_superior = (outlier_superior/df[nome_col].shape[0]) * 100
    
        return quartil_25, quartil_50, quartil_75, limite_inferior, limite_superior, outlier_inferior, percentual_outlier_inferior, outlier_superior, percentual_outlier_superior
     
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None, None, None, None, None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None, None, None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None, None, None, None, None, None, None
    
def imprimir_outliers(df, nome_col):
    '''Função que determina os limites superior e inferior para detecção de Outliers de um ou mais atributos'''
    try:
        quartil_25, quartil_50, quartil_75, limite_inferior, limite_superior, outlier_inferior, percentual_outlier_inferior, outlier_superior, percentual_outlier_superior = gerar_valor_outliers(df, nome_col)

        print(f'\n\n Detecção de Outliers do atributo {nome_col}:')
        print(f'\n - O limite inferior é igual a, aproximadamente, {limite_inferior}. Valores abaixo deste limite podem ser considerados Outliers Inferiores;')
        print(f'\n - O total de outliers de limite inferior é {outlier_inferior:.2f}, o que corresponde a {percentual_outlier_inferior:.2f}% do total de registros;')
        print(f'\n - O limite superior é igual a, aproximadamente, {limite_superior}. Valores acima deste limite podem ser considerados Outliers Superiores;')
        print(f'\n - O total de outliers de limite superior é {outlier_superior:.2f}, o que corresponde a {percentual_outlier_superior:.2f}% do total de registros;')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')

def gerar_regra_ouro_normal(df, nome_col):
    '''Função que determina os valores da regra de ouro da Distribuição Normal de um ou mais atributos'''
    try:
        media = df[nome_col].mean()
        desvio_padrao = df[nome_col].std()

        percentual_68_acima = media + desvio_padrao
        percentual_68_abaixo = media - desvio_padrao

        percentual_95_acima = media + (2 * desvio_padrao)
        percentual_95_abaixo = media - (2 * desvio_padrao)

        percentual_99_acima = media + (3 * desvio_padrao)
        percentual_99_abaixo = media - (3 * desvio_padrao)

        return media, desvio_padrao, percentual_68_acima, percentual_68_abaixo, percentual_95_acima, percentual_95_abaixo, percentual_99_acima, percentual_99_abaixo

    
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None, None, None, None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None, None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None, None, None, None, None, None
        
def imprimir_regra_ouro_normal(df, nome_col):
    '''Função que determina o percentual da amostra a partir da média e desvio padrão da Curva de Distribuição Normal'''
    try:
        media, desvio_padrao, percentual_68_acima, percentual_68_abaixo, percentual_95_acima, percentual_95_abaixo, percentual_99_acima, percentual_99_abaixo = gerar_regra_ouro_normal(df, nome_col) 
        print(f'\n\n Regra de Ouro da Distribuição Normal do atributo {nome_col}:')
        print(f'\n - 68% da amostra está compreendida entre, aproximadamente, {percentual_68_abaixo:.2f} e {percentual_68_acima:.2f};')
        print(f'\n - 95% da amostra está compreendida entre, aproximadamente, {percentual_95_abaixo:.2f} e {percentual_95_acima:.2f};')
        print(f'\n - 99.7% da amostra está compreendida entre, aproximadamente, {percentual_99_abaixo:.2f} e {percentual_99_acima:.2f}.')

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None, None, None, None, None, None, None, None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None, None, None, None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None, None, None, None, None, None, None, None