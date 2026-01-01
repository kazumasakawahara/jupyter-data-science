# 📊 General Analysis - 一般データ分析環境

Python + JupyterLab によるデータ分析用の仮想環境です。  
日本語表示対応済み。パッケージ管理には **uv** を使用しています。

---

## 📁 フォルダ構成

```
general-analysis/
├── notebooks/              # 作業用フォルダ（.ipynbファイルを保存）
├── .venv/                  # 仮想環境（自動生成）
├── pyproject.toml          # パッケージ管理ファイル
├── uv.lock                 # 依存関係ロックファイル
├── sample_japanese.py      # 日本語表示サンプルコード
├── start-jupyter.command   # JupyterLab起動スクリプト
└── README.md               # このファイル
```

---

## 🚀 起動方法

### 方法1: デスクトップアイコンから
デスクトップの **「JupyterLab（データ分析）」** をダブルクリック

### 方法2: ターミナルから
```bash
cd ~/Data-Science/general-analysis
uv run jupyter lab --notebook-dir=./notebooks
```

---

## 📦 インストール済みパッケージ

### データ操作
| パッケージ | 用途 |
|-----------|------|
| pandas | データフレーム操作・分析 |
| numpy | 数値計算 |
| openpyxl | Excelファイル読み書き |

### 可視化
| パッケージ | 用途 |
|-----------|------|
| matplotlib | グラフ作成（基本） |
| seaborn | 統計的可視化 |
| plotly | インタラクティブグラフ |
| japanize-matplotlib | 日本語表示対応 |

### ネットワーク分析
| パッケージ | 用途 |
|-----------|------|
| networkx | ネットワーク分析・グラフ理論 |
| graphviz | グラフ可視化（決定木など） |

### 時系列分析
| パッケージ | 用途 |
|-----------|------|
| statsmodels | 統計分析（ARIMA、季節分解など） |
| prophet | 時系列予測（Meta開発） |
| pmdarima | ARIMAパラメータ自動最適化 |

---

## 🇯🇵 日本語表示の使い方

ノートブックの最初に以下を追加するだけで、グラフに日本語が表示できます。

```python
import japanize_matplotlib
```

### サンプルコード

```python
import japanize_matplotlib
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [10, 25, 15, 30, 20], marker='o')
plt.title('日本語タイトル')
plt.xlabel('横軸（日本語）')
plt.ylabel('縦軸（日本語）')
plt.grid(True)
plt.show()
```

---

## 📈 使用例

### pandas - データ読み込み
```python
import pandas as pd

# CSVファイル読み込み
df = pd.read_csv('data.csv')

# Excelファイル読み込み
df = pd.read_excel('data.xlsx')

# 基本統計量
df.describe()
```

### seaborn - 可視化
```python
import japanize_matplotlib
import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    '都市': ['東京', '大阪', '名古屋', '福岡'],
    '人口': [1400, 275, 232, 160]
})

sns.barplot(data=data, x='都市', y='人口')
plt.title('主要都市の人口')
plt.show()
```

### networkx - ネットワーク図
```python
import japanize_matplotlib
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('本人', '母'), ('本人', '父'), ('本人', '配偶者')])

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', 
        node_size=2000, font_size=12)
plt.show()
```

### Prophet - 時系列予測
```python
from prophet import Prophet
import pandas as pd

# データ準備（ds: 日付, y: 値）
df = pd.DataFrame({
    'ds': pd.date_range('2024-01-01', periods=100, freq='D'),
    'y': [100 + i*0.5 for i in range(100)]
})

# モデル作成・予測
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
model.plot(forecast)
```

---

## 🔧 パッケージの追加方法

新しいパッケージを追加したい場合：

```bash
cd ~/Data-Science/general-analysis
uv add パッケージ名
```

例：
```bash
uv add scipy  # 科学計算ライブラリを追加
```

---

## ⚠️ トラブルシューティング

### JupyterLabが起動しない場合
```bash
cd ~/Data-Science/general-analysis
uv sync  # 依存関係を再同期
uv run jupyter lab --notebook-dir=./notebooks
```

### 日本語が文字化けする場合
ノートブックの最初のセルで以下を実行：
```python
import japanize_matplotlib
```

---

## 📅 作成日

2025年1月1日
# jupyter-data-science
