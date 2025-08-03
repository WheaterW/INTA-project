ssh server rsa-key min-length
=============================

ssh server rsa-key min-length

Function
--------



The **ssh server rsa-key min-length** command sets the minimum length of RSA public keys allowed by the SSH server.

The **undo ssh server rsa-key min-length** command restores the default minimum length of RSA public keys allowed by the SSH server to 512 bits.



By default, the minimum length of RSA public keys allowed by the SSH server is 512 bits.


Format
------

**ssh server rsa-key min-length** *min-length-val*

**undo ssh server rsa-key min-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *min-length-val* | Sets the minimum length of RSA public keys. | The value is an integer that ranges from 512 to 4096. The default value is 512. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure the minimum length of RSA public keys allowed by the SSH server. After the configuration, the user can bind the RSA public key only when the length of the RSA public key is greater than or equal to the specified value.


Example
-------

# Set the minimum length of the RSA public key that can be used by the SSH server to 3072 bits.
```
<HUAWEI> system-view
[~HUAWEI] ssh server rsa-key min-length 3072

```