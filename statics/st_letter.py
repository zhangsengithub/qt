from pdfminer.high_level import extract_text
from collections import Counter
import string
import argparse

def count_letter_freq(pdf_path):
    """统计 PDF 中字母频率"""
    # 提取文本并转为小写
    text = extract_text(pdf_path).lower()
    
    # 过滤非字母字符
    letters = [char for char in text if char in string.ascii_lowercase]
    
    # 统计字母出现次数
    letter_counts = Counter(letters)
    total_letters = sum(letter_counts.values())
    
    # 计算频率（百分比）
    letter_freq = {
        letter: (count / total_letters) 
        for letter, count in letter_counts.items()
    }
    
    # 按字母顺序打印结果
    for letter in sorted(letter_freq):
        print(f"{letter}: {letter_freq[letter]:.4f}")

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="统计 PDF 文件中字母的频率")
    parser.add_argument("pdf_file", help="输入的 PDF 文件路径")
    args = parser.parse_args()
    
    # 调用函数
    count_letter_freq(args.pdf_file)
