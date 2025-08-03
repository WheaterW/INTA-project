telnet ipv6 server disable
==========================

telnet ipv6 server disable

Function
--------



The **telnet ipv6 server disable** command disables the IPv6 Telnet server service.

The **undo telnet ipv6 server disable** command enables the IPv6 Telnet server service.



By default, IPv6 telnet server is enabled.


Format
------

**telnet ipv6 server disable**

**undo telnet ipv6 server disable**


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

You can run this command to control the Telnet server status. The client can connect to the server through Telnet only after the Telnet service is enabled on the server and the source interface of the Telnet server is configured.When the Telnet server is shut down, the existing Telnet connections are not interrupted, but new connections are not allowed.


Example
-------

# Stop the IPv6 Telnet service.
```
<HUAWEI> system-view
[~HUAWEI] telnet ipv6 server disable

```