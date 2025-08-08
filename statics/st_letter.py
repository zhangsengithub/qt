from pdfminer.high_level import extract_text
from collections import Counter
import string
import argparse
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体（使用系统自带字体）
rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 尝试这些字体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 然后在你的绘图代码后添加：
plt.rcParams['font.size'] = 12  # 可调整字体大小

def count_letter_freq(pdf_path):
    """统计 PDF 中字母频率并生成直方图"""
    # 提取文本并转为小写
    text = extract_text(pdf_path).lower()
    
    # 过滤非字母字符
    letters = [char for char in text if char in string.ascii_lowercase]
    
    # 统计字母出现次数
    letter_counts = Counter(letters)
    total_letters = sum(letter_counts.values())
    
    # 计算频率（小数形式）
    letter_freq = {
        letter: (count / total_letters)
        for letter, count in letter_counts.items()
    }
    
    # 按频率从高到低排序
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    letters_sorted = [item[0] for item in sorted_freq]
    freqs_sorted = [item[1] for item in sorted_freq]
    
    # 生成直方图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(letters_sorted, freqs_sorted, color='skyblue')
    
    # 添加数据标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.4f}',
                 ha='center', va='bottom', fontsize=8)
    
    # 设置图表标题和标签
    plt.title('字母频率分布（按频率降序排序）', fontsize=14)
    plt.xlabel('字母', fontsize=12)
    plt.ylabel('频率', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 自动调整布局并显示
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="统计 PDF 文件中字母的频率并生成直方图")
    parser.add_argument("pdf_file", help="输入的 PDF 文件路径")
    args = parser.parse_args()
    
    # 调用函数
    count_letter_freq(args.pdf_file)
