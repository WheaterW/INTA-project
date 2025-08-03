sm2 local-key-pair
==================

sm2 local-key-pair

Function
--------



The **sm2 local-key-pair** command configures the SM2 key pair used to request a certificate in offline mode.

The **undo sm2 local-key-pair** command deletes the SM2 key pair used to request a certificate in offline mode.



By default, the system does not configure the SM2 key pair used to request a certificate in offline mode.


Format
------

**sm2 local-key-pair** *key-name*

**undo sm2 local-key-pair**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the SM2 key pair. | The value must be an existing SM2 key pair name. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The PKI entity that requests a certificate from the CA using offline PKCS#10 mode must contain a public key. Run this command to configure the SM2 key pair.

**Prerequisites**

The SM2 key pair used in certificate application has been created using the **pki sm2 local-key-pair create** command, or the SM2 key pair has been imported to the device memory using the **pki import sm2-key-pair** command.

**Precautions**

An SM2 key pair can be referenced by only one PKI realm.


Example
-------

# Configure the SM2 key pair that is referenced by the PKI realm test.
```
<HUAWEI> system-view
[~HUAWEI] pki sm2 local-key-pair create test
 Info: The name of the new key-pair will be: test
 Generating key-pairs...  
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] sm2 local-key-pair test

```