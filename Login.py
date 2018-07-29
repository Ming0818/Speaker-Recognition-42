from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dicti import *
from homeapp import *

fname = ''

class Training_file:
    def __init__(self):
        root = Tk()
        root.title("Log In")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bggif/10.jpg')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding TextBoxes

        user_label = Label(root, bg="black", fg="white", text="User name")
        user_label.config(font=("Courier", 20))
        user_label.place(relx=0.35, rely=0.4, anchor='w')
        global v1
        v1 = StringVar()
        user_entry = self.EntryWithPlaceholder(root,"Enter the Username","black",textvariable = v1)
        user_entry.place(relx=0.65, rely=0.4, anchor='e')
        user_entry.config(font = ("Courier",14))
        user_label = Label(root,bg="black", fg="white", text="Password")
        user_label.config(font=("Courier", 20))
        user_label.place(relx=0.35, rely=0.5, anchor='w')
        global v2
        v2 = StringVar()
        user_entry = self.EntryWithPlaceholder(root, "Enter the Password","black",textvariable = v2)
        user_entry.config(font = ("Courier",14))
        user_entry.place(relx=0.65, rely=0.5, anchor='e')


        ## Adding Buttons

        rec_button = Button(root, text="SignUp", bd=0, bg="black", fg="white", font=("Courier",15),command = self.reco)
        rec_button.place(relx=0.45, rely=0.65, anchor=CENTER)

        play_button = Button(root, text="SignIn", bd=0, bg="black", fg="white", font=("Courier",15),command = self.play)
        play_button.place(relx=0.55, rely=0.65, anchor=CENTER)

        train_button = Button(root, text="Forget Password", bd=0, bg="black", fg="white", font=("Courier",15))
        train_button.place(relx=0.5, rely=0.75, anchor=CENTER)

        root.mainloop()


    ## Class for a placeholder

    class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',textvariable = None):
            super().__init__(master,textvariable = textvariable)

            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.foc_in)
            self.bind("<FocusOut>", self.foc_out)

            self.put_placeholder()

        def put_placeholder(self):
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

        def foc_in(self, *args):
            if self['fg'] == self.placeholder_color:
                self.delete('0', 'end')
                self['fg'] = self.default_fg_color

        def foc_out(self, *args):
            if not self.get():
                self.put_placeholder()
                
    ## Function for resizing the Image

    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo

    ## Recording

    def reco(self):
            global fname
            global v1,v2
            print(str(v1.get()),str(v2.get()))
            signup(str(v1.get()),str(v2.get()))

    ## Playing the last recorded

    def play(self):
            global fname
            global v1,v2
            p = signin(str(v1.get()),str(v2.get()))
            print(p)
            if(p=="PASS"):
                print("sucess")
                home()
            elif(p=="Sorry"):
                print("Username or Password maybe incorrect")
            else:
                print("Username or Password maybe incorrect")


xyz = Training_file()
