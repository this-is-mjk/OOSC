import json

def tester():
    try:
        with open('output.json', 'r') as file:
            data = json.load(file)[0]
            # check number of question
            if len(data['questions']) != 10:
                print("ERROR: INCORRECT NUMBER OF QUESTIONS")
                return
            #check length of question < 80
            for question in data['questions']:
                if len(question) > 80:
                    print("ERROR: INCORRECT LENGTH OF QUESTION")
                    return
            #check links 
            if len(data['relevant_links']) != 5:
                print("ERROR: INCORRECT NUMBER OF LINKS")
                return
            #topics
            for obj in data['relevant_links']:
                if len(obj['url'] ) == 0 or len(obj["title"]) == 0:
                    print("ERROR: ERROR IN URL OR TITLE")
                    return
            print("SUCCESS")
    except:
        print("ERROR IN FILE")
tester()