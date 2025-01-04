def masterMind(guess, solution):
    hits, pseudohits = 0, 0
    solutionChars = {}
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            hits += 1
        else:
            if solution[i] not in solutionChars:
                solutionChars[solution[i]] = 0
            solutionChars[solution[i]] += 1
    for i in range(len(guess)):
        if guess[i] != solution[i] and guess[i] in solutionChars:
            pseudohits += 1
            solutionChars[guess[i]] -= 1
            if solutionChars[guess[i]] == 0:
                del solutionChars[guess[i]]
    return hits, pseudohits



guess =    ""
solution = "BRRY"
hits, pseudohits = masterMind(guess, solution)
print(hits, pseudohits)
