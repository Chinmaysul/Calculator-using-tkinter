#--------------------------------------------ALL IN ONE CALCULATOR--------------------------------------------

#                                Working description:

#1)	This program is designed to calculate and plot functions.
#2)	This Program consists of the following options:
#a)	To compute values of some mathematical functions and perform mathematical operations on numbers  using “Numeric Calculator”.
#b)	To plot mathematical functions of single variable 'x' and analyse their graphs using “Graphical Calculator”.
#c)	To find derivatives and slope at a point and indefinite as well as definite integrals of mathematical functions using “Calculus”.
#d)	To assign common constants and store them in an easy-to-access table and use them in performing tedious calculations. 


#--------------------------------------------IMPORTED MODULES----------------------------------------------   
from tkinter import *               #Design user-friendly interface
import mysql.connector              #database connectivity for storing pre-defined constants
import math                         #to use constants like pi,e and functions like sin(),cos() etc
import numpy as np                  #for defining domain of variable 'x', and other mathematical functions
import sympy as sym                 #For calculus functions- differentiation, integration
from tkinter import messagebox      #Displaying error in constant terms
from matplotlib import pyplot as plt#For Plotting graphs of single variable functions

#------------------------------------------------------------------------------------------------------------
global x #Plotting variable 'x', ex: 2*x+5 is plotted in graph
global e
global k #Calculus variable 'k' (not displayed in interface, used for compatibility with Sympy Module)
x=np.linspace(-6,6,10000) 
k=sym.Symbol('k')
db=mysql.connector.connect(host='localhost',user='root',passwd='Samarpan1!',database='project')
cur=db.cursor()

global tb       #textbox for entering expression
#global tt
global l        #holds all expressions displayed on graph
global p        #flag in calculus for checking empty entered expression
global calcexpression   #Sympy formatted expression
global expression       #Numpy formatted expression
global outexpression    #User readable calculus expression
global expressionT      #user-readable numeric expression
global outexpressionT   #String displayed as output in calculus calculator
global equation         #String displayed as output in numeric calculator
global integral         #stores inetgral expression
global outarea          #displays area

#--------------------------------------------------COMMON BUTTONS-------------------------------------------------------------------------------------------------
# Buttons:[1,2....9,  +,-,*,/,//,^,   trignometric and inverse trignometric,  log,e,  [](itf),{}(fpf),(,)]
# Have been defined here and used globally in all calculators

