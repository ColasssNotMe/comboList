import customtkinter as ctk
import pyperclip


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # define var
        self.currentLine = 0

        # create widgets
        self.geometry("400x600")
        self.title("Combo List Spitter")
        self.fileName = ctk.CTkEntry(self, width=100, placeholder_text="File Name")
        self.fileName.pack(pady=10)
        self.splitBy = ctk.CTkEntry(self, width=100, placeholder_text="Split by")
        self.splitBy.pack(pady=10)
        self.submit = ctk.CTkButton(self, text="Split", command=self.readFile)
        self.submit.pack(pady=10)

        # TODO: testing
        self.fileName.insert(string="combo.txt", index="0")
        self.splitBy.insert(string=" ", index="0")

        # show name
        self.textName = ctk.CTkTextbox(self, width=100, height=100)
        self.textName.pack(pady=10)

        # button to copy name
        self.copyName = ctk.CTkButton(
            self,
            text="Copy Name",
            command=self.copyNameText,
        )
        self.copyName.pack(pady=10)

        # show ID
        self.textID = ctk.CTkTextbox(self, width=100, height=100)
        self.textID.pack(pady=10)

        # button to copy ID
        self.copyID = ctk.CTkButton(
            self,
            text="Copy ID",
            command=self.copyIDText,
        )
        self.copyID.pack(pady=10)

    def copyIDText(self):
        text = self.textID.get("1.0", "end-1c")
        print(text)
        pyperclip.copy(text)

    def copyNameText(self):
        text = self.textName.get("1.0", "end-1c")
        print(text)
        pyperclip.copy(text)

    def readFile(self):
        with open(self.fileName.get(), "r", encoding="utf-8") as file:
            data = file.readlines()
            if self.currentLine < len(data):
                next_line = data[self.currentLine]
                splitText = next_line.split(self.splitBy.get())
                if splitText == [] or splitText[0] == "\n":
                    self.currentLine += 1
                else:
                    self.textID.delete("1.0", "end")
                    self.textName.delete("1.0", "end")
                    name = splitText[0]
                    print(splitText)
                    id = splitText[1]
                    self.textID.insert(text=id, index="1.0")
                    self.textName.insert(text=name, index="1.0")
                    self.currentLine += 1
            else:
                pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
