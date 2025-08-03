display evpn vpn-instance mac-duplication
=========================================

display evpn vpn-instance mac-duplication

Function
--------



The **display evpn vpn-instance mac-duplication** command displays information about suppression on MAC route flapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display evpn vpn-instance name** *vpn-instance-name* **mac-duplication** [ **bridge-domain** *bd-id* ] [ **mac-address** *mac-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *bd-id* | Displays a BD ID. | The value is an integer ranging from 1 to 16777215. |
| **mac-address** *mac-address* | Displays a MAC address. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **name** *vpn-instance-name* | Displays the name of an EVPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string.  This value should be the same as BD ID. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about MAC duplication suppression, run the **display evpn vpn-instance mac-duplication** command. The command output displays parameters related to MAC duplication suppression and information about the suppressed MAC routes.Note: For specifying specific MAC queries, BD needs to be specified for BD EVPN.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about MAC duplication suppression in PW scenarios.
```
<HUAWEI> display evpn vpn-instance name evpna mac-duplication
Status codes: s - suppressed
  VPN-Instance Name and ID : evpna, 5
  Detect loop-times        : 5
  Detect cycle(s)          : 180
  Retry cycle(s)           : 540
  Black Hole               : Disabled
 
  Mac-address    BdTag/VlanId BdId     MTimes SuppressTime        LastSource              
s 00e0-fc55-01c9 0            100      3      2020-04-08 14:47:16 PW<peerip:1.1.1.1 vcid:100 vctype:vlan>

```

# Display information about MAC duplication suppression.
```
<HUAWEI> display evpn vpn-instance name 100 mac-duplication
Status codes: s - suppressed
  VPN-Instance Name and ID : 100, 5
  Detect loop-times        : 5
  Detect cycle(s)          : 180
  Retry cycle(s)           : 540
  Black Hole               : Enabled
 
  Mac-address    BdTag/VlanId BdId     MTimes SuppressTime        LastSource              
s 00e0-fc55-01c9 0            100      3      2020-04-08 14:47:16 2001:DB8::1

```

**Table 1** Description of the **display evpn vpn-instance mac-duplication** command output
| Item | Description |
| --- | --- |
| Status codes | Status code. |
| VPN-Instance Name and ID | EVPN instance name and ID. |
| Detect loop-times | Threshold for the number of times a MAC route flaps. |
| Detect cycle(s) | Detection period. |
| Retry cycle(s) | Hold-off time to unsuppress MAC duplication. |
| Black Hole | Whether blackhole MAC route is enabled. |
| Mac-address | MAC address of the blackhole MAC route. |
| BdId | BD ID. |
| MTimes | Number of MAC duplication suppression times. |
| SuppressTime | Date and time when MAC duplication was suppressed. |
| LastSource | Source port. |
| BdTag | BD ID. |
| peerip | Peer IP Address of PW. |
| vcid | VC ID. |
| vctype | Encapsulation type of a PW. |