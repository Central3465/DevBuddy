import random

motivation = [
    "Want that Framework laptop or Apple iPad from Terra? If so, then get coding bucko!",
    "Your mind isn't working if you just doomscroll all day.",
    "Your github profile heatmap isn't going to grow unless you actually commit.",
    "Come on, what are you doing? GEt coding!",
    "You can do it!"
]

def ui():
    show()

def show():
    poo = random.randint(0, len(motivation) - 1)
    quote = motivation[poo]
    print(quote)
