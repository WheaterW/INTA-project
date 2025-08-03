display evpn mac-duplication
============================

display evpn mac-duplication

Function
--------



The **display evpn mac-duplication** command displays information about MAC duplication suppression in all EVPN instances.

The **display evpn mac-duplication statistics** command displays statistics about MAC duplication suppression of all EVIs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display evpn mac-duplication** [ **statistics** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Enables the function to collect statistics about MAC address suppression of all EVPN instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring MAC duplication suppression, run the **display evpn mac-duplication** command to check information about MAC duplication suppression in all EVPN instances, including parameters related to MAC duplication suppression and information about suppressed MAC routes. You can run the **display evpn mac-duplication statistics** command to view statistics about MAC duplication suppression of all EVPN instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about MAC duplication suppression of all EVPN instances.
```
<HUAWEI> display evpn mac-duplication
Status codes: s - suppressed
  VPN-Instance Name and ID : 1, 1

  Detect loop-times       : 3
  Detect cycle(s)            : 600
  Retry cycle(s)              : 540
  Black Hole                 : Disabled

  Mac-address    BdTag/VlanId BdId     MTimes SuppressTime        LastSource
s 00e0-fc12-3456 0            1        3      2022-01-21 06:12:09 Eth-Trunk10.1
Status codes: s - suppressed
  VPN-Instance Name and ID : 2, 2

  Detect loop-times        : 3
  Detect cycle(s)             : 600
  Retry cycle(s)               : 540
  Black Hole                   : Disabled

```

# Display statistics about MAC duplication suppression of all EVPN instances.
```
<HUAWEI> display evpn mac-duplication statistics
Total number of suppressed mac-address : 8
----------------------------------------
EVPN-Instance Name     Suppressed Number
----------------------------------------
1                      3                
3                      1                
4                      1                
5                      2                
6                      1

```

**Table 1** Description of the **display evpn mac-duplication** command output
| Item | Description |
| --- | --- |
| Status codes | Status code. |
| VPN-Instance Name and ID | EVPN instance name and ID. |
| Detect loop-times | Threshold for the number of times a MAC route flaps. |
| Detect cycle(s) | Detection period. |
| Retry cycle(s) | Hold-off time to unsuppress MAC duplication. |
| Black Hole | Whether blackhole MAC route is enabled. |
| Mac-address | MAC address of the blackhole MAC route. |
| BdTag/VlanId | BD ID or VLAN ID. |
| BdId | BD ID. |
| MTimes | Number of MAC duplication suppression times. |
| SuppressTime | Date and time when MAC duplication was suppressed. |
| LastSource | Source port. |
| Total number of suppressed mac-address | Total number of MAC addresses suppressed in all EVPN instances. |
| EVPN-Instance Name | Name of the EVPN instance. |
| Suppressed Number | Number of times that suppression is performed. |