# current.py
import tkinter as tk

class CurrentStatusUI:
    def __init__(self, root):
        self.root = root
        root.title("Current Status")

        self.company_name_var = tk.StringVar()
        self.current_folder_var = tk.StringVar()
        self.company_list_position_var = tk.StringVar()
        self.companies_not_found_var = tk.StringVar()

        tk.Label(root, text="Current Company:").pack(pady=5)
        tk.Label(root, textvariable=self.company_name_var).pack(pady=5)

        tk.Label(root, text="Into Folder:").pack(pady=5)
        tk.Label(root, textvariable=self.current_folder_var).pack(pady=5)

        tk.Label(root, text="Progress:").pack(pady=5)
        tk.Label(root, textvariable=self.company_list_position_var).pack(pady=5)

        tk.Label(root, text="Companies not found:").pack(pady=5)
        tk.Label(root, textvariable=self.companies_not_found_var).pack(pady=5)

    def update_status(self, company_name="", total_links_found=0, current_folder="", company_list_position=0, company_total=0, companies_not_found=0):
        self.company_name_var.set(company_name)
        self.current_folder_var.set(current_folder)
        self.company_list_position_var.set(f"{company_list_position}/{company_total} remaining")
        self.companies_not_found_var.set(companies_not_found)
    def thread_safe_update(self, **kwargs):
        self.root.after(0, self.update_status, **kwargs)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrentStatusUI(root)
    root.mainloop()
