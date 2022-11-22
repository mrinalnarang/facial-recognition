from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        
        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=45)


        img_top=Image.open(r"E:\project\images\main background.jpg")
        img_top=img_top.resize((1530,798),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530 ,height=798)
        
        #frame1
        main_frame=Frame(f_lbl,bd=2,bg="white",)
        main_frame.place(x=50,y=50,width=700,height=290)

        img_top1=Image.open(r"E:\project\images\mrinal.jpeg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl2=Label(main_frame,image=self.photoimg_top1)
        f_lbl2.place(x=470,y=50,width=200,height=200)

        #developer1 info
        dev_label=Label(main_frame,text="Mrinal",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=80)
        dev_label=Label(main_frame,text="MCA Sec-B",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=140)
        dev_label=Label(main_frame,text="03650404421",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=200)   

        #frame2
        main_frame2=Frame(f_lbl,bd=2,bg="white",)
        main_frame2.place(x=800,y=50,width=680,height=290)

        img_top2=Image.open(r"E:\project\images\akansha.jpeg")
        img_top2=img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl3=Label(main_frame2,image=self.photoimg_top2)
        f_lbl3.place(x=450,y=50,width=200,height=200)

        #developer2 info
        dev_label=Label(main_frame2,text="Akansha",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=80)
        dev_label=Label(main_frame2,text="MCA Sec-A",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=140)
        dev_label=Label(main_frame2,text="00614004421",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=200)
        #frame3
        main_frame3=Frame(f_lbl,bd=2,bg="white",)
        main_frame3.place(x=50,y=400,width=700,height=290)

        img_top3=Image.open(r"E:\project\images\namit.jpeg")
        img_top3=img_top3.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl4=Label(main_frame3,image=self.photoimg_top3)
        f_lbl4.place(x=470,y=50,width=200,height=200)

        #developer3 info
        dev_label=Label(main_frame3,text="Namit",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=80)
        dev_label=Label(main_frame3,text="MCA Sec-A",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=140)
        dev_label=Label(main_frame3,text="02414004421",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=200)

        #frame4
        main_frame4=Frame(f_lbl,bd=2,bg="white",)
        main_frame4.place(x=800,y=400,width=680,height=290)

        img_top4=Image.open(r"E:\project\images\ishaan.jpeg")
        img_top4=img_top4.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)

        f_lbl5=Label(main_frame4,image=self.photoimg_top4)
        f_lbl5.place(x=450,y=50,width=200,height=200)

        #developer4 info
        dev_label=Label(main_frame4,text="Ishaan",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=80)
        dev_label=Label(main_frame4,text="MCA Sec-A",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=140)
        dev_label=Label(main_frame4,text="02914004421",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=200)
        

if __name__ ==  "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()