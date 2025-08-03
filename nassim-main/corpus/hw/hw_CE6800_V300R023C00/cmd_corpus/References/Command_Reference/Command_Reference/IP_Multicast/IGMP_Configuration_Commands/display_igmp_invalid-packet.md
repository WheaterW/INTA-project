display igmp invalid-packet
===========================

display igmp invalid-packet

Function
--------



The **display igmp invalid-packet** command displays statistics about received invalid IGMP messages and details about these messages.




Format
------

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **invalid-packet** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **message-type** { **query** | **report** | **leave** } ] \*

**display igmp invalid-packet** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **message-type** { **query** | **report** | **leave** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays statistics about received invalid IGMP messages in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Displays statistics about received invalid IGMP messages in all instances. | - |
| **interface** *interface-type* | Displays statistics about invalid IGMP messages received by a specified interface type. | - |
| *interface-number* | Displays statistics about invalid IGMP messages received by a specified interface number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **message-type** | Displays statistics about received invalid IGMP messages of a specific message type. | - |
| **query** | Displays statistics about received invalid Query messages. | - |
| **report** | Displays statistics about received invalid Report messages. | - |
| **leave** | Displays statistics about received invalid Leave messages. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics and details about received invalid IGMP messages, run the **display igmp invalid-packet** command. The command output helps you locate and rectify IGMP faults.If IGMP entries fail to be generated on a multicast network, you can first run the **display igmp invalid-packet** command to check whether devices have received invalid IGMP messages. If the command output contains statistics about invalid IGMP messages, run the **display igmp invalid-packet verbose** command to view details about invalid IGMP messages to locate faults.Before using the **display igmp invalid-packet** command, note the following:

* If neither vpn-instance vpn-instance-name nor all-instance is specified, the command displays statistics about received invalid IGMP messages in the public network instance.
* If interface is specified, the command displays statistics about invalid IGMP messages received by the specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about received invalid IGMP messages in the public network instance.
```
<HUAWEI> display igmp invalid-packet

           Statistics of invalid packets for public net:
--------------------------------------------------------------------
IGMP Query invalid packet:
Unwanted Source List    : 1000        Zero Max Resp Code      : 0
Fault Length            : 1000        Invalid Multicast Group : 0
Bad Checksum            : 0

IGMP Report invalid packet:
Fault Length            : 0           Invalid Multicast Group : 0
Invalid Multicast Source: 0           Bad Checksum            : 0
Illegal Report Type     : 0

IGMP Leave invalid packet:
Invalid Multicast Group : 0           Bad Checksum            : 0
--------------------------------------------------------------------

```

**Table 1** Description of the **display igmp invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | VPN instance in which statistics about invalid IGMP messages are displayed. |
| IGMP Query invalid packet | Statistics about invalid IGMP Query messages. |
| IGMP Report invalid packet | Statistics about invalid IGMP Report messages. |
| IGMP Leave invalid packet | Statistics about invalid IGMP Leave messages. |
| Unwanted Source List | Messages with unwanted source lists. |
| Zero Max Resp Code | Number of IGMP messages whose Max Resp Code field is 0. |
| Fault Length | Messages with invalid lengths. |
| Invalid Multicast Group | Invalid multicast group addresses. |
| Invalid Multicast Source | Invalid multicast source addresses. |
| Bad Checksum | Messages with checksum errors. |
| Illegal Report Type | Number of messages with the illegal Report message type. |