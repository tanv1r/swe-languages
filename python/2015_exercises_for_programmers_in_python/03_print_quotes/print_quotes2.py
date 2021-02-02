quotes_and_names = {
    """These aren't the droids you're looking for.""": 'Obi-Wan Kenobi',
    """Life is like riding a bicycle.""": 'Albert Einstein',
    """Don't fool yourself. You're the easiest person to fool.""": 'Richard Feynman'
}

for q, n in quotes_and_names.items():
    print(n + " says, " + str('"') + q + str('"'))