COLOR = True
def BLUE(): return '\033[94m' if COLOR else ""
def RESET(): return '\033[0m' if COLOR else ""
def BLUEBG(): return '\033[44m' if COLOR else ""


class Bit:
    def __init__(self, value):
        if not (value == 1 or value == 0):
            raise ValueError("bit value can only by 1 || 0")
        self.value = bool(value)

    def set(self, value):
        if not (value == 1 or value == 0):
            raise ValueError("bit value can only by 1 || 0")
        self.value = bool(value)

    def __bool__(self):
        return self.value

    def __invert__(self):
        return Bit(not self.value)

    def __repr__(self):
        return str(int(self.value))

    def __str__(self):
        return str(int(self.value))

    def __or__(self, obj2):
        if self.value or obj2.value:
            return (Bit(1))
        else:
            return (Bit(0))

    def __and__(self, obj2):
        if self.value and obj2.value:
            return (Bit(1))
        else:
            return (Bit(0))

    def __eq__(self, obj2):
        if self.value == obj2:
            return Bit(1)
        else:
            return Bit(0)

    def __ne__(self, obj2):
        if self.value != obj2.value:
            return Bit(1)
        else:
            return Bit(0)

    def flip(self):
        self.value = not self.value


def bstr2BitList(s):
    return [Bit(int(c)) for c in s]


def _kmapcoord(bits: Bit) -> int:
    if (~bits[0]) & (~bits[1]):
        return 0
    if (~bits[0]) & (bits[1]):
        return 1
    if (bits[0]) & (bits[1]):
        return 2
    if (bits[0]) & (~bits[1]):
        return 3


class kmap4():
    def __init__(self, bitListList: [[Bit]]):
        """
        Makes a 4x4 Karnaugh map from an arry: [ [bit] ]
        """

        self.kmap = [[Bit(0) for i in range(4)] for j in range(4)]
        for bits in bitListList:
            if len(bits) != 4:
                raise TypeError("kmap4: bitmatrix item's length != 4")

        for bits in bitListList:
            dc = bits[0:2]
            ba = bits[2:4]
            self.kmap[_kmapcoord(ba)][_kmapcoord(dc)] = Bit(1)

    def __repr__(self):
        labels = ["00", "01", "11", "10"]
        return "⟍ DC\n" + "BA⟍ " + " ".join(labels) + "\n" + "\n".join(
            ["  " + labels[i] + " " + "  ".join([(BLUE() if COLOR() and b else "") + str(b) + (
                RESET() if COLOR() else "") for b in row]) for i, row in enumerate(self.kmap)]
        )

def write_bin_file_from_hex_string(fname, hex_string):
    """
    @param hexString: String of 2-digit hex numbers, separated by commas
                      (can have spaces, tabs and newlines)
    """
    with open(fname, "wb") as bf:
        byte_array = bytearray(
            hex_string.split(",").map(lambda x: x.strip()).filter(
                lambda x: x).map(lambda x: int(x, 16))
        )
        bf.write(byte_array)
    with open(fname, "rb") as bf:
        hex_line = bf.read().hex()
        for line in [hex_line[i:i+32] for i in range(0, len(hex_line), 32)]:
            print(*[line[i:i+2] for i in range(0, len(line), 2)])
