class LineChart():
    
    import turtle
    
    def __init__(self,datatag="Blank",hierarch=[],value=[],x_type="Blank",y_type="Blank"):
        self.tag = datatag
        self.hir = hierarch
        self.val = value
        self.x = x_type
        self.y = y_type

    
    def screen(self,width,textSize):
        height = width
        #calculation
        start = width/8 #find graph start point
        end = 7*width/8 #find chart line end coordinate
        length = width-2*width/8 # find length of a chart line
        big_round = (sorted(self.val)[len(self.val)-1]//(10**(len(str(sorted(self.val)[len(self.val)-1]))-1))+1)*(10**(len(str(sorted(self.val)[len(self.val)-1]))-1)) #find rounded biggest data value element
        screen = self.turtle.Screen() #screen
        chart = self.turtle.Turtle() #chart
        line = self.turtle.Turtle() #graph
        screen.setup(width,height) #create screen
        screen.setworldcoordinates(0,0,width,height) #set (0,0) as bottom left corner and (width,height) as top right corner of the screen
        screen.title(self.tag) #create window title
        #config chart turtle
        chart.hideturtle()
        chart.speed(0)
        chart.pensize(width=5)
        #config graph turtle
        line.speed(1)
        line.pensize(width=3)
        line.color("gold")
        line.penup()
        #draw chart line
        line.setpos(start,start)
        chart.penup()
        #write Title
        chart.setpos(width/2,height-start/3)
        chart.write(self.tag, move=False, align="center", font=("Segoe UI", int(4*textSize/3), "bold italic"))
        #write y axis
        chart.setpos(start,length+start+14*start/100)
        chart.write(self.y, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write x axis
        chart.setpos(length+start+14*start/100,start+2*start/10)
        chart.write(self.x, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write 0 as start
        chart.setpos(start-2*start/10,start-2*start/10)
        chart.write(0, move=False, align="right", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #draw chart line
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(start,end)
        chart.penup()
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(end,start)
        #draw y axis little line and write y axis value
        for i in range(1,7):
            chart.penup()
            chart.setpos(start-start/10,i*length/7+start)
            chart.pendown()
            chart.setpos(start+start/10,i*length/7+start)
            chart.penup()
            chart.setpos(start-2*start/10,i*length/7+start)
            chart.write("{:.2f}".format(i*big_round/6), move=False, align="right", font=("Segoe UI", int(textSize), "bold italic"))
        #draw x axis little line and write x axis data hierarch
        for i in range(1,len(self.hir)+1):
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+start/10)
            chart.pendown()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start-start/10)
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start-4*start/10)
            chart.write(self.hir[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        #draw graph line
        for i in range(1,len(self.val)+1):
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.dot(start/8)
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.pendown()
        #config graph turtle again
        line.color("grey")
        line.speed(0)
        #write data value
        for i in range(1,len(self.val)+1):
            line.penup()
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7)+start/10)
            line.write(self.val[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        line.hideturtle()
        #make it always appear until user close the window
        self.turtle.mainloop()
        
    #check if the data or screen config is appropriate
    def display(self,width="",textSize=""):
        try:
            self.screen(width,textSize)
        except:
            try:
                self.screen(800,12)
            except:
                print("DataInputError: Please check your data and try again.")

dataTitle1 = "Thailand Cumulative COVID-19 Confirm Case Every 6 Months" 
x_type1 = "Time"
y_type1 = "Cases (People)"
x_axis1 = ["Q2-2020","Q4-2020","Q2-2021","Q4-2021","Q2-2022"] # At least it has to be an array with the same length as y_axis
y_axis1 = [43,3787,26031,1920000,2910000] # Has to be only an array(List,Tuple) of numbers

dataTitle2 = "The Attendances over this week"
x_type2 = "Day"
y_type2 = "Attendance (People)"
x_axis2 = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
y_axis2 = [40,20,21,35,42]

dataTitle3 = "ปริมาณน้ำฝนสัปดาห์นี้"
x_type3 = "วัน"
y_type3 = "ปริมาณน้ำฝน (mm)"
x_axis3 = ["อาทิตย์","จันทร์","อังคาร","พุธ","พฤหัสฯ","ศุกร์","เสาร์"]
y_axis3 = [10,0,20,30,0,0,0]

#Using LineChart
#LineChart(Data Title,X values,Y values,X type,Y type).screen(Squared window length,Text size) to visualize datas to line chart

#LineChart(dataTitle1,x_axis1,y_axis1,x_type1,y_type1).display(600,9)
#LineChart(dataTitle2,x_axis2,y_axis2,x_type2,y_type2).display(800,12)
LineChart(dataTitle3,x_axis3,y_axis3,x_type3,y_type3).display()
