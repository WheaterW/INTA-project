ssh server assign
=================

ssh server assign

Function
--------



The **ssh server assign** command assigns a host key or PKI certificate to an SSH server.

The **undo ssh server assign** command deletes a host key or PKI certificate assigned to an SSH server.



By default, no key or PKI certificate is assigned to an SSH server.


Format
------

**ssh server assign** { **rsa-host-key** *key-name* | **dsa-host-key** *key-name* | **ecc-host-key** *key-name* | **sm2-host-key** *key-name* | **pki** *key-name* }

**undo ssh server assign rsa-host-key**

**undo ssh server assign dsa-host-key**

**undo ssh server assign ecc-host-key**

**undo ssh server assign sm2-host-key**

**undo ssh server assign pki**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rsa-host-key** *key-name* | Assigns an RSA host key to an SSH server and specifies the name of the RSA host key. | The value is a string of 1 to 35 case-insensitive characters and can only contain digits, letters, and underscores (\_). |
| **dsa-host-key** *key-name* | Assigns a DSA host key to an SSH server and specifies the name of the DSA host key. | The value is a string of 1 to 35 case-insensitive characters and can only contain digits, letters, and underscores (\_). |
| **ecc-host-key** *key-name* | Assigns an ECC host key to an SSH server and specifies the name of the ECC host key. | The value is a string of 1 to 35 case-insensitive characters and can only contain digits, letters, and underscores (\_). |
| **sm2-host-key** *key-name* | Assigns an SM2 host key to an SSH server and specifies the name of the SM2 host key. | The value is a string of 1 to 35 case-insensitive characters and can only contain digits, letters, and underscores (\_). |
| **pki** *key-name* | Assigns a PKI realm to an SSH server and specifies the name of the PKI realm. | The value is a string of 1 to 64 case-insensitive characters without spaces. If an initial certificate is loaded to the specified PKI realm, the certificate is delivered in interactive mode. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to reference the generated RSA, DSA, SM2, and ECC keys or assign a PKI certificate to the SSH server to ensure security of the SSH server.



**Prerequisites**

A key pair has been created using one of the following commands based on the selected key:

* The **rsa key-pair label** command creates an RSA key pair with a specified label name.
* The **dsa key-pair label** command creates a DSA key pair with a specified label name.
* The **ecc key-pair label** command creates an ECC key pair with a specified label name.
* The **sm2 key-pair label** command creates an SM2 key pair with a specified label name.
* The **pki realm** command creates a PKI realm with a specified signature.
* For security purposes, you are not advised to use the RSA algorithm whose length is fewer than 3072 digits for SSH user authentication. You are advised to use the ECC authentication algorithm instead.

**Configuration Impact**

The RSA, DSA, or ECC key assigned to an SSH server takes precedence over the RSA, DSA, or ECC key created using the rsa local-key-pair create, dsa local-key-pair create, or ecc local-key-pair create command, respectively. If the ssh server assign command is not run, an SSH server uses the key-pair created using the rsa local-key-pair create, dsa local-key-pair create, or ecc local-key-pair create command.

**Precautions**

* The RSA host key and server key in a pair must differ in length by 128 bits. Otherwise, SSHv1 clients cannot log in to the server.
* If an RSA host key and an RSA server key have been assigned to an SSH server, and the RSA host key or server key is changed, or the key length is changed in a local RSA key pair so that the keys do not differ in length by 128 bits, SSHv1 applications are affected.
* Deleting an RSA, DSA, or ECC key pair also deletes the key assigned to an SSH server.
* This command takes effect for both IPv4 and IPv6 clients.

Example
-------

# Assign an initial PKI certificate to the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] ssh server assign pki default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI]

```

# Assign a PKI certificate to an SSH server.
```
<HUAWEI> system-view
[*HUAWEI] ssh server assign pki domainA

```

# Assign an SM2 host key named sm2key001 to an SSH server.
```
<HUAWEI> system-view
[~HUAWEI] sm2 key-pair label sm2key001
[*HUAWEI] ssh server assign sm2-host-key sm2key001

```

# Assign an ECC host key named ecckey to an SSH server.
```
<HUAWEI> system-view
[~HUAWEI] ecc key-pair label ecckey
[*HUAWEI] ssh server assign ecc-host-key ecckey

```