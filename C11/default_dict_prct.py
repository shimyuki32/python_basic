from collections import defaultdict
def no_idea():
    return "Huh?"

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'

print(bestiary)

print(bestiary['C'])
print(bestiary)