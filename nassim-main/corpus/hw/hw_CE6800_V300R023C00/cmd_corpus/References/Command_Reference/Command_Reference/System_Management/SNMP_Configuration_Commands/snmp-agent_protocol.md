snmp-agent protocol
===================

snmp-agent protocol

Function
--------



The **snmp-agent protocol** command configures SNMP to receive and respond to NMS IPv4 or IPv6 request packets through VPN instances or the public network.

The **undo snmp-agent protocol** command restores the default configuration.



By default, SNMP receives and responds to NMS IPv4 or IPv6 request packets through all VPN instances or the public network.


Format
------

**snmp-agent protocol** [ **ipv6** ] { **vpn-instance** *vpn-instance-name* | **public-net** }

**undo snmp-agent protocol** [ **ipv6** ] { **vpn-instance** | **public-net** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Configures SNMP to receive and respond to NMS IPv6 request packets through a VPN instance or the public network.  If the ipv6 parameter is not specified, SNMP receives and responds to NMS IPv4 request packets through a VPN instance or the public network. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance through which SNMP receives and responds to NMS request packets. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **public-net** | Configures SNMP to receive and respond to NMS request packets through the public network. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, SNMP receives and responds to NMS IPv4 or IPv6 request packets through all VPN instances or the public network, which has security risks. To reduce the risks and narrow down the attack scope, run the snmp-agent protocol [ ipv6 ] vpn-instance vpn-instance-name command to bind SNMP to a specified VPN instance so that only this VPN instance is listened to. If network management through the public network is required, run the snmp-agent protocol [ ipv6 ] public-net command to enable SNMP to listen to the public network to prevent security risks.

**Configuration Impact**

After the snmp-agent protocol [ ipv6 ] vpn-instance vpn-instance-name command is run, the device can communicate with the NMS only through the SNMP Agent protocol bound to the specified VPN instance.


Example
-------

# Configure SNMP to receive and respond to NMS request packets through the VPN instance named abc.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] snmp-agent protocol vpn-instance abc

```

# Configure SNMP to receive and respond to NMS request packets through the public network.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent protocol public-net

```

# Configure SNMP to receive and respond to NMS IPv6 request packets through the public network.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent protocol ipv6 public-net

```