reset igmp control-message counters
===================================

reset igmp control-message counters

Function
--------



The **reset igmp control-message counters** command deletes statistics about IGMP messages.




Format
------

**reset igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **message-type** { **query** | **report** } ]

**reset igmp control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **message-type** { **query** | **report** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all instances. | - |
| **interface** *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies the name of an interface. | - |
| **message-type** | Indicates an IGMP message type. | An IGMP message can a Query or Report message. |
| **query** | Indicates Query messages. | - |
| **report** | Indicates Report messages. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before using the **reset igmp control-message counters** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command deletes statistics about IGMP messages in the public network instance.
* If interface is specified, the command deletes statistics about IGMP messages on the specified interface.
* If both message-type and interface are specified, the command deletes statistics about a specified type of IGMP messages on the specified interface.Deleting statistics about IGMP messages does not affect the normal running status of IGMP.

Example
-------

# Clear statistics about IGMP messages on VLANIF 1 in the public network instance.
```
<HUAWEI> reset igmp control-message counters interface Vlanif 1

```

# Delete statistics about IGMP messages on all interfaces in the public network instance.
```
<HUAWEI> reset igmp control-message counters

```