import mysql.connector
import pandas as pd
import json
import re
shop_file = pd.read_csv(r'path') # path to 3-p5s3708k.csv
peach = shop_file.values.tolist()
df = pd.read_excel(r'path') #path to 5-awte8wbd.xlsx
category_title_fa = df[df.columns[5]]
ctg = category_title_fa.values.tolist()
attributes = df[df.columns[9]]
attr = attributes.values.tolist()
title_alt = df['title_alt'][:].values.tolist()
prid = df[df.columns[0]].values.tolist()
prtifa = df[df.columns[1]].values.tolist()
prtien = df[df.columns[2]].values.tolist()
url = df[df.columns[3]].values.tolist()
ctgkey = df[df.columns[6]].values.tolist()
brnamefa = df[df.columns[7]].values.tolist()
brnameen = df[df.columns[8]].values.tolist()
bookind = []
puzzleind = []
mouseind = []
keyboardind = []
glassind = []
phonecaseind = []
count1 = 0
for word in prtien:
    if word != word:
        prtien[count1] = "NULL"
    count1 += 1
count2 = 0
for word in url:
    if word != word:
        url[count2] = "NULL"
    count2 += 1
count3 = 0
for word in ctgkey:
    if word != word:
        ctgkey[count3] = "NULL"
    count3 += 1

# indexes of each product:

for i in range(0, len(ctg)):
    if ctg[i] == "کتاب چاپی":
        bookind.append(i)
for i in range(0, len(ctg)):
    if category_title_fa[i] == "پازل":
        puzzleind.append(i)

for i in range(0, len(ctg)):
    if ctg[i] == "ماوس (موشواره)":
        mouseind.append(i)

for i in range(0, len(ctg)):
    if ctg[i] == "کیبورد (صفحه کلید)":
        keyboardind.append(i)

for i in range(0, len(ctg)):
    if ctg[i] == "کیف و کاور گوشی":
        phonecaseind.append(i)

for i in range(0, len(ctg)):
    if ctg[i] == "محافظ صفحه نمایش گوشی":
        glassind.append(i)

books_attr_list = []
book_attributes = []
attr_dict = {}
# book_attributes:

for i in range(0, len(bookind)):
    if attr[bookind[i]] == attr[bookind[i]]:
        books_attr_list.append(json.loads(attr[bookind[i]]))  # list of lists of dictionaries

for i in range(0, len(books_attr_list)):  # for every row in excel
    for j in range(0, len(books_attr_list[i])):  # for each dictionary of a row
        attr_dict[books_attr_list[i][j].get("Key")] = books_attr_list[i][j].get("Value")
    book_attributes.append(attr_dict.copy())
    attr_dict.clear()

# puzzle attributes:

puzzle_attr_list = []
puzzle_attributes = []
for i in range(0, len(puzzleind)):
    if attr[puzzleind[i]] == attr[puzzleind[i]]:
        puzzle_attr_list.append(json.loads(attr[puzzleind[i]]))

for i in range(0, len(puzzle_attr_list)):  # for every row in excel
    for j in range(0, len(puzzle_attr_list[i])):  # for each dictionary of a row
        attr_dict[puzzle_attr_list[i][j].get("Key")] = puzzle_attr_list[i][j].get("Value")
    puzzle_attributes.append(attr_dict.copy())
    attr_dict.clear()

#  mouse attributes:

mouse_attr_list = []
mouse_attributes = []
for i in range(0, len(mouseind)):
    if attr[mouseind[i]] == attr[mouseind[i]]:
        mouse_attr_list.append(json.loads(attr[mouseind[i]]))

for i in range(0, len(mouse_attr_list)):  # for every row in excel
    for j in range(0, len(mouse_attr_list[i])):  # for each dictionary of a row
        attr_dict[mouse_attr_list[i][j].get("Key")] = mouse_attr_list[i][j].get("Value")
    mouse_attributes.append(attr_dict.copy())
    attr_dict.clear()

# keyboard attributes:

keyboard_attr_list = []
keyboard_attributes = []

for i in range(0, len(keyboardind)):
    if attr[keyboardind[i]] == attr[keyboardind[i]]:
        keyboard_attr_list.append(json.loads(attr[keyboardind[i]]))

for i in range(0, len(keyboard_attr_list)):  # for every row in excel

    for j in range(0, len(keyboard_attr_list[i])):  # for each dictionary of a row
        attr_dict[keyboard_attr_list[i][j].get("Key")] = keyboard_attr_list[i][j].get("Value")
    keyboard_attributes.append(attr_dict.copy())
    attr_dict.clear()

