import unittest
from convert import encode, decode, flatten, parse


class TestEncodeDecode(unittest.TestCase):

    def test_flatten(self):
        unflatt1 = ['apple', '1', 'banana', '2']
        unflatt2 = ['dog', '3', 'cat', '7', 'monkey', '4']
        self.assertEqual(flatten(unflatt1), "apple1banana2")
        self.assertEqual(flatten(unflatt2), "dog3cat7monkey4")

    def test_encode(self):
        raw = "                                ,#@',,,,,,,,,,,,+@+,"
        self.assertEqual(flatten(encode(raw)), "32 1,1#1@1'12,1+1@1+1,")

    def test_parse(self):
        unparsed = "38 1,1#4@1+1,1"
        self.assertEqual(parse(unparsed),
        [[38, ' '], [1, ','], [1, '#'], [4, '@'], [1, '+'], [1, ','], ''])

    def test_decode(self):
        encoded = "37 1,1#1@1'2,1+1@1+1,1"
        self.assertEqual(decode(parse(encoded)),
        "                                     ,#@',,+@+,")

    def test_encode_and_decode(self):
        raw = "                                ,#@',,,,,,,,,,,,+@+,"
        encoded = flatten(encode(raw))
        decoded = decode(parse(encoded))
        self.assertEqual(raw, decoded)


if __name__ == '__main__':
    unittest.main()
