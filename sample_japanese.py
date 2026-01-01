# -*- coding: utf-8 -*-
"""
日本語表示のサンプルコード
JupyterLabで実行する際の参考にしてください
"""

# ============================================
# 日本語表示の設定（これを最初に実行）
# ============================================
import japanize_matplotlib  # これをインポートするだけでOK！
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ============================================
# サンプル1: matplotlibで日本語グラフ
# ============================================
def sample_matplotlib():
    """matplotlibで日本語タイトル・ラベルを表示"""
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 15, 30, 20]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linewidth=2)
    plt.title('日本語タイトルのグラフ', fontsize=14)
    plt.xlabel('横軸ラベル（日本語）')
    plt.ylabel('縦軸ラベル（日本語）')
    plt.grid(True)
    plt.show()

# ============================================
# サンプル2: seabornで日本語グラフ
# ============================================
def sample_seaborn():
    """seabornで日本語を含むデータを可視化"""
    data = pd.DataFrame({
        '都市': ['東京', '大阪', '名古屋', '福岡', '札幌'],
        '人口（万人）': [1400, 275, 232, 160, 197]
    })
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x='都市', y='人口（万人）', palette='viridis')
    plt.title('主要都市の人口比較', fontsize=14)
    plt.show()

# ============================================
# サンプル3: networkxで日本語ノード
# ============================================
def sample_networkx():
    """networkxで日本語ラベルのネットワーク図"""
    import networkx as nx
    
    G = nx.DiGraph()
    G.add_edges_from([
        ('本人', '母'),
        ('本人', '父'),
        ('本人', '配偶者'),
        ('本人', '子供1'),
        ('本人', '子供2'),
        ('母', '祖母'),
        ('父', '祖父'),
    ])
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, 
            with_labels=True, 
            node_color='lightblue',
            node_size=2000,
            font_size=12,
            font_family='IPAexGothic',  # 日本語フォント指定
            arrows=True,
            edge_color='gray')
    plt.title('家族関係のネットワーク図', fontsize=14)
    plt.show()

# ============================================
# 実行例（JupyterLabで各関数を呼び出し）
# ============================================
if __name__ == '__main__':
    print("JupyterLabで以下を実行してください：")
    print()
    print("import japanize_matplotlib")
    print("sample_matplotlib()")
    print("sample_seaborn()")
    print("sample_networkx()")
