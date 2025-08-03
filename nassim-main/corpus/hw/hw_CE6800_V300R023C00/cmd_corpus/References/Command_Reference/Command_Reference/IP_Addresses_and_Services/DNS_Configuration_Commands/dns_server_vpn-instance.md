dns server vpn-instance
=======================

dns server vpn-instance

Function
--------



The **dns server vpn-instance** command configures the device to send DNS query requests to the DNS server on a specified VPN network.

The **undo dns server vpn-instance** command disables the device from sending DNS query requests to the DNS server on a specified VPN network.



By default, the device can only send DNS query requests to the DNS server on a public network.


Format
------

**dns server vpn-instance** *vpn-instance-name*

**undo dns server vpn-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an interface on the device and the DNS server have reachable routes to each other and the interface is on a VPN network, the device must use the DNS server on the VPN network for DNS query so that DNS packets can be exchanged properly.

**Precautions**

* If this command is run more than once, the latest configuration overrides the previous one.
* The device can send DNS query requests to a DNS server on a public network or a VPN.
* When the **dns server vpn-instance** command is run to enable the VPN instance to which the specified DNS server belongs, the IPv4 or IPv6 address family must be enabled for the VPN instance. Otherwise, the function does not take effect.
* This configuration does not take effect for the DNS server, source address, or domain name suffix with a specified VPN instance.

Example
-------

# Configure the device to send DNS query requests to the DNS server on the VPN network vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns server vpn-instance vpn1

```