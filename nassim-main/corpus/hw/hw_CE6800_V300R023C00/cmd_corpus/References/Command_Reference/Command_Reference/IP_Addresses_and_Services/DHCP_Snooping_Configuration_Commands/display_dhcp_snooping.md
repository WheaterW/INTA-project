display dhcp snooping
=====================

display dhcp snooping

Function
--------



The **display dhcp snooping** command displays DHCP snooping running information.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display dhcp snooping** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **bridge-domain** *bd-id* ]

For CE6820H, CE6820H-K, CE6820S, CE6885-LL (low latency mode):

**display dhcp snooping** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays DHCP snooping running information on a specified interface. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| **vlan** *vlan-id* | Displays DHCP snooping running information in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Displays DHCP snooping running information in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dhcp snooping** command to view DHCP snooping running information. If no interface, VLAN, or BD is specified, global DHCP snooping running information is displayed. If an interface, VLAN, or BD is specified, DHCP snooping running information on the specified interface, in the specified VLAN, or in the specified BD is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display global DHCP snooping running information.
```
<HUAWEI> display dhcp snooping
 DHCP snooping global running information :
 DHCPv4 snooping                          : Enable
 Static user max number                   : 1024
 Current static user number               : 1
 Dhcp user(dhcpv4) max number             : 8192
 Current dhcpv4 user number               : 0
 Alarm threshold                          : 5
 Check dhcp-rate                          : Disable  (default)
 Dhcp-rate limit(pps)                     : 5000     (default)
 Alarm dhcp-rate                          : Disable  (default)
 Alarm dhcp-rate threshold                : 100      (default)
 Bind-table autosave                      : Disable  (default)
 Client position transfer allowed         : Enable   (default)
 Server record                            : Disable  (default)
 Check server-vlan                        : Disable  (default)
 DHCP snooping packet-flow log            : Disable  (default)
 Offline remove mac-address               : Disable  (default)
 Arp detect                               : Disable  (default)

 DHCP snooping running information for interface 10GE1/0/1 :
 DHCP snooping                              : Enable
 Trusted interface                          : No       (default)
 Dhcp user(dhcpv4) max number               : 8192
 Current dhcpv4 user number                 : 0
 Check dhcp-giaddr                          : Enable
 Check dhcp-chaddr                          : Disable  (default)
 Alarm dhcp-chaddr                          : Enable
 Alarm dhcp-chaddr threshold                : 5
 Discarded dhcp packets for check chaddr    : 0
 Check dhcp-request                         : Disable  (default)
 Alarm dhcp-request                         : Enable
 Alarm dhcp-request threshold               : 5
 Discarded dhcp packets for check request   : 0
 Alarm dhcp-reply                           : Enable
 Alarm dhcp-reply threshold                 : 5
 Discarded dhcp packets for check reply     : 3

```

