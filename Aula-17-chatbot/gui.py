import tkinter as tk
from chatbot import chatBot

class chatBotGUI:
    def __init__(self):
        self.chatbot = chatBot()
        self.window = tk.Tk()
        self.window.title('chatBot')

        self.user_name = None

        self.banned_words= ['babaca', 'bobao', 'burro',]

        self.chat_area = tk.Text(self.window, height=20, width=50, state='disabled' )
        self.chat_area.pack()
        self.chat_area.tag_config('user', foreground='red')
        self.chat_area.tag_config('bot', foreground='green')
        self.chat_area.tag_config('system', foreground='blue')

        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack()
        self.entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.window, text='Enviar', command=self.send_message)
        self.send_button.pack()

        self.display_message('Sistema: olá! qual é o seu nome?\n', 'system')

    def has_banned_words(self, text):
        text = text.lower()
        for word in self.banned_words:
            if word in text:
                return True
        return False

    def send_message(self, event=None):
        user_input = self.entry.get()

        if user_input:

            if self.has_banned_words(user_input):
                self.display_message('Bot:Por Favor, evite palavras ofensivas.\n', 'bot')
                self.entry.delete(0, tk.END)
                return


            if self.user_name is None:
                self.user_name = user_input
                self.display_message(f'{self.user_name}: {user_input}\n', 'user')
                self.display_message(f'Bot: prazer em te conhecer, {self.user_name}\n', 'bot')
                self.display_message(f'Bot: qual pergunta deseja fazer?\n', 'bot')
            else:
                self.display_message(f'{self.user_name}:{user_input}\n', 'user74')
                response = self.chatbot.get_response(user_input)
                self.display_message(f'Bot:{response}\n', 'bot')

                self.entry.delete(0, tk.END)


    def display_message(self, message, tag):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message, tag)
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def run(self):
        self.window.mainloop()
