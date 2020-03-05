# ch3cksum
ch3cksum helps you to get files digests in order to compare them with a provided checksum.  
SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 supported as well as MD5 algorithm.  
Simple & based on hashlib.

Requires Python 3.8 (and the Assignment Expressions)  

### Usage
    $ python3 ch3cksum.py [-h] [-c CHECKSUM] {hash,compare} {md5,sha1,sha224,sha256,sha384,sha512} file
