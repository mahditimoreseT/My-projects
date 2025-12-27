import tkinter as tk

def calculate_share():
    try:
        total_amount = float(entry_total_amount.get())
        num_people = int(entry_num_people.get())

        if num_people == 0:
            label_result.config(text="خطا: تعداد نفرات صفر است")
            return

        share = total_amount / num_people
        label_result.config(text=f"سهم هر نفر: {share:.0f} تومان")

    except ValueError:
        label_result.config(text="خطا: عدد وارد کنید")


root = tk.Tk()
root.title("محاسبه سهم")

tk.Label(root, text="مبلغ کل:").pack()
entry_total_amount = tk.Entry(root)
entry_total_amount.pack()


tk.Label(root, text="تعداد نفرات:").pack()
entry_num_people = tk.Entry(root)
entry_num_people.pack()

tk.Button(root, text="محاسبه سهم", command=calculate_share).pack()


label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
