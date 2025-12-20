import tkinter as tk
#////////////////////////////////////////////
def dong():
    try:
        a = float(e1.get())
        b = int(e2.get())

        if b == 0:
            l.config(text="خطا: تعداد صفر است")
            return

        c = a / b
        l.config(text=f"سهم هر نفر: {c:.0f} تومان")

    except ValueError:
        l.config(text="خطا: عدد وارد کنید")
#///////////////////////////////////////////////////
root = tk.Tk()
root.title("Dong Calc")
#/////////////////////////////////////////////////
tk.Label(root, text="مبلغ کل:").pack()
e1 = tk.Entry(root)
e1.pack()
#/////////////////////////////////////////////////
tk.Label(root, text="تعداد نفرات:").pack()
e2 = tk.Entry(root)
e2.pack()
#/////////////////////////////////////////////////////
tk.Button(root, text="محاسبه سهم", command=dong).pack()
#/////////////////////////////////////////////////////////
l = tk.Label(root, text="")
l.pack()
#////////////////////////////////////////////////////////
root.mainloop()
#////////////////////////////////////////////////////////