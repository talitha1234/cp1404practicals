"""
Wikipedia API & Python Library
Estimate time: 30 mins
Actual time: 60 mins
"""
import wikipedia

title = input("Title: ")
while title != "":
    try:
        choice = wikipedia.page(title, auto_suggest=False)
        print(choice.title)
        print(wikipedia.summary(choice))
        print(choice.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    title = input("Title: ")




