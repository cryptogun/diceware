#!/usr/bin/env python3
# coding: utf-8
from random import SystemRandom

try:
    # python2
    input = raw_input
except NameError:
    # python3
    pass

KEY_ENTROPY = 13

print(
'''
>>>>>>>>>>>>>>>警告<<<<<<<<<<<<<<<
请勿使用电脑生成重要的密码!!! 因为电脑可能含有恶意软件!
本脚本只用于看看diceware长什么样, 或者生成不重要的密码.

建议:
拿出硬币和纸笔.
双手包住硬币摇动随意次, 从而引入随机变量.
不知道正反面, 向上抛. 抛硬币13次*8回并记录结果.
每抛一次, 信息熵 +1bit.
打印密码表 wordlist.txt.
记忆拼音密码. 由符号分隔.
几天后, 确保密码记住了之后, 销毁记录结果的纸张.

风险换方便: 无需硬币和纸笔, 在Tail系统下运行本脚本, 生成密码.
更大风险换更多方便: 无需打印, 抛硬币13次*8回并记录结果, 打开密码表, "匀速拖动, 随机停顿", 查看并记忆拼音密码.
>>>>>>>>>>>>>>>警告<<<<<<<<<<<<<<<
'''
)

wordlist = {}

with open('wordlist.txt', 'r') as f:
    for line in f:
        line = line.strip()
        parts = line.split('\t')
        if len(parts) != 4:
            continue
        wordlist[parts[0].replace(' ', '')] = (parts[2], parts[3])


if '1' * KEY_ENTROPY not in wordlist:
    print('%s不在词典中. 请检查词典第一列的长度是否为%d.'%('1' * KEY_ENTROPY, len(KEY_ENTROPY)))
    exit(1)

# https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python
cryptogen = SystemRandom()

count = 0
while True:
    count += 1
    print('生成中...')
    password = []
    for i in range(8):
        random_01s = bin(cryptogen.randint(0, 2 ** KEY_ENTROPY - 1))[2:].zfill(KEY_ENTROPY)
        password.append((wordlist[random_01s], ))

    print('\n结果:')
    print('每节强度: %dbit'%KEY_ENTROPY)
    print('简单密码: 前4个. 普通密码: 前6个. 高级密码: 请用硬币生成.')
    print_pinyin = []
    print_hanzi = []
    print_example = []
    for i in range(len(password)):
        word = password[i][0]
        print_pinyin.append(word[0].strip())
        print_hanzi.append(word[1].replace('例: ', '')[:len('密码')])
        print_example.append('%s\t%s'%(word[0], word[1].replace('例: ', '')))

    print('.'.join(print_pinyin))
    print('.'.join(print_hanzi))
    for i in print_example:
        print(i)
    if count >= 10:
        print('不许挑剔! 挑剔10次相当于少了一位数字的密码哦.')
        print('目前累计生成%d个密码.'%count)
        print('如果上述密码都是为了同一个目的, 最好还是在上面的生成密码中挑选.')

    print('\n警告: 请勿使用电脑生成重要的密码!!!')
    input('\n按Ctrl+c退出软件. 按回车生成下一个密码...')

