display mld ssm-mapping group
=============================

display mld ssm-mapping group

Function
--------



The **display mld ssm-mapping group** command displays configured Source-Specific Multicast (SSM) mappings and check whether an interface is enabled with the Multicast Listener Discovery (MLD) SSM mapping function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld ssm-mapping group** [ *ipv6-group-address* ]

**display mld** { **vpn-instance** *instance-name* | **all-instance** } **ssm-mapping** **group** [ *ipv6-group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies an IPv6 multicast group address. | The value ranges from FF00::0 to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal notation. |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When running display mld ssm-mapping command,If group SsmappingGrpAddr is specified, only SSM mappings related to a specified group are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the SSM mappings of all source/group addresses in the public network instance.
```
<HUAWEI> display mld ssm-mapping group
MLD SSM-Mapping conversion table of VPN Instance: public net
 Total 3 entries, 3 entries matched

 00001: (2001:db8:1::1, FF37::)

 00002: (2001:db8:1::2, FF37::)

 00003: (2001:db8:1::3, FF37::1)

```

**Table 1** Description of the **display mld ssm-mapping group** command output
| Item | Description |
| --- | --- |
| MLD SSM-Mapping conversion table of VPN Instance | VPN instance to which the MLD SSM mapping conversion table belongs. |
| Total 3 entries | Number of multicast entries configured with SSM mappings. |
| 3 entries matched | Number of SSM mapping entries matching the query conditions. |
| (2001:db8:1::1, FF37::) | Number of an (S, G) entry. |