class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            for char in string:
                encoded_string += chr(ord(char) + 3)
            encoded_string += chr(0)
        print(encoded_string)
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        decoded_str = ""
        for char in s:
            if char == chr(0):
                decoded_strs.append(decoded_str)
                decoded_str = ""
            else:
                decoded_str += chr(ord(char) - 3)
        return decoded_strs


