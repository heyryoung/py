from builtins import staticmethod
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import nltk #class는 import로 가져운다.
import re
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SamsungReport:
    def __init__(self):
        self.okt = Okt()

    def read_file(self):
        self.okt.pos("삼성정자 글로벌 센터 전자 사업부", stem=True)
        filename = './driver/kr-Report_2018.txt'
        with open(filename, 'r' ,encoding='utf-8') as f:
            texts = f.read()
            print('>>>>' + texts)

        return texts

    def hook(self):
        texts = self.read_file()
        hangeul = self.extract_hangeul(texts)
        tokens = self.change_token(hangeul)
        nouns = self.extract_noun(self,tokens)
        stopwords = self.read_stopword()
        texts = self.remove_stopword(nouns,stopwords)
        self.find_freq(texts)

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        return tokenizer.sub('',temp)

    @staticmethod
    def download():
        nltk.download()

    @staticmethod
    def extract_noun(self, texts):
        noun_tokens = []
        for i in texts:
            token_pos = self.okt.pos(i)
            t = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(t)) > 1:
                noun_tokens.append(''.join(t))
        texts = ' '.join(noun_tokens)
        print("----------추출된 명사 300 ------------")
        #print(texts[:300])
        #return texts
        return noun_tokens[:300]

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        print("-----------------------")
        print(tokens[:7])
        return tokens




    def read_stopword(self):   #필요 없는 단어 목록을 읽어온다.
        stopfile = './driver/stopwords.txt'
        with open(stopfile, 'r' , encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split()
        print(stopwords[:10])
        return stopwords

    @staticmethod
    def remove_stopword( nouns , stopwords):  # 주입받은 필요없는 단어를 삭제하여 리턴한다.
        for noun in nouns:
          print (noun + "-----------------")
        return [noun for noun in nouns if noun not in stopwords]

    def find_freq(self,texts):  # 중요한 단어를 눈에 띄게 표시해 준다. 중요함의 기준은 빈도수이다.
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False) #로직을 통해 가공된 결과물을 리턴한다. (=dict ) // 이것을 자바스크립트에 던지면 JSON으로 받는다.
        print('자주 사용된 단어 1 ~ 30')
        print(freqtxt[:30])
        return freqtxt



class SamsungReport:
    def __init__(self):
        self.okt = Okt()


    def read_file(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = './driver/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts


    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp


    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        return tokens


    def extract_noun(self):
        noun_tokens = []
        tokens = self.change_token(self.extract_hangeul(self.read_file()))
        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))
        texts = " ".join(noun_tokens)
        return texts


    @staticmethod
    def download():
        nltk.download()


    @staticmethod
    def read_stopword():
        stopfile = './driver/stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        return stopwords


    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        stopwords = self.read_stopword()
        texts = [text for text in tokens
                    if text not in stopwords]
        return texts


    def hook(self):
        texts = self.remove_stopword()
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:30])
        return freqtxt

    def draw_worfcloud(self):
        texts = self.remove_stopword()
        wcloud = WordCloud('./driver/D2Coding.ttf', relative_scaling=0.2 , background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='billnear')
        plt.axis('off')
        plt.show()



#--------------------------------------------------------
# class SamsungReport:
#     def __init__(self):
#         self.okt = Okt()
#
#
#     def read_file(self):
#         self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
#         filename = './data/kr-Report_2018.txt'
#         with open(filename, 'r', encoding='utf-8') as f:
#             texts = f.read()
#         return texts
#
#
#     @staticmethod
#     def extract_hangeul(texts):
#         temp = texts.replace('\n', ' ')
#         tokenizer = re.compile(r'[^ ㄱ-힣]+')
#         temp = tokenizer.sub('', temp)
#         return temp
#
#
#     @staticmethod
#     def change_token(texts):
#         tokens = word_tokenize(texts)
#         return tokens
#
#
#     def extract_noun(self):
#         noun_tokens = []
#         tokens = self.change_token(self.extract_hangeul(self.read_file()))
#         for token in tokens:
#             token_pos = self.okt.pos(token)
#             temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
#             if len(''.join(temp)) > 1:
#                 noun_tokens.append("".join(temp))
#         texts = " ".join(noun_tokens)
#         return texts
#
#
#     @staticmethod
#     def download():
#         nltk.download()
#
#
#     @staticmethod
#     def read_stopword():
#         stopfile = './data/stopwords.txt'
#         with open(stopfile, 'r', encoding='utf-8') as f:
#             stopwords = f.read()
#         stopwords = stopwords.split(' ')
#         return stopwords
#
#
#     def remove_stopword(self):
#         texts = self.extract_noun()
#         tokens = self.change_token(texts)
#         stopwords = self.read_stopword()
#         texts = [text for text in tokens
#                     if text not in stopwords]
#         return texts
#
#
#     def hook(self):
#         texts = self.remove_stopword()
#         freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
#         print(freqtxt[:30])
#         return freqtxt

