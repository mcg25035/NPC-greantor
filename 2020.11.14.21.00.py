from tkinter import *
import tkinter.messagebox
def show_code():
    tkinter.messagebox.showinfo(title='請以下列方式填寫對話碼', message='NPC say ㄟ幹 穿山甲ㄟ\nNPC say ㄟ蟑螂 這可以養嗎?\nPlayer say 我不知道你抓回家\nNPC say 借過借過不要跑\nNPC say 歐乎 他跑掉了 好屌歐')
def show_code2():
    tkinter.messagebox.showinfo(title='請以下列方式填寫條件碼',message='need clicknpc,物品ID(英文)x數量,物品ID(英文)x數量\n可以選擇逗號隔開其中的幾種使用\n物品ID(英文)x數量 此任務式可重複使用\n例如:只點擊npc即可完成前置任務 : need clicknpc\n例如:點擊npc並繳交24個石頭 : need clicknpc,stonex24\n例如:點擊npc並繳交4個石頭和2個骨頭 : need clicknpc,stonex4,bonex2')
def show_code3():
    tkinter.messagebox.showinfo(title='頭顱指令填寫方式',message='例如使用這個頭顱 : https://minecraft-heads.com/custom-heads/humans/4772-donald-trump\n---\n/give @p minecraft:player_head{display:{Name:"{\"text\":\"Donald Trump\"}"},SkullOwner:{Id:[I;1066066484,631524838,-1395072433,-1446377403],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2E5ZTIwOGU4MzEyNjVlODU5MTkyNzFiNTk1NzZkZWZkYjNhYzhmOTM5YmIyMDQ0MzE5ZjVhYzYxMGYyMWUxIn19fQ=="}]}}} 1')
def show_code4():
    tkinter.messagebox.showinfo(title='輸入範例',message='未染色的皮革裝 輸入欄空白\n黑色的皮革裝 輸入欄#1D1D21\n鐵胸甲 輸入欄iron_chestplate')
a = Tk()
a.geometry("950x720")
b = Label(text="NPC名稱(英文字母)")
b.grid(row=1,column=1)
c = Entry()
c.grid(row=1,column=2)
d = Label(text="對話內容產生碼")
d.grid(row=2,column=1)
e = Text()
e.grid(row=2,column=2)
f = Button(text="點我查看\n產生碼格式",command=show_code)
f.grid(row=2,column=3)
g = Label(text="任務名稱(英文字母)")
g.grid(row=3,column=1)
g1 = Entry()
g1.grid(row=3,column=2)
h = Label(text="任務名稱(中文，顯示於玩家端)")
h.grid(row=4,column=1)
i = Entry()
i.grid(row=4,column=2)
j = Label(text="任務目標(中文敘述，顯示於玩家端)")
j.grid(row=5,column=1)
k = Entry()
k.grid(row=5,column=2)
l = Label(text="前置任務(英文字母)\n(無請輸入No)")
l.grid(row=6,column=1)
m = Entry()
m.grid(row=6,column=2)
n = Label(text="前置任務解鎖條件碼\n(無前置任務輸入No)")
n.grid(row=7,column=1)
o = Entry()
o.grid(row=7,column=2)
p = Button(text="點我查看\n條件碼格式",command=show_code2)
p.grid(row=7,column=3)
q = Label(text="頭顱指令\n從minecraft-heads.com取得")
q.grid(row=8,column=1)
r = Entry()
r.grid(row=8,column=2)
s = Button(text="點我查看範例",command=show_code3)
s.grid(row=8,column=3)
t = Label(text="胸甲\n空白或只輸入顏色就是皮革\n輸入其他ID代表其他胸甲")
t.grid(row=9,column=1)
u = Entry()
u.grid(row=9,column=2)
v = Button(text="點我查看範例",command=show_code4)
v.grid(row=9,column=3)
w = Label(text="護腿\n空白或只輸入顏色就是皮革\n輸入其他ID代表其他護腿")
w.grid(row=10,column=1)
x = Entry()
x.grid(row=10,column=2)
y = Label(text="靴子\n空白或只輸入顏色就是皮革\n輸入其他ID代表其他靴子")
y.grid(row=11,column=1)
z = Entry()
z.grid(row=11,column=2)
b1 = Button(text="產生mcfunction")
b1.grid(row=12,column=2)
c1 = Button(text="直接匯入伺服器(需有網路)")
c1.grid(row=12,column=3)
a.mainloop()
