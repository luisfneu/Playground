def matcher(country):
    data = [("Usa", "English"), ("Brazil", "Portuguese"), ("Spain", "Spanish"),
            ("Italy", "Italian"), ("France", "French"), ("Germany", "German")]
    return [lang for c, lang in data if c == country][0]
print(matcher("Brazil"))
print(matcher("Spain"))
print(matcher("Italy"))
print(matcher("Germany"))