rip valid-ttl-hops
==================

rip valid-ttl-hops

Function
--------



The **rip valid-ttl-hops** command enables RIP Generalized TTL Security Mechanism (GTSM) and sets the time to live (TTL) value to be detected.

The **undo rip valid-ttl-hops** command cancels the function.



By default, RIP GTSM is disabled.


Format
------

**rip valid-ttl-hops** *valid-ttl-hops-value* [ **vpn-instance** *vpn-instance-name* ]

**undo rip valid-ttl-hops** [ *valid-ttl-hops-value* ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *valid-ttl-hops-value* | Specifies the number of TTL value to be detected.  The valid TTL range of the detected packets is [ 255 -<ttl>. 1, 255 ]. | The value is an integer ranging from 1 to 255. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance.  If this parameter is used, you need only to specify the TTL value to be detected by the VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an attacker simulates RIP packets and keeps sending them to a device, the device directly sends the packets to the RIP module on the control plane without checking their validity. As a result, the control plane of the device is busy processing these packets and the CPU usage is high. GTSM protects a device against such attacks by checking whether the TTL value in an IP packet header is within a pre-defined range to improve system security.The **rip valid-ttl-hops** command is used to enable RIP GTSM.

**Precautions**

GTSM must be enabled on devices at both ends.If GTSM is enabled on a device, after the device receives a RIP packet, it checks whether the TTL value in the packet is in a pre-defined range. If the TTL value is beyond the pre-defined range, the device considers the packet as an attack packet and discards it.


Example
-------

# Enable RIP GTSM and set the maximum number of TTL hops to 5 for the packets that can be accepted by the router.
```
<HUAWEI> system-view
[~HUAWEI] rip valid-ttl-hops 5

```