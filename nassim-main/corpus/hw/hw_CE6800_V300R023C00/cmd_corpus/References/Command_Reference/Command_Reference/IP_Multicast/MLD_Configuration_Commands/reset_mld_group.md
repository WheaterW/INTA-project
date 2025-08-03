reset mld group
===============

reset mld group

Function
--------



The **reset mld group** command clears the records about Multicast Listener Discovery (MLD) groups that an interface dynamically joins.

The **reset mld group ssm-mapping** command deletes the multicast groups configured with Source-Specific Multicast (SSM) mapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mld group** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr6* [ *GrpMaskLen* ] [ *SrcAddr6* [ *SrcMaskLen* ] ] } }

**reset mld group ssm-mapping** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr6* [ *GrpMaskLen* ] } }

**reset mld** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr6* [ *GrpMaskLen* ] [ *SrcAddr6* [ *SrcMaskLen* ] ] } }

**reset mld** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** **ssm-mapping** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr6* [ *GrpMaskLen* ] } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Deletes multicast groups configured with SSM mapping on each interface. | - |
| **interface** *port-type* *port-num* | Specifies the type and number of an interface. | - |
| *port-name* | Specifies the name of an interface. | - |
| *GrpAddr6* | Specifies a multicast group address. | The address ranges from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal format. |
| *GrpMaskLen* | Specifies the mask length of the multicast group address. | The value is an integer ranging from 8 to 128. |
| *SrcAddr6* | Specifies a multicast source address. | The address ranges from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal format. |
| *SrcMaskLen* | Specifies the mask length of the multicast source address. | The value is an integer ranging from 8 to 128. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used to clear records about all MLD groups that an interface dynamically joins, including common multicast groups and the multicast groups configured with Source-Specific Multicast (SSM) mapping.An interface can rejoin the multicast group after the records about this group are cleared.


Example
-------

# Delete all the groups that 100GE1/0/1 dynamically joins.
```
<HUAWEI> reset mld group interface 100GE 1/0/1 all

```

# Delete the multicast group FF03::101:0 from 100GE1/0/1.
```
<HUAWEI> reset mld group interface 100GE 1/0/1 ff03::101:0

```

# Clear the records about the groups that all the interfaces dynamically join.
```
<HUAWEI> reset mld group all

```

# Delete the SSM mapping policy for groups in the range of FF03::101:0 to FF03::101:FFFF on 100GE1/0/1.
```
<HUAWEI> reset mld group ssm-mapping interface 100 100GE1/0/1 ff03::101:0 112

```

# Delete the multicast groups in the range of FF03::101:0 to FF03::101:FFFF on 100GE1/0/1.
```
<HUAWEI> reset mld group interface 100GE 1/0/1 ff03::101:0 112

```