# 接收用户输入的字符串
text = input("请输入字符串：")

# 统计每个字符出现的频率
char_freq = {}
for char in text:
    # 如果字符是字母（可根据需求调整，比如包含其他字符）
    if char.isalpha():
        char_freq[char] = char_freq.get(char, 0) + 1

# 按字符出现频率降序排序
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

# 打印结果
for char, freq in sorted_chars:
    print(f"{char}: {freq}")
