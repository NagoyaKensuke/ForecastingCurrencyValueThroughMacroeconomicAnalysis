import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# FREDのAPIキーを入力 (要登録)
fred = Fred(api_key='API')

# 日本のマネーサプライデータを取得
japan_m1 = fred.get_series('MANMM101JPM189N')
japan_m2 = fred.get_series('MYAGM2JPM189N')
japan_m3 = fred.get_series('MABMM301JPM189N')

# アメリカのマネーサプライデータを取得
us_m1 = fred.get_series('M1SL')
us_m2 = fred.get_series('M2SL')
us_m3 = fred.get_series('MABMM301USM189S')

# データを1つのDataFrameにまとめる
data = pd.DataFrame({'Japan M1': japan_m1, 'Japan M2': japan_m2, 'Japan M3': japan_m3,
                     'US M1': us_m1, 'US M2': us_m2, 'US M3': us_m3})

# 欠損値を削除
data = data.dropna()

# インデックスを日付に設定
data.index = pd.to_datetime(data.index)

# 日本とアメリカのマネーサプライデータを同じ基準年に合わせるために、最初の値で割る
base_year = data.index.min()
for column in data.columns:
    data[f'{column} Normalized'] = data[column] / data.loc[base_year, column]

# グラフのサイズを設定
plt.figure(figsize=(12, 6))

# 日本とアメリカの正規化されたマネーサプライをプロット
for column in data.columns:
    if 'Normalized' in column:
        plt.plot(data[column], label=column)

# グラフのタイトルと軸ラベルを設定
plt.title('Money Supply Comparison: Japan vs United States')
plt.xlabel('Date')
plt.ylabel('Normalized Money Supply')

# 凡例を表示
plt.legend()

# グラフを表示
plt.show()
