from tkinter import*
import sqlite3
root=Tk()
root.title("My Project")
root.geometry("500x500")
root.config(bg='light pink')
 
#database
conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db")
c=conn.cursor()

 
def submit(): 
    conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db")
    c=conn.cursor()

    c.execute("INSERT INTO myinfo VALUES(:fname,:lname,:age,:address,:email)",
              {
               'fname':fname.get(),
                 'lname':lname.get(),
                 'age':age.get(),
                'address':address.get(),
                 'email':email.get(),
             })
     
    conn.commit()
    conn.close() 
    fname.delete(0,END)
    lname.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)
 
def query():
    conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db" )
    c=conn.cursor()
    c.execute("SELECT *,oid FROM myinfo")
    records=c.fetchall()

    print_records=''
    for record in records:
        print_records +=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+"\t"+str(record[5])+"/n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=30,column=0,columnspan=2)

    conn.commit
    conn.close()

def delete():
    conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db")
    c=conn.cursor()
    c.execute("DELETE from myinfo WHERE oid=?", (str(delete_box.get()),))

    conn.commit()
    conn.close()

def update():

    conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db")
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute(""" UPDATE myinfo SET
        fname=:first,
        lname=:last,
        age=:age,
        address=:address,
        email=:email

        WHERE oid=:oid""",
            {
                'first':fname_editor.get(),
                'last':lname_editor.get(),
                'age':age_editor.get(),
                'address':address_editor.get(),
                'email':email_editor.get(),
                'oid':record_id
        

                })

    conn.commit()
    conn.close()



def edit():
    editor=Tk()
    editor.title('Update Record from database')
    editor.geometry("500x500")

    conn=sqlite3.connect("D:/MAAM SOL/nelizapersonalinfo.db")
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT * FROM myinfo WHERE oid=?",(str(record_id),))
    records=c.fetchall()

    global fname_editor
    global lname_editor
    global age_editor
    global address_editor
    global email_editor
    
    fname_editor=Entry(editor,width=30)
    fname_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    lname_editor=Entry(editor,width=30)
    lname_editor.grid(row=1,column=2,padx=20)
    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=2,padx=20)
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=3,column=2,padx=20)
    email_editor=Entry(editor,width=30)
    email_editor.grid(row=4,column=2,padx=20)

    fname_label=Label(editor,text="First Name")
    fname_label.grid(row=0,column=0)
    lname_label=Label(editor,text="Last Name")
    lname_label.grid(row=1,column=0)
    age_label_label=Label(editor,text= "Age")
    age_label_label.grid(row=2,column=0)
    address_label_label=Label(editor,text= "Address")
    address_label_label.grid(row=3,column=0)
    email_label_label=Label(editor,text= "Email")
    email_label_label.grid(row=4,column=0)


    for record in records:
       fname_editor.insert(0, record[0])
       lname_editor.insert(0, record[1])
       age_editor.insert(0, record[2])
       address_editor.insert(0, record[3])
       email_editor.insert(0, record[4])
       
       

    save_btn=Button(editor,text="Save Record", command=update)
    save_btn.grid(row=10, column=0, columnspan=2,pady=10,padx=10,ipadx=140)


    conn.commit()
    conn.close()

    
'''
c.execute("""CREATE TABLE "myinfo" (
          "fname"      TEXT,
          "lname"      TEXT,
          "age" INTEGER,
          "address"     TEXT,
          "email" TEXT,
)""")
'''

#clear the text boxes

fname=Entry(root,width=30,bg="white", fg="black")
fname.grid(row=0,column=1,padx=20)

lname=Entry(root,width=30,bg="white", fg="black")
lname.grid(row=1,column=1,padx=20)

age=Entry(root,width=30,bg="white", fg="black")
age.grid(row=2,column=1,padx=20)

address=Entry(root,width=30,bg="white", fg="black")
address.grid(row=3,column=1,padx=20)

email=Entry(root,width=30,bg="white", fg="black")
email.grid(row=4,column=1,padx=20)


#create textbox label
fname_label=Label(root,text="First Name")
fname_label.grid(row=0,column=0)
lname_label=Label(root,text="Last Name")
lname_label.grid(row=1,column=0)
age_label_label=Label(root,text= "Age")
age_label_label.grid(row=2,column=0)
address_label_label=Label(root,text= "Address")
address_label_label.grid(row=3,column=0)
email_label_label=Label(root,text= "Email")
email_label_label.grid(row=4,column=0)


#create submit button

submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1)

delete_box_label=Label(root,text= "Select ID.No")
delete_box_label.grid(row=10,column=0)

query_btn=Button(root,text="Delete Records",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

edit_btn=Button(root,text= "Edit Record", command=edit)
edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

                                                                                                                          
