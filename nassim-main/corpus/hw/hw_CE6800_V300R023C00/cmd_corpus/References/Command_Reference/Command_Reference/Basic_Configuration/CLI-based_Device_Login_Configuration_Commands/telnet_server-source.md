telnet server-source
====================

telnet server-source

Function
--------



The **telnet server-source** command specifies a source interface for a Telnet server.

The **undo telnet server-source** command restores the default setting.



By default, the source interface of a Telnet server is not specified.


Format
------

**telnet server-source -i** { *interface-type* *interface-number* | *interface-name* }

**telnet server-source all-interface**

**undo telnet server-source -i** { *interface-type* *interface-number* | *interface-name* }

**undo telnet server-source all-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Specifies the source interface type and interface number of a Telnet server. | - |
| **all-interface** | Indicates that any interface having an IP address configured can be used as the source interface of a Telnet server. | - |
| **-i** *interface-name* | Specifies the source interface name of a Telnet server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, you can run the **telnet server-source** command to specify a source interface address for the Telnet server. Then only authorized users can log in to the Telnet server.

* If the **telnet server-source -i** command is run and the **telnet server-source all-interface** command is not, the specified interface is used as the source interface.
* If the **telnet server-source all-interface** command is run and the **telnet server-source -i** command is not, any valid interface on the device can be used as the source interface, including any physical interface with an IP address configured and any created logical interface with an IP address configured.
* If both the **telnet server-source -i** and **telnet server-source all-interface** commands are run, the interface specified in the **telnet server-source -i** command is preferentially used as the source interface of the Telnet server. If the specified source interface fails to be used for login, the system selects an interface from other valid interfaces for login.
* If no source interface is specified using the **telnet server-source** command, users cannot log in to the system through Telnet.

**Prerequisites**

A loopback interface has been created if you want to specify it as the source interface of a Telnet server using the **telnet server-source** command. Otherwise, the command cannot be executed.

**Configuration Impact**

After the source interface is specified, the system only allows Telnet users to log in to the Telnet server through this source interface, and Telnet users logging in through other interfaces are denied. Note that setting this parameter only affects Telnet users that attempt to log in to the Telnet server, and it does not affect Telnet users that have logged in to the server.

**Precautions**

* The Telnet protocol has security risks. You are advised to use the SSH v2 protocol.
* If a source interface or source IPv6 address is specified for a Telnet server, Telnet users must be able to communicate with the specified source interface or source IPv6 address at Layer 3 to ensure that authorized Telnet users can log in to the server.
* If the specified source interface is bound to a VPN instance, the Telnet server is also bound to the VPN instance.
* If the VPN instance bound to the specified source interface is deleted, the VPN configuration specified in the command is not cleared but does not take effect. In this case, the Telnet server uses the public network instance instead. If the VPN instance with the same name as the deleted one is reconfigured, the VPN function will be restored.
* If the **telnet server-source all-interface** command is run, users can log in to the Telnet server through any valid IPv4 interface, which increases system security risks. Therefore, running the command is not recommended.
* If the bound source interface is deleted, the interface configuration in the command is not deleted but does not take effect. If the source interface with the same name as the deleted one is reconfigured, the function will be restored.


Example
-------

# Specify loopback 0 as the source interface of the Telnet server.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 0
[~HUAWEI-LoopBack0] ip address 10.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] telnet server-source -i Loopback 0

```

# Allow any IPv4 interface address on the Telnet server to be used as the source IPv4 address of the server.
```
<HUAWEI> system-view
[~HUAWEI] telnet server-source all-interface

```