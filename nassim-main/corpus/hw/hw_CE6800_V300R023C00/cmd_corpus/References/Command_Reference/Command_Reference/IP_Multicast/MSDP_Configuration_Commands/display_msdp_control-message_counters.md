display msdp control-message counters
=====================================

display msdp control-message counters

Function
--------



The **display msdp control-message counters** command displays statistics about received, sent, and discarded Multicast Source Discovery Protocol (MSDP) messages.




Format
------

**display msdp control-message counters** [ **message-type** { **data-packets** | **keepalive** | **notification** | **sa-request** | **sa-response** | **traceroute-reply** | **traceroute-request** | **unknown-type** | **source-active** } | **peer** *peer-address* ] \*

**display msdp** { **all-instance** | **vpn-instance** *vpn-instance-name* } **control-message** **counters** [ **message-type** { **data-packets** | **keepalive** | **notification** | **sa-request** | **sa-response** | **traceroute-reply** | **traceroute-request** | **unknown-type** | **source-active** } | **peer** *peer-address* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **message-type** | Displays statistics about MSDP messages of a specified type. | The MSDP message types include Source-Active, Source-Active Request, Source-Active Response, Keepalive, Notification, Traceroute Request, Traceroute Reply, Data Packets, and Unknown Type. |
| **data-packets** | Displays statistics about Data Packets messages. | - |
| **keepalive** | Displays statistics about KeepAlive messages. | - |
| **notification** | Displays statistics about Notification messages. | - |
| **sa-request** | Displays statistics about Source-Active Request messages. | - |
| **sa-response** | Displays statistics about Source-Active Response messages. | - |
| **traceroute-reply** | Displays statistics about Traceroute Reply messages. | - |
| **traceroute-request** | Displays statistics about Traceroute Request messages. | - |
| **unknown-type** | Displays statistics about Unknown Type messages. | - |
| **source-active** | Displays statistics about Source-Active messages. | - |
| **peer** *peer-address* | Displays statistics about MSDP messages of a specified MDSP peer.  peer-address specifies the IP address an MSDP peer. | The value is in dotted decimal notation. |
| **all-instance** | Displays statistics about MSDP messages in all instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays statistics about MSDP messages in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Before using the **display msdp control-message counters** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command displays statistics about MSDP messages in the public network instance.
* If peer peer-address is specified, the command displays statistics about MSDP messages of a specified MSDP peer.
* If message-type is specified, the command displays statistics about MSDP messages of a specified type.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about MSDP messages of the peer 3.3.3.3 in the public network instance.
```
<HUAWEI> display msdp control-message counters peer 3.3.3.3
 VPN-Instance: public net
 MSDP message counters for peer: 3.3.3.3
                          Received         Sent             Invalid
 Source-Active            0                0                0
 Source-Active Request    0                0                0
 Source-Active Response   0                0                0
 KeepAlive                48               49               0
 Notification             0                1                0
 Traceroute Request       0                -                -
 Traceroute Reply         0                -                -
 Data Packets             0                0                0
 Unknown Type             1                -                1

```

**Table 1** Description of the **display msdp control-message counters** command output
| Item | Description |
| --- | --- |
| MSDP message counters for peer | IP address of the MSDP peer. |
| Received | Number of received messages. |
| Sent | Number of sent messages. |
| Invalid | Number of discarded messages. |
| Source-Active | Statistics about Source-Active messages. |
| Source-Active Request | Statistics about Source-Active Request messages. |
| Source-Active Response | Statistics about Source-Active Response messages. |
| KeepAlive | Statistics about KeepAlive messages. |
| Notification | Notification message. |
| Traceroute Request | Statistics about Traceroute Request messages. |
| Traceroute Reply | Statistics about Traceroute Reply messages. |
| Data Packets | Statistics about Data Packets messages. |
| Unknown Type | Statistics about Unknown Type messages. |
| VPN-Instance | Instance in which MSDP message statistics are displayed. |