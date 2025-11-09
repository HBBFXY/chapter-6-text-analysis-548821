# -*- 编码: utf-8 -*-
# 在此文件处编辑代码

def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    参数：
        text - 输入的字符串
    返回：
        list - 按字符频率降序排列的字符列表（格式为["字符:频率", ...]）
    """
    # 统计字符频率
    freq_dict = {}
    for char in text:
        # 排除换行符（因输入是多行合并，换行符不需要统计）
        if char != '\n':
            freq_dict[char] = freq_dict.get(char, 0) + 1
    
    # 按频率降序排序，再按字符升序（频率相同时）
    sorted_items = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # 格式化为"字符:频率"的列表
    return [f"{char}:{count}" for char, count in sorted_items]


# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
    
    # 提示用户比较不同语言
    print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
