certificate load
================

certificate load

Function
--------



The **certificate load** command loads a certificate to an SSL policy.

The **undo certificate load** command unloads a certificate from an SSL policy.



By default, no certificates are loaded to SSL policies.


Format
------

**certificate load** { **pem-cert** | **pem-chain** } *certFile* **key-pair** *keyType* **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ]

**certificate load pfx-cert** *certFile* **key-pair** *keyType* **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ]

**certificate load pfx-cert** *certFile* **key-pair** *keyType* **mac** [ **cipher** *macCode* **auth-code** **cipher** *authCode* ]

**undo certificate load**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pem-cert** | Loads a PEM certificate to an SSL policy.  The PEM format is most commonly used.  The PEM format is applicable to text files transmitted between systems. | - |
| **pem-chain** | Loads a PEM certificate chain to an SSL policy. | - |
| *certFile* | Specifies the name of a certificate file.  This file must be saved in the security sub-directory of the system directory. | The value is a string of 1 to 64 characters.  The name of this file must be the same as that of the file to be uploaded.  If spaces are used, the string must start and end with double quotation marks (""). |
| **key-pair** *keyType* | Indicates the key pair type. | Enumerated type. The options are as follows:   * dsa: indicates that the key pair type is DSA. * rsa: indicates that the key pair type is RSA.   To ensure high security, do not use the RSA key pair whose length is less than 3072 bits. |
| **key-file** *keyFile* | Specifies the name of a key pair file.  This file must be saved in the security sub-directory of the system directory. | The value is a string of 1 to 64 characters.  The name of this file must be the same as that of the file to be uploaded.  If spaces are used, the string must start and end with double quotation marks (""). |
| **auth-code** | Specifies a PFX trusted-CA file. | - |
| **cipher** *authCode* | Specifies the authentication code of the key pair file.  The authentication code is used for identity authentication, ensuring that only authorized users can log in to a server. | The value is a string of characters that can be letters or digits. The password can be a string of 1 to 31 characters in cleartext or a string of 32 to 168 characters in ciphertext.  The characters do not include the question mark (?) or spaces. However, when double quotation marks ("") are used around a password, spaces are allowed in the password. |
| **cipher** *macCode* | Specifies the message authentication code. | The value is a string of case-sensitive characters that can be letters or digits. The password can be a string of 1 to 31 characters in cleartext or a string of 32 to 168 characters in ciphertext. |
| **pfx-cert** | Loads a PFX certificate to an SSL policy.  The PFX format is a universal digital certificate format. The file name extension of a PFX digital certificate is .pfx.  The PFX format is a binary format that can be converted into the PEM format. | - |
| **mac** | Specifies the message authentication code. | - |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

SSL provides the following security mechanisms:

* Data transmission privacy: Data to be transmitted is encrypted using symmetric cryptography.
* Message integrity: A MAC algorithm is used to verify message integrity during data transmission.
* Identify authentication: Digital-signed certificates are used for identity authentication.A digital certificate in the PEM or PFX format is issued by a Certificate Authority (CA). The digital certificate describes the identity of a digital user, helping establish a trusted relationship with the peer to meet high security requirements.The digital certificate includes information such as the name of a person or an organization that applies for the certificate, public key, digital-signed signature of the CA that issues the digital certificate, and validity period of the digital certificate. A CA can issue a certificate chain along with a digital certificate. After receiving a certificate chain, the receiver owns all the certificates on the chain.

**Prerequisites**

The **ssl policy** command has been used in the system view to create an SSL policy.

**Precautions**

* Only one certificate or certificate chain can be loaded to an SSL policy. Before loading a certificate or certificate chain, you must unload the existing certificate or certificate chain.
* For security purposes, after a certificate is loaded successfully, the system deletes the corresponding key pair file.
* If the PEM certificate loaded to an SSL policy is not in X.509v3 version, the system displays a message indicating risks and recommending X.509v3 digital certificates. You can also run the **display security risk feature ssl** command to view risk warning information.
* For TLS 1.3, an RSA certificate with the SHA-256 or a higher-version hash algorithm signature must be loaded.
* Associate the cipher suite list specified for an SSL policy with an SSL version:

1. The cipher suite list specified for the SSL policy cannot be empty and must contain at least one cipher suite.
2. If the cipher suite list specified for the SSL policy does not contain the TLS 1.3 cipher suite, the latest SSL version is set to TLS 1.2, that is, TLS 1.3 is disabled.
3. If the cipher suite list bound to an SSL policy does not contain TLS 1.1 or TLS 1.2 cipher suites, the earliest SSL version is set to TLS 1.3. That is, TLS 1.1 and TLS 1.2 are disabled.

* TLS 1.3 is incompatible with the DSA certificate. After this certificate is loaded, TLS 1.3 is disabled.
* TLS 1.3 is incompatible with the certificate whose signature algorithm is SHA1. After this certificate is loaded, TLS 1.3 is disabled.
* To properly use TLS 1.3, load an RSA certificate with the SHA-256 or a higher-version hash algorithm signature.
* If an RSA certificate is loaded to the SSL server, the cipher suite that uses the DSS certificate verification algorithm and is configured for the client does not take effect.
* If a DSA certificate is loaded to the SSL server, the cipher suite that uses the RSA certificate verification algorithm and is configured for the client does not take effect.
* To reduce security risks, you are advised to load the officially applied certificate and key pair.
* To ensure the integrity of the certificate chain, run the **certificate load pem-chain** command to load the certificate chain file.
* To enhance security, you are advised to use a certificate with higher security. The signature algorithm length of the RSA/DSA certificate is greater than or equal to 3072 bits, and the hash algorithm of the certificate is SHA-256 or later.
* If the signature algorithm length of the RSA/DSA certificate is fewer than 2048 bits or the hash algorithm of the certificate is SHA1, SHA-224, MD4, or MD5, you must run the **install feature-software WEAKEA** command.
* You cannot run the **certificate load** command to load an initial device certificate. If you need to use the initial device certificate, use the PKI realm mode.


Example
-------

# Load a PEM certificate to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] certificate load pem-cert servercert.pem key-pair dsa key-file serverkey.pem auth-code cipher YsHsjx_202206

```

# Load a PFX certificate to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] certificate load pfx-cert servercert.pfx key-pair rsa key-file serverkey.pfx auth-code cipher YsHsjx_202206

```

# Load a PEM certificate chain to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] certificate load pem-chain chain-servercert.pem key-pair rsa key-file chain-servercertkey.pem auth-code cipher YsHsjx_202206

```