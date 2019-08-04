# 统一
def readexcel():
    import xlrd
    import random
    import time
    path = input('请将Excel文件放在D盘根目录下，并以xlsx为后缀名，'
                 '\n'
                 '文件内表名默认不要改变\n'
                 '第一列为学号，第二列为姓名，\n'
                 '同时第一行需要有学号，姓名的标头\n'
                 '>>>>>>>>>>>>>>>>>>\n'
                 '请输入文件名(不带后缀名)：\n')
    path = 'D:/' + path + '.xlsx'
    column = int(input('请输入需要的列数'))
    workbook = xlrd.open_workbook(path)
    sheetlist = workbook.sheet_names()
    sheetname = sheetlist[0]
    sheet1 = workbook.sheet_by_index(0)
    sheet1 = workbook.sheet_by_name(sheetname)
    stu_list = []
    count = 0
    for i in range(1, sheet1.nrows):
        stu_list.append(sheet1.cell(i,1).value)
        count = count + 1
    random.shuffle(stu_list)
    row = len(stu_list) // column + 1
    arr_tuple = tuple(stu_list)
    for i in range(0, row):
        for j in range(0, column):
            if j + i * column >= count: break
            print(arr_tuple[j + i * column], end='\t')
        print()
    print("\n\n\n")
while True:
    readexcel()
