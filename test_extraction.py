from extraction import get_statistics

text = "I want this to count the words \n I use and this needs to work"
expected_word_count = 14

content = get_statistics(text)

print(content["word_count"])
print(content["word_usage"])
if expected_word_count == content["word_count"]:
    print("success")