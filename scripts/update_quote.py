import re
import random

def get_random_quote():
    """Return a random quote from a predefined collection."""
    
    quotes = [
        # 1–20: Western / software-related / philosophy
        ("The unexamined life is not worth living.", "Socrates"),
        ("Be yourself; everyone else is already taken.", "Oscar Wilde"),
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
        ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
        ("First, solve the problem. Then, write the code.", "John Johnson"),
        ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
        ("In order to be irreplaceable, one must always be different.", "Coco Chanel"),
        ("Simplicity is the soul of efficiency.", "Austin Freeman"),
        ("Make it work, make it right, make it fast.", "Kent Beck"),
        ("The best error message is the one that never shows up.", "Thomas Fuchs"),
        ("Talk is cheap. Show me the code.", "Linus Torvalds"),
        ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
        ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
        ("Truth can only be found in one place: the code.", "Robert C. Martin"),
        ("Perfection is achieved not when there is nothing more to add, but when there is nothing more to take away.", "Antoine de Saint-Exupery"),
        ("Knowledge is power.", "Francis Bacon"),
        ("The only true wisdom is in knowing you know nothing.", "Socrates"),
        ("Fortune favors the bold.", "Virgil"),
        ("It is not the strongest of the species that survive, but the most adaptable.", "Charles Darwin"),

        # 21–40: Eastern / Islamicate / Indic philosophers and rulers
        ("He who conquers himself is the mightiest warrior.", "Chingiz Khan"),
        ("The greatest victory is the one that requires no battle.", "Timur"),
        ("Do not be content with small deeds; strive for greatness.", "Babur"),
        ("Knowledge is a treasure, but practice is the key to it.", "Al-Farabi"),
        ("Work for a cause, not for applause.", "Rumi"),
        ("The wise adapt themselves to circumstances, as water shapes itself to the vessel.", "Confucius"),
        ("A person who moves a mountain begins by carrying away small stones.", "Confucius"),
        ("Without effort, nothing grows but weeds.", "Gandhi"),
        ("Patience is bitter, but its fruit is sweet.", "Aristotle"),
        ("The harder the conflict, the greater the triumph.", "George Washington"),
        ("A journey of a thousand miles begins with a single step.", "Lao Tzu"),
        ("Do not seek to follow in the footsteps of the wise; seek what they sought.", "Matsuo Basho"),
        ("The wind and the waves are always on the side of the ablest navigator.", "Edward Gibbon"),
        ("Do not let what you cannot do interfere with what you can do.", "John Wooden"),
        ("Work hard in silence; let success make the noise.", "Frank Ocean"),
        ("Success is no accident. It is hard work, perseverance, learning, and love of what you are doing.", "Pelé"),
        ("Discipline is the bridge between goals and accomplishment.", "Jim Rohn"),
        ("Small deeds done are better than great deeds planned.", "Peter Marshall"),
        ("Do not be afraid to make mistakes; they are the stepping stones to mastery.", "Unknown"),
        ("He who is not courageous enough to take risks will accomplish nothing in life.", "Muhammad Ali"),

        # 41–60: Additional modern and philosophical quotes suitable for engineers
        ("Elegance is not a dispensable luxury but a quality that decides between success and failure.", "Edsger W. Dijkstra"),
        ("Programs are meant to be read by humans and only incidentally for computers to execute.", "Harold Abelson"),
        ("Debugging is like being the detective in a crime movie where you are also the murderer.", "Filipe Fortes"),
        ("Any sufficiently advanced technology is indistinguishable from magic.", "Arthur C. Clarke"),
        ("Simplicity is prerequisite for reliability.", "Edsger W. Dijkstra"),
        ("The function of good software is to make the complex appear simple.", "Grady Booch"),
        ("Perseverance is the hard work you do after you get tired of doing the hard work you already did.", "Newt Gingrich"),
        ("Do not pray for an easy life, pray for the strength to endure a difficult one.", "Bruce Lee"),
        ("Genius is one percent inspiration, ninety-nine percent perspiration.", "Thomas Edison"),
        ("Success is the sum of small efforts repeated day in and day out.", "Robert Collier"),
        ("Strive not to be a success, but rather to be of value.", "Albert Einstein"),
        ("The expert in anything was once a beginner.", "Helen Hayes"),
        ("Opportunities multiply as they are seized.", "Sun Tzu"),
        ("The best way to predict the future is to invent it.", "Alan Kay"),
        ("Great works are performed not by strength, but by perseverance.", "Samuel Johnson"),
        ("Vision without execution is hallucination.", "Thomas Edison"),
        ("Knowledge without practice is useless.", "Al-Ghazali"),
        ("A man who has committed a mistake and doesn’t correct it is committing another mistake.", "Confucius"),
        ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
        ("An investment in knowledge pays the best interest.", "Benjamin Franklin"),
        ("Mistakes are the portals of discovery.", "James Joyce"),
    ]

    return random.choice(quotes)


def update_readme(quote, author):
    """Update the README.md file with a new quote."""
    
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pattern to match the existing quote section
    quote_pattern = (
        r'(<div align="center" style="margin-bottom:30px; line-height:1\.5; max-width:650px;">'
        r'.*?<span style="font-size:20px; color:#FFD700; font-style:italic; margin:0 10px;">)'
        r'(.*?)'
        r'(</span>.*?<div style="margin-top:10px; font-size:16px; color:#FFD700; font-style:italic;">.*?– )'
        r'(.*?)'
        r'(</div>.*?</div>)'
    )
    
    # Replace with the new quote and author
    new_content = re.sub(
        quote_pattern,
        rf'\1{quote}\3{author}\5',
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Quote updated successfully!")
        print(f"New quote: '{quote}' – {author}")
    else:
        print("⚠️ No changes made to README.md")


if __name__ == "__main__":
    quote, author = get_random_quote()
    update_readme(quote, author)
