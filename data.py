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

def chalna_select_mistakes():
    conn = sqlite3.connect('Chalna.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    database_list = conn.execute(
        "SELECT NUMBER, HANZI, TRANSCRIPTION, TRANSLATION FROM MAIN WHERE TYPE=='mistake'").fetchall()
    conn.commit()
    print("Чтение данных по TYPE=='main' выполнено")
    conn.close()
    return database_list

def minus_karma(listus):
    conn = sqlite3.connect('Chalna.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    f = conn.execute("SELECT count(*) FROM main WHERE TYPE == 'mistake' and HANZI == '%s' and TRANSCRIPTION == '%s' and TRANSLATION == '%s'" % (listus[0], listus[1], listus[2])).fetchall()
    print(f[0][0])
    if f[0][0] == 0:
        conn.execute("INSERT INTO MAIN (TYPE, HANZI, TRANSCRIPTION, TRANSLATION, MISSFLAG) VALUES (?, ?, ?, ?, ?)", ('mistake', listus[0], listus[1], listus[2], 3))
        print("Запись в TYPE==MISSFLAG выполена")
        print("Слово добавлено в mistake")
    conn.commit()
    conn.close()

def plus_karma(listus):
    conn = sqlite3.connect('Chalna.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    conn.execute("UPDATE main SET MissFlag = MissFlag -1 WHERE TYPE == 'mistake' and MissFlag <> 0 and HANZI == '%s' and TRANSCRIPTION == '%s' and TRANSLATION == '%s'" % (listus[0], listus[1], listus[2]))
    conn.commit()
    print("Запись в TYPE==MISSFLAG выполена")
    print("Значение ошибки уменьшено")
    conn.close()
    karma_refresh()

def karma_refresh():
    conn = sqlite3.connect('Chalna.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    conn.execute(
        "DELETE FROM main WHERE TYPE == 'mistake' and MissFlag == 0" )
    conn.commit()
    print("Удаление старых записей выполенено")
    conn.close()


def search_in_database(seachdata):
    conn = sqlite3.connect('test.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    database_list = conn.execute(
        "SELECT TYPE, HANZI, TRANSCRIPTION, TRANSLATION FROM MAIN WHERE HANZI == '%s' OR TRANSCRIPTION== '%s' OR TRANSLATION== '%s'" % (seachdata, seachdata, seachdata)).fetchall()
    conn.commit()
    print("Чтение данных выполнено")
    conn.close()
    return database_list

def add_to_db(hanzi, transcription, translation):
    conn = sqlite3.connect('test.db')
    print('Подключено к БД')
    print('Проверка на доступность...')
    conn.execute(
        "INSERT INTO MAIN (TYPE, HANZI, TRANSCRIPTION, TRANSLATION) VALUES (?, ?, ?, ?)", ('check', hanzi, transcription, translation))
    conn.commit()
    print("Добавление данных завершено")
    conn.close()

if __name__ == '__main__':
   #search_in_database(['偶尔', 'ou er', 'какое-то гавно'])
   add_to_db('ou er', 'ougeer', 'ouger')
   print(search_in_database('ou er'))
