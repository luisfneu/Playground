def pattern_matcher(country):
    countries = ["Usa", "Brazil", "Spain", "Italy", "France", "Germany"]
    languages = ["English", "Portuguese", "Spanish", "Italian", "French", "German"]
    return languages[countries.index(country)]

print(pattern_matcher("Usa"))
print(pattern_matcher("France"))