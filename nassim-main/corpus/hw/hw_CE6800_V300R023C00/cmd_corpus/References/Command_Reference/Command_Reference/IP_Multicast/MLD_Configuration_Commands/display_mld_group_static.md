display mld group static
========================

display mld group static

Function
--------



The **display mld group static** command displays information about Multicast Listener Discovery (MLD) groups, including MLD groups that hosts dynamically join by sending Report messages and multicast groups that hosts are configured to statically join by using commands.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld group** [ *GrpAddr6* | **interface** { *port-type* *port-num* | *port-name* } ] \* **static** [ **verbose** ]

**display mld** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** [ *GrpAddr6* | **interface** { *port-type* *port-num* | *port-name* } ] \* **static** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *port-type* *port-num* | Specifies the type and number of an interface. | - |
| **interface** *port-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **static** | Displays information about MLD groups that hosts statically join. | - |
| **verbose** | Displays detailed information about MLD multicast groups that hosts join. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |
| **group** *GrpAddr6* | Specifies an IPv6 multicast group address. | The value is in hexadecimal notation and in the format of FFxA:xxxx:xxxx::xxxx, in which x ranges from 0 to F and A is 0 or ranges from 3 to F. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If static is specified, the command displays only information about MLD groups that hosts statically join. Otherwise, the command displays information about all MLD groups that hosts join.If both static and verbose are specified, the command displays detailed information about MLD groups that hosts statically join.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about MLD groups that hosts statically join.
```
<HUAWEI> display mld all-instance group static verbose
Static join group information of VPN-Instance: public net
 100GE1/0/1:
  Total 16 entries 
   Group Address    Source Address   Reference num   Multicast Boundary
   FF17::1  ::  1  NO
   FF17::2  ::  1  NO
   FF17::3  ::  1  NO
   FF17::4  ::  1  NO
   FF17::5  ::  1  NO
   FF17::6  ::  1  NO
   FF17::7  ::  1  NO
   FF17::8  ::  1  NO
   FF17::9  ::  1  NO
   FF18::1  ::  1  NO
   FF18::2  ::  1  NO
   FF18::3  ::  1  NO
   FF18::4  ::  1  NO
   FF18::5  ::  1  NO
   FF18::6  ::  1  NO
   FF18::7  ::  1  NO

```

**Table 1** Description of the **display mld group static** command output
| Item | Description |
| --- | --- |
| Static join group information of VPN-Instance | Information about MLD groups that hosts statically join. |
| Total 16 entries | Total number of static multicast groups on the device. |
| Group Address | Multicast group address. |
| Source Address | Source address. |
| 10GE1/0/1 | Interface where the multicast group exists. |