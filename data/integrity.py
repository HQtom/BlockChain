import jieba
import math
import re



# @staticmethod
def integrity_check(s1, s2):
    stopwords = ["stop"]
    s1_cut = [i for i in jieba.cut(s1, cut_all=True) if (i not in stopwords) and i != '']
    s2_cut = [i for i in jieba.cut(s2, cut_all=True) if (i not in stopwords) and i != '']
    word_set = set(s1_cut).union(set(s2_cut))

    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1

    s1_cut_code = [0] * len(word_dict)

    for word in s1_cut:
        s1_cut_code[word_dict[word]] += 1

    s2_cut_code = [0] * len(word_dict)
    for word in s2_cut:
        s2_cut_code[word_dict[word]] += 1
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
    sq1 += pow(s1_cut_code[i], 2)
    sq2 += pow(s2_cut_code[i], 2)

    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 3)
    except ZeroDivisionError:
        result = 0.0

    print("\nsimilarity：%f" % result)
    return result

