import json
import random

# データ生成の設定
NUM_RECORDS = 100000  # 10万レコード生成

# 簡易的なパターン定義（実際にはここに実データの読み込み処理などが入ります）
# デモ用に、番号付きの文型を大量に生成します
templates_ja = [
    "これは{id}番目の例文です",
    "私は{id}が好きです",
    "{id}について教えてください",
    "天気予報によると{id}日は晴れです",
    "新語{id}という言葉を覚えました"
]

templates_en = [
    "This is example sentence number {id}",
    "I like {id}",
    "Tell me about {id}",
    "According to the weather forecast, it will be sunny on day {id}",
    "I learned the new word new_word_{id}"
]

templates_zh = [
    "这是第{id}个例句",
    "我喜欢{id}",
    "请告诉我关于{id}的事情",
    "根据天气预报，{id}日是晴天",
    "我学会了新词 new_word_{id}"
]

print(f"{NUM_RECORDS}件のデータを生成中...")

data = []

for i in range(1, NUM_RECORDS + 1):
    # ランダムにテンプレートを選択
    t_ja = random.choice(templates_ja).format(id=i)
    t_en = random.choice(templates_en).format(id=i)
    t_zh = random.choice(templates_zh).format(id=i)
    
    # データ構造：どの言語から検索しても hit するように登録
    record = {
        "id": i,
        "ja": t_ja,
        "en": t_en,
        "zh": t_zh
    }
    data.append(record)

    # 進捗表示 (10%ごと)
    if i % 10000 == 0:
        print(f"  ... {i}件完了")

# JSONファイルとして保存
output_file = "dictionary_data.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print(f"完了！ '{output_file}' に保存されました。")
print(f"総データ数: {len(data)} 件")
print("次に、このファイルを読み込む HTML アプリケーションを実行してください。")
