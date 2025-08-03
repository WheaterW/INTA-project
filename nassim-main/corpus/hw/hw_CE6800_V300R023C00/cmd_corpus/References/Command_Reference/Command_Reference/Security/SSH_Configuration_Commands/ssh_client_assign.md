ssh client assign
=================

ssh client assign

Function
--------



The **ssh client assign pki** command binds a PKI realm to an SSH client.

The **undo ssh client assign pki** command unbinds a PKI realm from an SSH client.

The **ssh client assign sm2-host-key** command assigns an SM2 host key to an SSH client.

The **undo ssh client assign sm2-host-key** command deletes the SM2 host key assigned to an SSH client.



By default, no PKI realm is bound to an SSH client.

By default, no SM2 host key is assigned to an SSH client.




Format
------

**ssh client assign** { **sm2-host-key** *key-name* | **pki** *pki-domain* }

**undo ssh client assign sm2-host-key**

**undo ssh client assign pki**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of an SM2 host key assigned to an SSH client. | The value is a string of 1 to 35 case-insensitive characters, spaces not supported. The string can contain only letters, digits, and underscores (\_). |
| **pki** *pki-domain* | Specifies the PKI realm bound to the SSH client. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When the device functions as an SSH client and uses a certificate for authentication, you can run the ssh client assign pki command to bind a PKI realm to the SSH client.

When the device functions as an SSH client and uses the SM2 algorithm for authentication, you can run the ssh client assign sm2-host-key command to assign a specified SM2 key pair to the SSH client.



**Prerequisites**



The **pki domain** *domain-name*command has been run to create a PKI realm with a specified signature.

A key pair has been created using the **sm2 key-pair label** command on the SSH client.



**Precautions**



If the PKI realm bound to the SSH client becomes invalid, run the **undo ssh client assign pki** command to unbind the PKI realm from the SSH client, and then run the **ssh client assign pki** command to bind a new PKI realm to the SSH client.If the SM2 public key saved on the SSH client becomes invalid, run the **undo ssh client peer assign** command to unbind the SM2 public key from the SSH client, and then run the **ssh client peer assign** command to assign a new SM2 public key to the SSH client.This command applies to both IPv4 and IPv6.




Example
-------

# Assign a PKI certificate to an SSH client.
```
<HUAWEI> system-view
[~HUAWEI] ssh client assign pki domainA

```

# Assign the SM2 host key named sm2key001 to the SSH client at 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] sm2 key-pair label sm2key001
[*HUAWEI] commit
[~HUAWEI] ssh client assign sm2-host-key sm2key001

```

# Assign an initial PKI certificate to the SSH client.
```
<HUAWEI> system-view
[~HUAWEI] ssh client assign pki default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:Y
[*HUAWEI]

```