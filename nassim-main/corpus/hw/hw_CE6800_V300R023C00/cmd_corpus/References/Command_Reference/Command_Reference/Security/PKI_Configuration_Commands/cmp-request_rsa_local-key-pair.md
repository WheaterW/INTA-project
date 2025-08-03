cmp-request rsa local-key-pair
==============================

cmp-request rsa local-key-pair

Function
--------



The **cmp-request rsa local-key-pair** command configures the RSA key pair used for certificate application through CMPv2.

The **undo cmp-request rsa local-key-pair** command deletes the RSA key pair used for certificate application through CMPv2.



By default, the RSA key pair used to apply for certificate through CMPv2 is not configured.


Format
------

**cmp-request rsa local-key-pair** *key-name* [ **regenerate** [ *key-bit* ] ]

**undo cmp-request rsa local-key-pair**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the RSA key pair. | The value is a string of 1 to 64 case-sensitive characters. |
| **regenerate** | Indicates that the RSA key pair is updated together with certificate update. | - |
| *key-bit* | Specifies the bits of the RSA key pair generated during the certificate update. | The value is an integer that ranges from 2048 to 4096 bit. The default value is 3072 bit. |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the CMPv2 is used to apply for certificate, the certificate request message sent by the PKI entity to CA must contain public key information. Therefore, you need to configure an RSA key pair for certificate application through CMPv2.

Note the following during configurations:

* If regenerate is unspecified, the system uses the original RSA key pairs during automatic updates.
* If regenerate is specified, the system generates new RSA key pairs during certificate updates for the application for certificates and overwrites the original certificates and RSA key pairs with the new ones.

**Prerequisites**

The RSA key pair for certificate application has been created using the **pki rsa local-key-pair create** command or the RSA key pair has been imported to the memory using the **pki import rsa-key-pair** command.

**Precautions**

One RSA key pair can be referenced only by one CMP session.


Example
-------

# Configure the RSA key pair to be referenced by CMP session test and update the RSA key pair during the certificate update.
```
<HUAWEI> system-view
[~HUAWEI] pki rsa local-key-pair create test
Info: The name of the new key-pair will be: test
The size of the public key ranges from 2048 to 4096 and is an even number.
If the input value is an odd number, the size of the public key is the input value minus one.
Input the bits in the modules:3072
Generating key-pairs...
Generating key-pairs finished
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request rsa local-key-pair test regenerate 3072

```