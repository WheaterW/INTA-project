enrollment-request signature message-digest-method
==================================================

enrollment-request signature message-digest-method

Function
--------



The **enrollment-request signature message-digest-method** command sets the message digest method of signature for the enrollment request.

The **undo enrollment-request signature message-digest-method** command restores the default message digest method.



By default, the message digest method of signature for the enrollment request is sha-256.


Format
------

**enrollment-request signature message-digest-method** { **md5** | **sha1** | **sha-256** | **sha-384** | **sha-512** | **sm3** }

**undo enrollment-request signature message-digest-method**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Sets the digest method used for the enrollment request packet of signed certificate to MD5. | - |
| **sha1** | Sets the digest method used for the enrollment request packet of signed certificate to SHA1. | - |
| **sha-256** | Sets the digest method used for the enrollment request packet of signed certificate to SHA2-256. | - |
| **sha-384** | Sets the digest method used for the enrollment request packet of signed certificate to SHA2-384. | - |
| **sha-512** | Sets the digest method used for the enrollment request packet of signed certificate to SHA2-512. | - |
| **sm3** | Sets the digest method used for the enrollment request packet of signed certificate to SM3. | - |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The digest algorithm used on a PKI entity must be the same as that used on the CA server.The md5 and sha1 parameters in this command can be used only after the weak security algorithm/protocol feature package has been installed using the **install feature-software WEAKEA** command.In a specified PKI realm, when an SM2 key pair is used to apply for a certificate in offline mode, the digest algorithm used by signature certificate registration requests must be set to SM3. When an RSA key pair is used to apply for a certificate in offline mode, do not set the digest algorithm used by signature certificate registration requests to SM3. Otherwise, offline certificate application fails.


Example
-------

# Set the message-digest method of signature for enrollment request to be sha-384.
```
<HUAWEI> system-view
[~HUAWEI] pki realm e
[*HUAWEI-pki-realm-e] enrollment-request signature message-digest-method sha-384

```