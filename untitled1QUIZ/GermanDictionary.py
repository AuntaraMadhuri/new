# Common German words meaning in English for tourists
german_to_english = {
    "hallo": "hello",
    "gut": "good",
    "danke": "thanks",
    "guten tag": "good day",
    "guten abend": "good evening",
    "tschuss": "bye",
    "super": "great",
    "nein": "no",
    "klingt gut": "sounds good",
    "bitte": "Please",
    "willkommen": "welcome",
    "deutsch": "german",
    "hilfe": "help",
    "hunde": "dogs",
}
# you can ask questions 3 times a day

start_daily = 0
daily_limit = 3

while start_daily < daily_limit:
    german = input("Enter a german word: ")
    print(german_to_english.get(german, "Not in the list"))
    start_daily += 1

else:
    print("Sorry. You crossed daily limit")
