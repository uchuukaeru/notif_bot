# 配信通知Discord-bot
## 概要
> ミラティブの配信をDiscordに通知するbot<br>

## 動作環境
> WindowsPC<br>

## 言語
> python3.9.7<br>

## 対応サイト
> mirrativ<br>

## 使用方法
> python3 main.py /*サーバID*
※ただし、サーバIDはserver.jsonに記載しているものに限る。

## 前提ライブラリ
標準ライブラリ<br>
> from urllib import request<br>
> import json<br>
> import datetime as dt<br>
> import sys<br>

非標準ライブラリ<br>
> import discord※discord.pyは更新が停止していることを理解しておいてください。<br>
> from discord.ext import tasks<br>
> from bs4 import BeautifulSoup<br>
> from selenium import webdriver<br>
> import chromedriver_binary※動作環境によって変化します。<br>

## ファイル
### main.py
bot本体<br>
### log.py
ログファイルの操作に関する関数群<br>
#### メインとして動作させた場合の挙動
なし<br>
#### 関数一覧
output_log
replace_in_list
log_match
serious_error

### notif.py
webスクレイピングと通知に関する関数群<br>
#### メインとして動作させた場合の挙動
最新の配信の情報を取得しターミナルに出力する。この際、ログファイルには出力されない<br>
#### 関数一覧
connect_test
sq
get_Livelist
get_name_dy
html_del_tags
make_link
input_USERLIST
get_USERLIST
notif

### command.py
コマンド関連の処理に関する関数群<br>
#### メインとして動作させた場合の挙動
コマンドの動作テストを行える。この際、ログファイルには出力されない。<br>
#### 関数一覧
sort_COMMAND
input_COMMAND
List_com
Help_com
Readme_com
funcselect
typeselect

### command.json
botで対応するコマンドを記述するjsonファイル<br>
#### 記述例<br>
{<br>
    "message":"/*コマンド*",<br>
    "type":/*タイプ*,<br>
    "return":/*出力する文章*<br>
}<br>
#### タイプ
> message    :returnの内容をそのまま出力する。<br>
> function   :何らかの関数の結果を出力する。"return"は不要。<br>
### userlist.json
botで通知する配信者を記述するjsonファイル<br>
server.jsonへの吸収を検討中(2021/12/23)<br>
#### 記述例<br>
{<br>
    "ID":/*配信者のミラティブのユーザID*,<br>
    "name":/*配信者名*※無くても構わない<br>
}<br>
### server.json
botを導入するサーバとルーム(チャンネル)を記述するjsonファイル<br>
userlist.jsonの吸収を検討中(2021/12/23)<br>
#### 記述例<br>
{<br>
    "server name":/*Discordサーバ名*※無くても構わない,<br>
    "server id":/*DiscordサーバID*,<br>
    "channel name":/*ルーム(チャンネル)名*※無くても構わない,<br>
    "channel id":/*ルーム(チャンネル)ID*<br>
}<br>
### .log
botの稼働状況を出力するテキストファイル/ログファイル<br>
### .token
Discord-bot用のトークンを保存しておくテキストファイル<br> 

## 今後の開発予定
優先順に上から<br>
> RaspberryPiでの動作が正常になるように改良<br>
> server.jsonへのuserlist.jsonの吸収<br>
> 各サーバごとに通知する配信者を切り替える<br>
> ソフト立ち上げの際、server.jsonに書かれていないサーバでも稼働するように調整したい。<br>
> discord側から、通知する配信者を追加できるようにしたい。<br>
> コマンドを増やしたい。<br>
> 機能の追加<br>
> データベースの導入?<br>