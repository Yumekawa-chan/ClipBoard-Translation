# ClipBoard-Translation
# 説明
Ctrl+Cでコピーした任意の言語の文章をCtrl+Vでペーストすると指定した言語で翻訳されます。

# 必要なpip
・googletrans

`pip install googletrans`

だと実行時に失敗するので

`pip install googletrans==4.0.0-rc1`

こっちね。

# コード説明
### 言語を設定する
10行目

`trans_txt = tr.translate(txt,src='en',dest='ja').text`

srcが翻訳したい言語

destが翻訳後の言語

### 終了方法
PromptでCtrl+C、当たり前すぎたかな。

# 使用例
Excelを使った英語のテストなど。秒速で終わります。

![image](https://user-images.githubusercontent.com/82374688/141104059-cd6f2c45-c5d6-4096-8625-df59a204c348.png)

