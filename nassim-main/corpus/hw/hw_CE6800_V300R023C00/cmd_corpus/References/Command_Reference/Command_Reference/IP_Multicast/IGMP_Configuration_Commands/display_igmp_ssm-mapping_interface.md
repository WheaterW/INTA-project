display igmp ssm-mapping interface
==================================

display igmp ssm-mapping interface

Function
--------



The **display igmp ssm-mapping interface** command displays configured source-specific multicast (SSM) mappings and whether IGMP SSM mapping is enabled on an interface.




Format
------

**display igmp ssm-mapping interface** [ *interface-type* *interface-number* | *interface-name* ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **ssm-mapping** **interface** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Indicates all instances. | - |
| **interface** *interface-type* *interface-number* | Displays whether IGMP SSM mapping is enabled on an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

By default, SSM group addresses range from 232.0.0.0 to 232.255.255.255. If SSM group addresses beyond this range are configured using the **ssm-policy** command and static SSM mapping rules are configured using the **ssm-mapping** command.Before using the **display igmp ssm-mapping** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command displays SSM mappings in the public network instance.
* If group-address is specified, the command displays SSM mappings of the specified group.
* If interface is specified, the command displays whether SSM mapping is enabled on the specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display whether IGMP SSM mapping is enabled on 100GE 1/0/1 in the public network instance.
```
<HUAWEI> display igmp ssm-mapping interface 100GE1/0/1
 IGMP SSM-Mapping is enabled

```

**Table 1** Description of the **display igmp ssm-mapping interface** command output
| Item | Description |
| --- | --- |
| IGMP SSM-Mapping is enabled | SSM mapping is enabled on an interface. |