from tkinter import messagebox as ms

class Error:
    def throw_error():
        answear = ms.askquestion("ERROR", "соединение потеряно\nВы хотите закрыть программу?")
        if answear == "yes":
            return "y"
        else:
            shutdown_response = ms.askquestion("Shutdown", "Вы хотите перезагрузить систему?")
            if shutdown_response == "yes":
                return "r"