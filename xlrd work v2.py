import xlrd
import xlwt

file_location = """Momentum Cohort Analysis May 1-7.xlsx"""

workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_name('Sheet1')

top = sheet.col_values(2,1)

top100 = []
for t in set(top):
	t = str(t) + " "
	top100.append(t)

cr_filename = input("Insert name of cr file here. Remember to add .xlsx : ")

cr_sheet = input("Insert name of cr sheet here: ")

wb = xlrd.open_workbook(cr_filename)
sheetcr = wb.sheet_by_name(cr_sheet)
colcr = sheetcr.col_values(0,1)

matches = set(colcr) & set(top100)
print(matches)


print(len(matches))

new_workbook = xlwt.Workbook()

sheet_name = input("Insert name of sheet here: ")

new_sheet = new_workbook.add_sheet(sheet_name)

new_sheet.write(0,0,"Device ID")
new_sheet.write(1,2,"Count: " + str(len(matches)))

for e, match in enumerate(matches):
		new_sheet.write(e+1,0,str(match))

name = input("Input name of file. Remember to add .xls : ")
new_workbook.save(name)