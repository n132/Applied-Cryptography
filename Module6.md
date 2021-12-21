# Authenticated Encryption

- Gen({--n) Tag(k,m) Vrfy(k.m,t) 
- In previous -lectures, we learned how to protect the Confidentiality of the Message. In L- integrity(& authenticity) is the new goal. Detecting rather than provention.
- MA(MACs), (KG,E,D) vs. (Gen,Tag,Vrfy)→ key is not a secrecy.
- existentially unforgeable  
- Why encryption not enough(Some Symmetric Encryptions such as SE based on PRG and SE based on ECB)
- PRF → MAC(EU+CMA) ; How to extent? 
    - Some bad examples. Tag(k,(m-m-)==>
        - (F(k,m-,F(k,m-) → Get the Tag(k,(m-m-) from Tag(k, (m-m-)
        - (F(k,m- ^ F(k,m-) → Get Tag(k,(m-m-) from Tag(k, (m-m-)
        - (F(k,-m-,F(k,-m-)→ Get Tag(k,(m-) from Tag(k,(m-m-) 
        - (F(k,L|-m-,F(k,L|-m-) → Get Tag(k,(m-m-) from Tag(k,(m-m-) & Tag(k,(m-m-)
    - BC Modes(CBC, OFB, CTR) (length of output == input) → an improve → uses some mechanism like CBC to get a fixed-length output. 
- (Gen,H) collision-resistant hash functions, birthday attack, Merkle-Damgaard ((Gen,h)→(Gen,H)). MD-SHA-3
- CRH → MACS
    - fixedTag(k-H(k-m))
    - H(k|m)
    - H(k' xor opad | H( k' xor ipad | m))
- Application(Virus fingerprinting, Deduplication, File sharing, Merkle tree)
- IND-CCA-secure Encryption
    - KG'=(KG(),Gen())→ k-k2
    - Enc'(k-k-m)=( Enc(k- m)→ c-t=Tag(k- c-) → c
    - Dec'(k- k- c) = Vrfy(k-c-t)+ Dec(k-c-
-. Time stamp + session token (The final version)

- A useful but not "useful" skill — hybrid proof.
- some notation G() → RG(), R() or F()→ RF(),