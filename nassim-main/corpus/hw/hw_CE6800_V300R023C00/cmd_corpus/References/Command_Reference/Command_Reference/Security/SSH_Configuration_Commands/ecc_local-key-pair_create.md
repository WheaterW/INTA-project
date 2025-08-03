ecc local-key-pair create
=========================

ecc local-key-pair create

Function
--------



The **ecc local-key-pair create** command generates a local ECC host key pair.



By default, no local ECC host key pair exists in the system.


Format
------

**ecc local-key-pair create**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ecc** | Displays the public key in the local ECC key pair. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A local key pair is a prerequisite to a successful SSH login. Compared with the RSA algorithm used by the **rsa local-key-pair create** command, the ECC algorithm shortens the key length, accelerates the encryption, and improves the security. The length of the ECC server key pair and the host key pair can be 256 bits, 384 bits, and 521 bits. By default, the length of the key pair is 521 bits.

**Precautions**

The new key pair is named in the Host\_ECC format.If you log in to the device in SSH mode for the first time and no local key pair is configured, the system automatically generates a key pair.This command is a one-time operation command and is not saved in the configuration file. You only need to run this command once. After the device restarts, you do not need to run this command again.


Example
-------

# Generate a local ECC host key pair and a server key pair.
```
<HUAWEI> system-view
[~HUAWEI] ecc local-key-pair create
Info: The key name will be: Host_ECC
Info: The key modulus can be any one of the following: 256, 384, 521.
Info: Key pair generation will take a short while.
Please input the modulus [default=521]:521
Info: Generating keys...
Info: Succeeded in creating the ECC host keys.

```