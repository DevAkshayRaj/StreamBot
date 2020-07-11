import mysql.connector
from mysql.connector import Error
def getSongByName(name):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             #cursor.execute("INSERT INTO songs(song_id,song_name,song_genre,song_artist,song_album,song_composer,played_count,song_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (5,'Uyirini-Uyire','melody','saindhavi','thandavam','gvprakashkumar',0,r'D:\Projects\Songs\Uyirini-Uyire.mp3'))  
             cursor.execute("select song_link from songs where song_name = %s", (name,))
             updateCountName(name)
             #cursor.execute("select song_link from songs where song_name = %s", (name,))
             record = cursor.fetchall()
             #print(record[0][0])
             connection.commit()
             cursor.close()
             connection.close()
             return record[0][0]
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'
def getSongByArtistName(name):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             #cursor.execute("INSERT INTO songs(song_id,song_name,song_genre,song_artist,song_album,song_composer,played_count,song_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (5,'Uyirini-Uyire','melody','saindhavi','thandavam','gvprakashkumar',0,r'D:\Projects\Songs\Uyirini-Uyire.mp3'))  
             cursor.execute("select song_link from songs where song_artist = %s", (name,))
             record = cursor.fetchall()
             updateCountArtist(name)
             #print(record[0][0])
             connection.commit()
             cursor.close()
             connection.close()
             return record[0][0]
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'
def getSongByComposerName(name):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             #cursor.execute("INSERT INTO songs(song_id,song_name,song_genre,song_artist,song_album,song_composer,played_count,song_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (5,'Uyirini-Uyire','melody','saindhavi','thandavam','gvprakashkumar',0,r'D:\Projects\Songs\Uyirini-Uyire.mp3'))  
             cursor.execute("select song_link from songs where song_composer = %s", (name,))
             record = cursor.fetchall()
             updateCountComposer(name)
             #print(record[0][0])
             connection.commit()
             cursor.close()
             connection.close()
             return record[0][0]
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'
def getSongByGenreName(name):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             #cursor.execute("INSERT INTO songs(song_id,song_name,song_genre,song_artist,song_album,song_composer,played_count,song_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (5,'Uyirini-Uyire','melody','saindhavi','thandavam','gvprakashkumar',0,r'D:\Projects\Songs\Uyirini-Uyire.mp3'))  
             cursor.execute("select song_link from songs where song_genre = %s", (name,))
             record = cursor.fetchall()
             #print(record[0][0])
             updateCountGenre(name)
             connection.commit()
             
             cursor.close()
             connection.close()
             return record[0][0]
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'
def getSongByAlbumName(name):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             #cursor.execute("INSERT INTO songs(song_id,song_name,song_genre,song_artist,song_album,song_composer,played_count,song_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (5,'Uyirini-Uyire','melody','saindhavi','thandavam','gvprakashkumar',0,r'D:\Projects\Songs\Uyirini-Uyire.mp3'))  
             cursor.execute("select song_link from songs where song_album = %s", (name,))
             #cursor.execute("update songs set played_count=0 where song_id=1")
             record = cursor.fetchall()
             #print(record[0][0])
             updateCountAlbum(name)
             connection.commit()
             cursor.close()
             connection.close()
             return record[0][0]
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'
def updateCountName(x):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=played_count+1 where song_name=%s",(x,))
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def updateCountAlbum(x):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=played_count+1 where song_album=%s",(x,))
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def updateCountArtist(x):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=played_count+1 where song_artist=%s",(x,))
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def updateCountComposer(x):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=played_count+1 where song_composer=%s",(x,))
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def updateCountGenre(x):
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=played_count+1 where song_genre=%s",(x,))
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def getTopList():
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("select song_name from songs order by played_count Desc;")
             record = cursor.fetchall()
             message=''
             for row in record:
                 message=message+'<br>'+row[0]+'<br>'
                 #print(row[0])
             connection.commit()
             cursor.close()
             connection.close()
             return message
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none'    
def removeCount():
    try:
        connection = mysql.connector.connect(host='localhost',database='coda_project',user='root',password='rohitsharma45')
        if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("update songs set played_count=0 ")
             connection.commit()
             cursor.close()
             connection.close()
             return 'done'
    except (Error,IndexError) as e:
        print("Error while connecting to MySQL", e)
        return 'none' 

