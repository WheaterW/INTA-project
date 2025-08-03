Cryptography
============

Cryptography is the basis for secure information transmission on networks. It relies on mathematical techniques to transform cleartext into unreadable ciphertext, ensuring the integrity and confidentiality of communication. Encryption algorithms are classified into reversible encryption algorithms and irreversible encryption algorithms. Reversible encryption algorithms are further classified into symmetric encryption algorithms and asymmetric encryption algorithms.

#### Irreversible Encryption

Irreversible encryption is usually used as the basis of encryption to generate a message digest. Irreversible encryption compares two encrypted ciphertexts to check whether data is modified during transmission. The original non-cipher text information cannot be inferred from the ciphertext. Common irreversible encryption algorithms include Message Digest algorithm 5 (MD5), secure hash algorithm (SHA), and Hash-based Message Authentication Code (HMAC) that requires a key. SHA includes SHA1, SHA256, and SHA512.


#### Symmetric Key Cryptography

Symmetric key cryptography, also known as shared key cryptography, utilizes the same key to encrypt and decrypt data. It includes stream ciphers and block ciphers.

[Figure 1](#EN-US_CONCEPT_0000001564006245__fig_dc_fd_pki_000501) shows the symmetric key encryption and decryption process.

**Figure 1** Symmetric key encryption and decryption process  
![](figure/en-us_image_0000001564006289.png)
Users A and B have negotiated the symmetric key. The encryption and decryption process is as follows:

1. User A uses the symmetric key to encrypt data and sends the encrypted data to user B.
2. User B decrypts the data using the symmetric key and gets the original data.
   
   Symmetric key cryptography features high efficiency, simple algorithm, and low cost. It is suitable for encrypting a large amount of data. However, it is difficult to implement because the two parties must exchange their keys securely before communication. Besides, it is difficult to expand because each pair of communicating parties needs to negotiate keys, and n users need to negotiate n x (n â 1)/2 different keys.

The algorithms commonly used in symmetric key cryptography include Data Encryption Standard (DES), Triple Data Encryption Standard (3DES), and Advanced Encryption Standard (AES). These algorithms are block cryptographic algorithms.


#### Public Key Cryptography

Public key cryptography, also known as asymmetric key cryptography, employs a pair of different keys â a public key and a private key â for data encryption and decryption. The public key is freely accessible, whereas the private key is kept confidential by its sole owner.

Public key cryptography mitigates the security risks associated with sharing and managing a symmetric key between parties. In an asymmetric key pair, the public key is used to encrypt data and the private key is used to decrypt data. The sender uses the public key of the receiver to encrypt the data, and the receiver uses its own private key to decrypt data. The receiver's private key is only known by the receiver, so the data is secure.

[Figure 2](#EN-US_CONCEPT_0000001564006245__fig_dc_fd_pki_000502) shows the public key encryption and decryption process.

**Figure 2** Public key encryption and decryption process  
![](figure/en-us_image_0000001513166026.png)
Assume that user A has the public key of user B. The encryption and decryption process is as follows:

1. User A uses the public key of user B to encrypt data and sends the encrypted data to user B.
2. User B decrypts the data using its own private key and gets the original data.

Attackers cannot use one key in a key pair to figure out the other key. The data encrypted by a public key can only be decrypted by the private key of the same user. However, the public key cryptography requires a long time to encrypt a large amount of data, and the encrypted data is too long, consuming much bandwidth.

Public key cryptography is suitable for encrypting sensitive information such as keys and identities to provide higher security.

The algorithms commonly used in public key cryptography include Diffie-Hellman (DH), Ron Rivest, Adi Shamirh, LenAdleman (RSA), Digital Signature Algorithm (DSA),.


#### Chinese Cryptographic Algorithms

Chinese cryptographic algorithms refer to the commercial cryptography approved by China's State Cryptography Administration and are used to encrypt information that does not involve state secrets. To ensure the security of commercial cryptography, China has formulated a series of cryptographic standards, including symmetric encryption algorithms, elliptic curve asymmetric encryption algorithms, and hash algorithms. The following table lists the algorithms contained in the Chinese cryptographic algorithm suite. The SM2, SM3, and SM4 algorithms are mainly used in PKI.

**Table 1** Overview of the Chinese cryptographic algorithm suite
| Algorithm | Type | Function | Corresponding International Algorithm | Disclosed or Not |
| --- | --- | --- | --- | --- |
| SM1 | Symmetric encryption | Block cipher algorithm | AES128 | No, it exists in the hardware only in the form of an IP core. |
| SM2 | Elliptic curve asymmetric cryptography | ECC encryption and decryption, signature verification, and key exchange | RSA, ECC | Yes, it has been incorporated into ISO international standards. |
| SM3 | Hashing | Digital signature and verification in commercial cryptography applications, generation and verification of message authentication codes, and generation of random numbers | SHA-256 | Yes, it has been incorporated into ISO international standards. |
| SM4 | Block cipher | Block encryption and decryption. The structure about encryption and decryption is same. The only difference is that the decryption key is the reverse of the encryption key. | DES, AES | Yes |
| SM7 | Block cipher | Block cipher and decipher | - | No, it exists in the hardware only in the form of an IP core. |
| SM9 | ID-based asymmetric cryptography | Signature verification, key exchange, as well as key encapsulation, encryption, and decryption | - | Yes, it has been incorporated into ISO international standards. |
| ZUC | Stream cipher | ZUC stream cipher algorithm and symmetric encryption algorithm | EEA3 & EIA3 | Yes |
| SSF33 | Block cipher | Block cipher and decipher | - | No |