def buttons(windowK):
    button1 = Button(windowK, text=' 1 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('1'), height=3, width=10)
    button1.grid(row=2, column=0) 
  
    button2 = Button(windowK, text=' 2 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('2'), height=3, width=10) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(windowK, text=' 3 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('3'), height=3, width=10) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(windowK, text=' 4 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('4'), height=3, width=10) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(windowK, text=' 5 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('5'), height=3, width=10) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(windowK, text=' 6 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('6'), height=3, width=10) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(windowK, text=' 7 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('7'), height=3, width=10) 
    button7.grid(row=4, column=0) 
      
    button8 = Button(windowK, text=' 8 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('8'), height=3, width=10) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(windowK, text=' 9 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('9'), height=3, width=10) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(windowK, text=' 0 ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press('0'), height=3, width=10) 
    button0.grid(row=5, column=1) 
  
    plus = Button(windowK, text=' + ', fg='black', bg='thistle2',activebackground='red',command=lambda: press("+"), height=3, width=10) 
    plus.grid(row=2, column=3) 
  
    minus = Button(windowK, text=' - ', fg='black', bg='thistle2',activebackground='red',command=lambda: press("-"), height=3, width=10) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(windowK, text=' * ', fg='black', bg='thistle2',activebackground='red',command=lambda: press("*"), height=3, width=10) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(windowK, text=' / ', fg='black', bg='thistle2',activebackground='red',command=lambda: press("/"), height=3, width=10) 
    divide.grid(row=5, column=3) 
  
    rem = Button(windowK, text=' Mod ', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS("%","Mod"), height=3, width=10) 
    rem.grid(row=6, column=1) 

    intdiv = Button(windowK, text=' // ', fg='black', bg='thistle2',activebackground='red',command=lambda: press("//"), height=3, width=10) 
    intdiv.grid(row=6, column=2)

    power=Button(windowK, text='^', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS('**','^'), height=3, width=10) 
    power.grid(row=6, column=3)

    Decimal= Button(windowK, text='.', fg='black', bg='thistle2',activebackground='red',command=lambda: press('.'), height=3, width=10) 
    Decimal.grid(row=6, column=0) 
        
    sin = Button(windowK, text=' sin ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("sin"), height=3, width=10) 
    sin.grid(row=2, column=4) 
  
    cos = Button(windowK, text=' cos ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("cos"), height=3, width=10) 
    cos.grid(row=3, column=4) 
  
    tan = Button(windowK, text=' tan ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("tan"), height=3, width=10) 
    tan.grid(row=4, column=4) 
  
    sec = Button(windowK, text=' sec ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("sec"), height=3, width=10) 
    sec.grid(row=6, column=4)

    cot = Button(windowK, text=' cot ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("cot"), height=3, width=10) 
    cot.grid(row=7, column=4) 

    cosec = Button(windowK, text=' cosec ', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math("cosec"), height=3, width=10) 
    cosec.grid(row=5, column=4) 

    pi = Button(windowK, text=' π ', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS("3.1415926535",'π'), height=3, width=10) 
    pi.grid(row=7, column=2)

    coti= Button(windowK, text='cot-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arccot'), height=3, width=10) 
    coti.grid(row=7, column=5)

    tani= Button(windowK, text='tan-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arctan'), height=3, width=10) 
    tani.grid(row=4, column=5)

    sini= Button(windowK, text='sin-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arcsin'), height=3, width=10) 
    sini.grid(row=2, column=5)

    cosi= Button(windowK, text='cos-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arccos'), height=3, width=10) 
    cosi.grid(row=3, column=5)

    seci= Button(windowK, text='sec-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arcsec'), height=3, width=10) 
    seci.grid(row=6, column=5)

    coseci= Button(windowK, text='cosec-1', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('arccosec'), height=3, width=10) 
    coseci.grid(row=5, column=5)

    ln= Button(windowK, text='ln', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('log'), height=3, width=10) 
    ln.grid(row=8, column=4)

    log= Button(windowK, text='log<10>', fg='black', bg='lavenderblush',activebackground='red',command=lambda: press_math('log10'), height=3, width=10) 
    log.grid(row=8, column=5)

    gif= Button(windowK, text='[]', fg='black', bg='thistle2',activebackground='red',command=lambda: press_math('floor'), height=3, width=10) 
    gif.grid(row=7, column=0)

    fpf= Button(windowK, text='{}', fg='black', bg='thistle2',activebackground='red',command=lambda: press_fpf(), height=3, width=10) 
    fpf.grid(row=7, column=1)

    e= Button(windowK, text='e', fg='black', bg='lavenderblush2',activebackground='red',command=lambda: pressS('2.718281828459045','e'), height=3, width=10) 
    e.grid(row=7, column=3)

    b1 = Button(windowK, text=' ( ', fg='black', bg='darkseagreen1',activebackground='red',command=lambda: press("("), height=3, width=10) 
    b1.grid(row=5, column=0)

    b2 = Button(windowK, text=' ) ', fg='black', bg='darkseagreen1',activebackground='red',command=lambda: press(")"), height=3, width=10) 
    b2.grid(row=5, column=2)


# ---------------------------------------------------------------------NUMERIC CALCULATOR-----------------------------------------------------------------------------
#Used for basic arithmetic,exponential,trignometric and logarithmic computations
'''def mainN():
    global expression
    global window
    window=Toplevel(windowM)
    expression=''
    global expressionT
    expressionT=''
    global calcexpression
    calcexpression=''
    global equation
    global tt
    window.configure(bg="light steel blue3")
    window.geometry("500x500")
    window.title("Calculator")
    equation=StringVar()
    tb = Entry(window, textvariable=equation)
    tb.grid(row=0,columnspan=6,ipadx=180,ipady=10)
    tb.bind("<Key>", "pass")
    tt = Entry(window)
    tt.grid(row=9,column=1,columnspan=2,ipadx=20,ipady=10)

    cst= Label(window, text='Enter constant',bg='light blue')
    cst.grid(row=9,column=0)

    per = Button(window, text=' % of ', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS("/100*","% of "), height=3, width=10) 
    per.grid(row=8, column=3)

    cnst= Button(window, text='Enter Constant', fg='black', bg='PaleTurquoise1',activebackground='red',command=lambda: press_cnst(), height=2, width=10) 
    cnst.grid(row=9, column=3)

    equal = Button(window, text=' = ', fg='black', bg='darkseagreen1',activebackground='red',command=equalto,height=3, width=10) 
    equal.grid(row=8, column=1)

    cl = Button(window, text='Clear', fg='black', bg='darkseagreen1',activebackground='red',command=cleartext1, height=3, width=10) 
    cl.grid(row=8, column=0)

    inv = Button(window, text='1/x', fg='black', bg='darkseagreen1',activebackground='red',command=lambda: inverse(), height=3, width=10) 
    inv.grid(row=8, column=2) 

    buttons(window)
    window.mainloop()

def inverse():
    global equation
    global expression
    global expressionT
    expression='1/('+expression+')'
    expressionT='1/('+expressionT+')'
    equation.set(expressionT)
def cleartext1():
    global equation
    global expression
    global expressionT
    expression = ""
    expressionT = ""
    equation.set("") 

def equalto():
    try:
        global expression
        global expressionT
        global tb
        total = str(eval(expression)) 
        equation.set(total)
        expression=str(total)
        expressionT=expression
    except:
        equation.set('infinity')
        expression=""

def press_cnst():
    global tt
    k=tt.get()
    global expression
    global expressionT
    global equation
    cur.execute("SELECT val FROM trial WHERE name=%s",[k])
    c=cur.fetchall()
    cnst=c[0][0]
    cnst_val=cnst.replace('e','np.e')


    expression=expression+ str(cnst_val)
    expressionT=expressionT+ str(cnst)
    equation.set(expressionT)

def press_cnst():
    global expression
    global expressionT
    global equation
    k=n.get()
    cur.execute("SELECT val FROM trial WHERE name like %s",[k])
    cnst_val=cur.fetchall()[0][0]
    expression=expression+ str(cnst_val)
    expressionT=expressionT+ str(cnst_val)
    equation.set(expressionT)'''
# Main window for Numeric calculator:
def mainN():
    global expression
    global cnst
    global window
    window=Toplevel(windowM)
    expression=''
    global expressionT
    expressionT=''
    global calcexpression
    calcexpression=''
    global equation
    global tt
    global n
    window.configure(bg="light steel blue3")
    window.geometry("500x500")
    window.title("Calculator")
    equation=StringVar()
    n=StringVar()
    tb = Entry(window, textvariable=equation,font="calibri 20")
    tb.grid(row=0,columnspan=6,ipadx=105,ipady=10)
    tb.bind("<Key>", "pass")
    
# Some extra buttons specific to Numeric calculator
    cst= Label(window, text='Enter constant',bg='light blue')
    cst.grid(row=9,column=0)

    per = Button(window, text=' % ', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS("/100*","%"), height=3, width=10) 
    per.grid(row=8, column=3)

    fact= Button(window, text='!', fg='black', bg='thistle2',activebackground='red',command=lambda: press_fact(), height=3, width=10) 
    fact.grid(row=8, column=2)

    cnst= Button(window, text='Enter Constant', fg='black', bg='PaleTurquoise1',activebackground='red',command=press_cnst, height=2, width=10) 
    cnst.grid(row=9, column=2)

    equal = Button(window, text=' = ', fg='black', bg='darkseagreen1',activebackground='red',command=equalto,height=3, width=10) 
    equal.grid(row=8, column=1)

    cl = Button(window, text='Clear', fg='black', bg='darkseagreen1',activebackground='red',command=cleartext1, height=3, width=10) 
    cl.grid(row=8, column=0) 

#Displaying drop-down of constants
    buttons(window)
    cur.execute("SELECT name FROM trial")
    a=cur.fetchall()
    b=list()
    for i in range(0,len(a)):
        b.append(a[i][0])
    n.set("     ")
    cnst= OptionMenu(window,n,*b)
    cnst.grid(column=1, row=9) 

    window.mainloop()


#Defining functions of above buttons [Clear,=,Enter constant,!]    
def cleartext1():
    global equation
    global expression
    global expressionT
    expression = ""
    expressionT = ""
    equation.set("") 

def equalto():
    try:
        global expression
        global expressionT
        global tb
        total = str(eval(expression)) 
        equation.set(total)
        expression=str(total)
        expressionT=expression
        
    except:
        equation.set('infinity')
        expression=""

def press_cnst():
    global expression
    global expressionT
    global equation
    k=n.get()
    cur.execute("SELECT val FROM trial WHERE name like %s",[k])
    cnst_val=cur.fetchall()[0][0]
    expression=expression+ str(cnst_val)
    expressionT=expressionT+ str(cnst_val)
    equation.set(expressionT)

def press_fact():
    global equation
    global expression
    global expressionT
    expressionT=expressionT+'fact('
    expression=expression+'math.factorial('
    equation.set(expressionT)




#-----------------------------------------------------------------------CONSTANT TERMS---------------------------------------------------------------------------------
# This is interface:  
#       > Allows user to access list of pre-defined constants( which are stored in MSQL DATABASE).
#       > Define new constants (which are not saved after main window is closed).
#       > Defined constants can be accesed in Numeric, Graphical calculators by 'Drop Down Box'

global name
global val

#Main window for contsants
def main1():
    global windowC
    windowC=Toplevel(windowM)
    global name
    global val
    global deff
    windowC.configure(bg="lavenderblush2")
    windowC.geometry("400x350")
    windowC.title("Constants")

    Name=''
    Val=''
    Def=''

#Buttons for Constants
    name = Entry(windowC)
    name.grid(row=1,column=2,columnspan=6,ipadx=50,ipady=10)

    label1= Label(windowC, text='Name of Constant:',bg='lavenderblush1')
    label1.grid(row=1,column=1)
    label1.config(font=('ariel', 14))

    val = Entry(windowC)
    val.grid(row=2,column=2,columnspan=6,ipadx=50,ipady=10)

    label2= Label(windowC, text='Value of Constant:',bg='lavenderblush1')
    label2.grid(row=2,column=1)
    label2.config(font=('ariel', 14))

    
    deff = Entry(windowC)
    deff.grid(row=3,column=2,columnspan=6,ipadx=50,ipady=10)

    label3= Label(windowC, text='Use of Constant:',bg='lavenderblush1')
    label3.grid(row=3,column=1)
    label3.config(font=('ariel', 14))

    button()
    windowC.mainloop()


#Accepts entered [Name,Value,Use] for user defined constant
#Verifies if name is redundant displays error message box (assigns default name: c)
#Checks datatype of value, if invalid displays error message box and sets default value 8.31144
def enter():
    global name
    global nm
    global val
    global deff
    Name= name.get()
    Val= val.get()
    Def= deff.get()
    cur.execute('SELECT NAME FROM TRIAL')
    S=cur.fetchall()
    for i in S:
        if (Name in i or Name== ''):
            Name='c'
            messagebox.showerror('error','Name already exists or name not defined')
        try:
            eval(Val)
        except:
            Val='8.3144'
            messagebox.showerror('error','Value Entered should be numeric')
            
    arr=(Name,Val,Def)
    cur.execute('INSERT IGNORE INTO trial VALUES(%s,%s,%s)',arr)
    
#Displays all pre and user defined constants
def show():
    root=Tk()
    root.configure(bg="light steelblue3")
    root.geometry("1250x500")
    root.title("Constant Table")
    cur.execute('SELECT * FROM trial')
    x=cur.fetchall()
    for i in range(len(x)):
        for j in range(3): 
            ent= Entry(root, width=35, bg="lavenderblush2",fg='black',font=('Ink Free',16,'bold'))                   
            ent.grid(row=i, column=j) 
            ent.insert(END, x[i][j]) 

#Buttons: 'Set' and 'Show Constants' for defining and looking at constant terms
def button():
    setit=Button(windowC, text='Set', fg='black', bg='light steelblue3',activebackground='black',command= enter, height=5, width=20) 
    setit.place(x=120, y=150)

    showit=Button(windowC, text='Show all Constants', fg='black', bg='light steelblue3',activebackground='black',command= show, height=5, width=20) 
    showit.place(x=120, y=250)

##-------------------------------------------------------------GRAPHICAL CALCULATOR------------------------------------------------------------------------------------
#This interface is designed to :
#    > Define and Plot (single variable) functions
#    > Plot Tangent: by specifying 'x-coordinate' from where tangent is drawn to current curve
#    > Plots multiple curves at a time, allowing user to analyze them
#    > Provides MAX{},MIN{} functions

# Main Window of Graphical Calculator 
def mainG():
    global windowG
    windowG=Toplevel(windowM)
    windowG.configure(bg="light blue")
    windowG.geometry("2000x750")
    windowG.title("Graphical Calculator")

    print('How To Plot:')

    z=Label(windowG,text=' Here to help',bg='lavenderblush2', fg='black')
    z.config(font =("Ink Free", 20,'bold'))
    z.place(x=800, y=75)

    a=Label(windowG,text=' PLOT :plots your entered expression( entered at top left of window',bg='light steel blue3')
    a.config(font =("Ink Free", 14,'bold'))
    a.place(x=600, y=150)

    b=Label(windowG,text=' ADD TANGENT: adds tangent at *entered x coordinate* ',bg='light steel blue3')
    b.config(font =("Ink Free", 14,'bold'))
    b.place(x=600, y=180)
    
    c=Label(windowG,text=' CLEAR : clears out current expression',bg='light steel blue3')
    c.config(font =("Ink Free", 14,'bold'))
    c.place(x=600, y=210)

    o=Label(windowG,text=' CLEAR GRAPHS : clears out all graphs and added functions',bg='light steel blue3')
    o.config(font =("Ink Free", 14,'bold'))
    o.place(x=600, y=240)


    global calcexpression
    calcexpression=''
    global expression
    expression=''
    global outexpression
    outexpression=''
    global expressionT
    expressionT=''
    global outexpressionT
    outexpressionT=''
    global equation
    global integral
    integral=''
    global outarea
    outarea=StringVar()
    global equation
    equation=StringVar()
    global l
    l=[]
    global p
    p=0

    tb = Entry(windowG, textvariable=equation,font="calibri 20")
    tb.grid(row=0,columnspan=6,ipadx=105,ipady=10)

    global output
    output=StringVar()
    integral=StringVar()
    buttons(windowG)
    buttonsG()

    global textentry
    textentry=Entry(windowG, width=10,bg='white')
    textentry.grid(row=9,column=0,sticky=W)   #tangent

    global value
    value=textentry.get()

    global points
    #points=textarea.get()
    windowG.mainloop()

# Handles transformations bw user entered function(expressionT), python formatted function (expression)
# And sympy formated (calcexpression)
def press_math(function):
    global expression
    global expressionT
    global calcexpression
    global w

    expressionT=expressionT+function+'('

    dic1={'cosec':'1/np.sin(','cot':'1/np.tan(','sec':'1/np.cos('}
    dic2={'arccosec':'np.arcsin(1/','arcsec':'np.arccos(1/','arccot':'np.arctan(1/','arcsin':'np.arcsin(','arccos':'np.arccos(','arctan':'np.arctan(}'}

    if str(function) in dic1:
        expression=expression+dic1.get(function)
        if function!='cosec':
            calcexpression=expression.replace('np','sym')
        else:
            calcexpression=calcexpression+'sym.csc('

    elif str(function) in dic2:
        expression=expression+dic2.get(function)
        f=function[3::]
        if function!='arccosec':
            calcexpression=calcexpression+'sym.'+'a'+f+'('
        else:
            calcexpression=calcexpression+'sym.acsc('
            
    else:
        calcexpression=calcexpression+'sym.'+function+'('
        expression=expression+'np.'+function+'('    
    equation.set(expressionT)
    calcexpression.replace('cosec','csc')


#Converts 'x' into 'k' for calcexpression
def pressT(x,k):
    global equation
    global expression 
    global expressionT
    global calcexpression

    calcexpression=calcexpression + k
    expression = expression + x
    expressionT=  expressionT + x
    equation.set(expressionT)
    #print(calcexpression)

def press(num):
    global equation
    global expression 
    global expressionT
    global calcexpression

    calcexpression=calcexpression + num
    expression = expression + num
    expressionT=  expressionT + num
    equation.set(expressionT)

def pressS(num,rep):   
    global equation
    global expression 
    global expressionT
    global calcexpression

    calcexpression=calcexpression + num
    expressionT= expressionT + rep 
    expression = expression + num 
    equation.set(expressionT)

def cleartext():
    global equation
    global expression
    global expressionT
    global calcexpression                  
    global outexpression
    global outexpressionT
    global output
    global addfun
    global outarea
    global slopeval
    global ta

    
    calcexpression=""
    expression = ""
    expressionT = ""
    equation.set("")
    output.set("")
    outexpression=""
    outexpressionT=""
    outarea.set("")
    integral.set("")
    slopeval.set("")
    ta=""


def inverse():
    global expression
    global expressionT
    global equation
    global calcexpression
    
    calcexpression="1/("+ calcexpression+")"
    expression="1/("+ expression+")"
    expressionT="1/("+ expressionT+")"
    equation.set(expressionT)


def fpf(a):
    b=a-np.floor(a)
    return b

def press_fpf():    
    global expression
    global expressionT
    global equation
    global calcexpression
    calcexpression=calcexpression+'fpf('
    expression=expression+'fpf('
    expressionT=expressionT+'fpf('
    equation.set(expressionT)



# Pop-up Window that is displayed in case of Syntax Errors
def syntaxError():
    windowE=Tk()
    windowE.title('Help')
    windowE.configure(bg='light steelblue3')
    windowE.geometry("600x250")
    l=Label(windowE,text=' Syntax error',bg='lavenderblush2', fg='red')
    l.config(font =("Ink Free", 20,'bold'))
    l.place(x=60, y=10)

    a=Label(windowE,text=' Some common errors:',bg='light steel blue3')
    a.config(font =("Ink Free", 12,'bold'))
    a.place(x=50, y=90)

    b=Label(windowE,text='   >> Not all brackets are closed ',bg='light steel blue3')
    b.config(font =("Ink Free", 12,'bold'))
    b.place(x=50, y=130)

    d=Label(windowE,text='   >> Blank expression ',bg='light steel blue3')
    d.config(font =("Ink Free", 12,'bold'))
    d.place(x=50, y=160)
    
    c=Label(windowE,text="   >>Coefficients of terms 'ex:3x' must be mentioned as '3*x'",bg='light steel blue3')
    c.config(font =("Ink Free", 12,'bold'))
    c.place(x=50, y=190)
    
    h=Label(windowE,text=" There is a syntax error in entered expression  ",fg='red')
    h.config(font =("Ink Free", 14,'bold'))
    h.place(x=50, y=60)

#Pop up window that is displayed in case of Type errors
#ex: user enters 2,4 (array) instead of entering single numeric value for 'x-coordinate' for tangent
def typeError():
    windowte=Tk()
    windowte.title('Help')
    windowte.configure(bg='light steelblue3')
    windowte.geometry("600x100")
    l=Label(windowte,text=' Type error',bg='lavenderblush2', fg='red')
    l.config(font =("Ink Free", 20,'bold'))
    l.place(x=60, y=10)

    a=Label(windowte,text=' ex: 2 ; 7.34',bg='light steel blue3')
    a.config(font =("Ink Free", 12,'bold'))
    a.place(x=50, y=90)
    a=Label(windowte,text='not: ex: 2,3  ; (5)',bg='light steel blue3')
    a.config(font =("Ink Free", 12,'bold'))
    a.place(x=50, y=90)
    
    h=Label(windowte,text=" X coordinate should only contain one value  ",fg='red')
    h.config(font =("Ink Free", 14,'bold'))
    h.place(x=50, y=60)

#Takes [value], i.e 'x-coordinate' and Plots Tangent accordingly
def slope(value):
    global calcexpression
    global expressionT
    global x
    global k
    global expression
    global l
    global addfun
    global sp
    global constant

    p=1
    print('v',type(value))
    try:
        eval(expression)
    except SyntaxError:
        syntaxError()   #Pop up window displayed if syntax error
        p=0
    else:
        try:
            c=expression.replace('x',str(value))
            constant=eval(c)
        except:
            typeError()  #Pop up window displayed if type error
            p=0
    if p==1:
        c=expression.replace('x',str(value))
        constant=eval(c)
        derivative=sym.diff(eval(calcexpression))
        d=convert(str(derivative)) 
        m=str(d).replace('x',value)
        sp=eval(m)
        
        g=str(sp)+'*(x-'+str(value)+')+'+str(constant)
        
        n='Tangent( '+str(value)+' , '+expressionT+')'
        l.append([g,n])

#Main Plotting Funtion
#Takes [expressionT] and plots curve using Plotpy module
def pltmany(value):
    global l
    global sp
    global constant
    global addfun
    global f
    global expression
    global expressionT
    global calcexpression
    global x
    global k
    global sp
    global constant

    if bool(value)!=False :
        slope(value)

#Creating list of multiple functions being plotted    
    f='Added:'
    for i in l:
        f=f+':   '+i[1]
    g=[expression,expressionT]
    if 'max' in g[1] or 'min' in g[1]:
        g[0]=g[0][0:-1]+'],axis=0)'
    if g not in l:
        try:
            eval(g[0])
        except SyntaxError:
            syntaxError()
        else:
            l.append(g)
            f=f+':   '+g[1]
            addfun.set(f)

    #from matplotlib import pyplot as plt
    plt.clf()
    plt.style.use('seaborn-deep')

    for i in l:
        print(i)
        try:
            plt.plot(x,eval(i[0]),label=i[1])
        except ValueError:
            plt.plot(x,eval(i[0]+'+0*x'),label=i[1])
            
    plt.title('graphs')
    plt.xlabel('x-axis')
    plt.ylabel('f(x)')
    plt.legend(loc='upper right')
    plt.tight_layout
    plt.grid(True)
    plt.show()


def clearlist():
    global l
    global addfun
    l=[]
    addfun.set("")


        

#MAX{f1,f2,...fn} only plots the maximum 'y' from {f1,f2,...fn}
def maxf():
    global l
    global expressionT
    global x
    global k
    global expression

    expressionT=expressionT+'max('
    expression=expression+'np.max(['
    equation.set(expressionT)

#MIN{f1,f2,...fn} only plots the minimum 'y' from {f1,f2,...fn}
def minf():
    global l
    global expressionT
    global x
    global k
    global expression
    expressionT=expressionT+'min('
    expression=expression+'np.min(['
    equation.set(expressionT)


#Handles conversions bw different format expressions    
def convert(l):
    f1=['sin(','cos(','tan(','log(']        
    f2=['anp.sin(','anp.cos(','anp.tan(','anp.cosec(','anp.sec(','anp.cot(']
    dic1={'csc(':'1/np.sin(','cot(':'1/np.tan(','sec(':'1/np.cos('}
    f5=['a1/np.tan(','a1/np.sin(','a1/np.cos(']
    
    for i in f1:
        l=l.replace(i,'np.'+i)

    for i in f2:
        p='np.arc'+i[4::]
        l=l.replace(i,p)

    for i in dic1:
        l=l.replace(i,dic1.get(i))

    for i in f5:
        p='np.arc'+i[6::]
        l=l.replace(i,p)
        
    l=l.replace('k','x')
    l=l.replace('sqrt','np.sqrt')
    return l

# Used for MAX{},MIN{} functions
def comma():
    global equation
    global expression 
    global expressionT
    global calcexpression

    calcexpression=calcexpression + '0*x'+','+ '0*x'
    expression = expression + '0*x'+','+ '0*x'
    expressionT=  expressionT + '0*x'+ ','+ '0*x'
    equation.set(expressionT)

#some extra buttons for Graphical Calculator
def buttonsG():
    global value
    global points
    global tt

    buttonx = Button(windowG, text=' x ', fg='black', bg='darkseagreen1',activebackground='red',command=lambda: pressT('x','k'),height=3, width=10)
    buttonx.grid(row=8, column=4)

    cl = Button(windowG, text='Clear', fg='black', bg='darkseagreen1',activebackground='red',command=cleartext, height=3, width=10) 
    cl.grid(row=8, column=5) 

    ma= Button(windowG, text='max', fg='black', bg='thistle2',activebackground='red', command=lambda:maxf(), height=3, width=10)
    ma.grid(row=8, column=2)

    mi= Button(windowG, text='min', fg='black', bg='thistle2',activebackground='red', command=lambda:minf(), height=3, width=10)
    mi.grid(row=8, column=3)

    ptmny= Button(windowG, text=' PLOT', fg='black', bg='LightGoldenrod1',activebackground='red', command=lambda:pltmany(textentry.get()), height=3, width=10)
    ptmny.grid(row=10, column=2)

    ptmny= Button(windowG, text='clear graphs', fg='black', bg='darkseagreen1',activebackground='red', command=lambda:clearlist(),height=3, width=10)
    ptmny.grid(row=10, column=3)

    comma= Button(windowG, text=',', fg='black', bg='thistle2',activebackground='red',command=lambda: press(','), height=3, width=10) 
    comma.grid(row=6, column=1)

    ln= Button(windowG, text='ln', fg='black', bg='thistle2',activebackground='red',command=lambda: press_math('log'), height=3, width=10) 
    ln.grid(row=8, column=0)

    rem = Button(windowG, text=' Rem ', fg='black', bg='thistle2',activebackground='red',command=lambda: pressS("%","Rem"), height=3, width=10) 
    rem.grid(row=8, column=1)

    Label (windowG, text='enter x coordinate(for TANGENT)',bg='light blue',fg='black').grid(row=9,column=1,sticky=W,columnspan=4)
  
    tt = Entry(windowG)
    tt.grid(row=12,column=1,columnspan=2,ipadx=20,ipady=10)

    cst= Label(windowG, text='Enter constant',bg='light blue')
    cst.grid(row=11,column=0)

    cnst= Button(windowG, text='Enter Constant', fg='black', bg='PaleTurquoise1',activebackground='red',command=lambda: press_cnst(), height=2, width=10) 
    cnst.grid(row=12, column=5)

    global addfun
    addfun=StringVar()
    Label(windowG, textvariable=addfun,bg='light blue',fg='black').grid(row=1,column=0,sticky=W,columnspan=5)

##----------------------------------------------------------------------CALCULUS CALCULATOR--------------------------------------------------------------------------------------
#This interface is designed to:
#       > Find derivative, integral
#       > Find definite derivative ie slope of tangent at user specified 'x-coordinate'
#       > Find area under curve bw user specified end points

#Main window for Calculus Calculator
def mainS():
    global windowS
    global v
    global calcexpression
    calcexpression=''
    global expression
    expression=''
    global outexpression
    outexpression=''
    global expressionT
    expressionT=''
    global outexpressionT
    outexpressionT=''
    global equation
    equation=StringVar()
    global slopeval
    slopeval=StringVar()
    global tdf 
    global dvalue       #'x-coordinate' for definite derivative
    global outarea      #Displays area bw two points
    outarea=StringVar()
    global textarea
    global output       #Variable string displaying derivative, inetgral
    output=StringVar() 
    global l
    l=[]
    global p
    p=0
    global integral
    integral=StringVar()
    windowS=Toplevel(windowM)
    windowS.configure(bg="light blue")
    windowS.geometry("500x720")
    windowS.title("Calculus")
    v=sym.Symbol('x')

# Text boxes 
    tdf=Entry(windowS, width=10,bg='white')
    tdf.grid(row=14,column=0,sticky=W)

    dvalue=tdf.get()

    tb = Entry(windowS, textvariable=equation,font="calibri 20")
    tb.grid(row=0,columnspan=6,ipadx=105,ipady=10)
    tb.bind("<Key>", "pass")
    to = Entry(windowS, textvariable=output,font="calibri 20")
    to.grid(row=10,columnspan=6,ipadx=105,ipady=10)
    to.bind("<Key>", "pass")
    
    
    ta = Entry(windowS, textvariable=outarea,font="calibri 20")
    ta.grid(row=12,columnspan=6,ipadx=105,ipady=10)
    buttons(windowS)
   
    textarea=Entry(windowS, width=10,bg='white')
    textarea.grid(row=11,column=0,sticky=W)
    ts = Entry(windowS, textvariable=slopeval,font="calibri 20")##
    ts.grid(row=15,columnspan=6,ipadx=105,ipady=10)
    ButtonsS()

#Calculates derivative and conerts differnt formats
def di():
    global p
    global calcexpression
    global outexpression
    global outexpressionT
    global k
    global output 
    
    try:
        a=sym.diff(eval(calcexpression))

        outexpressionT=str(a).replace('**','^')
        outexpressionT=outexpressionT.replace('k','x')
        outexpression=convert(str(a))  #converts to np format
        
        output.set('Derivative:   '+outexpressionT)

        p=2
    except:
        output.set('non differentiable function')
        
#Calculates integral and conerts differnt formats
def inte():
    global calcexpression
    global outexpression
    global outexpressionT
    global p
    global output
    try:
        calcexpression=calcexpression.replace('acsc(','asin(1/')
        a=sym.integrate(eval(calcexpression))
        outexpressionT=str(a).replace('**','^')
        outexpressionT=outexpressionT.replace('k','x')
        outexpression=convert(str(a))#converts to np format
        if 'Integral(' in outexpression:
            output.set('Non integrable')
        else:
            eval(outexpression)
            output.set('Integral:   '+outexpressionT)
    except:
        output.set('Function cant be integrated')


#Calculates Definite derivative, ie derivative for given value of 'x' [dvalue]
def defderivative(dvalue):
    global calcexpression
    global expressionT
    global x
    global k
    global expression
    global l
    global addfun
    global sp
    global constant
    global tdf
    global slopeval

    p=1
    try:
        eval(expression)
    except SyntaxError:
        syntaxError()
        p=0
    if p==1:
        print(dvalue)
        derivative=sym.diff(eval(calcexpression))
        d=convert(str(derivative)) 
        m=str(d).replace('x',dvalue)
        sp=eval(m)
        slopeval.set(sp)

#Takes [a] which is array of two values- lower limit and upper limit x-coordinates
#Computes area under curve bw lower and upper limits
def area(points):
    global calcexpression
    global x
    global k
    global l
    global outarea

    try:
        a=sym.integrate(eval(calcexpression))
        y=convert(str(a))
        p=points.split(',')
        y1=y.replace('x',p[0])
        y2=y.replace('x',p[1])
        q=y2+' - '+y1
        areaexp='area: '+expressionT+':bw :'+p[0]+','+p[1]+'='+str(eval(q))
        outarea.set(areaexp)
    except:
        outarea.set('error')



#some extra buttons of Calculus    
def ButtonsS():
    global dvalue
    global tdf
    d= Button(windowS, text=' differentiate', fg='black', bg='darkseagreen1',activebackground='red', command=lambda:di(), height=3, width=10)
    d.grid(row=8, column=2)

    i= Button(windowS, text=' integrate', fg='black', bg='darkseagreen1',activebackground='red', command=lambda:inte(),height=3, width=10)
    i.grid(row=8, column=3)

    buttonx = Button(windowS, text=' x ', fg='black', bg='darkseagreen1',activebackground='red',command=lambda: pressT('x','k'),height=3, width=10)
    buttonx.grid(row=8, column=1)

    cl = Button(windowS, text='Clear', fg='black', bg='darkseagreen1',activebackground='red',command=cleartext, height=3, width=10) 
    cl.grid(row=8, column=0)

    are=Button(windowS, text='Area (2 points)', fg='black', bg='darkseagreen1',activebackground='red', command=lambda:area(textarea.get()), width=10)
    are.grid(row=11, column=5)

    der=Button(windowS, text=' Definite slope', fg='black', bg='darkseagreen1',activebackground='red', command=lambda:defderivative(tdf.get()), width=10)
    der.grid(row=14, column=5)
    
#-------------------------------------------------------------- WELCOME SCREEN------------------------------------------------------------------------------------------
#Main Interface that user sees:
#    >Numeric calculator
#    >Graphical calculator
#    >Constants
#    >Calculus

#Main window for Welcome screen
global windowM
windowM=Tk()
windowM.configure(bg="black")

canvas = Canvas(windowM, width = 3000, height = 1000)
canvas.configure(bg="light steel blue3")
canvas.pack()

imag=PhotoImage(file="calculator.gif") 
canvas.create_image(450,10, anchor=NW, image=imag) 

windowM.title("Menu")

l = Label(windowM, text = "CALCULATOR", bg='lavenderblush2', fg='black') 
l.config(font =("Ink Free", 30,'bold'))
l.place(x=120, y=10)

windowM.geometry("2050x800")
windowM.title("Menu")

NC= Button(windowM, text='Numeric Calculator', fg='black', bg='thistle2',activebackground='black',command= mainN ,height=3, width=16) 
NC.config(font =("Ink Free",14,'bold'))
NC.place(x=160, y=190)

GC= Button(windowM, text='Graphical Calculator', fg='black', bg='thistle2',activebackground='black',command= mainG , height=3, width=16) 
GC.config(font =("Ink Free",14,'bold'))
GC.place(x=160, y=310)

CNST= Button(windowM, text='Constants', fg='black', bg='thistle2',activebackground='black',command= main1, height=3, width=16) 
CNST.config(font =("Ink Free",14,'bold'))
CNST.place(x=160, y=430)

SREP=Button(windowM, text='Calculus', fg='black', bg='thistle2',activebackground='black',command= mainS, height=3, width=16) 
SREP.config(font =("Ink Free",14,'bold'))
SREP.place(x=160, y=550)

windowM.mainloop()
 #----------------------------------------------------END OF CODE----------------------------------------------------------------

