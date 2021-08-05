from flask import Flask,render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/newstudent')
def new_student():
    return render_template('student.html')

@app.route('/searchstudent')
def searchstudent():
    return render_template('searchstudent.html')

@app.route('/findstudent',methods=['POST','GET']) 
def findstudent():
    # rows=[]
    if request.method == 'POST':

        name = request.form['nm']
        name = name.lower()

        con = mysql.connector.connect(host="localhost",user="jagmohan",password="mySQLjagmohan@5252",database="jaggudb") 
    
        cur = con.cursor()

        cur.execute("SELECT * FROM students")
    
        rows = (cur.fetchall())
   
        return render_template('findstudent.html',rows=rows,name=name)

    return ("No Records Related To Search")

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        
        try:
            
            nm = request.form['nm']
            roll = request.form['roll']
            br = request.form['br']
            eml = request.form['eml']
            sem = request.form['sem']
            
            with mysql.connector.connect(host="localhost",user="jagmohan",password="mySQLjagmohan@5252",database="jaggudb") as con:

                cur = con.cursor()
                
                
                sql = "INSERT INTO students (Name, Rollno, Branch, Email, Semester) VALUES(%s,%s,%s,%s,%s)"
                val = (nm,roll,br,eml,sem)
                cur.execute(sql,val)

                con.commit()
                # msg = "Details Added Successfully"

        except:
            con.rollback()
            # msg = "Error In Insert Operation"
            con.close()

        finally:
            return render_template('result.html',msg=nm)


@app.route('/list')
def list():
    
    con = mysql.connector.connect(host="localhost",user="jagmohan",password="mySQLjagmohan@5252",database="jaggudb") 
    # con.row_factory = mysql.Row 
    
    cur = con.cursor()

    cur.execute("SELECT * FROM students")
    
    rows = cur.fetchall()
   
    return render_template('list.html',rows=rows)



















@app.route('/api')
def student():
    con = mysql.connector.connect(host="localhost",user="jagmohan",password="mySQLjagmohan@5252",database="jaggudb") 
    
    cur = con.cursor()

    cur.execute("SELECT * FROM students")
    
    rows = cur.fetchall()
    result = []
    for i in rows:
        d = dict()
        
        d['Name'] = i[0]
        d['Rollno'] = i[1]
        d['Branch'] = i[2]
        d['Email'] = i[3]
        d['Semester'] = i[4]

        result.append(d)
            


    return jsonify(result)














if __name__ == '__main__':
    app.run(debug=True)

