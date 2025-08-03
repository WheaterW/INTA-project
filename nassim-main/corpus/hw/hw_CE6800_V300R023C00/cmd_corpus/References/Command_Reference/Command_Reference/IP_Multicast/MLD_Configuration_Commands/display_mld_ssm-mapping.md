display mld ssm-mapping
=======================

display mld ssm-mapping

Function
--------



The **display mld ssm-mapping** command displays configured Source-Specific Multicast (SSM) mappings and checks whether an interface is enabled with the Multicast Listener Discovery (MLD) SSM mapping function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld ssm-mapping interface** [ *interface-type* *interface-number* | *interface-name* ]

**display mld** { **vpn-instance** *instance-name* | **all-instance** } **ssm-mapping** **interface** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When running **display mld ssm-mapping** command, note the following points,if interface is specified, the command output shows whether the specified interface is enabled with the MLD SSM mapping function.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about interfaces configured with SSM mapping.
```
<HUAWEI> display mld ssm-mapping interface
Interface information of VPN-Instance: public net
100GE1/0/1(FE80::1)

```

**Table 1** Description of the **display mld ssm-mapping** command output
| Item | Description |
| --- | --- |
| Interface information of VPN-Instance | VPN instance to which an interface configured with SSM mapping belongs. |
| 100GE1/0/1(FE80::1) | Type and number of an interface (IP address). |