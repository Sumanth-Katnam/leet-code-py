import string

def read_redacted():
    redacted = open('d:/Work/redacted.txt', 'r')

    redacted_words = []
    word = ''
    for char in iter(lambda: redacted.read(1), ''):
        if char in [' ', '\n', '']:
            redacted_words.append(word.lower())
            word = ''
        else:
            word += char
    redacted_words.append(word.lower())
    return redacted_words

def redact_text(redacted_words):
    input_txt = open('d:/Work/actualText.txt', 'r')

    word = ''
    final_text = ''
    for char in iter(lambda: input_txt.read(1), ''):
        if char in [' ', '\n']:
            if word.lower() in redacted_words:
                final_text += '_REDACTED_' + char
            else:
                final_text += word + char

            word = ''
        else:
            if char not in string.punctuation:
                word += char
            

    if word in redacted_words:
        final_text += '_REDACTED_'
    else:
        final_text += word

    return final_text
    

if __name__ == '__main__':
    banned = read_redacted()
    print(banned)
    print(redact_text(banned))
