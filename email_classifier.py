import tkinter as tk
from email_classifier_function import email_classifier, censor

class App(object):
    '''Create GUI interface with Tkinter for email classifier'''
    
    def __init__(self):
        
        # initializes tcl/tk interpreter and creates the root window. 
        self.root = tk.Tk()
        self.root.wm_title("Email Classifier")
        self.frame = tk.Frame(self.root, width=400, height=10)
        self.frame.pack()

        # Welcome Message
        tk.Message(self.root, text="This program scans emails and censors any classified words it finds. Never worry about classification leaks again!", width=300, justify='center', font=("Arial", 12, "bold italic")).pack(pady=40)

        # User input for classified words
        tk.Label(self.root, text="Enter classified words/phrases. Seperate each word by comma").pack()
        self.classified_user_input = tk.StringVar()
        tk.Entry(self.root, textvariable=self.classified_user_input).pack()

        # User input for email text 
        tk.Label(self.root, text="Copy email and paste text here").pack()
        self.email_user_input = tk.Text(self.root, height=10, width=40)
        self.email_user_input.pack()

        # Submit for classification button 
        tk.Button(self.root, text="Classify Email", command=self.clicked).pack()
      
        # Labels for returned results 
        self.error_message = tk.Label(self.root, text=" ", fg="red")
        self.original_classified_input = tk.Label(self.root, text="Classified Words:", fg="blue")
        self.original_email_input = tk.Label(self.root, text="Original Email:")
        self.classified_flag_result = tk.Label(self.root, text="Contains Classified Words:", fg="red")
        self.return_classified_text_label = tk.Label(self.root, text="Classified Email:")
        self.return_classified_text = tk.Label(self.root, fg="blue")
        
        # add labels to GUI
        self.error_message.pack()
        self.original_classified_input.pack()
        self.original_email_input.pack() 
        self.classified_flag_result.pack()
        self.return_classified_text_label.pack()
        self.return_classified_text.pack()
      
        # keeps Tkinter running
        self.root.mainloop()

    # function to reset previous messages 
    def reset(self):
        self.error_message['text'] = ' '
        self.classified_flag_result['text'] = ' '
        self.return_classified_text['text'] = ' '
        
    def clicked(self):
        
        # clear past returned values
        self.reset()

        # get submitted user input from entry boxes
        classified = self.classified_user_input.get()
        email = self.email_user_input.get("1.0",'end-1c')

        # test for problems with classified words user input
        try: 
            if ',' in classified: 
                classified_input_cleaned = classified.replace(" ", "").split(',')
            else:
                classified_input_cleaned = classified.replace(" ", "").split()
               
        except (ValueError, TypeError, NameError):
            self.error_message['text'] = "If there are multiple classified words, please seperate with commas"

        # if user input is blank, return
        if classified_input_cleaned == '' or email == '' or len(classified_input_cleaned) < 1 or len(email) < 1:
            self.error_message['text'] = "Empty input, please try again"
            self.error_message.configure("red", foreground="red")
            return

        # return finished data to GUI 
        try:
            result = email_classifier(classified_input_cleaned, email)
            self.original_classified_input['text'] = "Classified words: " + ' '.join(classified_input_cleaned)
            self.original_email_input['text'] = "Original email: " + email
            self.classified_flag_result['text'] = "Classified words found? " + str(result[0])
            self.return_classified_text['text'] = result[1]
        except (ValueError, TypeError, NameError):
            self.error_message['text'] = "There was a problem with classification. Please review your input and try again."
     
App()