# glass attributes:

glass_attr_list = []
glass_attributes = []

for i in range(0, len(glassind)):
    if attr[glassind[i]] == attr[glassind[i]]:
        glass_attr_list.append(json.loads(attr[glassind[i]]))

for i in range(0, len(glass_attr_list)):  # for every row in excel

    for j in range(0, len(glass_attr_list[i])):  # for each dictionary of a row
        attr_dict[glass_attr_list[i][j].get("Key")] = glass_attr_list[i][j].get("Value")
    glass_attributes.append(attr_dict.copy())
    attr_dict.clear()

# case attributes:

phonecase_attr_list = []
phonecase_attributes = []

for i in range(0, len(phonecaseind)):
    if attr[phonecaseind[i]] == attr[phonecaseind[i]]:
        phonecase_attr_list.append(json.loads(attr[phonecaseind[i]]))

for i in range(0, len(phonecase_attr_list)):  # for every row in excel

    for j in range(0, len(phonecase_attr_list[i])):  # for each dictionary of a row
        attr_dict[phonecase_attr_list[i][j].get("Key")] = phonecase_attr_list[i][j].get("Value")
    phonecase_attributes.append(attr_dict.copy())
    attr_dict.clear()

# keys for columns of each attribute table

book_keys = book_attributes[0].keys()
puzzle_keys = puzzle_attributes[0].keys()
mouse_keys = mouse_attributes[0].keys()
keyboard_keys = keyboard_attributes[0].keys()
phonecase_keys = phonecase_attributes[1].keys()
glass_keys = glass_attributes[0].keys()

# title_alt parsing

title_alt_lists = []
for i in range(len(title_alt)):
    s = str(title_alt[i])
    title_alt_lists.append(set(re.split(',|،|-|/', s.lower())))
book_title_alt = []
puzzle_title_alt = []
mouse_title_alt = []
keyboard_title_alt = []
phonecase_title_alt = []
glass_title_alt = []
for i in range(len(bookind)):
    book_title_alt.append(list(title_alt_lists[bookind[i]]))
for i in range(len(puzzleind)):
    puzzle_title_alt.append(list(title_alt_lists[puzzleind[i]]))
for i in range(len(mouseind)):
    mouse_title_alt.append(list(title_alt_lists[mouseind[i]]))
for i in range(len(keyboardind)):
    keyboard_title_alt.append(list(title_alt_lists[keyboardind[i]]))
for i in range(len(phonecaseind)):
    phonecase_title_alt.append(list(title_alt_lists[phonecaseind[i]]))
for i in range(len(glassind)):
    glass_title_alt.append(list(title_alt_lists[glassind[i]]))

# -------------------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YOUR_PASSWORD", #fill
    database="DATABASE_NAME" #fill
)
mycursor = mydb.cursor()
mycursor.execute("USE DATABASE_NAME") #fill

# creating table attribute , title , others
mycursor.execute("CREATE TABLE IF NOT EXISTS big_table (product_id INT NOT NULL,product_title_fa VARCHAR(255),category_title_fa VARCHAR(255),brand_name_fa VARCHAR(255),PRIMARY KEY (product_id))")
mycursor.execute("CREATE TABLE IF NOT EXISTS category(category_title_fa VARCHAR(255),category_keywords varchar(255),primary key(category_title_fa))")
mycursor.execute("CREATE TABLE IF NOT EXISTS url(product_title_fa VARCHAR(255),product_title_en VARCHAR(255),url VARCHAR(255),PRIMARY KEY(product_title_fa)  )")
mycursor.execute("CREATE TABLE IF NOT EXISTS brand(brand_name_fa VARCHAR(255),brand_name_en VARCHAR(255),primary key(brand_name_fa))")
table_name_attributes = ["book_attributes", "puzzle_attributes", "mouse_attributes", "keyboard_attributes",
                         "phonecase_attributes", "glass_attributes"]
table_column = [book_keys, puzzle_keys, mouse_keys, keyboard_keys, phonecase_keys, glass_keys]
for table_names, table_column in zip(table_name_attributes, table_column):
    sql = 'CREATE TABLE IF NOT EXISTS {} (product_id INT NOT NULL,' + '`{}` TEXT, ' * len(
        table_column) + 'PRIMARY KEY (product_id),FOREIGN KEY (product_id) REFERENCES big_table(product_id))'
    sql = sql.format(table_names, *table_column)
    mycursor.execute(sql)

    sql = """CREATE TABLE IF NOT EXISTS title (product_id INT,title_alt VARCHAR(255),
    primary key (product_id,title_alt))"""
    sql = sql.format()
    mycursor.execute(sql)
