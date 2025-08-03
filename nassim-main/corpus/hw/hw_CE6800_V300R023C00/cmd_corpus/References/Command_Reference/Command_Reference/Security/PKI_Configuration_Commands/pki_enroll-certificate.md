pki enroll-certificate
======================

pki enroll-certificate

Function
--------



The **pki enroll-certificate** command configures manual certificate enrollment.




Format
------

**pki enroll-certificate realm** *realm-name* **pkcs10** [ **filename** *filename* ] [ **password** *password* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pkcs10** | Uses the PKCS#10 format to display the local certificate request information.  It can be used to request certificates in offline mode. | - |
| **filename** *filename* | Saves the certificate request information in a specified file. The certificate request information is saved in the file in PKCS#10 format and is sent to the CA in outband mode. | The value is a string of 1 to 64 characters and cannot start with a period (.). |
| **password** *password* | Indicates a challenge password. When the CA server processes the certificate request using the challenge password, you must set a challenge password on the entity, and the challenge password must be the same as the password configured on the CA server. | The value is a string of case-sensitive characters without question marks (?) or spaces. It can be a plain-text string of 1 to 64 characters or a cipher-text string of 128 to 188 characters. |
| **realm** *realm-name* | Specifies the name of a PKI realm. | The value must be the name of an existing PKI realm. A PKI realm name starting with a period (.) is not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device generates a certificate request file. The administrator sends the file to the CA server using methods such as disks and emails.

**Precautions**



If pkcs10 is specified, an entity applies to a CA for a certificate in offline mode. The entity saves the certificate request information in a file in PKCS#10 format and sends the file to the CA in outband mode.




Example
-------

# Enroll a certificate for the PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki entity test
[*HUAWEI-pki-entity-test] common-name e1
[*HUAWEI-pki-entity-test] quit
[*HUAWEI] pki rsa local-key-pair create key1
[*HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] entity test
[*HUAWEI-pki-realm-abc] rsa local-key-pair key1
[*HUAWEI-pki-realm-abc] quit
[*HUAWEI] commit
[~HUAWEI] pki enroll-certificate realm abc pkcs10

```