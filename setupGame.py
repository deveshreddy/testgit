import tkinter
import time
class setup:

    def __init__(self):
        #initializing setup window
        self.setup_window = tkinter.Tk()
        self.setup_window.title("Black Jack Setup")
        self.setup_window.geometry("400x150")
        self.setup_window.configure(background='blue')

        #variable to store the count of the players
        self.ask_count = tkinter.IntVar()

        #variable for setting the text on screen
        self.result_text = tkinter.StringVar()

        #begin the process
        self._process_window()

    #this function is the face of the setup display screen
    def _interface(self):
        # label the frame
        tkinter.Label(self.setup_window, text = "Enter no of players").grid(row = 0, column =1)

        #text_box section
        text_box = tkinter.Entry(self.setup_window, textvariable = self.ask_count)
        text_box.grid(row=1, column=2)

        #Buttons section
        okbutton = tkinter.Button(self.setup_window,text='Okay', command =self.button_clicked)
        cancelbutton = tkinter.Button(self.setup_window, text ="cancel", command = self.setup_window.destroy)
        okbutton.grid(row =2 , column =3, sticky ='e')
        cancelbutton.grid(row=2,column=4,sticky = 'w')

        #text for displaying the nature of the entered value


    def button_clicked(self):
        self.result_text_label = tkinter.Label(self.setup_window, background='red', textvariable=self.result_text)
        self.result_text_label.grid(row=3, column=0, columnspan=3)

        if self.ask_count.get() == 0:
            self.result_text.set('lazy')

        elif self.ask_count.get() <0 or self.ask_count.get()>4 :
            self.result_text.set('wrong, 1-4 people are allowed to play')

        else:
            self.result_text.set("enjoy the game, hit continue")
            continuebutton = tkinter.Button(self.setup_window,text='continue', command =self.setup_window.destroy)
            continuebutton.grid(row =3, column =4, sticky ='e')


    # time.sleep(5)
            # self.setup_window.destroy()


    def _process_window(self):
        self._interface()
        if self.ask_count.get() == 0 :
            self.setup_window.mainloop()

        elif  0<self.ask_count.get()<5:
            self.setup_window.quit()


        print(self.ask_count.get())

# this is the main function
__name__ = '__main__'

#begins the setup
def start_setup():
    if __name__ == '__main__':
        #begin the setup
        x = setup()
        return x.ask_count.get()

