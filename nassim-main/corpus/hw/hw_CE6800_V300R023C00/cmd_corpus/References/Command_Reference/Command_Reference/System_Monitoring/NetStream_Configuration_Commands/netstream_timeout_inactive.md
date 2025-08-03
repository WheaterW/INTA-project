netstream timeout inactive
==========================

netstream timeout inactive

Function
--------



The **netstream timeout inactive** command sets the inactive aging time of a flow.

The **undo netstream timeout inactive** command restores the default setting.



By default, the inactive aging time of the original flows and flexible flows is 15 seconds.


Format
------

**netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **inactive** *inactive-interval*

**undo netstream timeout** { **ip** | **ipv6** | **vxlan** **inner-ip** } **inactive** [ *inactive-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | IPv4 packets. | - |
| **ipv6** | IPv6 packets. | - |
| **vxlan** | VXLAN packets. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| *inactive-interval* | Specifies the inactive aging time of original flows and flexible flows. | The value is an integer in the range from 1 to 604800, in seconds. The default value is 15. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently, while the memory capacity of the NDE is limited. Earlier flows in the memory need to be exported to release space for the new flows. The process of exporting old flows is called aging. All flows in the NDE memory will be exported to the NSC for analysis.When the inactive time (from the last packet receiving time to the current time) of an original or flexible flow exceeds the specified inactive aging time, the flow is exported to the destination.To quickly detect the status of an inactive flow, set the inactive time to a small value; however, this setting increases the frequency at which NetStream packets are sent. To reduce the frequency at which NetStream packets are exported and improve statistics collecting efficiency, set the inactive time to a large value.

**Precautions**

If you set multiple aging modes on the device, a flow is aged when it matches any criterion.


Example
-------

# Set the inactive aging time of NetStream flows to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] netstream timeout ip inactive 20

```