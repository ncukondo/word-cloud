#coding: utf-8
from wordcloud import WordCloud
import requests
import MeCab


#ワードクラウド作成関数(日本語テキスト版)
def create_wordcloud_ja(text):
    fontpath = 'NotoSansCJKjp-Regular.otf'
    stop_words_ja = ['もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ', 'すべて']
    #形態素解析
    tagger = MeCab.Tagger() 
    tagger.parse('') 
    node = tagger.parseToNode(text)

    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words_ja:
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)
    wordcloud = WordCloud(background_color="white",
                        font_path=fontpath,
                        width=900,
                        height=500,
                        contour_width=1,
                        contour_color="black",
                        stopwords=set(stop_words_ja)).generate(word_chain)

    wordcloud.to_file("wc_image_ja.png")


#必要ファイルの呼び出し
#テキストの読み込み
with open('text.txt', 'r', encoding='utf-8') as fi:
    text = fi.read()

create_wordcloud_ja(text)
