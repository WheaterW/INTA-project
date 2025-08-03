display igmp interface
======================

display igmp interface

Function
--------



The **display igmp interface** command displays IGMP configurations and state information on interfaces.




Format
------

**display igmp interface** [ *interface-type* *interface-number* | *interface-name* ] [ **verbose** ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **interface** [ *interface-type* *interface-number* | *interface-name* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Displays IGMP configurations and state information on an interface that has the specified type and number.  interface-type interface-number specifies the type and number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **verbose** | Displays detailed IGMP configurations and state information. | - |
| **vpn-instance** *vpn-instance-name* | Displays IGMP configurations and state information in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-instance** | Displays IGMP configurations and state information in all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check IGMP interface's status or locate faults in IGMP interfaces, run the **display igmp interface** command to view IGMP configurations and state information on interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IGMP configurations and state information on interfaces in the public network instance.
```
<HUAWEI> display igmp interface 100GE 1/0/1
Interface information of VPN Instance: public net
 100GE1/0/1(192.168.101.2):
   IGMP is enabled
   Current IGMP version is 2
   IGMP state: up
   IGMP group policy: none
   IGMP limit: -
   Query interval for IGMP (negotiated): -
   Query interval for IGMP (configured): 60 s
   Other querier timeout for IGMP: 0 s
   Maximum query response time for IGMP: 10 s
   Querier for IGMP: 192.168.101.2 (this router)
   Total 1 IGMP Group reported

```

**Table 1** Description of the **display igmp interface** command output
| Item | Description |
| --- | --- |
| Interface information of VPN Instance | Instance in which IGMP configurations and state information are displayed. |
| IGMP is enabled | Indicates that IGMP has been enabled on an interface using the igmp enable command. |
| IGMP state | Status of an IGMP interface.   * up: indicates that the IGMP status is Active. * down: indicates that the IGMP status is Inactive. |
| IGMP group policy | Number of an ACL used in an IGMP group policy to control the number of groups that an interface can join.  The ACL is applied to the IGMP group policy using the igmp group-policy command.  If the displayed value in the IGMP group policy field is not none, the groups that the hosts can join have been specified, and IGMP filters Report messages of hosts according to the ACL. If the multicast group G is not included in the groups specified in the ACL, modify or delete the ACL to ensure that members of G can be served. |
| IGMP limit | Maximum number of IGMP entries. |
| Current IGMP version | IGMP version configured using the igmp version command. |
| Query interval for IGMP (negotiated) | Interval negotiated by non-queriers for sending Query messages, in seconds.  The negotiated value is supported by IGMPv3 only. |
| Query interval for IGMP (configured) | Configured interval at which an interface sends IGMP Query messages, in seconds. The value is specified using the igmp timer query command. |
| Other querier timeout for IGMP | Keepalive period of other IGMP queriers. The value decreases by one per second. The timeout period can be set by using the igmp timer other-querier-present command. The value is 0 on the interface that functions as the querier. |
| Querier for IGMP | IGMP querier In IGMPv1, a querier is selected based on the multicast routing protocol; in IGMPv2, the router with the lowest IP address acts as the querier on a shared network segment. |
| Total 1 IGMP Group reported | Number of IGMP groups that this interface dynamically joins, not including IGMP groups that this interface statically joins. The value increases by one when a new interface joins and decreases by one when an interface leaves. |
| 100GE1/0/1(192.168.101.2) | Interface Name. |