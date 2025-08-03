display erps
============

display erps

Function
--------



The **display erps** command displays information about ERPS rings and ports that are added to the ERPS rings.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display erps** [ **ring** *ring-id* ] [ **verbose** ]

**display erps ring** *ring-id* **exchange-vlan**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ring** *ring-id* | Displays information about a specified ERPS ring and ports that are added to the ERPS ring. | The value is an integer ranging from 1 to 255. |
| **verbose** | Displays detailed information about ERPS rings and ports that are added to the ERPS rings. | - |
| **exchange-vlan** | Displays the VLAN exchange information of an ERPS ring. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To monitor the network running status and maintain devices on a Layer 2 network running ERPS, run the **display erps** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about ERPS 1 and ports that are added to ERPS 1.
```
<HUAWEI> display erps ring 1
D  : Discarding
F  : Forwarding
R  : RPL Owner
N  : RPL Neighbour
FS : Forced Switch
MS : Manual Switch
Ring  Control  WTR Timer  Guard Timer  Port 1               Port 2              
ID    VLAN     (min)      (csec)
--------------------------------------------------------------------------------
   1      100          1           50  (D)10GE1/0/1           (F,R)10GE1/0/1
--------------------------------------------------------------------------------

```

# Display detailed information about all ERPS rings and ports that are added to the ERPS rings.
```
<HUAWEI> display erps verbose
Ring ID                             : 101
Description                         : Ring 101
Control Vlan                        : 1001
Protected Instance                  : 4091 
WTR Timer Setting (min)             : 1      Running (s)           : 0  
Guard Timer Setting (csec)          : 200    Running (csec)        : 0  
Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0  
WTB Timer Running (csec)            : 0  
Ring State                          : Idle
RAPS_MEL                            : 7
Revertive Mode                      : Revertive
R-APS Channel Mode                  : -
Version                             : 2
Sub-ring                            : No 
Forced Switch Port                  : -
Manual Switch Port                  : -
TC-Notify                           : -
Time since last topology change     : 0 days 0h:31m:49s
--------------------------------------------------------------------------------
Port                Port Role     Port Status     Signal Status
--------------------------------------------------------------------------------
100GE1/0/1             Common        Discarding      Non-failed      
100GE1/0/2             Common        Forwarding      Non-failed      

Ring ID                             : 102
Description                         : Ring 102
Control Vlan                        : 1002
Protected Instance                  : 4092 
WTR Timer Setting (min)             : 1      Running (s)           : 0  
Guard Timer Setting (csec)          : 200    Running (csec)        : 0  
Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0  
WTB Timer Running (csec)            : 0  
Ring State                          : Idle
RAPS_MEL                            : 7
Revertive Mode                      : Revertive
R-APS Channel Mode                  : -
Version                             : 2
Sub-ring                            : No 
Forced Switch Port                  : -
Manual Switch Port                  : -
TC-Notify                           : -
Time since last topology change     : 0 days 4h:12m:20s
--------------------------------------------------------------------------------
Port                Port Role     Port Status     Signal Status
--------------------------------------------------------------------------------
100GE1/0/1             Common        Forwarding      Non-failed      
100GE1/0/2             RPL Owner     Discarding      Non-failed

```

# Display detailed information about ERPS ring 1 and ports that are added to ERPS ring 1.
```
<HUAWEI> display erps ring 1 verbose
Ring ID                             : 1
Description                         : Ring 102
Control Vlan                        : 1002
Protected Instance                  : 4092 
Service Vlan                        : 200 to 400
WTR Timer Setting (min)             : 1      Running (s)           : 0  
Guard Timer Setting (csec)          : 200    Running (csec)        : 0  
Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0  
WTB Timer Running (csec)            : 0  
Ring State                          : Idle
RAPS_MEL                            : 7
Revertive Mode                      : Revertive
R-APS Channel Mode                  : -
Version                             : 2
Sub-ring                            : No 
Forced Switch Port                  : -
Manual Switch Port                  : -
TC-Notify                           : -
Time since last topology change     : 0 days 4h:13m:40s
--------------------------------------------------------------------------------
Port                Port Role     Port Status     Signal Status
--------------------------------------------------------------------------------
100GE1/0/1             Common        Forwarding      Non-failed      
100GE1/0/2             RPL Owner     Discarding      Non-failed

```

