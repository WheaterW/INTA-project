set net-manager vpn-instance
============================

set net-manager vpn-instance

Function
--------



The **set net-manager vpn-instance** command configures the default IPv4 VPN instance used by the NMS to manage the device.

The **undo set net-manager vpn-instance** command deletes the configured default IPv4 VPN instance.

The **set net-manager ipv6 vpn-instance** command configures the default IPv6 VPN instance used by the NMS to manage the device.

The **undo set net-manager ipv6 vpn-instance** command deletes the configured default IPv6 VPN instance.



By default, no default VPN instance is set on a device.


Format
------

**set net-manager vpn-instance** *vpn-instance-name*

**set net-manager ipv6 vpn-instance** *vpn-instance-name*

**undo set net-manager vpn-instance**

**undo set net-manager ipv6 vpn-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of an IPv4 VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *vpn-instance-name* | Specifies the IPv6 VPN name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **ipv6** | Specifies the IPv6 VPN instance. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When the NMS manages devices through a VPN, device management information needs to be sent to the NMS through the VPN.The **set net-manager vpn-instance** command is used on a device to set a default VPN instance used by the NMS to implement device management. The default VPN instance will be used by the device to communicate with the NMS.

**Prerequisites**

A VPN instance has been created on the device.

**Configuration Impact**



The VPN configured using the **set net-manager vpn-instance** command affects the following service modules: TFTP client, FTP client, SFTP client, SCP client, Info Center module, SNMP module, and performance management module (depending on the device). After this command is configured, if you need to access the public network through the preceding service module, you must specify the public-net parameter in the command of the corresponding module. For example, if an SFTP client is used to access a remote server, the public-net parameter must be specified in the **sftp** command.After the bound VPN instance is deleted, the VPN configuration in this command is not cleared, but the function does not take effect. In this case, the server on the device selects the public network. After the VPN instance with the same name is reconfigured, the VPN function is restored.




Example
-------

# Set the default IPv6 VPN instance to v2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance v2
[*HUAWEI-vpn-instance-v2] quit
[*HUAWEI] set net-manager ipv6 vpn-instance v2

```

# Set the default VPN instance to v1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance v1
[*HUAWEI-vpn-instance-v1] quit
[*HUAWEI] set net-manager vpn-instance v1

```