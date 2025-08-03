display smart-link flush
========================

display smart-link flush

Function
--------



The **display smart-link flush** command displays information about received Flush packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display smart-link flush**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before running the **reset smart-link flush** command to clear Flush packet statistics, run the display smart-link flush command to view information about received Flush packets. The information helps you learn about the primary and secondary link status and locate faults on interfaces.

**Prerequisites**

A Smart Link group on a downstream device has been enabled to send Flush packets using **flush send** command, and an interface on an upstream device has been enabled to receive Flush packets using the **smart-link flush receive** command.

**Follow-up Procedure**

Run the **reset smart-link flush** command to clear Flush packet statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about received Flush packets.
```
<HUAWEI> display smart-link flush
Receive flush packets count:               1191                                    
Receive last flush interface:              100GE1/0/1
Receive last flush packet time:            02:42:37 UTC-03:00 DST 2013/01/27    
Receive last flush packet source MAC:      00e0-fc12-3456                       
Receive last flush packet control VLAN ID: 311

```

**Table 1** Description of the **display smart-link flush** command output
| Item | Description |
| --- | --- |
| Receive flush packets count | Number of received Flush packets. |
| Receive last flush interface | Interface that received the latest Flush packet. |
| Receive last flush packet time | Time and data that the latest Flush packet was received. The format is HH:MM:SS UTC+HH:MM DST YYYY/MM/DD. |
| Receive last flush packet source MAC | Source MAC address of the latest received Flush packet. |
| Receive last flush packet control VLAN ID | Control VLAN ID of the latest received Flush packet. |