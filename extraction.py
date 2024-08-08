import pdfplumber

def extract_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return get_statistics(text)

async def get_statistics(text):
    word_count = 0
    current_word = ""
    word_usage = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char == " ":
            word_count += 1
            if current_word in word_usage:
                word_usage[current_word] += 1
            else:
                word_usage[current_word] = 1
            current_word = ""
        else:
            char = str(char)
            current_word += char
            if current_word.endswith("\n"):
                current_word = current_word[:-1]
            if "\n" in current_word:
                current_word = current_word[1:]


    return {
        "word_count": word_count,
        "word_usage": word_usage
    }