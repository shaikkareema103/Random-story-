import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
when_choice = random.choice(when)
who_choice = random.choice(who)
name_choice = random.choice(name)
residence_choice = random.choice(residence)
went_choice = random.choice(went)
happened_choice = random.choice(happened)
story = (f"{when_choice}, {who_choice} named {name_choice} who lived in {residence_choice}, "
         f"went to the {went_choice} and {happened_choice}.")
print(story)
