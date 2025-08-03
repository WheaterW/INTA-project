scp server enable (System view)
===============================

scp server enable (System view)

Function
--------



The **scp server enable** command enables the SCP service on the SSH server.

The **undo scp server enable** command disables the SCP service on the SSH server.



By default, the SCP service is disabled on the SSH server.


Format
------

**scp ipv4 server enable**

**scp ipv6 server enable**

**undo scp ipv4 server enable**

**undo scp ipv6 server enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Enables the SCP IPv6 service. | - |
| **ipv4** | Enables the SCP IPv4 service. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To use SCP for file transfer, you must enable the SCP service on the SSH server. A client can connect to a remote SSH server by SCP only after the SCP service is enabled on the SSH server.To enable the IPv4 SCP service on an SSH server, run the **scp ipv4 server enable** command. To enable the IPv6 SCP service on an SSH server, run the **scp ipv6 server enable** command.



**Precautions**

If you disable the SCP service on the SSH server, all the clients that log in to the server through SCP will be disconnected.


Example
-------

# Enable SCP on the server.
```
<HUAWEI> system-view
[~HUAWEI] scp server enable

```