**Table 1** Description of the **display erps** command output
| Item | Description |
| --- | --- |
| D : Discarding | The port is in the Discarding state. |
| F : Forwarding | The port is in the Forwarding state. |
| R : RPL Owner | The port is the RPL owner port. |
| N : RPL Neighbour | The port is the RPL neighbor port. |
| FS : Forced Switch | The port is blocked by an FS operation. |
| Forced Switch Port | Port that has been blocked by an FS operation. A hyphen (-) indicates that no port has been blocked by an FS operation.  For details on how to configure an FS mode, see erps ring protect-switch or port protect-switch. |
| MS : Manual Switch | The port is blocked by an MS operation. |
| Manual Switch Port | Port that has been blocked by an MS operation. A hyphen (-) indicates that no port has been blocked by an MS operation.  For details on how to configure an FS mode, see erps ring protect-switch or port protect-switch. |
| Ring ID | ID of the ERPS ring. |
| Ring State | Status of the ERPS ring:   * idle: The current blocking point is the RPL owner port. * protection: A fault has occurred on a link or a device. * pending: It is a transitional state in the ERPS ring negotiation. For example, the blocking point is being switched back to the RPL owner port. * ForcedSwitch: It is the FS mode for blocking an ERPS port. * ManualSwitch: It is the MS mode for blocking an ERPS port. |
| Control VLAN | Control VLAN. For details on how to configure the control VLAN, see control vlan. |
| WTR Timer Setting (min) | Value of the WTR timer. Setting refers to the set value, whereas Running refers to the actual running value. For details on how to configure the WTR timer, see wtr-timer. |
| Guard Timer Setting (csec) | Value of the guard timer. Setting refers to the set value, whereas Running refers to the actual running value. For details on how to configure the guard timer, see guard-timer. |
| Port 1 | A port that is added to the specified ERPS ring. |
| Port 2 | Another port that is added to the specified ERPS ring. |
| Port | Port that is added to the ERPS ring. |
| Port Role | Port role:   * RPL owner. * Common. * RPL Neighbour. |
| Port Status | Port status:   * Forwarding. * Discarding. |
| Description | Description of an ERPS ring. For details on how to configure the description, see description. |
| Protected Instance | ERP instance. For details on how to configure the ERP instance, see protected-instance. |
| Running (s) | Value of the actual running. |
| Running (csec) | Value of the actual running. |
| Running (deciseconds) | Value of the actual running. |
| Holdoff Timer Setting (deciseconds) | Value of the hold-off timer. Setting refers to the set value, whereas Running refers to the actual running value. For details on how to configure the WTR timer, see holdoff-timer. |
| WTB Timer Running (csec) | Value of the WTB timer. |
| RAPS\_MEL | Maintenance entity group level (MEL) value. For details on how to configure the MEL value, see raps-mel. |
| Revertive Mode | Revertive or non-revertive switching mode to be used after an ERPS link fault recovers.   * Revertive: re-blocks the RPL owner port after an ERPS link fault recovers. * Non-revertive: retains the RPL owner port status and still blocks the port of the faulty link after an ERPS link fault recovers.   For details on how to configure the revertive or non-revertive switching mode, see revertive. |
| R-APS Channel Mode | Ring Auto Protection Switching (R-APS) PDU transmission mode on a sub-ring.   * -: The current ring is not a sub-ring. * Virtual Channel: The sub-ring uses VCs to transmit R-APS PDUs. * Non-virtual-channel: The sub-ring uses NVCs to transmit R-APS PDUs.   For details on how to configure the R-APS PDU transmission mode on a sub-ring, see virtual-channel. |
| Version | ERPS version:   * 1: ERPSv1. * 2: ERPSv2.   For details on how to configure the ERPS version, see version. |
| Sub-ring | ERPS sub-ring ID. For details on how to configure an ERPS sub-ring ID, see sub-ring. |
| TC-Notify | The ERPS ring is configured to notify other ERPS rings of its topology change. A hyphen (-) indicates that the ERPS ring does not notify other ERPS rings when its topology changes.  For details on how to configure the topology change notification function, see tc-notify erps ring. |
| Time since last topology change | Time past since the last topology changed. |
| Signal Status | Signal status:   * Failed. * Non-failed. |
| Service Vlan | Service VLAN associated with ERPS.  The service VLANs are mapped to protected instances and do not contain the control VLAN. |