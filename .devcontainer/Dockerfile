FROM python:3.8-buster

# 作業ディレクトリを作り移動する
WORKDIR /work

# 日本語フォントのインストール
RUN apt update \
  && curl -o /tmp/NotoSansCJKjp-hinted.zip https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
  && unzip -o -d /usr/share/fonts/noto /tmp/NotoSansCJKjp-hinted.zip \
  && chmod 644 /usr/share/fonts/noto/*.otf \
  && fc-cache -fv

# MeCabインストール
# ldconfigはライブラリパスのキャッシュ更新用
RUN wget  -O ./mecab.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' \
  && tar zxvf mecab.tar.gz \
  && cd mecab-0.996 \
  && ./configure \
  && make \
  && make check \
  && make install \
  && ldconfig \
  && cd ../ \
  && rm -rf mecab-0.996

# IPA辞書インストール
# 半角記号が名詞・サ変接続になるのを記号・一般に変更
RUN wget   -O mecab-ipadic.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM' \ 
  && tar zxvf mecab-ipadic.tar.gz \
  && cd mecab-ipadic-2.7.0-20070801 \
  && iconv -f eucjp -t utf8 unk.def > unk_utf8.def \
  && sed -i -e 's/SYMBOL,1283,1283,17585,名詞,サ変接続,\*,\*,\*,\*,\*/SYMBOL,1283,1283,17585,記号,一般,\*,\*,\*,\*,\*/' unk_utf8.def \
  && mv unk.def unk.def.original \
  && iconv -f utf8 -t eucjp unk_utf8.def > unk.def \
  && ./configure --with-charset=utf8 --enable-utf8-only \
  && make \
  && make install \
  && cp unk.def /usr/local/lib/mecab/dic/ipadic \
  && cd ../ \
  && rm -rf mecab-ipadic-2.7.0-20070801

# MeCabのPythonラッパー他必要ライブラリ
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# インストールに使用したファイルを削除
RUN rm -rf /work/*

#  ユーザーを作成してデフォルトユーザーにする
RUN groupadd -r pyuser \
  && adduser --ingroup pyuser --gecos "" --disabled-login pyuser
USER pyuser
