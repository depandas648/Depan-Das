# ───────────── String Operations Program ─────────────

# Original string
text = "HTML stands for hyper text markup language?"

print("Original String:")
print(f'"{text}"')
print("\n───────────── Results ─────────────")

# a) Length of the string
length = len(text)
print(f"a) Length of the string         : {length}")

# b) Word count of the string
word_count = len(text.split())
print(f"b) Word count                  : {word_count}")

# c) Reverse the string
reversed_string = text[::-1]
print(f"c) Reversed string             : \"{reversed_string}\"")

# d) Position of the word "Hyper"
position = text.lower().find("hyper")
if position != -1:
    print(f"d) Position of the word 'Hyper': {position}")
else:
    print("d) Word 'Hyper' not found in the string.")

# e) Replace "Text" with "Media"
replaced_string = text.replace("text", "Media")
print(f"e) Modified string             : \"{replaced_string}\"")

print("────────────────────────────────────────────") 