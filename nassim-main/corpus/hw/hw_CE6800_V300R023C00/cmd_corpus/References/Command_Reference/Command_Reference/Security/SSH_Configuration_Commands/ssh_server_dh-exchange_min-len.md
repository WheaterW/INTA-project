ssh server dh-exchange min-len
==============================

ssh server dh-exchange min-len

Function
--------



The **ssh server dh-exchange min-len** command configures the minimum key length supported during Diffie-hellman-group-exchange key exchange between the SSH server and client.

The **undo ssh server dh-exchange min-len** command restores the default minimum key length supported during Diffie-hellman-group-exchange key exchange between the SSH server and client.



By default, the minimum key length supported is 3072 bits.


Format
------

**ssh server dh-exchange min-len** *min-len*

**undo ssh server dh-exchange min-len**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *min-len* | Specifies the minimum Diffie-hellman-group-exchange key length supported on the SSH server. | The value can be either 1024 or 2048 or 3072 or 4096, in bits. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the SSH client supports the Diffie-hellman-group-exchange key of more than 1024 bits, run the **ssh server dh-exchange min-len** command to set the minimum key length to 3072 bits to improve security.

**Precautions**



If the minimum key length of the Diffie-hellman-group-exchange algorithm is less than or equal to 2048 bits, security risks exist. Before using the Diffie-hellman-group-exchange algorithm, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package. You are advised to set the minimum length to 3072 bits.This command takes effect for both IPv4 and IPv6.




Example
-------

# Set the minimum key length supported during Diffie-hellman-group-exchange key exchange between the SSH server and client to 3072 bits.
```
<HUAWEI> system-view
[~HUAWEI] ssh server dh-exchange min-len 3072

```