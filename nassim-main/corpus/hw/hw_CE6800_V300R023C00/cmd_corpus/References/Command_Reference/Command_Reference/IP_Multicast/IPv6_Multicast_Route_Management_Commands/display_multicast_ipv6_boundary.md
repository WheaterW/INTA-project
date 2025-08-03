display multicast ipv6 boundary
===============================

display multicast ipv6 boundary

Function
--------



The **display multicast ipv6 boundary** command displays information about the multicast boundaries configured on all the interfaces of a device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display multicast ipv6 boundary** [ *ipv6-group-address* [ *ipv6-group-mask-length* ] ] [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display multicast ipv6** { **vpn-instance** *instance-name* | **all-instance** } **boundary** [ *ipv6-group-address* [ *ipv6-group-mask-length* ] ] [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies an IPv6 multicast group address. | The value ranges from FF00::0 to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| *ipv6-group-mask-length* | Specifies the mask length of an IPv6 multicast group address. | The value is an integer ranging from 8 to 128. |
| **interface** *interface-type* | Specifies the type of an interface. If this parameter is specified, information about the multicast boundary configured on the specified interface is displayed. | - |
| *interface-number* | Specifies the type and the number of an interface. If this parameter is specified, information about the multicast boundary configured on the specified interface is displayed. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a multicast boundary is configured by using the **multicast ipv6 boundary** command, the display **multicast ipv6 boundary** command can be used to check the configuration of the multicast boundary.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the IPv6 multicast boundaries configured on all interfaces of a device.
```
<HUAWEI> display multicast ipv6 boundary
IPv6 multicast boundary information of VPN-Instance: public net
Total: 2 ...
Interface           Boundary
100GE1/0/1          FF02::111:0/16
FF03::222:0/16

```

**Table 1** Description of the **display multicast ipv6 boundary** command output
| Item | Description |
| --- | --- |
| IPv6 multicast boundary information of VPN-Instance | Information about an IPv6 multicast boundary. |
| Interface | Interface configured with a multicast boundary. |
| Boundary | Multicast boundary. |
| Total | Total number of IPv6 multicast boundaries. |