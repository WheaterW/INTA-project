display msdp invalid-packet
===========================

display msdp invalid-packet

Function
--------



The **display msdp invalid-packet** command displays statistics about received invalid Multicast Source Discovery Protocol (MSDP) messages and details about these messages.




Format
------

**display msdp invalid-packet** [ **message-type** { **keepalive** | **notification** | **sa-request** | **sa-response** | **source-active** } | **peer** *peer-address* ] \*

**display msdp** { **all-instance** | **vpn-instance** *vpn-instance-name* } **invalid-packet** [ **message-type** { **keepalive** | **notification** | **sa-request** | **sa-response** | **source-active** } | **peer** *peer-address* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **message-type** | Displays statistics about invalid messages of a specified type. | - |
| **keepalive** | Displays statistics about received invalid Keepalive messages. | - |
| **notification** | Displays statistics about invalid Notification messages. | - |
| **sa-request** | Displays statistics about received invalid Source-Active Request messages. | - |
| **sa-response** | Displays statistics about received invalid Source-Active Response messages. | - |
| **source-active** | Displays statistics about received invalid Source-Active messages. | - |
| **peer** *peer-address* | Displays statistics about invalid MSDP messages received from a specified peer. peer-address specifies an MSDP peer address. | The value is in dotted decimal notation. |
| **all-instance** | Displays statistics about received invalid MSDP messages in all instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays statistics about received invalid MSDP messages in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics and details about received invalid MSDP messages, run the **display msdp invalid-packet** command. The command output helps you locate and rectify MSDP faults.If MSDP peer relationships fail to be set up on a multicast network, you can first run the **display msdp invalid-packet** command to check whether devices have received invalid MSDP messages.Before using the **display msdp invalid-packet** command, note the following:

* If vpn-instance vpn-instance-name is specified, the command displays statistics about received invalid MSDP messages in the specified vpn-instance instance.
* If peer peer-addr is specified, the command displays statistics about invalid MSDP messages received from the specified peer.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid MSDP messages received from a specified peer in the public network instance.
```
<HUAWEI> display msdp invalid-packet peer 1.1.1.1

             Statistics of invalid packets for public net:                      
--------------------------------------------------------------------            
MSDP SA invalid packet:
Fault Length            : 0           Bad Length-x            : 0
Bad Sprefix             : 0           Invalid Multicast Group : 0
Invalid Multicast Source: 0           Bad Encap Data          : 0
Illegal RP Addr         : 0           RP Loop                 : 0
MSDP SA Response invalid packet:
Fault Length            : 0           Bad Length-x            : 0
Bad Sprefix             : 0           Invalid Multicast Group : 0
Invalid Multicast Source: 0           Illegal RP Addr         : 0
RP Loop                 : 0
MSDP SA Request invalid packet:
Fault Length            : 0           Invalid Multicast Group : 0
MSDP Keep Alive invalid packet:
Fault Length            : 0
MSDP Notification invalid packet:
Fault Length            : 0                                                                           
--------------------------------------------------------------------

```

**Table 1** Description of the **display msdp invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | Instance in which statistics about received invalid MSDP messages are displayed. |
| MSDP SA invalid packet | Statistics about received invalid Source-Active (SA) messages. |
| MSDP SA Response invalid packet | Statistics about received invalid SA Response messages. |
| MSDP SA Request invalid packet | Statistics about received invalid SA Request messages. |
| MSDP Keep Alive invalid packet | Statistics about received invalid KeepAlive messages. |
| MSDP Notification invalid packet | Statistics about received invalid Notification messages. |
| Fault Length | Invalid message lengths. |
| Bad Length-x | Number of messages with invalid Length-x fields. |
| Bad Sprefix | Number of messages with invalid Sprefix fields. |
| Bad Encap Data | Number of messages with invalid data encapsulated. |
| Invalid Multicast Group | Invalid multicast group addresses. |
| Invalid Multicast Source | Invalid multicast source addresses. |
| Illegal RP Addr | Number of messages with invalid rendezvous point (RP) addresses. |
| RP Loop | Number of messages whose RP addresses are local addresses. |