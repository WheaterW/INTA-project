display dfs-group consistency-check status
==========================================

display dfs-group consistency-check status

Function
--------



The **display dfs-group consistency-check status** command displays the status of consistency check on both devices in an M-LAG.




Format
------

**display dfs-group consistency-check status**


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

You can run the **display dfs-group consistency-check status** command to check the status of consistency check on both devices in an M-LAG.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the running status of M-LAG configuration consistency check.
```
<HUAWEI> display dfs-group consistency-check status
--------------------------------------------------------------------------------                        
Local Status : Enable                                                                                   
Peer Status  : Enable                                                                                   
--------------------------------------------------------------------------------                        
Configuration          Send times        Failed times                                                   
--------------------------------------------------------------------------------                        
BD                              0                   0                                                   
BDIF                            0                   0                                                   
VLAN                            2                   0                                                   
Port VLAN                       3                   0                                                   
VLAN instance                   1                   0                                                   
STP port                        3                   0                                                   
LACP                            2                   0                                                   
VLANIF                          1                   0                                                   
MLAG member number              3                   0                                                   
MAC aging                       1                   0                                                   
ARP aging                       1                   0                                                   
Static MAC                      1                   0                                                   
Static ARP                      1                   0
MLAG IP                         41                  0                                                                           
MLAG mode                       0                   0    
V-STP Enable                    1                   0
LACP M-LAG System-Id            1                   0
LACP M-LAG Priority             1                   0
STP Edged-port                  3                   0
LACP Mode                       2                   0
Peer-link STP                   2                   0
Exclude VLAN                    5                   0
Election mode                   1                   0
STP Vlan                        0                   0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs-group consistency-check status** command output
| Item | Description |
| --- | --- |
| Local Status | Whether the M-LAG configuration consistency check is enabled. |
| Peer Status | Whether the M-LAG configuration consistency check is enabled. |
| Configuration | Configuration type of M-LAG configuration consistency check:  BD.  BDIF.  VLAN.  Port VLAN.  VLAN instance.  STP port.  LACP.  VLANIF.  MLAG member number.  MAC aging.  ARP aging.  Static MAC.  Static ARP.  MLAG IP.  MLAG mode.  V-STP Enable.  LACP M-LAG System-Id.  LACP M-LAG Priority.  STP Edged-port.  LACP Mode.  Peer-link STP.  Exclude VLAN.  Election mode.  STP Vlan. |
| Send times | Number of times that the M-LAG local device successfully sends packets. |
| Failed times | Number of times that the M-LAG local device fails to send packets. |