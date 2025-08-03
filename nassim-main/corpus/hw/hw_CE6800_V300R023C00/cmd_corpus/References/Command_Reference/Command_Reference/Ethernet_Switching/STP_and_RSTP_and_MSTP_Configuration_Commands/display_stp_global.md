display stp global
==================

display stp global

Function
--------



The **display stp global** command displays global Spanning Tree Protocol (STP) information in a Multiple Spanning Tree Protocol (MSTP) process.




Format
------

**display stp global**


Parameters
----------

None

Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device has many interfaces, running the **display stp** command displays a large amount of information, which is challenging to query wanted information and global information quickly. Running the **display stp brief** command displays only information about spanning trees on interfaces, but not global information.To view global brief STP information in a specified MSTP process., run the display stp global command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief STP information of MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] display stp global
Protocol Status            : Enabled                                            
Bpdu-filter default        : Disabled                                           
Tc-protection              : Disabled                                           
Tc-protection threshold    : 1                                                  
Tc-protection interval     : 2s                                                 
Edged port default         : Enabled                                            
Pathcost-standard          : Dot1t                                              
Timer-factor               : 3                                                  
Transmit-limit             : 10                                                 
Bridge-diameter            : 7                                                  
CIST Global Information: 
  Mode                :MSTP
  CIST Bridge         :61440.00e0-fc12-3456
  Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  CIST Root/ERPC      :61440.00e0-fc12-3456 / 0
  CIST RegRoot/IRPC   :61440.00e0-fc12-3456 / 0
  CIST RootPortId     :0.0
  BPDU-Protection     :Disabled
  TC or TCN received  :85
  TC count per hello  :0
  STP Converge Mode   :Normal
  Share region-configuration :Enabled
  Time since last TC  :0 days 9h:12m:34s
  Number of TC        :13
  Topo Change Flag    :0

```

**Table 1** Description of the **display stp global** command output
| Item | Description |
| --- | --- |
| Protocol Status | Spanning Tree Protocol (STP) status:   * Enabled. * Disabled. |
| Bpdu-filter default | Whether the function of configuring device interfaces as bridge protocol data unit (BPDU) filter interfaces is enabled:   * Enabled. * Disabled. |
| Tc-protection | Topology change (TC) protection status:   * Enabled. * Disabled. |
| Tc-protection threshold | Maximum number of TC BPDUs that the MSTP device can process within a specified time. |
| Tc-protection interval | Time the MSTP device takes to process the maximum number of TC BPDUs. |
| Edged port default | Whether the function of configuring all ports of the switch as edge ports is enabled:   * Enabled. * Disabled. |
| Pathcost-standard | Method of calculating the MSTP path cost. |
| Timer-factor | Multiplier of Hello time. |
| Transmit-limit | Maximum number of BPDUs that the current interface can send each Hello time. For details, see stp transmit-limit. |
| Bridge-diameter | Network diameter of the MSTP. |
| CIST Bridge | Common and internal spanning tree (CIST) bridge ID.   * The 16 left-most bits represent the bridge's priority in the CIST. * The 48 right-most bits represent the bridge's MAC address. |
| CIST Root/ERPC | CIST root bridge ID/Cost of the external path (path from the switch to the CIST root bridge). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | ID of the CIST root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| CIST Global Information | CIST Global Information. |
| Mode | STP mode:   * STP. * RSTP. * MSTP. |
| Config Times | Manually configured BPDU parameters:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| Active Times | BPDUs parameters that are being used:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| BPDU-Protection | Whether BPDU protection is enabled:   * Disabled. * Enabled. |
| TC or TCN received | Number of received TC or TCN BPDUs. |
| TC count per hello | Number of TC BPDUs received each Hello time. |
| STP Converge Mode | STP convergence mode, which can be fast or normal. |
| Share region-configuration | Whether the MST region configuration is shared. |
| Time since last TC | Time past since the last topology changed. |
| Number of TC | Number of topology changes. |
| Topo Change Flag | Whether the topology is changed:   * 0: The topology is not changed. * 1: The topology is changed. |