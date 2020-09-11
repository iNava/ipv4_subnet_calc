import re
from ipaddress import IPv4Address

#  https://realpython.com/python-ipaddress-module/
class MyIPv4(IPv4Address):
    @property
    def binary_repr(self, sep=".") -> str:
        """Represent IPv4 as 4 blocks of 8 bits."""
        return sep.join(f"{i:08b}" for i in self.packed)

    @property
    def hexd_repr(self) -> str:
        def int_to_hex(nr):
            h = format(int(nr), 'x')
            return '0' + h if len(h) % 2 else h

        """Represent IPv4 as Hexadecimal."""
        # return sep.join(hex(i) for i in self.packed)
        return ''.join(int_to_hex(i).upper() for i in self.packed)

    @classmethod
    def from_binary_repr(cls, binary_repr: str):
        """Construct IPv4 from binary representation."""
        # Remove anything that's not a 0 or 1
        i = int(re.sub(r"[^01]", "", binary_repr), 2)
        return cls(i)
