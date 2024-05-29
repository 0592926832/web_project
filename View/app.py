print("Content-Type:text/html")
print()
import mysql.connector
import cgi
 
form =cgi.FieldStorage()
#app = Flask(__name__)
   username=form.getvalue("username")
    email_address=form.getvalue("email_address")
    id=form.getvalue("id")
    password=form.getvalue("password")

    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student'
    )
    cur=con.cursor
   
    cur.execute("insert into register values(%s, %s, %s, %s)",(username, email_address, id, password))
    con.commit()
    cur.close()
    con.close()
    #return render_web project('C:\Users\TTC\web project\html\regester.html', register=register)

#if __name__ == '__main__':
   # app.run(debug=True)

#@app.route('/add_user', methods=['POST'])
#def register():
 

   # name = request.form['username']
   # email = request.form['email_address']
   #  id = request.form['id']
   # password = request.form['password']

   # conn = get_db_connection()
   # cursor = conn.cursor()
   # cursor.execute("INSERT INTO register (username, email_address, id, password) VALUES (%s, %s, %s,%s)", (name, email, id, password))
   # conn.commit()
   # cursor.close()
   # conn.close()
    
print("done")