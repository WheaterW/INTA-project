trusted-ca load
===============

trusted-ca load

Function
--------



The **trusted-ca load** command loads a trusted-CA file to a Secure Sockets Layer (SSL) policy.

The **undo trusted-ca load** command unloads a trusted-CA file from an SSL policy.



By default, no trusted-CA files are loaded to an SSL policy.


Format
------

**trusted-ca load** { **asn1-ca** | **pem-ca** } *caFile*

**trusted-ca load pfx-ca** *caFile* **auth-code** [ **cipher** *authCode* ]

**undo trusted-ca load** { **asn1-ca** | **pem-ca** | **pfx-ca** } *caFile*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **asn1-ca** | Specifies to load an ASN1 trusted-CA file to an SSL policy. | - |
| **pem-ca** | Specifies to load a PEM trusted-CA file to an SSL policy. | - |
| *caFile* | Specifies the name of a trusted-CA file.  This file must be saved in the security sub-directory of the system directory. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. |
| **pfx-ca** | Specifies to load a PFX trusted-CA file to an SSL policy. | - |
| **auth-code** | Specifies the authentication code of a PFX trusted-CA file. | - |
| **cipher** *authCode* | Specifies the authentication code of a PFX trusted-CA file.  The authentication code is used for identity authentication, ensuring that only authorized users can log in to the server. | The value is a string of case-sensitive characters that can be letters or digits. The password can be a string of 1 to 31 characters in simple text or a string of 32 to 168 characters in encrypted text.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

CAs are responsible for issuing digital certificates. The world-wide trusted CA is called a root CA. The root CA can authorize other CAs as subordinate CAs. The CA identity is described in a trusted-CA file. To ensure communications security, run the trusted-ca load command to load a trusted-CA file.

**Prerequisites**

The **ssl policy** command has been used in the system view to create an SSL policy.

**Configuration Impact**

If a user suffers a loss after the trusted-CA file is loaded, the user can use the file as evidence to seek legal actions against CA.

**Precautions**

* A maximum of four trusted-CA files can be loaded to an SSL policy.
* If the PEM trusted-CA file loaded to the SSL policy is not of the X.509v3 version, the system displays a message indicating risks. You are advised to use the X.509v3 CA certificate. You can also run the **display security risk feature ssl** command to view the risk information.
* To ensure high security, you are advised to use certificates with higher security. The signature algorithm length of the RSA/DSA certificate must be greater than or equal to 3072 bits, the signature algorithm length of the ECC certificate must be greater than or equal to 256 bits, and the hash algorithm of the certificate must be SHA-256 or later.
* If the signature algorithm length of the RSA/DSA certificate is less than 2048 bits, the signature algorithm length of the ECC certificate is less than 256 bits, or the hash algorithm of the certificate is SHA1, SHA-224, MD4, or MD5, run the **install feature-software WEAKEA** command.


Example
-------

# Load an ASN1 trusted-CA file to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] trusted-ca load asn1-ca servercert.der

```

# Load a PEM trusted-CA file to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] trusted-ca load pem-ca servercert.pem

```

# Load a PFX trusted-CA file to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] trusted-ca load pfx-ca servercert.pfx auth-code cipher YsHsjx_202206

```