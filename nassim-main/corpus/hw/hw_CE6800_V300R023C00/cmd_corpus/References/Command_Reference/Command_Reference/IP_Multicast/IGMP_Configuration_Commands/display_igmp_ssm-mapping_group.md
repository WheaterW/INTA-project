display igmp ssm-mapping group
==============================

display igmp ssm-mapping group

Function
--------



The **display igmp ssm-mapping group** command displays configured source-specific multicast (SSM) mappings and whether SSM mapping is enabled on an interface.




Format
------

**display igmp ssm-mapping group** [ *group-address* ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **ssm-mapping** **group** [ *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Displays SSM mappings about a specified multicast group. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Displays SSM mappings in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Displays SSM mappings in all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

By default, SSM group addresses range from 232.0.0.0 to 232.255.255.255. If SSM group addresses beyond this range are configured using the **ssm-policy** command and static SSM mapping rules are configured using the **ssm-mapping** command, run the display igmp **ssm-mapping** command to display SSM mappings and check whether SSM mapping is enabled on an interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the SSM mappings of all source-specific group addresses in the public network instance.
```
<HUAWEI> display igmp ssm-mapping group
IGMP SSM-Mapping conversion table of VPN Instance: public net
 Total 2 entries    2 entries matched

 00001: (10.1.0.2, 225.1.1.0)

 00002: (10.1.0.2, 239.255.255.0)

 Total 2 entries matched

```

**Table 1** Description of the **display igmp ssm-mapping group** command output
| Item | Description |
| --- | --- |
| IGMP SSM-Mapping conversion table of VPN Instance | Instance in which IGMP SSM mappings are displayed. |
| Total 2 entries 2 entries matched | Total number of entries configured with SSM mappings and total number of entries matching the query condition. |
| Total 2 entries matched | Number of SSM mapping entries matching the query condition. |
| 00001: (10.1.0.2, 225.1.1.0) | ID of an (S, G) entry. |