rsa local-key-pair
==================

rsa local-key-pair

Function
--------



The **rsa local-key-pair** command configures the RSA key pair used to request a certificate in an offline mode.

The **undo rsa local-key-pair** command deletes the RSA key pair used to request a certificate in an offline mode.



By default, the system does not configure the RSA key pair used to request a certificate an offline mode.


Format
------

**rsa local-key-pair** *key-name*

**undo rsa local-key-pair**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the RSA key pair. | The value must be an existing RSA key pair name. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The PKI entity that requests a certificate from the CA using offline PKCS#10 mode must contain a public key. Run this command to configure the RSA key pair.

**Prerequisites**

The RSA key pair for certificate application has been created using the **pki rsa local-key-pair create** command or the RSA key pair has been imported to the memory using the **pki import rsa-key-pair** command.

**Precautions**

An RSA key pair can be specified to only one PKI.


Example
-------

# Configure the RSA key pair that is referenced by the PKI realm test.
```
<HUAWEI> system-view
[HUAWEI] pki rsa local-key-pair create test
Info: The name of the new key-pair will be: test
The size of the public key ranges from 2048 to 4096 and is an even number.
If the input value is an odd number, the size of the public key is the input value minus one.
Input the bits in the modules:3072
Generating key-pairs...
Generating key-pairs finished
[HUAWEI] pki realm test
[HUAWEI-pki-realm-test] rsa local-key-pair test

```