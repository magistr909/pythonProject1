import sqlite3

"""Старый код"""
#Копирование данных
#def parse_file():
#    global wholedata
#    wholedata = []
#    with open('123.txt', mode='r', encoding='utf-8') as file:
#        lines = file.readlines()
#        for line in lines:
#            line = line.strip()
#            data = [word.strip() for word in line.split('|')]
#            wholedata.append(data)
#    print(wholedata)
#
#parse_file()
#conn = sqlite3.connect('Chalna.db')
#print("Opened database successfully")
#
#
#
#k=0
#for index in wholedata:
#    hanzi = index[0]
#    transcription = index[1]
#    translation = index[2]
#    conn.execute("INSERT INTO MAIN (Number, Type, Hanzi, Transcription, Translation) VALUES (?, ?, ?, ?, ?)", (k, 'main', hanzi, transcription, translation))
#    k+=1
#
#conn.commit()
#print("Records created successfully")
#conn.close()


"""___________________________________________________________Новый код___________________________________________________________________"""

def chalna_select_main():
    conn = sqlite3.connect('Chalna.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    database_list = conn.execute("SELECT NUMBER, HANZI, TRANSCRIPTION, TRANSLATION FROM MAIN WHERE TYPE=='main'").fetchall()
    conn.commit()
    print("Чтение данных по TYPE=='main' выполнено")
    conn.close()
    return database_list
print(chalna_select_main())