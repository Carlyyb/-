from pypinyin import lazy_pinyin
import re


pts = ["[1]+", "[2abc]+", "[3def]+", "[4ghi]+", "[5jkl]+", "[6mno]+", "[7pqrs]+", "[8tuv]+", "[9wxyz]+"]
def parse(words__):
    if words__ == "quit":
        return None
    for i in range(len(pts)):
        pt = pts[i]
        pattern = re.compile(pt)
        match = list(set(pattern.findall(words__)))
        if not match:
            continue
        match.sort()
        lst = []  # 存放已经转换过的拼音字符
        for j in match:
            if j in lst:
                continue
            if len(j) > 1:  # 处理match中多位字符
                for a in j:
                    if a in lst:
                        continue
                    else:
                        j = a
                        break
            words__ = words__.replace(j, str(i+1))
            lst.append(j)
    return words__


if __name__ == "__main__":
    print("输入quit退出")
    while True:
        words = parse("".join(lazy_pinyin(input("输入要转换为九宫格编号的汉字："))).lower())
        if words:
            print(words)
        else:
            break
