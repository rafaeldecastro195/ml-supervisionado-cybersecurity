import traceback

def drop_outlier(df, nome_col, outlier_inferior, outlier_superior):
    '''Funcao que exclui outliers, a partir dos valores do limite superior e inferior'''
    try:
        df = df.drop(df[(df[nome_col] < outlier_inferior) | (df[nome_col] > outlier_superior)].index)
        df = df.reset_index(drop=True)
        return df
    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados. Os dados do atributo {nome_col} sao {df[nome_col].dtype}')
        traceback.print_exc()
        return None
    except KeyError:
        print(f'A coluna {nome_col} nao foi encontrada. Favor digitar uma coluna valida.')
        traceback.print_exc()
        return None
    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
        traceback.print_exc()
        return None


def normalizar_feature(df, nome_col, escalonador, transformar_apenas=False, div_max=False, achatamento=False):
    '''Funcao generica para normalizar features aceitando qualquer escalonador do Scikit-Learn'''
    try:
        colunas = [nome_col] if isinstance(nome_col, str) else nome_col
        dados_selecionados = df[colunas]

        if not transformar_apenas:
            col_escalonada = escalonador.fit_transform(dados_selecionados)

        if transformar_apenas:
            col_escalonada = escalonador.transform(dados_selecionados)

        if div_max:
            max_escalonado = col_escalonada.max()
            if max_escalonado != 0:
                col_escalonada = col_escalonada / max_escalonado

        if achatamento:
            col_escalonada = col_escalonada.flatten()

        return col_escalonada

    except ValueError:
        print(f'Erro de valor. Confira a tipagem dos dados enviados.')
        traceback.print_exc()
        return None
    except KeyError:
        print(f'A coluna {nome_col} nao foi encontrada. Favor digitar uma coluna valida.')
        traceback.print_exc()
        return None
    except Exception as e:
        print(f'Ocorreu esse erro: {e}')
        traceback.print_exc()
        return None
