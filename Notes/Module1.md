# Classical Cryptography

- Some basics of algorithm and probability and classical crypto(all of them have very limited secrecy).
  - rot13 - algorithm is a secrecy
  - shift - small key space
  - mono alphabetic substitution cipher - key space = 26!  
  - poly alphabetic substitution cipher - key space = 26**len(key)
- Perfect secrecy (p[m]=p[m|c]) & one time pad
  - p[Gen return every key] = 1/|k|
  - for every m and c, there exists one k enc(c,k)==m
- We need more effective encryption scheme in modern cryptography. so these schemes do not satisfies PS.
- Shannon (prove if a scheme satisfies PC).