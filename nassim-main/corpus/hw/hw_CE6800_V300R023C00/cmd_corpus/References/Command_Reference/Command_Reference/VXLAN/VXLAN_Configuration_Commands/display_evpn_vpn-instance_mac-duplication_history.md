display evpn vpn-instance mac-duplication history
=================================================

display evpn vpn-instance mac-duplication history

Function
--------



The **display evpn vpn-instance mac-duplication history** command displays historical records of MAC route flapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display evpn vpn-instance name** *evpnName* **mac-duplication** **history**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *evpnName* | Specifies the name of an EVPN instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After MAC duplication suppression is configured, you can run the **display evpn vpn-instance mac-duplication history** command to view historical records about MAC duplication suppression, including parameters related to MAC duplication suppression and information about MAC duplication routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display historical records of MAC route flapping.
```
<HUAWEI> display evpn vpn-instance name bdevpn1 mac-duplication history
  VPN-Instance Name and ID : bdevpn1, 3

  Detect loop-times        : 5
  Detect cycle(s)          : 300
  Retry cycle(s)           : 300
  Black Hole               : Disabled 

  Mac-address    BdTag/VlanId BdId     MTimes    TimeStamp           CurrentLearn            LastLearn               
  00e0-fc12-3456 0            1        5         2022-08-23 12:18:41 Eth-Trunk1.1            2.2.2.2

```

**Table 1** Description of the **display evpn vpn-instance mac-duplication history** command output
| Item | Description |
| --- | --- |
| VPN-Instance Name and ID | EVPN instance name and ID. |
| Detect loop-times | Threshold for the number of times a MAC route flaps. |
| Detect cycle(s) | Detection period. |
| Retry cycle(s) | Hold-off time to unsuppress MAC duplication. |
| Black Hole | Whether blackhole MAC route is enabled. |
| Mac-address | MAC address that flaps. |
| BdTag/VlanId | BD ID/VLAN ID. |
| BdId | BD ID. |
| MTimes | Number of MAC duplication suppression times. |
| TimeStamp | Time when the last migration occurs. |
| CurrentLearn | Location of the learned MAC address. |
| LastLearn | Location of the MAC address that is learned last time. |