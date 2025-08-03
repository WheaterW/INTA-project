password
========

password

Function
--------



The **password** command sets the challenge password used for certificate application , which is also used to revoke a certificate.

The **undo password** command deletes the challenge password used for certificate application.



By default, no challenge password is configured.


Format
------

**password cipher** [ *password* ]

**undo password**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cipher** *password* | Specifies the challenge password used for certificate application. The password is displayed in ciphertext. | The value is a string of case-sensitive characters. It cannot contain question marks (?). The password is in plaintext that contains 1 to 64 characters or in ciphertext that contains 128 to 188 characters.  To improve communication security, it is recommended that the certificate revocation password contains at least three types of lowercase letters, uppercase letters, numerals, and special characters, and contains at least eight characters. |



Views
-----

PKI domain view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When a PKI entity applies for a certificate from CA, CA needs to verify the challenge password of the entity. CA accepts the certificate application request only when the challenge password is correct. You need to run this command to set a challenge password for the PKI entity.The challenge password is also used to revoke a certificate. It avoids misoperations in certificate revocation.

If you directly configure a challenge password when running the **password cipher** command, you do not need to enter the password again. If you do not configure a challenge password when running this command, you need to enter a challenge password twice.


Example
-------

# Set the challenge password used to apply for certificate.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] password cipher YsHsjx_202206
[*HUAWEI-pki-realm-abc] quit
[~HUAWEI] pki realm efg
[*HUAWEI-pki-realm-efg] password cipher
 Please enter the password:
 Please enter the password again:
[*HUAWEI-pki-realm-efg]

```