mydb.commit()
# ------------------------------------------------------------------------------------------------------------
# inserting data into title table:
title_names = [book_title_alt, puzzle_title_alt, mouse_title_alt, keyboard_title_alt, phonecase_title_alt,glass_title_alt]
ind_list = [bookind, puzzleind, mouseind, keyboardind, phonecaseind, glassind]
for guz,guz_ind in zip(title_names,ind_list):
    for i in range(0, len(guz)):
        for j in range(0, len(guz[i])):
            sql = """INSERT INTO title(product_id,title_alt) VALUES (%s,%s)"""
            val = (prid[guz_ind[i]], guz[i][j])
            try:
                mycursor.execute(sql, val)
            except:
                continue
mydb.commit()

# --------------------------------------------------
# insert into big table
for index in ind_list:
    for m in range(0, len(index)):
        sql = "INSERT INTO big_table(product_id, product_title_fa, category_title_fa, brand_name_fa) VALUES (%s,%s,%s,%s)"
        val = (prid[index[m]], prtifa[index[m]], ctg[index[m]], brnamefa[index[m]])
        mycursor.execute(sql, val)
mydb.commit()
# insert into category table
for index in ind_list:
    for m in range(0, len(index)):
        sql = "insert into category(category_title_fa, category_keywords)  VALUES (%s,%s)"
        val = (ctg[index[m]], brnamefa[index[m]])
        try:
            mycursor.execute(sql, val)
        except:
            continue
mydb.commit()
# insert into url table
for index in ind_list:
    for m in range(0, len(index)):
        sql = "insert into url(product_title_fa, product_title_en, url) VALUES (%s,%s,%s)"
        val = (prtifa[index[m]], prtien[index[m]],url[index[m]])
        try:
            mycursor.execute(sql, val)
        except:
            continue
mydb.commit()
# insert into brand table
for index in ind_list:
    for m in range(0, len(index)):
        sql = "insert into brand(brand_name_fa,brand_name_en) VALUES (%s,%s)"
        val = (brnamefa[index[m]], brnameen[index[m]])
        try:
            mycursor.execute(sql, val)
        except:
            continue
mydb.commit()
# -----------------------------------------------------------------------------------------------
# insert into attribute tables
# insert to book attributes

golabi_attribute = [book_attributes, puzzle_attributes, mouse_attributes, keyboard_attributes, phonecase_attributes,
                    glass_attributes]
for tab_name, ind, att_name in zip(table_name_attributes, ind_list, golabi_attribute):
    i = 0
    for row in att_name:
        cols = ''
        vals = ''
        for key in row:
            cols += " `{}` , "
            cols = cols.format(key)
            vals += " '{}' , "
            vals = vals.format(row.get(key))
        cols = cols[:-2]
        vals = vals[:-2]
        sql = """INSERT INTO {}(product_id, {} ) VALUES ({},{})"""
        pid = prid[ind[i]]
        sql = sql.format(tab_name, cols, pid, vals)
        try:
            mycursor.execute(sql)
        except:
            print("Digikala ride")
        i += 1
    if len(ind) > len(att_name):
        j = len(att_name)
        nullstring = "NULL, " * len(att_name[1].keys())
        nullstring = nullstring[0:-2]
        while j < len(ind):
            sql = """INSERT INTO {}(product_id, {} ) VALUES ({},{})""".format(tab_name, cols, prid[ind[j]], nullstring)
            try:
                mycursor.execute(sql)
            except:
                print("Digikala ride")
            j += 1
mydb.commit()
# -----------------------------------------------------------------------------------------------
# Indexing

sql = """CREATE TABLE IF NOT EXISTS orders(
id INT NOT NULL auto_increment,
ID_Order INT NOT NULL,
ID_Customer INT,
ID_Item INT,
DateTime_CartFinalize VARCHAR(255),
Amount_Gross_Order INT,
City_name_fa VARCHAR(255),
Quantity_Item INT,
PRIMARY KEY(id))"""
mycursor.execute(sql)
sqlind = """CREATE INDEX dt ON orders(DateTime_CartFinalize)"""
# mycursor.execute(sqlind)
sqlins = """INSERT INTO orders(ID_Order,ID_Customer,ID_Item,DateTime_CartFinalize,Amount_Gross_Order,City_name_fa,Quantity_Item)
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
for i in peach:
    try:
        mycursor.execute(sqlins, i)
    except:
        continue

mydb.commit()
mycursor.close()
mydb.close()
