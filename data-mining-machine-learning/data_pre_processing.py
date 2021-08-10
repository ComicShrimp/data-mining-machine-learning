import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


def __filter_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe[
        [
            "EMPRESA (NOME)",
            "MES",
            "AEROPORTO DE ORIGEM (UF)",
            "AEROPORTO DE ORIGEM (REGIAO)",
            "AEROPORTO DE DESTINO (UF)",
            "AEROPORTO DE DESTINO (REGIAO)",
            "NATUREZA",  # Voo domestico
            "GRUPO DE VOO",  # Target
            "DISTANCIA VOADA (KM)",
            "HORAS VOADAS",
        ]
    ]


def __select_domestic_flights(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe[(dataframe["NATUREZA"] == "DOMESTICA")]


def __delete_nan(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.dropna()


def __name_empresa_to_num(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["EMPRESA (NOME)"] = np.where(
        dataframe["EMPRESA (NOME)"] == "AZUL LINHAS AEREAS BRASILEIRAS S/A",
        3,
        np.where(
            dataframe["EMPRESA (NOME)"]
            == "GOL LINHAS AEREAS S.A. (EX- VRG LINHAS AEREAS S.A.)",
            2,
            np.where(dataframe["EMPRESA (NOME)"] == "TAM LINHAS AEREAS S.A.", 1, 0),
        ),
    )
    return dataframe


def __regiao_to_num(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe["AEROPORTO DE DESTINO (REGIAO)"] = np.where(
        dataframe["AEROPORTO DE DESTINO (REGIAO)"] == "SUDESTE",
        5,
        np.where(
            dataframe["AEROPORTO DE DESTINO (REGIAO)"] == "NORDESTE",
            4,
            np.where(
                dataframe["AEROPORTO DE DESTINO (REGIAO)"] == "NORTE",
                3,
                np.where(
                    dataframe["AEROPORTO DE DESTINO (REGIAO)"] == "CENTRO-OESTE",
                    2,
                    np.where(dataframe["AEROPORTO DE DESTINO (REGIAO)"] == "SUL", 1, 0),
                ),
            ),
        ),
    )

    dataframe["AEROPORTO DE ORIGEM (REGIAO)"] = np.where(
        dataframe["AEROPORTO DE ORIGEM (REGIAO)"] == "SUDESTE",
        5,
        np.where(
            dataframe["AEROPORTO DE ORIGEM (REGIAO)"] == "NORDESTE",
            4,
            np.where(
                dataframe["AEROPORTO DE ORIGEM (REGIAO)"] == "NORTE",
                3,
                np.where(
                    dataframe["AEROPORTO DE ORIGEM (REGIAO)"] == "CENTRO-OESTE",
                    2,
                    np.where(dataframe["AEROPORTO DE ORIGEM (REGIAO)"] == "SUL", 1, 0),
                ),
            ),
        ),
    )

    return dataframe


def __grupo_de_voo_to_num(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["GRUPO DE VOO"] = np.where(
        dataframe["GRUPO DE VOO"] == "NAO REGULAR", 1, 0
    )

    return dataframe

def __uf_to_num(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe["AEROPORTO DE ORIGEM (UF)"] = np.where(
        dataframe["AEROPORTO DE ORIGEM (UF)"] == "SP",
        27,
        np.where(
            dataframe["AEROPORTO DE ORIGEM (UF)"] == "BA",
            26,
            np.where(
                dataframe["AEROPORTO DE ORIGEM (UF)"] == "RJ",
                25,
                np.where(
                    dataframe["AEROPORTO DE ORIGEM (UF)"] == "MG",
                    24,
                    np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "AM",
                    23, 
                        np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "PR",
                        22,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "DF",
                        21,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "PE",
                        20,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "PA",
                        19,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "RS",
                        18,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "CE",
                        17,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "SC",
                        16,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "GO",
                        15,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "MT",
                        14,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "AL",
                        13,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "RN",
                        12,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "ES",
                        11,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "MS",
                        10,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "MA",
                        9,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "RO",
                        8,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "PI",
                        7,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "SE",
                        6,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "PB",
                        5,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "TO",
                        4,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "AP",
                        3,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "RO",
                        2,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "RR",
                        1,np.where(dataframe["AEROPORTO DE ORIGEM (UF)"] == "AC",0))))))))))))))))))))))
                        ),
                    ),
                ),
            ),
        ),
    )



def data_pre_processing(file_path: str) -> pd.DataFrame:

    raw_data = pd.read_csv(file_path, sep=";")

    filtered_data = __filter_columns(raw_data)
    filtered_data = __select_domestic_flights(filtered_data)
    filtered_data = __delete_nan(filtered_data)
    filtered_data = __name_empresa_to_num(filtered_data)
    filtered_data = __regiao_to_num(filtered_data)
    filtered_data = __grupo_de_voo_to_num(filtered_data)
    filtered_data = __uf_to_num(filtered_data)

    return filtered_data
