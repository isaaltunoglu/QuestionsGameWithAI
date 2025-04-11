# ilk olarak oyunun ana mekanizmasını yazacağız ve şöyle olmalı gemini ai ' in apisini kullanarak 
#sorualrı metin olarak çekeceğiz ve doğru cevabıda metinin alt kısımında verecek ve biz o doğru cevabı splitmetodu ile ayırıp
#kullanıcıdan bir cevap alcağaız ve doğru cevap ile karşılaştırırdığımızda eğer doğruysa kullanıcıya puan vereceğiz be bir sonraki
# soruya geçeceğiz eğer yanlış bir cevap verdiyse Kullanıcı ana ekranda doğru cevap buydu deyip tekrar oyanamak ister misin ekranı gelecek



questions = ["What is the capital of France?"] #Example
answers = ["A)Ankara B)Berlin C)Moscow D)Paris"]
right_answer = ["D"] #Example
useranswer = ""
score = 0
i = 0


while True:
    print(questions[i])
    print(answers[i])
    useranswer = str(input("Cevabınız Nedir: ")).capitalize()
    if useranswer == right_answer[i]:
        score += 10
        i += 1
    else:
        print(f"You lost. Your Score: {score}")








