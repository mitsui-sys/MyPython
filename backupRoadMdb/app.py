# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import configparser
# ファイルの存在チェック用モジュール
import os
import errno
import glob

#現在のディレクトリ
cdir = os.getcwd()

# 登録画面のGUI
def create_gui():
    # ----------------------------------------
    # コールバック関数群
    # ----------------------------------------    
    # 表示ボタンが押下されたときのコールバック関数
    def select_button():
        root.destroy()
        select_gui()
    # ----------------------------------------
    # 終了ボタンが押下されたときのコールバック関数
    def quit_button():
        root.destroy()
    # ----------------------------------------
    #設定ファイルを読み込む関数
    def readini():
        # configparserの宣言とiniファイルの読み込み
        config_ini = configparser.ConfigParser()
        config_ini_path = cdir+'\config.ini'

        # 指定したiniファイルが存在しない場合、エラー発生
        if not os.path.exists(config_ini_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)
        # config_ini.read(config_ini_path, encoding='utf-8')
        config_ini.read(config_ini_path, encoding='shift_jis')
        print("config.ini read")
        return config_ini

    # ----------------------------------------
    # 内訳テーブル(item)にあるitem_nameのタプルを作成する
    def createitemname():
        #設定ファイル 
        conf_ini = readini()
        print(conf_ini)
        # 空の「リスト型」を定義
        li = []
        dataNum = 0
        while len(li) < 10:
            var = conf_ini['CITY']['Name'+str(dataNum)]
            print(var)
            if len(var) > 0:
                # item_nameをリストに追加する
                li.append(var)
            dataNum = dataNum + 1
        # リスト型のliをタプル型に変換して、ファンクションに戻す
        return tuple(li)

    def createMdbName(cityname):
        path = cdir+"\\backup\\"+cityname+"\\*.lzh"
        print(path)
        return listup_files(path)

    #ファイルリスト取得
    def listup_files(path):
        flist = [os.path.abspath(p) for p in glob.glob(path)]
        return tuple(flist)

    #市町村コンボボックス選択時の処理
    def cb_selected(event):
        if len(combo.get()) == 0:
            return
        print(combo.get())
        listbox.delete(0,listbox.size())

        citylist = createMdbName(combo.get())
        print(citylist)
        for lzh in citylist:
            listbox.insert(tk.END,lzh)

    # ----------------------------------------
    # rootフレームの設定
    root = tk.Tk()
    root.title("道路台帳")
    root.geometry("550x400")

    # メニューの設定
    lframe = tk.LabelFrame(root,bd=2,relief="ridge",text="処理区分")
    # メニューの大きさ設定
    lframe.pack(padx=5,pady=5,fill="x")
    # チェック有無変数
    var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    var.set(0)
    # ラジオボタン作成
    rdo1 = tk.Radiobutton(lframe, value=0, variable=var, text='バックアップ')
    rdo1.pack(side="left")
    rdo2 = tk.Radiobutton(lframe, value=1, variable=var, text='リカバリー')
    rdo2.pack(side="left")

    # メニューの設定
    frameM = tk.Frame(root,bd=2,relief="ridge")
    frameM.pack(padx=5,pady=5,fill="x")
    # ラベルの設定
    label1 = tk.Label(frameM,text="市町村名",font=("",14),height=2)
    label1.pack(side="left")
    # 内訳コンボボックスの作成
    combo = ttk.Combobox(frameM, state='readonly',font=("",14),width=10)
    combo["values"] = createitemname()
    combo.current(0)
    combo.bind('<<ComboboxSelected>>', cb_selected) #項目が選択されたときの処理
    combo.pack(side="left")
    # テキストボックス
    txt1 = tk.Entry(frameM,bd=2,width=13)
    txt1.pack(side="left")
    txt2 = tk.Entry(frameM,bd=2,width=13)
    txt2.pack(side="left")

    # 圧縮ファイル一覧表示
    lframeA = tk.LabelFrame(root,bd=2,relief="ridge",text="圧縮ファイル一覧")
    lframeA.pack(padx=5,pady=5,fill="x")
    #スクロールバーの作成
    scroll=tk.Scrollbar(lframeA)
    #スクロールバーの配置を決める
    scroll.pack(side=tk.RIGHT,fill="y")
    #データ
    list_value=tk.StringVar()
    citylist = createMdbName(combo.get())
    list_value.set(citylist)
    #リストボックスの作成
    listbox=tk.Listbox(lframeA,height=8,listvariable=list_value,selectmode="single",yscrollcommand=scroll.set)
    listbox.pack(padx=5,pady=5,fill="x")
    #部品の動きをスクロールバーに反映させる
    scroll["command"]=listbox.yview

    # メニューの設定
    frameButton = tk.Frame(root,bd=2,relief="ridge",bg="DarkRed")
    frameButton.pack(padx=5,pady=5,fill="x")
    button1 = tk.Button(frameButton,text="退避",bd=2,width=10)
    button1.pack(padx=5,pady=5,side="left")
    button2 = tk.Button(frameButton,text="復元",bd=2,width=10)
    button2.pack(padx=5,pady=5,side="left")
    button3 = tk.Button(frameButton,text="終了",command=quit_button,bd=2,width=10)
    button3.pack(padx=5,pady=5,side="right")

    # メニューの設定
    frameLog = tk.Frame(root,bd=2,relief="ridge")
    frameLog.pack(padx=5,pady=5,fill="x")
    log = tk.Label(frameLog,bd=2,relief="ridge",font=("",14),text="処理を選択してください。")
    log.pack(side="left")

    
    root.mainloop()

# 表示画面のGUI
def select_gui():
    # ----------------------------------------
    # コールバック関数群
    # ----------------------------------------    
    # 登録ボタンが押下されたときのコールバック関数
    def create_button():
        root.destroy()
        create_gui()
    # ----------------------------------------
    # 終了ボタンが押下されたときのコールバック関数
    def quit_button():
        root.destroy()

    # rootフレームの設定
    root = tk.Tk()
    root.title("選択")
    root.geometry("400x500")

    # メニューの設定
    frame = tk.Frame(root,bd=2,relief="ridge")
    frame.pack(fill="x",side="bottom")
    button1 = tk.Button(frame,text="入力",command=create_button)
    button1.pack(side="left")
    button2 = tk.Button(frame,text="表示")
    button2.pack(side="left")
    button3 = tk.Button(frame,text="終了",command=quit_button)
    button3.pack(side="right")

    # メインループ
    root.mainloop()


# GUI画面の表示
create_gui()