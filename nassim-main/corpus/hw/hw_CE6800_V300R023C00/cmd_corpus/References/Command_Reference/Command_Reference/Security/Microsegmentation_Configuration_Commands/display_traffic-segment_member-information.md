display traffic-segment member-information
==========================================

display traffic-segment member-information

Function
--------



The **display traffic-segment member-information** command displays information about the EPG to which a specified member belongs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-segment member-information ip** *ip-address* [ *ip-address-netmask* | *mask-length* ] [ **vpn-instance** *vpn-instance-name* ]

**display traffic-segment member-information ipv6** *ipv6-address* [ *ipv6-address-netmask* | *ipv6mask-length* ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address-netmask* | Specifies the mask length of an IPv4 address. | The value is in dotted decimal notation and ranges from 128.0.0.0-255.255.255.255. The default value is 255.255.255.255. |
| *mask-length* | Specifies the mask length of an IPv4 address. | The value is an integer ranging from 1 to 32. The default value is 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **ipv6** *ipv6-address* | Specifies the IPv6 destination address. | The value is a 32-digit hexadecimal number in the format of X:X:X:X:X:X:X:X. The value range is 0::0-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| *ipv6-address-netmask* | Specifies the IPv6 address mask. | The value is a 32-digit hexadecimal number in the format of X:X:X:X:X:X:X:X. The value range is 8000::0-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. The default value is FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| *ipv6mask-length* | Specifies the length of the IPv6 address mask. | The value is an integer ranging from 1 to 128. The default value is 128. |
| **ip** *ip-address* | Specifies an IPv4 address. | The value is in dotted decimal notation and ranges from 0.0.0.0-255.255.255.255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about the EPG to which a specified member belongs, run the **display traffic-segment member-information** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the EPG to which the member with the IPv6 address 2001:db8:1::1 belongs.
```
<HUAWEI> display traffic-segment member-information ipv6 2001:db8:1::1 64
Slot: 1
-----------------------------------------------------------------------
Type        Name            Segment ID     Member Number     State
-----------------------------------------------------------------------
IPV6        --                       1                 2     Success
-----------------------------------------------------------------------

```

# Display information about the EPG to which the member at 1.1.1.1 belongs.
```
<HUAWEI> display traffic-segment member-information ip 1.1.1.1 24
Slot: 1
-----------------------------------------------------------------------
Type        Name            Segment ID     Member Number     State
-----------------------------------------------------------------------
IPV4        --                       1                 2     Success
-----------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-segment member-information** command output
| Item | Description |
| --- | --- |
| Type | Type of an EPG member. |
| Name | Name of an EPG. |
| Segment ID | ID of an EPG. |
| Member Number | Total number of members in an EPG. |
| State | Delivery status of EPG members.   * Success: The group member information is successfully delivered. * Fail: The group member information fails to be delivered. |
| Slot | Slot ID. |