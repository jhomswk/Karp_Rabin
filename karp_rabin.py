
class Rolling_Hash:
    """
    Rolling-Hash data structure.
    Maintains the hash value of a string as seen from
    a sliding window.
    """

    def __init__(self, base, prime):
        """
        Generates an empty rolling hash where strings 
        are represented as multi-digit numbers using
        the given base. The hash-function used is
        h(x) = x mod prime.
        """
        self.base = base
        self.prime = prime
        self.base_inverse = pow(base, prime-2, prime)
        self.magic = 1
        self.hash = 0


    def append(self, new):
        """
        Generates the hash value obtained after appending
        the new character to the current internal string.
        """
        self.hash = (self.hash*self.base + ord(new)) % self.prime
        self.magic = (self.magic*self.base) % self.prime


    def remove(self, old):
        """
        Generates the hash value obtained after removing
        the first character from the current internal
        string.
        """
        self.magic = (self.magic*self.base_inverse) % self.prime
        self.hash = (self.hash - ord(old)*self.magic) % self.prime


    def slide(self, old, new):
        """
        Generates the hash value obtained after sliding the
        window one step to the left, removing the previous
        first character and appending a new last character
        to the current internal string.
        """
        self.hash = (self.hash*self.base - ord(old)*self.magic + ord(new)) % self.prime


def karp_rabin(s, t, p=257):
    """
    Applies Karp-Rabin to check whether string s is
    contained into text t.
    """
    rhs = Rolling_Hash(256, p)
    rht = Rolling_Hash(256, p)

    for i in range(len(s)):
        rhs.append(s[i])
        rht.append(t[i])

    if rhs.hash == rht.hash and s == t[:len(s)]:
        return True

    for i in range(len(s), len(t)):
        rht.slide(t[i-len(s)], t[i])

        if rhs.hash == rht.hash and s == t[i-len(s)+1:i+1]:
            return True

    return False

