questions = [
    {
        "q.no.:" : '1',
        "question" : "Which club won 2015 UEFA Champions league?",
        "options" : ["FC Barcelona" ,"Real Madrid", "Bayren Munchen" , "Juventus"],
        "answer" : "FC Barcelona"
    },
    {
        "q.no.:": '2',
        "question": "Where weas the final of 2019 UEFA Champions League ?",
        "options": ["San Siro", "Wembly Stadium","Santiago Berbaneu", "Allianz Arena"],
        "answer" : "Santiago Berbaneu"
    },
    {
        "q.no.:": '3',
        "question": "In 2009 UEFA Champions League, Chelsea was beaten by Barcelona at ?",
        "options": ["Anfield", "Camp Nou", "Old Trafford", "Stamford Bridge"],
        "answer" : "Stamford Bridge"
    }
]

score = 0

for i in questions:
    data = (i["q.no.:"]) + i["question"] + "\n" + "The options are :" + "\n"+i["options"][0] + "\n"+i["options"][1]+"\n"+i["options"][2]+"\n"+i["options"][3] + "\n"
    ans = input(data)
    if ans == questions["answer"]:
        score += 1
print("Your score is : "+ score)