**Table 1** Description of the **display dhcp snooping** command output
| Item | Description |
| --- | --- |
| DHCP snooping global running information | Global running information about DHCP snooping. |
| DHCP snooping | Whether DHCP snooping is enabled on the interface or in the VLAN.  To enable DHCP snooping, run the dhcp snooping enable command. |
| DHCP snooping packet-flow log | Whether the log function is enabled for DHCP packet exchange.  To configure this function, run the dhcp snooping packet-flow log enable command. |
| DHCPv4 snooping | Whether DHCPv4 snooping is enabled globally.  To enable DHCP snooping, run the dhcp snooping enable command. |
| Static user max number | Maximum number of static users. |
| Current static user number | Number of current static users. |
| Current dhcpv4 user number | Number of online DHCPv4 users. |
| Dhcp user(dhcpv4) max number | Maximum number of DHCPv4 snooping binding entries. |
| Alarm threshold | Global alarm threshold for the number of discarded DHCP snooping messages.  To set the alarm threshold, run the dhcp snooping alarm threshold command. |
| Alarm dhcp-chaddr | Whether the device is enabled to generate an alarm when the number of DHCPv4 Request messages discarded because the CHADDR field in the DHCPv4 Request message does not match the MAC address in the frame header reaches the alarm threshold.  To configure this function, run the dhcp snooping alarm dhcp-chaddr enable command. |
| Alarm dhcp-chaddr threshold | Specifies the alarm threshold for the number of DHCP messages discarded because the CHADDR field in DHCPv4 Request messages does not match the MAC address in the frame header. An alarm is generated when the number of discarded DHCP messages exceeds the alarm threshold.  To configure this function, run the dhcp snooping alarm dhcp-chaddr threshold command. |
| Alarm dhcp-request | Whether the device is enabled to generate an alarm when the number of DHCPv4 request packets discarded because they do not match the binding entries reaches the threshold.  To configure this function, run the dhcp snooping alarm dhcp-request enable command. |
| Alarm dhcp-request threshold | Specifies the alarm threshold for the number of DHCPv4 request packets discarded because they do not match the DHCP snooping binding entries. An alarm is generated when the number of discarded DHCPv4 request packets exceeds the alarm threshold.  To configure this function, run the dhcp snooping alarm dhcp-request threshold command. |
| Alarm dhcp-reply | Whether the device is enabled to generate an alarm when the number of DHCPv4 Response messages discarded by untrusted interfaces from the DHCPv4 server reaches the threshold.  To configure this function, run the dhcp snooping alarm dhcp-reply enable command. |
| Alarm dhcp-reply threshold | Specifies the alarm threshold for the number of DHCPv4 response messages discarded by untrusted interfaces from the DHCPv4 server. An alarm is generated when the number of discarded DHCPv4 response messages exceeds the threshold.  To configure this function, run the dhcp snooping alarm dhcp-reply threshold command. |
| Alarm dhcp-rate | Whether the alarm function for checking the rate of sending DHCP messages to the DHCP stack is enabled.  To enable this function, run the dhcp snooping alarm dhcp-rate enable command. |
| Alarm dhcp-rate threshold | Alarm threshold for the number of DHCP messages sent to the DHCP protocol stack. An alarm is generated when the number of discarded DHCP messages reaches the threshold.  To enable this function, run the dhcp snooping alarm dhcp-rate threshold command. |
| Check server-vlan | Whether the DHCP snooping-enabled device is enabled to check VLAN IDs in DHCP reply packets.  To configure this function, run the dhcp snooping check server-vlan enable command. |
| Check dhcp-giaddr | Whether the device is enabled to check whether the GIADDR field in a DHCP Request message is 0.  To configure this function, run the dhcp snooping check dhcp-giaddr enable command. |
| Check dhcp-chaddr | Whether the device is enabled to check whether the CHADDR field in a DHCP Request message matches the source MAC address in the Ethernet frame header.  To enable this function, run the dhcp snooping check dhcp-chaddr enable command. |
| Check dhcp-request | Whether an interface is enabled to check DHCP Request messages.  To configure this parameter, run the dhcp snooping check dhcp-request enable command. |
| Check dhcp-rate | Whether the function of checking the rate of sending DHCP messages is enabled.  To enable this function, run the dhcp snooping check dhcp-rate enable command. |
| Dhcp-rate limit(pps) | Rate limit of DHCP messages, in pps.  To configure this function, run the dhcp snooping check dhcp-rate command. |
| Bind-table autosave | Whether a device is enabled to save the DHCP snooping binding table.  To enable this function, run the dhcp snooping user-bind autosave command. |
| Client position transfer allowed | Whether location transition is enabled for DHCP snooping users.  To configure this function, run the dhcp snooping user-transfer enable command. |
| Server record | Whether detection of DHCP servers is enabled globally.  To configure this function, run the dhcp snooping server record command. |
| Offline remove mac-address | Whether the device is enabled to delete the MAC address entry of a user when the DHCP snooping entry is deleted.  To configure this function, run the dhcp snooping user-offline remove mac-address command. |
| Arp detect | Whether association between ARP and DHCP snooping is enabled.  To configure this function, run the dhcp snooping user-bind arp-detect enable command. |
| Trusted interface | Whether an interface is a trusted interface.  To configure this function, run the dhcp snooping trusted command. |
| Discarded dhcp packets for check chaddr | Number of DHCPv4 Request packets whose CHADDR field does not match the MAC address in the frame header. After the alarm is generated, the counter is cleared and recounted. |
| Discarded dhcp packets for check request | Number of discarded DHCPv4 request packets that do not match binding entries. After the alarm is generated, the counter is cleared and recounted. |
| Discarded dhcp packets for check reply | Number of DHCPv4 response packets discarded by untrusted interfaces from the server. After the alarm is generated, the counter is cleared and recounted. |