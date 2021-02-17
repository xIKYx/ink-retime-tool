from tkinter import *
from math import floor,ceil
import json

window=Tk()

window.title("INK Retimer")

window.wm_attributes("-topmost",1)

Label(window,text="Retiming").grid(row=0,column=0,columnspan=7)

frV=StringVar()

Label(window,text="Framerate").grid(row=1,column=2,columnspan=2)
fps_field=Entry(window,width=5,justify=CENTER,textvariable=frV)
fps_field.grid(row=1,column=4)

startV=StringVar()
endV=StringVar()

Label(window,text="Start").grid(row=2,column=1)
start_field=Entry(window,width=30,textvariable=startV)
start_field.grid(row=2,column=2,columnspan=3)
start_time=Label(window,text="0.000")
start_time.grid(row=2,column=5)

Label(window,text="End").grid(row=3,column=1)
end_field=Entry(window,width=30,textvariable=endV)
end_field.grid(row=3,column=2,columnspan=3)
end_time=Label(window,text="0.000")
end_time.grid(row=3,column=5)

def calculate_time():
    try:
        fps=int(fps_field.get())
        
        startframe=floor(float(json.loads(start_field.get())["lct"])*fps)
        endframe=floor(float(json.loads(end_field.get())["lct"])*fps)
        
        start_time.configure(text=str(round(startframe/fps,3)))
        end_time.configure(text=str(round(endframe/fps,3)))
        
        duration=endframe-startframe
        seconds,frames=divmod(duration,fps)
        minutes,seconds=divmod(seconds,60)
        hours,minutes=divmod(minutes,60)
        milliseconds=round(frames/fps*1000)
        
        if hours!=0:
            final_time.configure(text="{0}:{1:0>2}:{2:0>2}.{3:0>3}".format(hours,minutes,seconds,milliseconds))
        elif minutes!=0:
            final_time.configure(text="{0}:{1:0>2}.{2:0>3}".format(minutes,seconds,milliseconds))
        elif seconds!=0:
            final_time.configure(text="{0}.{1:0>3}".format(seconds,milliseconds))
        else:
            final_time.configure(text="0.{0:0>3}".format(milliseconds))
    except Exception as e:
        final_time.configure(text="Error, check output")
        print("Error: {}".format(e))

def reset_time_fields():
    endV.set("")
    startV.set("")
    frV.set("")

def copy(text):
    window.clipboard_clear()
    window.clipboard_append(text)

def mod_message():
    copy(
        f'Mod Message: Time starts at {start_time.cget("text")} and ends at {end_time.cget("text")} at {fps_field.get()} fps to get a final time of {final_time.cget("text")}.'
    )


Button(window,text="Calculate",command=calculate_time).grid(row=8,column=1)
final_time=Label(window,text="0.000")
final_time.grid(row=4,column=2,columnspan=3)
Button(window,text="Clear",command=reset_time_fields).grid(row=8,column=5)
Button(window,text="Copy Mod Message to Clipboard",command=mod_message).grid(row=8,column=3,columnspan=2)

window.mainloop()
