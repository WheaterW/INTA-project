dns server source-interface
===========================

dns server source-interface

Function
--------



The **dns server source-interface** command configures the IP address of a specified interface as the source IP address of the DNS query messages sent by a device to the DNS server.

The **undo dns server source-interface** command restores the default setting.



By default, the source interface IP address is used as the source IP address of the DNS query messages sent by a device to the DNS server.


Format
------

**dns server source-interface** { *interface-type* *interface-number* | *interface-name* }

**undo dns server source-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies an interface name. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device sends DNS query messages to the DNS server through interface A, the IP address of interface A is used as the source IP address of the DNS query messages by default. If the DNS server only has routes destined for the IP address of interface B and does not have routes destined for the IP address of interface A, you need to set the source IP address of the DNS query messages to the IP address of interface B; otherwise, the DNS server may fail to return response packets due to a route query failure.

**Precautions**



This function is supported only if the device performs a DNS query through the DNS server with an IPv4 address and is not supported if the device performs a DNS query through the DNS server with an IPv6 address.The source interface must have a valid address that belongs to the same VPN as the DNS server address or the two addresses belong to a public network. Otherwise, this function does not take effect.




Example
-------

# Configure the IP address of 100GE1/0/1 as the source IP address of the DNS query messages sent by a device to the DNS server.
```
<HUAWEI> system-view
[~HUAWEI] dns server source-interface 100GE 1/0/1

```