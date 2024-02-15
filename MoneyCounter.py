import time
import tkinter

payRate = float(input("Input your pay rate as a float "))
root = tkinter.Tk()
root.title('Pay for the Day')

timeStart = time.strftime
timeStartStr = 'Initiated: ' + time.strftime('%H:%M:%S')
print(timeStartStr)

timeStartH = float(timeStart('%H'))
timeStartM = (float(timeStart('%M')))/60
timeStartS = (float(timeStart('%S')))/3600
timeStartConverted = timeStartH + timeStartM + timeStartS

def updater():
    timeNow = time.strftime('%H %M %S')
    timeNowH = int(time.strftime('%H'))
    timeNowM = (int(time.strftime('%M')))/60
    timeNowS = (int(time.strftime('%S')))/3600
    timeNowConverted = timeNowH + timeNowM + timeNowS

    timeDelta = timeNowConverted - timeStartConverted
    earned = '''You've earned: $''' + str(timeDelta * payRate)[0:7]
    textLabel.config(bg='#FFFFFF', fg='#008000', font=('calibri',  40, 'bold'), text = earned)
    textLabel.after(3000, updater)

textLabel = tkinter.Label(root, font=('Arial', 20, 'bold'))

textLabel.pack()

updater()
tkinter.mainloop()    
