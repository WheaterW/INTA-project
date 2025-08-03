reset igmp group
================

reset igmp group

Function
--------



The **reset igmp group** command deletes records about IGMP groups that interfaces dynamically join or information about multicast groups that are configured with source-specific multicast (SSM) mapping.




Format
------

**reset igmp group** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr4* [ **mask** { *GrpMask* | *GrpMaskLen* } ] [ *SrcAddr4* [ **mask** { *SrcMask* | *SrcMaskLen* } ] ] } }

**reset igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr4* [ **mask** { *GrpMask* | *GrpMaskLen* } ] [ *SrcAddr4* [ **mask** { *SrcMask* | *SrcMaskLen* } ] ] } }

**reset igmp group ssm-mapping** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr4* [ **mask** { *GrpMask* | *GrpMaskLen* } ] } }

**reset igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** **ssm-mapping** { **all** | **interface** { *port-type* *port-num* | *port-name* } { **all** | *GrpAddr4* [ **mask** { *GrpMask* | *GrpMaskLen* } ] } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all IGMP groups. | - |
| **interface** *port-type* *port-num* | Specifies the type and number of an interface. | - |
| *port-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *GrpAddr4* | Specifies the address of a multicast group. | The address is in dotted decimal notation and ranges from 224.0.0.0 to 239.255.255.255. |
| **mask** | Indicates the mask of a multicast source address or group address. | - |
| *GrpMask* | Specifies the mask of a multicast group address. | The address is in dotted decimal notation and ranges from 240.0.0.0 to 255.255.255.255. |
| *GrpMaskLen* | Specifies the mask length of a multicast group address. | The value is an integer ranging from 4 to 32. |
| *SrcAddr4* | Specifies a multicast source address. | The address is in dotted decimal notation. |
| *SrcMask* | Specifies the mask of a multicast source address. | The address is in dotted decimal notation and ranges from 240.0.0.0 to 255.255.255.255. |
| *SrcMaskLen* | Specifies the mask length of a multicast source address. | The value is an integer ranging from 0 to 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Indicates all instances. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is valid only for IGMP groups that interfaces dynamically join.Before using the reset igmp group command without ssm-mapping, note the following:

* If neither vpn-instance nor all-instance is specified, the command deletes records about IGMP groups that interfaces in the public network instance dynamically join.
* If the **reset igmp group all** command is used, the command deletes records about all IGMP groups that all interfaces of the device dynamically join.
* If interface interface-type interface-number all is specified, the command deletes records about all IGMP groups that a specified interface dynamically joins.
* If GrpAddr4 is specified, the command deletes records about a specified IGMP group.
* If SrcAddr4 is specified, the command deletes records about the IGMP groups of a specified source address.
* An interface can rejoin the IGMP group after records about this group are deleted.Before using the **reset igmp group ssm-mapping** command, note the following:
* If neither vpn-instance nor all-instance is specified, the command deletes information about multicast groups that are configured with SSM mapping in the public network instance.
* If all is specified, the command deletes information about all multicast groups that are configured with SSM mapping.
* If interface port-type port-number is specified, the command deletes information about multicast groups configured with SSM mapping on a specified interface.
* If both interface and GrpAddr4 are specified, the command deletes information about the specified multicast group configured with SSM mapping on a specified interface.

Example
-------

# Delete records of all IGMP groups on VLANIF 1 in the public network instance.
```
<HUAWEI> reset igmp group interface vlanif 1 all

```

# Delete information about multicast groups that are configured with SSM mapping rules on all interfaces.
```
<HUAWEI> reset igmp group ssm-mapping all

```

# Clear records about IGMP groups that all interfaces in the public network instance dynamically join.
```
<HUAWEI> reset igmp group all

```

# Delete records of the IGMP groups with the group address 225.0.0.1 on VLANIF 1 in the public network instance.
```
<HUAWEI> reset igmp group interface Vlanif 1 225.0.0.1

```

# Delete records of IGMP groups 225.1.1.0 through 225.1.1.255 on VLANIF 1 in the public network instance.
```
<HUAWEI> reset igmp group interface Vlanif 1 225.1.1.0 mask 255.255.255.0

```