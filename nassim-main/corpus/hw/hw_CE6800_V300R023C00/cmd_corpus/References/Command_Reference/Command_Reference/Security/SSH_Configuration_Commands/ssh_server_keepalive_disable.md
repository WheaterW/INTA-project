ssh server keepalive disable
============================

ssh server keepalive disable

Function
--------



The **ssh server keepalive disable** command disables the keepalive feature on the SSH server.

The **undo ssh server keepalive disable** command enables the keepalive feature on the SSH server.



By default, the keepalive feature is enabled on the SSH server.


Format
------

**ssh server keepalive disable**

**undo ssh server keepalive disable**


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

The SSH server sends a keepalive response to the SSH client only if the keepalive feature is enabled on the SSH server. Otherwise the server discards the connection.This command takes effect for both IPv4 and IPv6 connections.


Example
-------

# Disable the keepalive feature on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] ssh server keepalive disable

```