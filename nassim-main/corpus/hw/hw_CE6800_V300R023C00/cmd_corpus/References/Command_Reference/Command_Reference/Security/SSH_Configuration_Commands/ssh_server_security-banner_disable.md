ssh server security-banner disable
==================================

ssh server security-banner disable

Function
--------



The **ssh server security-banner disable** command disables the risk prompt function on the SSH server.

The **undo ssh server security-banner disable** command enables the risk prompt function on the SSH server.



By default, the risk prompt function is enabled on the SSH server.


Format
------

**ssh server security-banner disable**

**undo ssh server security-banner disable**


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

When an SSH client attempts to log in to an SSH server, but the negotiated algorithm is an insecure one, the SSH server generates a risk warning message and sends the message to the SSH client. However, if the SSH client cannot parse this type of message, it fails to interact with the server, leading to a login failure. To prevent this problem, you can run the **ssh server security-banner disable** command to disable the risk warning function triggered by the SSH server when an insecure algorithm is used between the SSH server and client.


Example
-------

# Disable the risk warning function triggered by an SSH server when an insecure algorithm is used between the SSH server and client.
```
<HUAWEI> system-view
[~HUAWEI] ssh server security-banner disable

```