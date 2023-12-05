**Name of Challenge:** RSA noob
**Points:** 60
**Category:** Cryptography

**Objective:** The objective of this challenge is to understand the vulnerability associated with using a small exponent (e) in RSA encryption.

**Solution:**
- In this challenge, you are given an RSA encryption with a small exponent (e = 1).
- In RSA encryption, the formula for encryption is typically expressed as: c = m^e MOD n, where 'c' is the ciphertext, 'm' is the plaintext, 'e' is the exponent, and 'n' is the modulus.
- With a small 'e' value, the original message can be easily decoded.
- In this scenario, you can perform the reverse operation of RSA to find the plaintext: m^e = tn + c, and m = inverse_root(tn + c, e), for some 't'.
- By incrementally trying different values of 't', you can essentially brute force your way to finding the flag.

Below is a Python script that demonstrates this approach:

```python
import gmpy2

n = 245841236512478852752909734912575581815967630033049838269083
e = 1
c = 9327565722767258308650643213344542404592011161659991421

for t in range(10):
    m, is_true_root = gmpy2.iroot(t * n + c, e)
    if is_true_root:
        print(f"Found, Iteration = {t}")
        print(m)
        print(f"Flag: {bytearray.fromhex(format(m, 'x')).decode()}")
        break
```

This script iterates through different values of 't', calculating 'm' using the RSA reverse operation. When it finds a valid root (i.e., 'is_true_root' is True), it prints the decrypted message, which is the flag.

**Flag:** CTFlearn{XXXXXXXXXX}

By solving this challenge, participants gain insights into the risks associated with using small exponents in RSA encryption and the importance of choosing strong cryptographic parameters.
