display ipv6 interface
======================

display ipv6 interface

Function
--------



The **display ipv6 interface** command displays IPv6 information about an interface.

The **display ipv6 interface description** command displays brief information on and descriptions of IPv6-related interfaces.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 interface** [ *interface-name* | *interface-type* *interface-number* ]

**display ipv6 interface description** [ *interface-name* | *interface-type* [ *interface-number* ] | **slot** *slot-number* [ **card** *card-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the interface name. If no interface name is specified, the command displays brief information on and descriptions of all IPv6-related interfaces. | - |
| *interface-type* | Specifies the interface type. If no interface type is specified, the command displays brief information on and descriptions of all IPv6-related interfaces. | The value is of the enumerated type. |
| *interface-number* | Specifies the interface number, which is used with interface-type to identify an interface. If no interface number is specified, the command displays brief information on and descriptions of all IPv6-related interfaces of the specified interface type. | - |
| **slot** *slot-number* | Specifies the slot number. If this parameter is not specified, the command displays brief information and descriptions of all IPv6-related interfaces. | - |
| **card** *card-number* | Specifies the interface subcard number. If no interface subcard number is specified, the command displays brief information on and descriptions of all IPv6-related interfaces on the specified slot. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If an interface is assigned an IPv6 address, run the **display ipv6 interface** command to view the IPv6 status and configuration on this interface.To view brief information on and descriptions of IPv6-related interfaces, run the **display ipv6 interface description** command.

**Follow-up Procedure**

You can run the **display interface description** command to view the description of the interface.You can run the **display interface** command to view detailed information about the operation and statistics of the interface.

**Precautions**

Ensure that the designated interfaces are assigned IPv6 addresses; otherwise, you cannot view information on the interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information on and descriptions of IPv6-related interfaces.
```
<HUAWEI> display ipv6 interface description
Codes:
      d(dampened),            D(down),                *D(administratively down),
      !D(FIB overload down),  ^D(standby),            l(loopback),
      s(spoofing),            U(up)
------------------------------------------------------------------------------
Number of interfaces whose physical status is Up: 1
Number of interfaces whose physical status is Down: 0
Number of interfaces whose protocol status is Up: 1
Number of interfaces whose protocol status is Down: 0

Interface                    Physical  Protocol  Description
100GE1/0/8                   U         U
[IPv6 Address/Prefix Length] 2001:db8:3c4d::/48

```

# Display tagged IPv6 information on a VLANIF interface.
```
<HUAWEI> display ipv6 interface Vlanif 1
Vlanif1 current state : UP 
IPv6 protocol current state : UP
IPv6 is enabled, link-local address is FE80::3AB8:6EFF:FE11:300
  Global unicast address(es):
    2001:DB8::1, subnet is 2001:DB8::/64 tag 1
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:1
    FF02::1:FF11:300
  MTU is 1500 bytes 
  ND DAD is enabled, number of DAD attempts: 1
  ND NUD is enabled, number of NUD attempts: 3
  ND NUD interval is 1000 milliseconds
  ND reachable time is 1200000 milliseconds
  ND stale time is 1200 seconds
  ND retransmit interval is 1000 milliseconds
  ND RAs are halted 
  ND Proxy is disabled

```

# Display IPv6 information on 100GE 1/0/8.
```
<HUAWEI> display ipv6 interface 100GE 1/0/8
100GE1/0/8 current state : UP current state : UP
IPv6 protocol current state : UP
IPv6 is enabled, link-local address is FE80::3AB8:6EFF:FE11:300
  Global unicast address(es):
    2001:DB8::1, subnet is 2001:DB8::/64
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:1
    FF02::1:FF11:300
  MTU is 1500 bytes
  ND DAD is enabled, number of DAD attempts: 1
  ND NUD is enabled, number of NUD attempts: 3
  ND NUD interval is 1000 milliseconds
  ND reachable time is 1200000 milliseconds
  ND stale time is 1200 seconds
  ND retransmit interval is 1000 milliseconds
  ND RAs are halted
  ND Proxy is disabled

```

**Table 1** Description of the **display ipv6 interface** command output
| Item | Description |
| --- | --- |
| current state | Physical status of the interface.   * UP. * DOWN. * Administratively DOWN. |
| IPv6 is enabled | The IPv6 capability is configured on the interface. |
| IPv6 protocol current state | Protocol status of the interface.   * UP. * DOWN. * Administratively DOWN. |
| IPv6 Address | IPv6 address of an interface. |
| link-local address | Link local address configured for that interface. |
| Global unicast address(es) | All unicast addresses configured on that interface.   * If the value is [DUPLICATE], the IPv6 address of the interface conflicts with that of a peer interface. * If the value is [TENTATIVE], IPv6 address detection has not completed. * If the value is [BLOCK], an IPv6 address same as this interface address has existed on the device. * If the involved ND entry does not exist, the ND entry fails to be created. |
| Joined group address(es) | All multicast addresses that have joined the interface. |
| MTU | MTU of the interface. |
| ND NUD interval | Neighbor unreachable detection interval. |
| ND reachable time | Time period for a neighbor to keep reachable. |
| ND stale time | Timeout period of the STALE state of ND entries. |
| ND retransmit interval | Retransmission interval. |
| ND RAs are halted | RA messages are suppressed. |
| ND Proxy is disabled | Proxy ND function is not enabled. |
| number of DAD attempts | Number of conflicting address detection times. |
| number of NUD attempts | Number of times neighbor unreachable detection. |
| Number of interfaces whose physical status is Up | Number of interfaces with the physical status of Up. |
| Number of interfaces whose protocol status is Up | Number of interfaces with the link layer protocol of Up. |
| Number of interfaces whose physical status is Down | Number of interfaces with the physical status of Down. |
| Number of interfaces whose protocol status is Down | Number of interfaces with the link layer protocol of Down. |
| Interface | Interface type and number. |
| Physical | Physical status of an interface. |
| Protocol | Link layer protocol status of an interface. |
| Description | Description of an interface. A long interface description is displayed across several rows. For a default situation, no information is displayed in this field. |
| tag | Route matching tag. |
| Codes | Abbreviations of the physical status and link protocol status. Abbreviated physical status of the interface is as follows:  * U: The physical status of the interface is Up. U(l): The interface is enabled with the loopback function. * D: The physical status of the interface is Down. * \*D: An administrator has run the shutdown command on the interface. * !D: The FIB module is in the overload suspension state. The link layer protocol of the interface goes Down. * ^D: The interface is in the standby state. * E: The Eth-Trunk interface goes Down due to E-Trunk protocol negotiation.  Abbreviated link layer protocol status is as follows:  * U: The status of the link layer protocol on the interface is Up. U(s): The link layer protocol of the interface is Up even though the interface is not assigned an IPv6 address. (s): An inherent attribute of the interface that will be displayed when the interface is assigned an IPv6 address. U(d): The protocol module of the interface is dampened. * D: The link layer protocol of the interface is Down or no IPv6 address is assigned to the interface. |
| Prefix Length | Prefix length of an interface address. |