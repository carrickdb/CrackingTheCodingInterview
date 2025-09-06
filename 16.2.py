from collections import defaultdict

class Counts:
    def __init__(self, book):
        self.counts = defaultdict(int)
        tokens = book.split()
        for t in tokens:
            self.counts[t] += 1

    def get_count(self, token):
        return self.counts[token]


book = """I'm 'Enery the Eighth, I am,
'Enery the Eighth I am, I am!
I got married to the widow next door,
She's been married seven times before
And every one was an 'Enery
She wouldn't have a Willie nor a Sam
I'm her eighth old man named 'Enery
'Enery the Eighth, I am!"""

counts = Counts(book)

print(counts.get_count("'Enery"))
print(counts.get_count("am!"))