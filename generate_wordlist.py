#!/usr/bin/env pythone
# coding: utf-8
# 制作8192 (2 ** 13)长度的diceware词典. 抛硬币13次产生"1位"密码.
import os


KEY_ENTROPY = 13
MAX_LENGTH = 8
MIN_LENGTH = 4 # a-z最短3位: log(8192, 26) = 2.77

MAX_EXAMPLE_HANZI = 5
MAINTAIN_PREFIXCODE = True

to_bin = lambda x, n: format(x, 'b').zfill(n)
def prettify(string, length = 4):
    # '00001' to '0 0001'
    return ' '.join([string[max(i - length, 0):i] for i in range(len(string), 0, -length)][::-1])


txt = []
with open(os.path.join('source', '现代汉语常用词表.txt'), 'r') as f:
    for line in f:
        # skip comments.
        if line.startswith('#'):
            continue
        parts = line.split('\t')
        # skip invalid lines.
        if len(parts) != 3:
            continue
        hanzi, pinyin, rank = parts
        hanzi = hanzi.strip()
        pinyin = ''.join(c for c in pinyin if c.isalpha())
        pinyin = pinyin.lower()
        rank = int(rank)
        # skip not 双音节词
        if len(hanzi) != len('汉语'):
            continue

        # limit pinyin length:
        if len(pinyin) < MIN_LENGTH or len(pinyin) > MAX_LENGTH:
            # skip other lengths. (其他长度数量少, 易被偷听. 推荐用"."分隔并放慢输入速度, 随机停顿.)
            continue
        txt.append([hanzi, pinyin, rank])

txt = sorted(txt, key=lambda x: x[2])

def in_nested(string, dic):
    pointer = dic
    for c in list(string):
        if c in pointer:
            pointer = pointer[c]
        else:
            return False
    return True

def append_nested(string, dic):
    pointer = dic
    length = len(string)
    i = 0
    while string[i] in pointer:
        pointer = pointer[string[i]]
        i += 1
        if i == length:
            return dic
    for j in range(i, length):
        pointer[string[j]] = {}
        pointer = pointer[string[j]]
    return dic



dictionary = {}
occupied_prefix = {}
skipped = 0
for parts in txt:
    hanzi, pinyin, rank = parts
    if pinyin not in dictionary:
        if MAINTAIN_PREFIXCODE:
            # 维持整体是prefix code, 从而一串拼音密码不会有错开的2种汉字解释,
            # 从而密码空间不会腰斩, 从而允许省略间隔符号.
            # 但是会因此排除了一些高频的词语. 排除: 1394 / 保留: 8192
            # 1. dictionary中是否有pinyin的前缀(pinyin更长):
            temp = pinyin
            still_prefixcode = True
            while temp != '' and still_prefixcode:
                if temp in dictionary:
                    still_prefixcode = False
                temp = temp[:-1]

            # 2. pinyin是否是dictionary中某个key的前缀(pinyin更短):
            if still_prefixcode:
                if in_nested(pinyin, occupied_prefix):
                    still_prefixcode = False

            if still_prefixcode:
                dictionary[pinyin] = {'rank': rank, 'words': [hanzi]}
                occupied_prefix = append_nested(pinyin, occupied_prefix)
            else:
                if len(dictionary) <= 2 ** KEY_ENTROPY:
                    skipped += 1
        else:
            dictionary[pinyin] = {'rank': rank, 'words': [hanzi]}

    else:
        if dictionary[pinyin]['rank'] > rank:
            dictionary[pinyin]['rank'] = rank
        if len(dictionary[pinyin]['words']) < MAX_EXAMPLE_HANZI:
            dictionary[pinyin]['words'].append(hanzi)

print('生成前%d个拼音的同时跳过了%d个会破坏前缀码的拼音.'%(2 ** KEY_ENTROPY, skipped))

with open(os.path.join('pinyin_excluded.txt'), 'r') as f:
    for line in f:
        pinyin = line.split()
        if pinyin:
            dictionary.pop(pinyin[0], None)


dictionary = sorted(dictionary.items(), key=lambda x: x[1]['rank'])
assert len(dictionary) >= 2 ** KEY_ENTROPY


dist = {}
with open('wordlist.txt', 'w') as f:
    for i in range(len(dictionary)):
        if i >= 2 ** KEY_ENTROPY:
            break
        pinyin, words = dictionary[i]
        f.write('%s\t%4d\t%s\t例: %s\n'%(prettify(to_bin(i, KEY_ENTROPY)), i,
            ('{0:%d}'%MAX_LENGTH).format(pinyin), ' '.join(words['words'])))

        length = len(pinyin)
        if length in dist:
            dist[length] += 1
        else:
            dist[length] = 1

print('混合词长分布:'),
print(dist)
print('词典制作完成.')
