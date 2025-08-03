signature algorithm-list
========================

signature algorithm-list

Function
--------



The **signature algorithm-list** command sets the signature algorithms supported during SSL handshakes.

The **undo signature algorithm-list** command restores the default signature algorithms supported during SSL handshakes.



By default, the signature algorithms are ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384 and rsa-pss-rsae-sha512.


Format
------

**signature algorithm-list** { **ecdsa-secp256r1-sha256** | **ecdsa-secp384r1-sha384** | **ecdsa-secp521r1-sha512** | **ed25519** | **ed448** | **rsa-pss-pss-sha256** | **rsa-pss-pss-sha384** | **rsa-pss-pss-sha512** | **rsa-pss-rsae-sha256** | **rsa-pss-rsae-sha384** | **rsa-pss-rsae-sha512** | **rsa-pkcs1-sha256** | **rsa-pkcs1-sha384** | **rsa-pkcs1-sha512** | **ecdsa-sha1** | **ecdsa-sha224** | **rsa-sha1** | **rsa-sha224** | **dsa-sha1** | **dsa-sha224** | **dsa-sha256** | **dsa-sha384** | **dsa-sha512** } \*

**undo signature algorithm-list**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ecdsa-secp256r1-sha256** | Indicates the ecdsa-secp256r1-sha256 algorithm. | - |
| **ecdsa-secp384r1-sha384** | Indicates the ecdsa-secp384r1-sha384 algorithm. | - |
| **ecdsa-secp521r1-sha512** | Indicates the ecdsa-secp521r1-sha512 algorithm. | - |
| **ed25519** | Indicates the ed25519 algorithm. | - |
| **ed448** | Indicates the ed448 algorithm. | - |
| **rsa-pss-pss-sha256** | Indicates the rsa-pss-pss-sha256 algorithm. | - |
| **rsa-pss-pss-sha384** | Indicates the rsa-pss-pss-sha384 algorithm. | - |
| **rsa-pss-pss-sha512** | Indicates the rsa-pss-pss-sha512 algorithm. | - |
| **rsa-pss-rsae-sha256** | Indicates the rsa-pss-rsae-sha256 algorithm. | - |
| **rsa-pss-rsae-sha384** | Indicates the rsa-pss-rsae-sha384 algorithm. | - |
| **rsa-pss-rsae-sha512** | Indicates the rsa-pss-rsae-sha512 algorithm. | - |
| **rsa-pkcs1-sha256** | Indicates the rsa-pkcs1-sha256 algorithm. | - |
| **rsa-pkcs1-sha384** | Indicates the rsa-pkcs1-sha384 algorithm. | - |
| **rsa-pkcs1-sha512** | Indicates the rsa-pkcs1-sha512 algorithm. | - |
| **ecdsa-sha1** | Indicates the ecdsa-sha1 algorithm. | - |
| **ecdsa-sha224** | Indicates the ecdsa-sha224 algorithm. | - |
| **rsa-sha1** | Indicates the rsa-sha1 algorithm. | - |
| **rsa-sha224** | Indicates the rsa-sha224 algorithm. | - |
| **dsa-sha1** | Indicates the dsa-sha1 algorithm. | - |
| **dsa-sha224** | Indicates the dsa-sha224 algorithm. | - |
| **dsa-sha256** | Indicates the dsa-sha256 algorithm. | - |
| **dsa-sha384** | Indicates the dsa-sha384 algorithm. | - |
| **dsa-sha512** | Indicates the dsa-sha512 algorithm. | - |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command can set the SSL signature algorithm.For better security, signature algorithms ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384, and rsa-pss-rsae-sha512 algorithms are recommended.

**Precautions**



The dsa-sha1, dsa-sha224, dsa-sha256, dsa-sha384, dsa-sha512, ecdsa-sha1, ecdsa-sha224, rsa-sha1 and rsa-sha224 parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.




Example
-------

# Set the SSL signature algorithm.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy a
[~HUAWEI-ssl-policy-a] signature algorithm-list ed25519 ed448

```