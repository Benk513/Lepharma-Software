# app/views/authentication_view.py

import customtkinter as ctk

class AuthenticationView(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#eee')
        
        self.geometry('600x400')
        self.resizable(width=False, height=False)
        
        self.title('Login To Lepharma')
        ctk.set_appearance_mode('light')
      

        self.username_label = ctk.CTkLabel(self,width=40,text='Username :')
        self.username_label.pack(pady=10)
 


    # def authenticate_user(self):
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()command=self.authenticate_user

    #     result = AuthenticationController.authenticate_user(username, password)
    #     if result["success"]:
           # self.destroy()   Close the login window
            #ProductView().mainloop()   Open the main application window
        # else:
        #     print(f"Error: {result['message']}")

if __name__ == "__main__":
    AuthenticationView().mainloop()


 