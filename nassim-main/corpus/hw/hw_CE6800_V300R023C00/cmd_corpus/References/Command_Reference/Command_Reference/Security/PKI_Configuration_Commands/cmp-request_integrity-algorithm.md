cmp-request integrity-algorithm
===============================

cmp-request integrity-algorithm

Function
--------



The **cmp-request integrity-algorithm** command configures an encryption algorithm used for CMPv2-based certificate application.

The **undo cmp-request integrity-algorithm** command restores the default encryption algorithm for CMPv2-based certificate application.



By default, the encryption algorithm SHA256 is used when CMPv2 is used to apply for a certificate.


Format
------

**cmp-request integrity-algorithm** { **hmac-sha256** | **hmac-sha1** }

**undo cmp-request integrity-algorithm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hmac-sha256** | Specifies the device to use the SHA256 algorithm for encryption when applying for a certificate in CMPv2 mode. | - |
| **hmac-sha1** | Specifies the device to use the SHA1 algorithm for encryption when applying for a certificate in CMPv2 mode. | - |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When CMPv2 is used to apply for a certificate, packets need to be encrypted using the hash algorithm. Use either of the following methods:

* If the SHA256 mode is used, the device uses the SHA256 algorithm to encrypt packets during certificate application.
* If the SHA1 mode is used, the device uses the SHA1 algorithm to encrypt packets during certificate application.The hmac-sha1 parameter can be used only after the weak security algorithm/protocol feature package has been installed using the **install feature-software WEAKEA** command.

Example
-------

# Set the encryption mode of CMPv2-based certificate application packets to SHA1.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request integrity-algorithm hmac-sha256

```