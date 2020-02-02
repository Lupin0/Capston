import sqlite3
 
conn = sqlite3.connect('abc.db') # 라이브러리와 연결
cur = conn.cursor() # cursor는 핸들러와 같은 역할
# cursor를 통 SQL 명령을 보내고 cursor를 통해 답을 받는다
 
cur.execute('DROP TABLE IF EXISTS Counts') # 이미 테이블이 존재하면 제거
 
cur.execute('''CREATE TABLE Counts (name TEXT)''')
 
fname = 'output.txt'
fh = open(fname)
for line in fh:
    pieces = line.split()
    name = pieces
    #cur.execute('SELECT count FROM Counts WHERE name = ? ', (name))
    # ?는 자리를 표시, sql 주입 방지, (email,) 형태는 튜플 안에 내용이 하나밖에 없다는 표시
    # cur.excute 는 직접 데이터를 빼오지 않 SQL을 훓어보고 문법 문제가 있는지 확인
    # 즉 데이터를 읽지는 않고 커서를 준비
    row = cur.fetchone() # 첫번째 레코드를 읽어 들인다

    cur.execute('''INSERT INTO Counts (name) VALUES (?)''', (name))
     
    conn.commit() # 메모리에 정보를 저장했다가 정보를 디스크로 옮긴다
    # commit은 속도가 느리기 때문에 하나하나 할때마다 하는 것은 비효율적
cur.close()