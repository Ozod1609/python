import sqlite3


conn = sqlite3.connect('roster.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', data)

# 3. Update Jadzia Dax to Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# 4. Display Name and Age of all Bajorans
cursor.execute('''
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
''')

results = cursor.fetchall()
print("Bajoran Members:")
for name, age in results:
    print(f"{name}, Age: {age}")


conn.commit()
conn.close()
 How to Run:
Save this code as roster_script.py.


yaml
Копировать
Редактировать
Bajoran Members:
Kira Nerys, Age: 29
