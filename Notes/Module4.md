# Pseudo-Random & Symmetric Encryption

- Random source(no bias no correlation) is expensive so we need Pseudo-R & what's Pseudo-R in modern Crypto.
- What's IND and how can we say something satisfies it?
- R-Generator(1.statistical (IND)&pass next-bit tests 2. m≥n+1), and the second requirement result in we could expand Pseudo-randomness 
- Randomness ←→ Hardness (wooo, what a great finding! HC(x)+ F(x) == R(x)), so G could be used to implement a crypto scheme.
- PRF and PRG and PRP
  - differences on input & output
  - PRF to PRG and PRG to PRF
  - PRF to PRP (Feistel)
  - G(k) XOR m vs. (r,f(k,r) XOR m)
- Symmetric encryption (KG(r)→k, E(k,m)→c, D(k,c)→m) 
  - constructure
  - security notions(IND< IND-CPA< IND-CCA)
  - Symmetric Encryption satisfies IND