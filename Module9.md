# Prologue

- Digital Signature
- PKI, Identity-based Encryption

# Digital Signature
secure `Data integrity` and `Authenticity`

## Digital Signature vs MACs
MACs:
- A and B share a random key
- Triple $(Gen,Tag,Vrfy)$

Digital Signature
- Use SK to sign and PK to verify
- Triple $(KG,Sign,Vrfy)$
- Publicly Verifiable
- Signer can't deny
- Transferable

## Security

Extentially Unforgeable under CPA
Universal Forgeable
