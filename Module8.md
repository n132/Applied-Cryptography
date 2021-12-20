# Prologue

We have learned Asymmetric Encryption in RSA part. This module would go through RSA and El-Gamal.

# Hybrid Encryption
runtime efficiency + reduced interaction  == Private-Key Encryption+ Public-Key Encryption

## Scheme
aES means asymmetric encryption and sES means symmetric encryption

---
$aES=((aKG,aE,aD),sES=(sKG,sE,sD)$

KG: $aKG\rightarrow(PK,SK)$

E: $(c1,c2): randomGen()\rightarrow k, c1=aE(PK,k), c2=sE(k,m)$

D: $k=aD(SK,c1),m'=sD(k,c2)$

---

## Security

> If aES satisfies IND-CPA-security and sES satisfies IND-security then ES satisfies IND-CPA-security

> if aES satisfies IND-CCA-security and sES is IND-CCA-security then ES satisfies IND-CCA-security