netstream timeout active
========================

netstream timeout active

Function
--------



The **netstream timeout active** command sets the active aging time of IPv4 flows, IPv6 flows, and VXLAN flows.

The **undo netstream timeout active** command restores the default setting.



By default, the active aging time of the IPv4 flows, IPv6 flows, and VXLAN flows is 1800 seconds.


Format
------

**netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **active** *active-interval*

**undo netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **active** [ *active-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | IPv4 packets. | - |
| **ipv6** | IPv6 packets. | - |
| **vxlan** | VXLAN packets. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| *active-interval* | Specifies the active aging time. | The value is an integer in the range from 1 to 604800, in seconds. The default value is 1800. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently, while the memory capacity of the NDE is limited. Earlier flows in the memory need to be exported to release space for the new flows. The process of exporting old flows is called aging. All flows in the NDE memory will be exported to the NSC for analysis.When the active time (from flow creation time to the current time) of an original or flexible flow exceeds the specified active aging time, the flow is exported to the destination.To quickly detect the status of an active flow, set the active time to a small value; however, this setting increases the frequency at which NetStream packets are sent. To reduce the frequency at which NetStream packets are exported and improve statistics collecting efficiency, set the active time to a large value.

**Precautions**

If you set multiple aging modes on the device, a flow is aged when it matches any criterion.


Example
-------

# Set the active aging time of NetStream flows to 80 seconds.
```
<HUAWEI> system-view
[~HUAWEI] netstream timeout ip active 80

```