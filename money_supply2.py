import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# FREDのAPIキーを入力 (要登録)
fred = Fred(api_key='API')

# 日本のM2データを取得
japan_m2 = fred.get_series('MYAGM2JPM189N')

# アメリカのM2データを取得
us_m2 = fred.get_series('M2SL')

# データを1つのDataFrameにまとめる
data = pd.DataFrame({'Japan M2': japan_m2, 'US M2': us_m2})

# 欠損値を削除
data = data.dropna()

# インデックスを日付に設定
data.index = pd.to_datetime(data.index)

# 日本とアメリカのM2データを同じ基準年に合わせるために、最初の値で割る
base_year = data.index.min()
data['Japan M2 Normalized'] = data['Japan M2'] / data.loc[base_year, 'Japan M2']
data['US M2 Normalized'] = data['US M2'] / data.loc[base_year, 'US M2']

# グラフのサイズを設定
plt.figure(figsize=(12, 6))

# 日本とアメリカの正規化されたM2をプロット
plt.plot(data['Japan M2 Normalized'], label='Japan M2')
plt.plot(data['US M2 Normalized'], label='US M2')

# グラフのタイトルと軸ラベルを設定
plt.title('Money Supply (M2) Comparison: Japan vs United States')
plt.xlabel('Date')
plt.ylabel('Normalized Money Supply (M2)')

# 凡例を表示
plt.legend()

# グラフを表示
plt.show()
