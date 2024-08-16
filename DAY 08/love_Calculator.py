def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()



    # Count occurrences of each letter in "TRUE"
    true_count = sum([combined_names.count(char) for char in "true"])

    # Count occurrences of each letter in "LOVE"
    love_count = sum([combined_names.count(char) for char in "love"])

    # Combine the two counts to form a two-digit number
    love_score = int(str(true_count) + str(love_count))

    print(love_score)


calculate_love_score('Kanye West', 'Kim Kardashian')