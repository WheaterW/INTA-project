display pim ipv6 invalid-packet message-type
============================================

display pim ipv6 invalid-packet message-type

Function
--------



The **display pim ipv6 invalid-packet message-type** command displays statistics about invalid IPv6 PIM messages received by a device and details of these messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 invalid-packet message-type** { **register** | **register-stop** | **crp** }

**display pim ipv6 vpn-instance** *vpn-instance-name* **invalid-packet** **message-type** { **register** | **register-stop** | **crp** }

**display pim ipv6 all-instance invalid-packet message-type** { **register** | **register-stop** | **crp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **register** | Displays statistics about invalid Register messages. | - |
| **register-stop** | Displays statistics about invalid Register-Stop messages. | - |
| **crp** | Displays statistics about invalid Candidate-Rendezvous Point (C-RP) messages. | - |
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

If IPv6 PIM entries fail to be generated on a multicast network, you can run the **display pim ipv6 invalid-packet** command first to check whether devices have received invalid IPv6 PIM messages.You can run the **display pim ipv6 invalid-packet message-type** command to view statistics about invalid IPv6 PIM messages received by a device in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid Register PIM IPv6 messages received in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] display pim ipv6 invalid-packet message-type register
                                                                                
             Statistics of invalid packets for public net:                      
--------------------------------------------------------------------   
Invalid PIM Register packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0           
Invalid Dest Addr       : 0           
--------------------------------------------------------------------

```

# Display statistics about invalid Register-Stop PIM IPv6 messages received in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] display pim ipv6 invalid-packet message-type register-stop
                                                                                
             Statistics of invalid packets for public net:                      
--------------------------------------------------------------------   
Invalid PIM Register-Stop packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0           
Invalid Dest Addr       : 0           IP Source not RP        : 0           
--------------------------------------------------------------------

```

# Display statistics about invalid C-RP PIM IPv6 messages received in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] display pim ipv6 invalid-packet message-type crp
                                                                                
             Statistics of invalid packets for public net:                      
--------------------------------------------------------------------   
Invalid PIM CRP packet:
Invalid Dest Addr       : 0           Invalid CRP Addr        : 0           
Fault Length            : 0           CRP Adv Fault Length    : 0           
Invalid Multicast Group : 0           
--------------------------------------------------------------------

```

**Table 1** Description of the **display pim ipv6 invalid-packet message-type** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | VPN instance to which statistics about invalid IPv6 PIM messages belong. |
| Invalid PIM Register packet | Statistics about invalid IPv6 PIM Register messages. |
| Invalid Multicast Source | Messages with invalid multicast source addresses. |
| Invalid Multicast Group | Messages with invalid multicast group addresses. |
| Invalid Dest Addr | Invalid destination addresses. |
| Invalid PIM Register-Stop packet | Number of invalid IPv6 PIM Register-Stop messages. |
| Invalid PIM CRP packet | Number of invalid IPv6 PIM CRP messages. |
| Invalid CRP Addr | Number of messages with invalid C-RP addresses. |
| IP Source not RP | Number of messages whose source addresses are not the RP address. |
| CRP Adv Fault Length | Messages whose CRP Adv fields are of invalid lengths. |
| Fault Length | Number of messages with invalid lengths. |
| command | Command line used. |