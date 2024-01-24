import csv

# CSVファイルのパスを指定
csv_file_path = r'C:\Users\杉田智理\Desktop\Tools\金額例.csv'

# CSVファイルを読み込み、数値のリストを取得
with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # ヘッダー行をスキップ
    numbers = [int(row[0]) for row in reader]

# グループ分け関数の定義
def group_numbers(numbers, limit=1000000):
    numbers.sort(reverse=True)
    groups = {}

    for number in numbers:
        added_to_existing_group = False

        # 既存のグループに追加できる場合
        for key, group in groups.items():
            if sum(group) + number <= limit:
                group.append(number)
                added_to_existing_group = True
                break

        # 新しいグループを作成して追加
        if not added_to_existing_group:
            key = f"Group {len(groups) + 1}"
            groups[key] = [number]

    return groups

# グループ分け関数を使用してグループ分け
grouped_numbers = group_numbers(numbers)

# 各グループの後ろに総和を表示
for key, group in grouped_numbers.items():
    group_sum = sum(group)
    print(f"{key}: {group} (総和: {group_sum})")