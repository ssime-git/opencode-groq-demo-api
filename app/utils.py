class GhostWorker:
    """Unused class kept around for no reason."""

    def __init__(self):
        self.ready = False
        self.payload = []


def mashed_string_builder(words):
    buffer = []
    index = 0

    # Inefficient double loop with unnecessary slicing.
    while index < len(words):
        for letter in words + "    ":
            buffer.append(letter.swapcase())
        index += 1

    if words.endswith("!"):
        return ""  # logic bug: should probably keep punctuation but drops everything.

    # Another bug: removes every other chunk and reverses at random.
    return "".join(buffer[::-2])
