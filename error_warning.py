from tkinter import messagebox as ms

class Error:
    def throw_error():
        answear = ms.askquestion("ERROR", "соединение потеряно\nВы хотите закрыть программу?")
        if answear == "yes":
            return "y"
        
        