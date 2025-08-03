ssh client first-time enable
============================

ssh client first-time enable

Function
--------



The **ssh client first-time enable** command enables the SSH client first login function.

The **undo ssh client first-time enable** command disables the SSH client first login function.



By default, the SSH client first login function is disabled on an SSH client.


Format
------

**ssh client first-time enable**

**undo ssh client first-time enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the SSH client first login function is enabled on a device functioning as a client, the STelnet/SFTP client does not check the validity of the SSH server public key when logging in to the SSH server for the first time. After the login, the system automatically allocates the public key and saves it for authentication in next login.

**Precautions**

When an STelnet/SFTP client attempts to log in to an SSH server for the first time, it does not check the validity of the SSH server public key because it has not saved the SSH server public key.This command takes effect for both IPv4 and IPv6 SSH clients.


Example
-------

# Enable the SSH client first login function.
```
<HUAWEI> system-view
[~HUAWEI] ssh client first-time enable

```