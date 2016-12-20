import re, sys

at_mention = r"@[A-Za-z_0-9]+"
hashtag = r"\#[A-Za-z_0-9]+"
url = r"https?://[A-Za-z]+\.co/[A-Za-z0-9]+"
punctuation = r"[?\.!,;\"\']+"
words = r"[A-Za-z\-]+"
# dot = u"\u2026"

tired_face = r"😭"


def tokenize(file_name):
    corpus = []

    token_regex = re.compile(at_mention + '|' + hashtag + '|' + url + '|' +
                             punctuation + '|' + words)

    with open(file_name) as f:
        for i, line in enumerate(f):
            tokens = token_regex.findall(line)

            corpus.extend(tokens)

    corpus.sort()
    return corpus


if __name__ == '__main__':
    corpus = tokenize("tweets.en.txt")
    vocab = {}
    for word in corpus:
        try:
            vocab[word.lower()] += 1
        except KeyError:
            vocab[word.lower()] = 1
    print(len(corpus))
    print(len(vocab))
    print(vocab['rt'])
