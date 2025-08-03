display pim ipv6 bfd session statistics
=======================================

display pim ipv6 bfd session statistics

Function
--------



The **display pim ipv6 bfd session statistics** command displays information statistics about PIM IPv6 BFD sessions.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 bfd session statistics**

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **bfd** **session** [ **neighbor** *ipv6-link-local-address* | **interface** { *interface-name* | *interface-type* *interface-number* } ] \*

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **bfd** **session** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |
| **neighbor** *ipv6-link-local-address* | Displays information about PIM IPv6 BFD sessions on a specified neighbor. | The value ranges from FE80:: to FE80:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal notation. |
| **interface** *interface-type* *interface-number* | Displays information about PIM IPv6 BFD sessions on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 bfd session statistics** command is used to display statistics about PIM IPv6 BFD sessions in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about PIM IPv6 BFD sessions in the public network instance.
```
<HUAWEI> display pim ipv6 bfd session statistics
 VPN-Instance: public net
  Total 1 PIM BFD session in this instance.

   Total 1 PIM BFD session up.
   Total 0 PIM BFD session down.

```

**Table 1** Description of the **display pim ipv6 bfd session statistics** command output
| Item | Description |
| --- | --- |
| Total 1 PIM BFD session in this instance | Total number of PIM IPv6 BFD sessions in the public network instance. |
| Total 1 PIM BFD session up | Total number of PIM IPv6 BFD sessions in the Up state in the public network instance. |
| Total 0 PIM BFD session down | Total number of PIM IPv6 BFD sessions in the Down state in the public network instance, that is, the total number of PIM IPv6 BFD sessions minus the number of PIM IPv6 BFD sessions in the Up state. |
| VPN-Instance | VPN instance to which PIM IPv6 BFD session information belongs. |