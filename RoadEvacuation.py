#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from Tkinter import *
import tkMessageBox

def displayResult():


    result.insert(END, "請里辦公處協助轉知里民有關林口區" + site.get('1.0','end-1c') + "於"
        + startYear.cget("text") + "年" + startMonth.get('1.0','end-1c') + "月" + startDay.get('1.0','end-1c') + "日至"
        + endYear.cget("text") + "年" + endMonth.get('1.0','end-1c') + "月" + endDay.get('1.0','end-1c') + "日"
        + "上午9時至下午16時止將進行管路挖掘工程。" + "\n\n"
        "有關" + optionMenuWidget.cget("text") + "於本區" + site.get('1.0','end-1c')
        + "道路挖掘案，核可施工日期為"
        + startYear.cget("text") + "年" + startMonth.get('1.0','end-1c') + "月" + startDay.get('1.0','end-1c') + "日至"
        + endYear.cget("text") + "年" + endMonth.get('1.0','end-1c') + "月" + endDay.get('1.0','end-1c') + "日"
        + "上午9時至下午16時止，惠請里辦公處協助宣導施工期間請用路人行經該路段時能提高注意、小心行駛。")

def clear():

    site.delete('1.0', END)
    result.delete('1.0', END)
    startMonth.delete('1.0', END)
    startDay.delete('1.0', END)
    endMonth.delete('1.0', END)
    endDay.delete('1.0', END)
    constructUnitVariable.set("單位")
    startYearVariable.set("年份")
    endYearVariable.set("年份")


if __name__ == "__main__":

    root = Tk()

    root.title("道路挖掘工程里長通知")
    root["padx"] = 40
    root["pady"] = 20


    # site
    Label(root, text="地址").grid(row=0, column=0)
    site = Text(root, height=1, width=10)
    site.grid(row=0, column=1,columnspan=6,sticky=W+E+N+S)
    site.insert(END, "")

    # construct unit
    constructUnit = [
    "欣泰石油氣股份有限公司",
    "台灣電力股份有限公司台北西區營業處",
    "台灣自來水公司第二區管理處林口服務所",
    "新北市政府水利局汙水下水道工程科",
    "中華電信股份有限公司臺灣北區電信分公司新北營運處第三客戶網路中心",
    "內政部營建署",
    "新北市政府交通局"
    ]

    constructUnitVariable = StringVar(root)
    constructUnitVariable.set("單位")
    optionMenuWidget = apply(OptionMenu, (root, constructUnitVariable) + tuple(constructUnit))
    optionMenuWidget.grid(row=1,column=1,columnspan=6)

    # Start year option
    Label(root, text="開始時間").grid(row=2,column=0)

    OPTIONS = [
    "105",
    "106",
    ]

    startYearVariable = StringVar(root)
    startYearVariable.set("年份") # default value

    startYear = apply(OptionMenu, (root, startYearVariable) + tuple(OPTIONS))
    startYear.grid(row=2,column=1)
    Label(root, text="年").grid(row=2, column=2)

    # Start month
    startMonth = Text(root, height=1, width=10)
    startMonth.grid(row=2,column=3,)
    startMonth.insert(END, "")
    Label(root, text="月").grid(row=2, column=4)

    # Start day
    startDay = Text(root, height=1, width=10)
    startDay.grid(row=2,column=5)
    startDay.insert(END, "")
    Label(root, text="日").grid(row=2, column=6)


    # End year option
    Label(root, text="結束時間").grid(row=3,column=0)
    endYearVariable = StringVar(root)
    endYearVariable.set("年份") # default value

    endYear = apply(OptionMenu, (root, endYearVariable) + tuple(OPTIONS))
    endYear.grid(row=3,column=1)
    Label(root, text="年").grid(row=3, column=2)

    # End month
    endMonth = Text(root, height=1, width=10)
    endMonth.grid(row=3,column=3)
    endMonth.insert(END, "")
    Label(root, text="月").grid(row=3, column=4)


    # End day
    endDay = Text(root, height=1, width=10)
    endDay.grid(row=3,column=5)
    endDay.insert(END, "")
    Label(root, text="日").grid(row=3, column=6)

    button = Button(root, text="輸出結果", command=displayResult)
    button.grid(row=4,column=3)

    button2 = Button(root, text="清除", command=clear)
    button2.grid(row=4,column=4)

    result = Text(root)
    result.grid(row=5,column=1,rowspan=6,columnspan=6,sticky=W+E+N+S)


    root.mainloop()
