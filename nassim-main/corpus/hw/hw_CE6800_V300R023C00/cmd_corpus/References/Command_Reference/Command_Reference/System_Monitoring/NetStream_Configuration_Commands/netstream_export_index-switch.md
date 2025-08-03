netstream export index-switch
=============================

netstream export index-switch

Function
--------



The **netstream export index-switch** command sets the number of digits in the interface index contained in an exported packet carrying flow statistics.

The **undo netstream export index-switch** command restores the default setting.



By default, the number of digits in interface indexes is 32.


Format
------

**netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **index-switch** { **16** | **32** }

**undo netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **index-switch** [ **16** | **32** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Sets the number of digits in the interface index contained in an exported packet carrying IPv4 flow statistics. | - |
| **ipv6** | sets the number of digits in the interface index contained in an exported packet carrying IPv6 flow statistics. | - |
| **vxlan** | Sets the number of digits in the interface index contained in an exported packet carrying VXLAN flexible flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| **index-switch** | Specifies the number of digits in the index of a specified interface. | The value is 16 or 32. The default value is 32. |
| **16** | Set the number of digits in an interface index to 16. | - |
| **32** | Set the number of digits in an interface index to 32. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the number of digits in an interface index to 16 or 32.The number of digits in the interface index is set according to the type of the interface index that can be parsed by the NMS. For example, if the NMS can parse 32-bit interface indexes, set the format of the interface indexes contained in exported NetStream packets to 32-bit.

**Precautions**

The interface index length in exported packets can be set to 32 bits only when the NMS supports 32-bit interface index; otherwise, the NMS cannot identify the NetStream packets.This command takes effect for only V9 exported packets.


Example
-------

# Change the number of digits in the interface index contained in an exported packet carrying IPv4 flow statistics from 16 to 32.
```
<HUAWEI> system-view
[~HUAWEI] netstream export ip version 9
[*HUAWEI] netstream export ip index-switch 32

```