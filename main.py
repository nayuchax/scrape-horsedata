import data
import scrape_controller
import re
import pandas as pd


# 行の表示数の上限を撤廃
pd.set_option('display.max_rows', None)
# 列の表示数の上限を撤廃
pd.set_option('display.max_columns', None)


# urlの取得
def url_setter(target: list[str]) -> list[str]:
    url_list = []
    for t in target:
        url = data.get_url(t)
        url_list.append(url)

    return url_list


# データ整形
def data_formatter(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()
    df_copy["騎手"] = df_copy["騎手"].replace(re.compile(r"\n"), '', regex=True)
    df_copy.drop(
        columns=["映像", "馬場指数", "ﾀｲﾑ指数", "厩舎ｺﾒﾝﾄ", "備考"],
        axis=1,
        inplace=True
    )
    return df_copy


# pandasDataFrame作成
def generate_pandas_dataframe(url: str) -> pd.DataFrame:
    table_list = scrape_controller.table_getter(url)
    columns = table_list[0]
    del table_list[0]

    df = pd.DataFrame(
        data=table_list,
        columns=columns,
    )

    return data_formatter(df)


# TODO concat再帰的処理
def concat_df(data_l: list[pd.DataFrame]) -> pd.DataFrame:
    c_df = pd.concat([data_l[0], data_l[1]])
    if n < 0:
        return c_df


    return concat_df(c_df, n)


url_list = url_setter(data.get_target_pattern())

data_list = []
for url in url_list:
    data = generate_pandas_dataframe(url)
    data_list.append(data)



# TODO pd結合 -> concat
