import re

safe = "abcdefghijklmnopqrstuvwxyz01234567890-_ .,"
tomap = (
    "éàèùçâêîôûëïüąćęłńóśźżříšžčýůňúěďáéäüößœ",
    (*"eaeucaeioueiuacelnoszzriszcyunuedae", "ae", "ue", "oe", "ss", "oe"),
)
map = {
    **{c: c for c in safe + safe.upper()},
    **{s: d for (s, d) in zip(*tomap)},
    **{s.upper(): d.upper() for (s, d) in zip(*tomap)},
}


def sanitize(s):
    return re.sub("_+", "_", "".join([map[c] if c in map else "_" for c in s]))

def remove_emoji(s):
    def remove_emoji(s):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', s)

if __name__ == "__main__":

    def test(s):
        print(f"{s} --> {sanitize(s)}")
        print(f"{s.upper()} --> {sanitize(s.upper())}")

    test("Pójdźże, kiń tę chmurność w głąb flaszy!")
    test("Příliš žluťoučký kůň úpěl ďábelské ódy")
    test("Fix, Schwyz! quäkt Jürgen blöd vom Paß")
    test("HellOO 😂🤣--😍🥰 there, you!.md")
    test("Voix ambiguë d’un cœur qui au zéphyr préfère les jattes de kiwis")
