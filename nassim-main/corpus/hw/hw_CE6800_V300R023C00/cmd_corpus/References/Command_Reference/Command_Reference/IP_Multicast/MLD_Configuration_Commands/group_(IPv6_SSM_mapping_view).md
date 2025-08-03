group (IPv6 SSM mapping view)
=============================

group (IPv6 SSM mapping view)

Function
--------



The **group** command configures IPv6 static SSM mapping source/group address mappings.

The **undo group** command deletes the IPv6 static SSM mapping source/group address mappings.



By default, no IPv6 static SSM mapping source/group address mapping is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**group** *group-ipv6-address* *mask-length* **source** *source-ipv6-address*

**undo group** { *group-ipv6-address* *mask-length* | **all** }

**undo group** *group-ipv6-address* *mask-length* **source** *source-ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-ipv6-address* | Indicates the IPv6 address of the multicast group. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. The value ranges from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| *mask-length* | Indicates the mask length of a multicast group. | The value is an integer, which can be 16, 32, 64, or 128. |
| **source** *source-ipv6-address* | Specifies the IPv6 address of a multicast source. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **all** | Delete all static SSM mapping source/group address mappings. | - |



Views
-----

IPv6 SSM mapping view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When users connected to different interfaces want to watch programs multicast by different multicast sources, run the **group** command to configure different SSM mappings for IPv6 policies of different interfaces. After that, MLD packets received by different interfaces can be mapped to different multicast sources and users' requirements can be answered.

**Prerequisites**

SSM mapping and a corresponding policy have been enabled on the interface using the mld snooping ssm-mapping enable [ policy policy-name ] command.


Example
-------

# Configure the mapping between the static multicast source 2001:db8:5::5 and the multicast group FF33::1/32 in the MLD SSM mapping policy ssmmap1.
```
<HUAWEI> system-view
[~HUAWEI] ssm-mapping ipv6 policy ssmmap1
[*HUAWEI-ssm-map6-ssmmap1] group ff33::1 32 source 2001:db8:5::5

```