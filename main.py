
import re
from google import genai
# This is a simple quiz game that generates questions using the Gemini API.

class Game():
    def __init__(self):
        self.score = 0
        self.index = 0
        self.questions = []
        self.options = []
        self.right_answers = []
        self.text = ""


    def create_text(self):
        client = genai.Client(api_key="YOUR-API-KEY HERE") #You can copy your Gemini API key from the Google Cloud Console.


        #Create a response with your own prompt but dont change prompt but you can translate other language.
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=''' 
        Lütfen aşağıdaki kurallara uygun şekilde 10 adet bilgi ve genel kültür sorusu üret:
        Her soru **** (iki yıldız) ile başlamalıdır.
        Her sorunun dört adet şıkkı olmalıdır. Şıklar a, b, c, d ile gösterilmeli ve her şıkkın başında & sembolü olmalıdır.
        Şıklardan sonra "Cevap Anahtarı" başlığı altında her sorunun doğru cevabını belirt.
        Cevap anahtarında her satır ! sembolüyle başlamalıdır ve 1. b, 2. c formatında olmalıdır.
        ''',)
        
        self.text = response.text

    def text_separater(self):
        self.text = self.text.splitlines()
        for line in self.text:
            if "*" in line:
                self.questions.append(line)
            if "!" in line:
                letter = re.search(r'([a-d])',line)
                self.right_answers.append(letter.group(1))
            if "&" in line:
                self.options.append(line)

    def init_game(self):
        self.score = 0
        self.index = 0
        self.questions = []
        self.options = []
        self.right_answers = []
        self.create_text()
        self.text_separater()
        while self.index < len(self.questions):
            print(self.questions[self.index])
            j = 4*self.index
            while j < (4 + self.index*4):
                print(self.options[j])
                j+=1
            useranswer = str(input("Cevabınız Nedir: "))
            if useranswer.lower() == str(self.right_answers[self.index]).lower():
                self.score += 10
                self.index += 1
            else:
                print(f"You lost. Your Score: {self.score}")
                choice = input("do you want to continue Y/n").lower()
                if choice == "y":
                    self.init_game()
                else:
                    break

if __name__ == "__main__":
    game = Game()
    game.init_game()

