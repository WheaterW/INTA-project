telnet server disable
=====================

telnet server disable

Function
--------



The **telnet server disable** command disables the Telnet service.

The **undo telnet server disable** command enables the Telnet service.



By default, the Telnet service is enabled.


Format
------

**telnet server disable**

**undo telnet server disable**


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

* You can run this command to control the Telnet server status. The client can connect to the server through Telnet only after the Telnet service is enabled on the server and the source interface of the Telnet server is configured.
* To enable the IPv4 Telnet service on a server, run the **undo telnet server disable** command.
* When the Telnet server is shut down, the existing Telnet connections are not interrupted, but new connections are not allowed.
* Telnet is not secure. STelnet is recommended because it is more secure.

**Precautions**

* To ensure high security, you are advised to use the STelnet service.
* This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Stop the Telnet service.
```
<HUAWEI> system-view
[~HUAWEI] telnet server disable

```