import csv

# 検索ソース
source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    for i in range(len(source)):
        if source[i] == word:
            print(f'{word}が見つかりました')
            break
        if i == len(source)-1:
            print(f'{word}は見つかりませんでした。追加登録します。')
            source.append(word)
            print(source)

    with open('search.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(source)

if __name__ == "__main__":
    search()
