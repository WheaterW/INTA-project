ssh server tcp forwarding enable
================================

ssh server tcp forwarding enable

Function
--------



The **ssh server tcp forwarding enable** command enables the local port forwarding function on the SSH server.

The **undo ssh server tcp forwarding enable** command disables the local port forwarding function on the SSH server.



By default, the tcp port forwarding service of SSH server is disabled.


Format
------

**ssh server tcp forwarding enable**

**undo ssh server tcp forwarding enable**


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

You can run this command to enable the local port forwarding service for the SSH server to allow the SSH server to establish TCP connections that cannot be established before due to limitations imposed by a firewall. The SSH server can receive forwarding request messages from the SSH client and establish a TCP connection (forwarding channel) with a host with a specified IP address and port number to forward data received from the client to the host only after the local port forwarding function is enabled on the SSH server.

**Precautions**

* A maximum of 32 forwarding channels can be established.
* If a forwarding channel remains idle for 10 minutes, it is disabled.

Example
-------

# Enable the tcp port forwarding service of SSH server.
```
<HUAWEI> system-view
[~HUAWEI] ssh server tcp forwarding enable
Info: Succeeded in starting the FWD server.

```