import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, Checkbutton, IntVar

def get_credentials_gui():
    class SignInApp:
        def __init__(self, root):
            self.email = None
            self.password = None
            self.folder_list = []
            self.file_path = None
            self.save_csv = None
            self.keyword = []
            self.default_filters_var = IntVar()

            self.btn_default_mode = tk.Button(root, text="Default Mode", command=self.set_default_mode)
            self.btn_default_mode.pack(pady=10)


            self.btn_sign_in = tk.Button(root, text="Enter Sign In Info", command=self.get_credentials)
            self.btn_sign_in.pack(pady=10)

            self.btn_filters = tk.Button(root, text="Filters", command=self.get_filters)
            self.btn_filters.pack(pady=10)
            
            self.btn_enter_folders = tk.Button(root, text="Enter Folders", command=self.get_folders, state=tk.DISABLED)
            self.btn_enter_folders.pack(pady=10)

            self.btn_select_csv = tk.Button(root, text="Enter CSV", command=self.select_csv_file, state=tk.DISABLED)
            self.btn_select_csv.pack(pady=10)

            self.btn_save_location = tk.Button(root, text="Select Save CSV", command=self.select_save_location, state=tk.DISABLED)
            self.btn_save_location.pack(pady=10)

            self.btn_exit_program = tk.Button(root, text="Run Program", command=root.quit)
            self.btn_exit_program.pack(pady=10)
            

            


        def get_credentials(self):
            self.email = simpledialog.askstring("Input", "Enter your email:")
            self.password = simpledialog.askstring("Input", "Enter your password:", show='*')
            if self.email and self.password:
                messagebox.showinfo("Info", "Credentials entered successfully!")
                self.btn_enter_folders.config(state=tk.NORMAL)  # Enable the "Enter Folders" button

        def get_folders(self):
            folders = simpledialog.askstring("Input", "Enter what sales navigator folders the results will save to. Max 4 folders. Separate by commas.")
            if folders:
                self.folder_list = [folder.strip() for folder in folders.split(",")][:4]  # Take up to 4 folders
                messagebox.showinfo("Info", f"Entered folders: {', '.join(self.folder_list)}")
                self.btn_select_csv.config(state=tk.NORMAL)  # Enable the "Enter CSV" button
        
        def get_filters(self):
            filters = simpledialog.askstring("Input", "Enter position to search for, separate each position by a comma:")
            if filters:
                self.keyword = [filter.strip() for filter in filters.split(",")]
                messagebox.showinfo("Info", f"Entered positions: {', '.join(self.keyword)}")

        def select_csv_file(self):
            self.file_path = filedialog.askopenfilename(title="Add full file path to file containing Excel CSV of companies", filetypes=[("CSV files", "*.csv")])
            if self.file_path:
                messagebox.showinfo("Info", f"Selected CSV file: {self.file_path}")
                self.btn_save_location.config(state=tk.NORMAL)  # Enable the "Select Save CSV" button
        def select_save_location(self):
            save_choice = messagebox.askyesnocancel("Save Unfound Data", "Do you want to save unfound data?")
            if save_choice is None:  # Cancel was pressed
                return
            elif save_choice:  # Yes was pressed
                self.save_csv = filedialog.asksaveasfilename(title="Add Full File path to 'uncreated' file location where the program will store all unfound results", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if self.save_csv:
                    messagebox.showinfo("Info", f"Save location selected: {self.save_csv}")
                    self.btn_run_program.config(state=tk.NORMAL)  # Enable the "Run Program" button
            else:  # No was pressed
                self.save_csv = None
                messagebox.showinfo("Info", "Unfound data will not be saved.")
                self.btn_run_program.config(state=tk.NORMAL)  # Enable the "Run Program" button

        def run_program(self):
            if self.email and self.password and self.folder_list and self.file_path and self.save_csv:
                root.quit()
                
        def set_default_mode(self):
            self.email = "Noah.wolfe3@gcu.edu"
            self.password = "heartland#1"
            self.file_path = "/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/filtered_1k_5k.csv"
            self.folder_list = ["Test-1"]
            self.keyword = ['ceo','president','lead','owner','engineer','senior','chief','partner','director','head','vp','evp','manager','advisor','development','officer','executive','retail','fundraising','cto','cmo','founder','coo','chairman','honor','cfo','sr']
            
            # Run the program (assuming you have a method called run_program)
            # self.run_program()  # Uncomment this if you have a method to run the program

            # Close the UI
            root.quit()

    root = tk.Tk()
    root.title("Sign In")

    # Set window size
    width = 800
    height = 600

    # Calculate position to center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    app = SignInApp(root)
    root.mainloop()

    return app.email, app.password, app.folder_list, app.file_path, app.keyword

if __name__ == "__main__":
    email, password, folder_list, file_path, keyword = get_credentials_gui()
    print(email, password, folder_list, file_path, keyword)