rsa key-pair label
==================

rsa key-pair label

Function
--------



The **rsa key-pair label** command creates an RSA key pair and configures a label name for it.

The **undo rsa key-pair label** command deletes the RSA key pair with a specified label name.



By default, a device does not have RSA local key pairs or RSA server key pairs.


Format
------

**rsa key-pair label** *label-name* [ **modulus** *modulus-bits* ]

**undo rsa key-pair label** *label-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *label-name* | Specifies the label name of an RSA key pair. | The value is a string of 1 to 35 case-insensitive characters. The string contains letters, digits, and underscores (\_). |
| **modulus** *modulus-bits* | Specifies the modulus bit value of an RSA key pair. | The value is 2048 bits, 3072 bits or 4096 bits. The default value is 3072 bits. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An RSA key is the authentication password of an SSH user, which improves the security of user authentication.Running the rsa key-pair label label-name command creates a new RSA key pair and stores it using the specified label-name

**Configuration Impact**

Running the **rsa key-pair label** command creates a new RSA key pair and stores it with the given label-name. The **undo rsa key-pair label** command deletes the specified RSA key pair from the database.

**Precautions**

The RSA key files stored in a storage medium cannot be manually deleted.To ensure high security, use the RSA key pair whose length is 3072 bits or higher.


Example
-------

# Generate an RSA key pair with the label name of ssh\_host and the modulus of 3072.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair label ssh_host modulus 3072

```