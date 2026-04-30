# Função para facilitar a exclusão de outliers

def drop_outlier(df, nome_col, outlier_inferior, outlier_superior):
    '''Função que exclui outliers, à partir de os valores do limite superior e inferior'''
    try:
        df = df.drop(df[(df[nome_col] < outlier_inferior) | (df[nome_col] > outlier_superior)].index)

        df = df.reset_index(drop=True)
        
        return df

    except ValueError:
            print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
            return None
            
    except KeyError:
            print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
            return None
    
    except Exception as e:
            print(f'Ocorreu o seguinte erro: {e}')
            return None
    
# Função que normaliza os dados, baseada em escalonamento robusto

def normalizar_feature_rs(df, nome_col, escalonador, div_max=False):
    '''Função usada para normalizar features com escalonamento robusto e possibilidade de dividir o resultado pelo valor máximo'''
    try:
        
        col_escalonada = escalonador.fit_transform(df[[nome_col]])

        if div_max:
            max_escalonado = col_escalonada.max()
            
            if max_escalonado != 0:
                return col_escalonada / max_escalonado
            
        return col_escalonada

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} são {df[nome_col].dtype}')
        return None
    except KeyError:
        print(f'A coluna {nome_col} não foi encontrada. Favor digitar uma coluna válida.')
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        return None