import spacy

nlp = spacy.load("en_core_web_sm")

def parse_command(text):
    doc = nlp(text)
    if "open" in text and "browser" in text:
        return "firefox"
    elif "list" in text and "files" in text:
        return "ls"
    elif "shutdown" in text:
        return "shutdown now"
    else:
        return None