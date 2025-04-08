import random

words = [
    {"japanese": "watashi", "english": "I, me"},
    {"japanese": "anata", "english": "you"},
    {"japanese": "desu", "english": "is, am, are"},
    {"japanese": "wa", "english": "topic marker"},
    {"japanese": "no", "english": "possessive or explanatory particle"},
    {"japanese": "ka", "english": "question marker"},
    {"japanese": "mo", "english": "also, too"},
    {"japanese": "ni", "english": "to, at, in"},
    {"japanese": "de", "english": "at, in, by"},
    {"japanese": "wo", "english": "direct object marker"},
    {"japanese": "iru", "english": "to be (for living things)"},
    {"japanese": "iku", "english": "to go"},
    {"japanese": "kuru", "english": "to come"},
    {"japanese": "suru", "english": "to do"},
    {"japanese": "mieru", "english": "to see, can see"},
    {"japanese": "iku", "english": "to go"},
    {"japanese": "kuru", "english": "to come"},
    {"japanese": "iru", "english": "to be (for animate objects)"},
    {"japanese": "aru", "english": "to be (for inanimate objects)"},
    {"japanese": "koto", "english": "thing, matter, fact"},
    {"japanese": "kore", "english": "this"},
    {"japanese": "sore", "english": "that"},
    {"japanese": "are", "english": "that (over there)"},
    {"japanese": "dore", "english": "which"},
    {"japanese": "dare", "english": "who"},
    {"japanese": "nani", "english": "what"},
    {"japanese": "doko", "english": "where"},
    {"japanese": "doushite", "english": "why, how"},
    {"japanese": "arigatou", "english": "thank you"},
    {"japanese": "gomennasai", "english": "sorry"},
    {"japanese": "hai", "english": "yes"},
    {"japanese": "iie", "english": "no"},
    {"japanese": "onegaishimasu", "english": "please"},
    {"japanese": "otsukaresama", "english": "thank you for your hard work"},
    {"japanese": "ohayou", "english": "good morning"},
    {"japanese": "konbanwa", "english": "good evening"},
    {"japanese": "sayounara", "english": "goodbye"},
    {"japanese": "wakaru", "english": "to understand, to know"},
    {"japanese": "hanasu", "english": "to speak, to talk"},
    {"japanese": "kiku", "english": "to listen, to ask"},
    {"japanese": "yomu", "english": "to read"},
    {"japanese": "kaku", "english": "to write"},
    {"japanese": "taberu", "english": "to eat"},
    {"japanese": "nomu", "english": "to drink"},
    {"japanese": "kau", "english": "to buy"},
    {"japanese": "uru", "english": "to sell"},
    {"japanese": "neru", "english": "to sleep"},
    {"japanese": "okiru", "english": "to wake up, to get up"},
    {"japanese": "suwaru", "english": "to sit"},
    {"japanese": "tatsu", "english": "to stand"},
    {"japanese": "aruku", "english": "to walk"},
    {"japanese": "hashiru", "english": "to run"},
    {"japanese": "suki", "english": "like, love"},
    {"japanese": "kirai", "english": "dislike, hate"},
    {"japanese": "ookii", "english": "big, large"},
    {"japanese": "chiisai", "english": "small, little"},
    {"japanese": "atarashii", "english": "new"},
    {"japanese": "furui", "english": "old"},
    {"japanese": "nagai", "english": "long"},
    {"japanese": "mijikai", "english": "short"},
    {"japanese": "takai", "english": "high, tall, expensive"},
    {"japanese": "yasui", "english": "cheap, inexpensive"},
    {"japanese": "ii", "english": "good, nice"},
    {"japanese": "warui", "english": "bad"},
    {"japanese": "isogashii", "english": "busy"},
    {"japanese": "tanoshii", "english": "fun, enjoyable"},
    {"japanese": "kanashii", "english": "sad"},
    {"japanese": "muzukashii", "english": "difficult, hard"},
    {"japanese": "kantan", "english": "easy, simple"},
    {"japanese": "hayai", "english": "fast, early"},
    {"japanese": "osoi", "english": "slow, late"},
    {"japanese": "genki", "english": "healthy, energetic, lively"},
    {"japanese": "hima", "english": "free time, not busy"},
    {"japanese": "ame", "english": "rain"},
    {"japanese": "yuki", "english": "snow"},
    {"japanese": "kaze", "english": "wind"},
    {"japanese": "sora", "english": "sky"},
    {"japanese": "umi", "english": "sea, ocean"},
    {"japanese": "yama", "english": "mountain"},
    {"japanese": "kawa", "english": "river"},
    {"japanese": "hi", "english": "day, sun"},
    {"japanese": "tsuki", "english": "month, moon"},
    {"japanese": "toshi", "english": "year"},
    {"japanese": "ji", "english": "hour, time"},
    {"japanese": "fun", "english": "minute, fraction"},
    {"japanese": "byou", "english": "second"},
    {"japanese": "hidari", "english": "left"},
    {"japanese": "migi", "english": "right"},
    {"japanese": "mae", "english": "front"},
    {"japanese": "ushiro", "english": "back"},
    {"japanese": "naka", "english": "middle, inside"},
    {"japanese": "soto", "english": "outside"},
    {"japanese": "ue", "english": "up, above"},
    {"japanese": "shita", "english": "down, below"},
    {"japanese": "chikai", "english": "near"},
    {"japanese": "tooi", "english": "far"},
    {"japanese": "daijoubu", "english": "okay, alright"},
    {"japanese": "sugoi", "english": "amazing, great"},
    {"japanese": "tanoshii", "english": "fun, enjoyable"}
]


def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['japanese']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
        
        if user_answer == correct_answer:
            print('Correct!!\n!')
            score += 1
        else:
            print(f"Wrong, idiot! The correct answer is'{word['english']}'.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the language Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()