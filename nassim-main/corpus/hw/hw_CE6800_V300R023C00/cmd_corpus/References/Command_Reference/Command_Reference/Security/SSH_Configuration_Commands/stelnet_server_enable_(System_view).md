stelnet server enable (System view)
===================================

stelnet server enable (System view)

Function
--------



The **stelnet server enable** command enables the STelnet service on the SSH server.

The **undo stelnet server enable** command disables the STelnet service on the SSH server.



By default, the STelnet service is not enabled on the SSH server.


Format
------

**stelnet ipv4 server enable**

**stelnet ipv6 server enable**

**undo stelnet ipv4 server enable**

**undo stelnet ipv6 server enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Enables the IPv6 STelnet service. | - |
| **ipv4** | Enables the IPv4 STelnet service. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To enable TCP port 22 to support the STelnet service, run the **stelnet server enable** command. A client can connect to a remote SSH server by STelnet only after the STelnet service is enabled on the SSH server.
* The **stelnet ipv4 server enable** command enables the IPv4 STelnet service on the SSH server.The **stelnet ipv6 server enable** command enables the IPv6 STelnet service on the SSH server.
* After you disable the STelnet service on the SSH server, all clients that have logged in through STelnet are disconnected.


Example
-------

# Enable the STelnet service on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] stelnet server enable

```