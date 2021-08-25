### CrackHell
CrackHell is a fast hash cracker using [MD5Decrypt](https://md5decrypt.net/en/) API to crack hashes.

### Limitation
Currently CrackHell is limited to `MD5`, `SHA1`, `SHA256` and `SHA512` hash types. More hash types will be added as time progresses.

### Usage 
```
$ python3 crackHell.py -c <hash to crack> [-t <specify hash type>]
```
### Features 
1. Automaticaly identifies hash type if not specified explicitly.
2. Supports MD5, SHA1, SHA256 and SHA512.
3. Does not rely on dictionary based hash cracking attacks.
4. Comparitively fast.

### Disadvantages 
1. Limited functionality.
