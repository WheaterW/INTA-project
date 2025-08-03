group (IPv4 SSM mapping view)
=============================

group (IPv4 SSM mapping view)

Function
--------



The **group** command configures static SSM mapping source/group address mappings.

The **undo group** command deletes the static SSM mapping source/group address mappings.



By default, no static SSM mapping source/group address mapping is configured.


Format
------

**group** *group-address* { *mask-length* | *mask* } **source** *source-address*

**undo group** { *group-address* { *mask-length* | *mask* } | **all** }

**undo group** *group-address* { *mask-length* | *mask* } **source** *source-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Indicates the address of the multicast group. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| *mask-length* | Indicates the mask length of a multicast group. | The value is an integer ranging from 4 to 32. |
| *mask* | Indicates the mask of a multicast group. | The value is in dotted decimal notation. |
| **source** *source-address* | Indicates the address of a multicast source. | The value is in dotted decimal notation. |
| **all** | Delete all static SSM mapping source/group address mappings. | - |



Views
-----

IPv4 SSM mapping view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When users connected to different interfaces want to watch programs multicast by different multicast sources, run the **group** command to configure different SSM mappings for IPv4 policies of different interfaces. After that, IGMP packets received by different interfaces can be mapped to different multicast sources and users' requirements can be answered.

**Prerequisites**

SSM mapping and a corresponding policy have been enabled on the interface using the **igmp ssm-mapping enable policy** command.


Example
-------

# Configure the static SSM mapping between the multicast source 10.10.1.1 and the multicast group 232.1.1.1/24 for the IGMP SSM mapping policy ssmmap1.
```
<HUAWEI> system-view
[~HUAWEI] ssm-mapping policy ssmmap1
[*HUAWEI-ssm-map-ssmmap1] group 232.1.1.1 24 source 10.10.1.1

```