## ASCII Art Encoder/Decoder

## Requirement
- Python 3


## Running
**Encoding**
```
python convert.py --encode data.txt
```
**Decoding**
```
python convert.py --decode encoded_data.txt
```

## Result
```
5.4K Sep 15  2016 data.txt
2.3K Feb  2 01:18 encoded_data.txt
5.4K Feb  2 01:18 decoded_data.txt
```
42.6% of the original size.

## Running tests
```
python test.py
```
or you can run both encode and decode, then run the following command:
```
diff data.txt decoded_data.txt
```


