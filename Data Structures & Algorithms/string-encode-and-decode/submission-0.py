class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded = encoded + str(length) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        while index < len(s):
            hash_pos = index
            while s[hash_pos] != "#":
                hash_pos += 1
            length = int(s[index:hash_pos])
            word_start = hash_pos + 1
            word_end = word_start + length
            word = s[word_start:word_end]
            decoded.append(word)
            index = word_end
        return decoded
