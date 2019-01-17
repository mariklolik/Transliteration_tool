g = {"А": "A",
     "Б": "B",
     "В": "V",
     "Г": "G",
     "Д": "D",
     "Е": "E",
     "Ё": "E",
     "Ж": "Zh",
     "З": "Z",
     "И": "I",
     "Й": "I",
     "К": "K",
     "Л": "L",
     "М": "M",
     "Н": "N",
     "О": "O",
     "П": "P",
     "Р": "R",
     "С": "S",
     "Т": "T",
     "У": "U",
     "Ф": "F",
     "Х": "Kh",
     "Ц": "Tc",
     "Ч": "Ch",
     "Ш": "Sh",
     "Щ": "Shch",
     "Ы": "Y",
     "Ь": "'",
     "Э": "E",
     "Ю": "Iu",
     "Ву": "W",
     " ": " ",
     "Я": "Ia"}
g2 = {}
for value, g in g.items():
    g2[g] = value
a = input()
k = ""
f = ["ь", "ъ", "Ъ", "Ь"]
for i in a:
    if i.upper() in g:
        if i.upper() in g:
            if i.upper() != i:
                k += g[i.upper()].lower()
            else:
                k += g[i]
    elif i.upper() in g2:
        if i.upper() != i:
            k += g2[i.upper()].lower()
        else:
            k += g2[i]
    else:
        k += i
print(k)