scp server enable
=================

scp server enable

Function
--------



The **scp server enable** command enables the SCP service on the SSH server.

The **undo scp server enable** command disables the SCP service on the SSH server.



By default, the SCP service is disabled on the SSH server.


Format
------

**scp server enable**

**undo scp server enable**


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

To use SCP for file transfer, you must enable the SCP service on the SSH server. A client can connect to a remote SSH server by SCP only after the SCP service is enabled on the SSH server.The **scp server enable** command enables both IPv4 and IPv6 SCP services on the SSH server.

**Precautions**

If you disable the SCP service on the SSH server, all the clients that log in to the server through SCP will be disconnected.


Example
-------

# Enable the SCP service on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] scp server enable

```