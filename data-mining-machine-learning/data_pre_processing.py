from typing import Tuple
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
        28,
        np.where(
            dataframe["AEROPORTO DE ORIGEM (UF)"] == "BA",
            27,
            np.where(
                dataframe["AEROPORTO DE ORIGEM (UF)"] == "RJ",
                26,
                np.where(
                    dataframe["AEROPORTO DE ORIGEM (UF)"] == "MG",
                    25,
                    np.where(
                        dataframe["AEROPORTO DE ORIGEM (UF)"] == "AM",
                        24,
                        np.where(
                            dataframe["AEROPORTO DE ORIGEM (UF)"] == "PR",
                            23,
                            np.where(
                                dataframe["AEROPORTO DE ORIGEM (UF)"] == "DF",
                                22,
                                np.where(
                                    dataframe["AEROPORTO DE ORIGEM (UF)"] == "PE",
                                    21,
                                    np.where(
                                        dataframe["AEROPORTO DE ORIGEM (UF)"] == "PA",
                                        20,
                                        np.where(
                                            dataframe["AEROPORTO DE ORIGEM (UF)"]
                                            == "RS",
                                            19,
                                            np.where(
                                                dataframe["AEROPORTO DE ORIGEM (UF)"]
                                                == "CE",
                                                18,
                                                np.where(
                                                    dataframe[
                                                        "AEROPORTO DE ORIGEM (UF)"
                                                    ]
                                                    == "SC",
                                                    17,
                                                    np.where(
                                                        dataframe[
                                                            "AEROPORTO DE ORIGEM (UF)"
                                                        ]
                                                        == "GO",
                                                        16,
                                                        np.where(
                                                            dataframe[
                                                                "AEROPORTO DE ORIGEM (UF)"
                                                            ]
                                                            == "MT",
                                                            15,
                                                            np.where(
                                                                dataframe[
                                                                    "AEROPORTO DE ORIGEM (UF)"
                                                                ]
                                                                == "AL",
                                                                14,
                                                                np.where(
                                                                    dataframe[
                                                                        "AEROPORTO DE ORIGEM (UF)"
                                                                    ]
                                                                    == "RN",
                                                                    13,
                                                                    np.where(
                                                                        dataframe[
                                                                            "AEROPORTO DE ORIGEM (UF)"
                                                                        ]
                                                                        == "ES",
                                                                        12,
                                                                        np.where(
                                                                            dataframe[
                                                                                "AEROPORTO DE ORIGEM (UF)"
                                                                            ]
                                                                            == "MS",
                                                                            11,
                                                                            np.where(
                                                                                dataframe[
                                                                                    "AEROPORTO DE ORIGEM (UF)"
                                                                                ]
                                                                                == "MA",
                                                                                10,
                                                                                np.where(
                                                                                    dataframe[
                                                                                        "AEROPORTO DE ORIGEM (UF)"
                                                                                    ]
                                                                                    == "RO",
                                                                                    9,
                                                                                    np.where(
                                                                                        dataframe[
                                                                                            "AEROPORTO DE ORIGEM (UF)"
                                                                                        ]
                                                                                        == "PI",
                                                                                        8,
                                                                                        np.where(
                                                                                            dataframe[
                                                                                                "AEROPORTO DE ORIGEM (UF)"
                                                                                            ]
                                                                                            == "SE",
                                                                                            7,
                                                                                            np.where(
                                                                                                dataframe[
                                                                                                    "AEROPORTO DE ORIGEM (UF)"
                                                                                                ]
                                                                                                == "PB",
                                                                                                6,
                                                                                                np.where(
                                                                                                    dataframe[
                                                                                                        "AEROPORTO DE ORIGEM (UF)"
                                                                                                    ]
                                                                                                    == "TO",
                                                                                                    5,
                                                                                                    np.where(
                                                                                                        dataframe[
                                                                                                            "AEROPORTO DE ORIGEM (UF)"
                                                                                                        ]
                                                                                                        == "AP",
                                                                                                        4,
                                                                                                        np.where(
                                                                                                            dataframe[
                                                                                                                "AEROPORTO DE ORIGEM (UF)"
                                                                                                            ]
                                                                                                            == "RO",
                                                                                                            3,
                                                                                                            np.where(
                                                                                                                dataframe[
                                                                                                                    "AEROPORTO DE ORIGEM (UF)"
                                                                                                                ]
                                                                                                                == "RR",
                                                                                                                2,
                                                                                                                np.where(
                                                                                                                    dataframe[
                                                                                                                        "AEROPORTO DE ORIGEM (UF)"
                                                                                                                    ]
                                                                                                                    == "AC",
                                                                                                                    1,
                                                                                                                    0,
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )

    dataframe["AEROPORTO DE DESTINO (UF)"] = np.where(
        dataframe["AEROPORTO DE DESTINO (UF)"] == "SP",
        28,
        np.where(
            dataframe["AEROPORTO DE DESTINO (UF)"] == "BA",
            27,
            np.where(
                dataframe["AEROPORTO DE DESTINO (UF)"] == "RJ",
                26,
                np.where(
                    dataframe["AEROPORTO DE DESTINO (UF)"] == "MG",
                    25,
                    np.where(
                        dataframe["AEROPORTO DE DESTINO (UF)"] == "AM",
                        24,
                        np.where(
                            dataframe["AEROPORTO DE DESTINO (UF)"] == "PR",
                            23,
                            np.where(
                                dataframe["AEROPORTO DE DESTINO (UF)"] == "DF",
                                22,
                                np.where(
                                    dataframe["AEROPORTO DE DESTINO (UF)"] == "PE",
                                    21,
                                    np.where(
                                        dataframe["AEROPORTO DE DESTINO (UF)"] == "PA",
                                        20,
                                        np.where(
                                            dataframe["AEROPORTO DE DESTINO (UF)"]
                                            == "RS",
                                            19,
                                            np.where(
                                                dataframe["AEROPORTO DE DESTINO (UF)"]
                                                == "CE",
                                                18,
                                                np.where(
                                                    dataframe[
                                                        "AEROPORTO DE DESTINO (UF)"
                                                    ]
                                                    == "SC",
                                                    17,
                                                    np.where(
                                                        dataframe[
                                                            "AEROPORTO DE DESTINO (UF)"
                                                        ]
                                                        == "GO",
                                                        16,
                                                        np.where(
                                                            dataframe[
                                                                "AEROPORTO DE DESTINO (UF)"
                                                            ]
                                                            == "MT",
                                                            15,
                                                            np.where(
                                                                dataframe[
                                                                    "AEROPORTO DE DESTINO (UF)"
                                                                ]
                                                                == "AL",
                                                                14,
                                                                np.where(
                                                                    dataframe[
                                                                        "AEROPORTO DE DESTINO (UF)"
                                                                    ]
                                                                    == "RN",
                                                                    13,
                                                                    np.where(
                                                                        dataframe[
                                                                            "AEROPORTO DE DESTINO (UF)"
                                                                        ]
                                                                        == "ES",
                                                                        12,
                                                                        np.where(
                                                                            dataframe[
                                                                                "AEROPORTO DE DESTINO (UF)"
                                                                            ]
                                                                            == "MS",
                                                                            11,
                                                                            np.where(
                                                                                dataframe[
                                                                                    "AEROPORTO DE DESTINO (UF)"
                                                                                ]
                                                                                == "MA",
                                                                                10,
                                                                                np.where(
                                                                                    dataframe[
                                                                                        "AEROPORTO DE DESTINO (UF)"
                                                                                    ]
                                                                                    == "RO",
                                                                                    9,
                                                                                    np.where(
                                                                                        dataframe[
                                                                                            "AEROPORTO DE DESTINO (UF)"
                                                                                        ]
                                                                                        == "PI",
                                                                                        8,
                                                                                        np.where(
                                                                                            dataframe[
                                                                                                "AEROPORTO DE DESTINO (UF)"
                                                                                            ]
                                                                                            == "SE",
                                                                                            7,
                                                                                            np.where(
                                                                                                dataframe[
                                                                                                    "AEROPORTO DE DESTINO (UF)"
                                                                                                ]
                                                                                                == "PB",
                                                                                                6,
                                                                                                np.where(
                                                                                                    dataframe[
                                                                                                        "AEROPORTO DE DESTINO (UF)"
                                                                                                    ]
                                                                                                    == "TO",
                                                                                                    5,
                                                                                                    np.where(
                                                                                                        dataframe[
                                                                                                            "AEROPORTO DE DESTINO (UF)"
                                                                                                        ]
                                                                                                        == "AP",
                                                                                                        4,
                                                                                                        np.where(
                                                                                                            dataframe[
                                                                                                                "AEROPORTO DE DESTINO (UF)"
                                                                                                            ]
                                                                                                            == "RO",
                                                                                                            3,
                                                                                                            np.where(
                                                                                                                dataframe[
                                                                                                                    "AEROPORTO DE DESTINO (UF)"
                                                                                                                ]
                                                                                                                == "RR",
                                                                                                                2,
                                                                                                                np.where(
                                                                                                                    dataframe[
                                                                                                                        "AEROPORTO DE DESTINO (UF)"
                                                                                                                    ]
                                                                                                                    == "AC",
                                                                                                                    1,
                                                                                                                    0,
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )

    return dataframe


def __remove_tipo_voo(dataframe: pd.DataFrame) -> None:
    del dataframe["NATUREZA"]


def data_pre_processing(file_path: str) -> pd.DataFrame:

    raw_data = pd.read_csv(file_path, sep=";")

    filtered_data = __filter_columns(raw_data)
    filtered_data = __select_domestic_flights(filtered_data)
    filtered_data = __delete_nan(filtered_data)
    filtered_data = __name_empresa_to_num(filtered_data)
    filtered_data = __regiao_to_num(filtered_data)
    filtered_data = __grupo_de_voo_to_num(filtered_data)
    filtered_data = __uf_to_num(filtered_data)
    __remove_tipo_voo(filtered_data)

    return filtered_data


def divide_dataframe(dataframe: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return (
        dataframe[
            [
                "EMPRESA (NOME)",
                "MES",
                "AEROPORTO DE ORIGEM (UF)",
                "AEROPORTO DE ORIGEM (REGIAO)",
                "AEROPORTO DE DESTINO (UF)",
                "AEROPORTO DE DESTINO (REGIAO)",
                "DISTANCIA VOADA (KM)",
                "HORAS VOADAS",
            ]
        ],
        dataframe["GRUPO DE VOO"],
    )
