netstream timeout tcp-session
=============================

netstream timeout tcp-session

Function
--------



The **netstream timeout tcp-session** command configures the aging of NetStream flows according to the FIN flag or the RST flag in the TCP packet header.

The **undo netstream timeout tcp-session** command restores the default setting.



By default, NetStream flows are not aged according to the FIN or RST flag in the TCP packet header.


Format
------

**netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **tcp-session**

**undo netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **tcp-session**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | IPv4 packets. | - |
| **ipv6** | IPv6 packets. | - |
| **vxlan** | VXLAN packets. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The FIN or RST flag in a TCP packet indicates that the TCP connection is terminated. When receiving a packet with the FIN or RST flag, the device immediately ages the corresponding NetStream flow. If this command is not run, NetStream flows are aged by following other criteria, for example, inactive aging time or bytes overflow.

**Precautions**

If you set multiple aging modes on the device, a flow is aged when it matches any criterion.Only original flows can be aged according to the FIN or RST flag in the TCP packet header.


Example
-------

# Configure the aging of NetStream flows according to the FIN or RST flag in the TCP packet header.
```
<HUAWEI> system-view
[~HUAWEI] netstream timeout ip tcp-session

```