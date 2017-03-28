from Tkinter import *
from Tablet import *
import setCameraPropertiesScript
import saveTemplateFileScript
import keyboard
import Config 

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_button.pack(side=LEFT)
        
        self.save_template_button = Button(frame, text="Save Template (s+s)", command=saveTemplateFileScript.saveTemplateFile)
        self.save_template_button.pack(side=LEFT)


        self.set_corners_button = Button(frame, text="Set Tablet Corners", command=self.setCorners)
        self.set_corners_button.pack(side=LEFT)

        self.show_tablet_button = Button(frame, text="Show Tablet", command=self.showTablet)
        self.show_tablet_button.pack(side=LEFT)

        self.save_template_button = Button(frame, text="Set Camera Properties", command=setCameraPropertiesScript.setCameraProperties)
        self.save_template_button.pack(side=LEFT)


        self.m_Tablet = TTablet()
        keyboard.add_hotkey(Config.HOTKEY_CLICK_LEFT, self.clickTabletLeft)        
        keyboard.add_hotkey(Config.HOTKEY_CLICK_RIGHT, self.clickTabletRight)        
        keyboard.add_hotkey(Config.HOTKEY_TURN_TABLET, self.turnTablet)        


    def turnTablet(self):
        self.m_Tablet.turnOnOff() #print "hi there, everyone!"

    def setCorners(self):
        self.m_Tablet.setCorners() #print "hi there, everyone!"

    def clickTabletLeft(self):
        self.m_Tablet.click("left")

    def clickTabletRight(self):
        self.m_Tablet.click("right")
        
    
    def showTablet(self):
        self.m_Tablet.showTablet() #print "hi there, everyone!"


root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below