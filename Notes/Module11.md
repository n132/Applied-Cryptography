# Prologue
Secure Communication
- TLS
- Entity Authentication
- Implementation
# TLS
- `asymmetric cryptography` to transfer the keys
- `certificates` for server authentification
- `symmetric encryption` for privacy
- `MACs` for message integraty

# Key Agreement Protocol

## Session Key generation

Alice and Bob share a long-term key already.

They could use the long-term key to generate session-key

with Hash functions, Timestamp amd random numbers.

## Key Agreement secure against eavesdroppers (Diff-Hellman)
1. Alice & Bob publicly agree on `g,p`
2. Alice send $g^x$ to Bob
3. Bob send $g^y$ to Alice
4. The symmetric key is $H(g^{x*y})$

- If CDH is hard, no efficient eavesdropper can compute K
- If DDH is hard, no efficient eavesdropper can compute any information about K
- If DL is easy, CDH and DDH is easy
  - if we could get $x$ from $g^x$, apparently DDH and CDH is easy
- If CDH is easy, DDH is easy 
  - if we could compute $g^{xy}$ from $g^x$ and $g^y$, apparently DDH is easy

## Authenticated Key Agreement with PKI (DH + Signature)
Similar to DH, but Alice and Bob use PKI to connect the PK and people's name.

And signature and verification are needed.

# IPSEC

- Transport Layer
- Build Tunnels between C/S 
- DH Key generation + Private-Key(AES CBC/GCM) + Authentication (SHA3) 
  - two keys are shared in DH, K1 for Private Key Encryption, K2 for Authentication

# Entity authentication

- User Authentication
  - Metigation of password-based authentication
  - Cryptographic protocols
- Serverr Authentication

## User Authentication

user proves he knows secret without revealing secret.
- One-time Password
  - Hash password bits, and sent the $t_{th}$ piece at time t.
- challenge-response
  - timestamp + random number + pseudo-random function   
- Zero-Knowledge Identification

# Server Authentication
The Server and the User are not equal, cuz server need to serve n users.
- Authentication by showing the certificate
- Authentication by showing easy-to-use secret

# Implementation
This topic is not hard and informational
- Key length
- Vul