
import xlwt
'''往EXCEl单元格写内容，每次写一行sheet:页签名称；row：行内容列表；rowIndex：行索引;
　　isBold:true:粗字段，false:普通字体'''
def WriterSheetRow( sheet, rowValueList, rowIndex):
    i = 0
    for sValue in rowValueList:
        strValue = sValue
        sheet.write(rowIndex, i, strValue)
        i = i+1

'''content 为二维list'''
def saveExcel(fileName, sheetName, content):

    wbk = xlwt.Workbook()

    sheet = wbk.add_sheet(sheetName, cell_overwrite_ok=True)

    content = list(content)
    for row in range(content.__len__()):
        row_values = content[row]
        WriterSheetRow(sheet, row_values, row)

    wbk.save(fileName )


