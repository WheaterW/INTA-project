display ipv6 nd proxy packet statistics
=======================================

display ipv6 nd proxy packet statistics

Function
--------



The **display ipv6 nd proxy packet statistics** command displays statistics about the current proxy ND.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd proxy packet statistics** [ **slot** *slot-num* | **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-num* | Specifies a slot ID. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | * interface-type: specifies the type of a specified interface. The value is a string of case-insensitive characters and does not contain spaces. * interface-number: specifies the number of an interface. The value is a string of case-insensitive characters and does not contain spaces. An interface number is in the format of slot number/subcard number/port number. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about the current proxy ND, run the **display ipv6 nd proxy packet statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the current proxy ND.
```
<HUAWEI> display ipv6 nd proxy packet statistics
Received NS Packet Statistics:
- -----------------------------------
Total              : 0
Destination IP
Unicast            : 0
Multicast          : 0
- -----------------------------------
Dropped NS Packet Statistics:
- -----------------------------------
Total              : 0
No Route           : 0
No Nd              : 0
Rate Limit         : 0
Other              : 0
- -----------------------------------
Sent NA Packet Statistics:
- -----------------------------------
Total              : 0
AnywayProxy        : 0
RouteProxy         : 0
InnerVlanProxy     : 0
InterVlanProxy     : 0
- -----------------------------------

```

**Table 1** Description of the **display ipv6 nd proxy packet statistics** command output
| Item | Description |
| --- | --- |
| Received NS Packet Statistics | Received NS packet statistics. |
| Total | Total number of packets. |
| Unicast | Number of NS messages with a unicast address as the destination address. |
| Multicast | Number of NS messages with a multicast address as the destination address. |
| Dropped NS Packet Statistics | Dropped NS packet statistics. |
| No Route | Number of NS messages discarded due to a lack of routes. |
| No Nd | Number of NS messages discarded due to a lack of ND entries. |
| Rate Limit | Number of NS messages discarded due to rate limit. |
| Other | Number of NS messages discarded due to other reasons. |
| Sent NA Packet Statistics | Sent NA packet statistics. |
| AnywayProxy | Number of NA messages sent in any proxy ND mode. |
| RouteProxy | Number of NA messages sent in routed proxy ND mode. |
| InnerVlanProxy | Number of NA messages sent in intra-VLAN proxy ND mode. |
| InterVlanProxy | Number of NA messages sent in inter-VLAN proxy ND mode. |