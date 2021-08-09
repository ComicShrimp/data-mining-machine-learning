import pandas as pd


def __filter_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe[
        [
            "EMPRESA (NOME)",
            "MÊS",
            "AEROPORTO DE ORIGEM (NOME)",
            "AEROPORTO DE ORIGEM (UF)",
            "AEROPORTO DE ORIGEM (REGIÃO)",
            "AEROPORTO DE DESTINO (NOME)",
            "AEROPORTO DE DESTINO (UF)",
            "AEROPORTO DE DESTINO (REGIÃO)",
            "NATUREZA",  # Voo domestico
            "GRUPO DE VOO",  # Target
            "PASSAGEIROS PAGOS",
            "PASSAGEIROS GRÁTIS",
            "CARGA PAGA (KG)",
            "CARGA GRÁTIS (KG)",
            "CORREIO (KG)",
            "COMBUSTÍVEL (LITROS)",
            "DISTÂNCIA VOADA (KM)",
            "DECOLAGENS",
            "ASSENTOS",
            "PAYLOAD",
            "HORAS VOADAS",
            "BAGAGEM (KG)",
        ]
    ]


def __select_domestic_flights(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe[(dataframe["NATUREZA"] == "")]


def data_pre_processing(file_path: str) -> pd.DataFrame:
    raw_data = pd.read_csv(file_path, sep=";")

    filtered_data = __filter_columns(raw_data)
