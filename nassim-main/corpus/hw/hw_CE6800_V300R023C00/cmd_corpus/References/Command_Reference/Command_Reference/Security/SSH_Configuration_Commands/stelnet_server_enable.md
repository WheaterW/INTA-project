stelnet server enable
=====================

stelnet server enable

Function
--------



The **stelnet server enable** command enables the STelnet service on the SSH server.

The **undo stelnet server enable** command disables the STelnet service on the SSH server.



By default, the STelnet service is not enabled on the SSH server.


Format
------

**stelnet server enable**

**undo stelnet server enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **server** | Specifies the Stelnet server. | - |



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
* The **stelnet server enable** command enables both IPv4 and IPv6 STelnet services on the SSH server.
* After you disable the STelnet service on the SSH server, all clients that have logged in through STelnet are disconnected.

Example
-------

# Enable the STelnet service on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] stelnet server enable

```