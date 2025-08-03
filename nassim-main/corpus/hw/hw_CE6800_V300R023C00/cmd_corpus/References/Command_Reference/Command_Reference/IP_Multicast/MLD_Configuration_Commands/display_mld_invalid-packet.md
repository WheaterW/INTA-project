display mld invalid-packet
==========================

display mld invalid-packet

Function
--------



The **display mld invalid-packet** command displays statistics about invalid Multicast Listener Discovery (MLD) messages received by a device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld invalid-packet** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **message-type** { **query** | **report** | **done** } ] \*

**display mld** { **vpn-instance** *vpn-instance-name* | **all-instance** } **invalid-packet** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **message-type** { **query** | **report** | **done** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about invalid MLD messages received by a specified interface. interface-type interface-number specifies the interface type and interface number. | - |
| **message-type** | Displays statistics about invalid MLD messages of a specific type. | - |
| **query** | Displays statistics about invalid Query messages. | - |
| **report** | Displays statistics about invalid Report messages. | - |
| **done** | Displays statistics about invalid Done messages. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display mld invalid-packet** command to view statistics of invalid MLD messages for fault location and rectification.If MLD entries fail to be generated on a multicast network, you can run the **display mld invalid-packet** command first to check whether devices have received invalid MLD messages.You can run the following related commands to view information about specific invalid MLD messages:

* Run the **display mld invalid-packet** command to view statistics about invalid MLD messages received by a device.
* Run the display mld invalid-packet interface command to view statistics about invalid MLD messages received by a specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid MLD messages received by a device in the public network instance.
```
<HUAWEI> display mld invalid-packet
         Statistics of invalid packets for public net:                      
- -------------------------------------------------------------------
MLD Query invalid packet:
Unwanted Source List    : 1000        Zero Max Resp Code      : 0
Fault Length            : 1000        Invalid Multicast Group : 0
Bad Checksum            : 0
MLD Report invalid packet:
Fault Length            : 0           Invalid Multicast Group : 0
Invalid Multicast Source: 0           Bad Checksum            : 0
Illegal Report Type     : 0
MLD Done invalid packet:
Invalid Multicast Group : 0           Bad Checksum            : 0            
- -------------------------------------------------------------------

```

**Table 1** Description of the **display mld invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | VPN instance in which statistics about invalid MLD messages need to be displayed. |
| MLD Query invalid packet | Invalid MLD Query messages. |
| MLD Report invalid packet | Invalid MLD Report messages. |
| MLD Done invalid packet | Invalid MLD Done messages. |
| Unwanted Source List | Messages with unwanted source lists. |
| Zero Max Resp Code | Messages with the Max Resp Code fields being 0. |
| Fault Length | Messages with invalid lengths. |
| Invalid Multicast Group | Invalid multicast group addresses. |
| Invalid Multicast Source | Invalid multicast source addresses. |
| Bad Checksum | Messages with checksum errors. |
| Illegal Report Type | Messages with the illegal Report message type. |