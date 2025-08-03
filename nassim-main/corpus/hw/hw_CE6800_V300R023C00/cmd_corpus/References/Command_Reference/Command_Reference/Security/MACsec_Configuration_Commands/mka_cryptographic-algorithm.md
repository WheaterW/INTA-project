mka cryptographic-algorithm
===========================

mka cryptographic-algorithm

Function
--------



The **mka cryptographic-algorithm** command configures the MKA key generation algorithm.

The **undo mka cryptographic-algorithm** command restores the default MKA key generation algorithm.



By default, the MKA key generation algorithm is AES-CMAC-128.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**mka cryptographic-algorithm** { **aes-cmac-128** | **aes-cmac-256** }

**undo mka cryptographic-algorithm**

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**mka cryptographic-algorithm sm4-cmac-128**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **aes-cmac-128** | Sets the MKA key generation algorithm to AES-CMAC-128. | - |
| **aes-cmac-256** | Sets the MKA key generation algorithm to AES-CMAC-256. | - |
| **sm4-cmac-128** | Sets the MKA key generation algorithm to SM4-CMAC-128.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MKA key generation algorithm is used to generate the key encrypting key (KEK) for encrypting and decrypting the SAK and the integrity check key (ICK). After generating an SAK, the key server sends an MKA packet carrying the encrypted SAK to the peer device. After receiving the MKA packet, the peer device checks the integrity of the packet. If the check fails, the peer device discards the packet. If the check succeeds, the peer device decrypts the packet to obtain the SAK.

* When AES-CMAC-128 is used as the key generation algorithm, the first 32 hexadecimal digits of the CAK are used to generate the key. If the length of the configured CAK is less than 32 bits, 0s are suffixed to the CAK until the length reaches 32 bits.
* When AES-CMAC-256 is used as the key generation algorithm, the first 64 hexadecimal digits of the CAK are used to generate the key. If the length of the configured CAK is less than 64 bits, 0s are suffixed to the CAK until the length reaches 64 bits.
* When SM4-CMAC-128 is used as the key generation algorithm, the first 32 hexadecimal digits of the CAK are used to generate the key. If the length of the configured CAK is less than 32 bits, 0s are suffixed to the CAK until the length reaches 32 bits.

**Precautions**

* Ensure that the same key generation algorithm is configured on both ends. Otherwise, the negotiation may fail.
* If the algorithm is set to SM4-CMAC-128, the switch can only connect to Huawei CE switches that support Chinese cryptographic algorithms.
* The key generation algorithm SM4-CMAC-128 is used only with the GCM-SM4-128 encryption algorithm. Different AES algorithms are used together.

Example
-------

# Set the MKA key generation algorithm to AES-CMAC-256 in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] mka cryptographic-algorithm aes-cmac-256

```