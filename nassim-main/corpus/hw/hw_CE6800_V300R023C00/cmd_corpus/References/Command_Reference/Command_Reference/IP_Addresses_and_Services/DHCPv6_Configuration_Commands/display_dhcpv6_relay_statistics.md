display dhcpv6 relay statistics
===============================

display dhcpv6 relay statistics

Function
--------



The **display dhcpv6 relay statistics** command displays packet statistics on a DHCPv6 relay agent.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 relay statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about the DHCPv6 relay agent with the specified interface type and number. | - |
| *interface-name* | Displays packet statistics on the DHCPv6 relay agent with a specified interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If a device is enabled with the DHCPv6 relay function, the system takes the statistics about DHCPv6 messages passing through the DHCP relay agent. After this command is run, you can view the statistics about DHCPv6 messages passing through the DHCP relay agent.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics about DHCPv6 messages on 100GE1/0/1.
```
<HUAWEI> display dhcpv6 relay statistics interface 100GE1/0/1
 Interface 100GE1/0/1 :                                                           
 MessageType              Receive          Send             Error               
 Solicit                  0                0                0                   
 Advertise                0                0                0                   
 Request                  0                0                0                   
 Confirm                  0                0                0                   
 Renew                    0                0                0                   
 Rebind                   0                0                0                   
 Reply                    0                0                0                   
 Release                  0                0                0                   
 Decline                  0                0                0                   
 Reconfigure              0                0                0                   
 Information-request      0                0                0                   
 Relay-forward            0                0                0                   
 Relay-reply              0                0                0                   
 UnknownType              0                0                0

```

**Table 1** Description of the **display dhcpv6 relay statistics** command output
| Item | Description |
| --- | --- |
| Interface | Interface enabled with DHCPv6-related functions. |
| MessageType | Type of DHCPv6 messages. |
| Receive | Number of received messages. |
| Send | Number of sent messages. |
| Error | Number of DHCPv6 messages that fail to be parsed. |