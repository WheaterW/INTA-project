display stp global (All views)
==============================

display stp global (All views)

Function
--------



The **display stp global** command displays global Spanning Tree Protocol (STP) information.




Format
------

**display stp global**


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



If a device has many interfaces, running the **display stp** command displays a large amount of information, which is challenging to query wanted information and global information quickly. Running the **display stp brief** command displays only information about spanning trees on interfaces, but not global information.To view global STP information conveniently, run the display stp global command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief STP information.
```
<HUAWEI> display stp global
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

**Table 1** Description of the **display stp global (All views)** command output
| Item | Description |
| --- | --- |
| Protocol Status | STP status:   * Enabled: STP is enabled. * Disabled: STP is disabled. |
| Bpdu-filter default | Whether the function of configuring a port as a BPDU filter port is enabled:   * Enabled: The function of configuring a port as a BPDU filter port is enabled. * Disabled: The function of configuring a port as a BPDU filter port is disabled. |
| Tc-protection | TC protection status:   * Enabled: TC protection is enabled. * Disabled: TC protection function is disabled. |
| Tc-protection threshold | Threshold for the maximum number of TC BPDUs that MSTP can process and immediately refresh forwarding entries per unit time. |
| Tc-protection interval | Time the MSTP device takes to process the maximum number of TC BPDUs. |
| Edged port default | Indicates whether the configuration is enabled.  Configure all ports on the device as edge ports.   * Enabled: All ports on the device are configured as edge ports. * Disabled: All ports on the device are disabled from being configured as edge ports. |
| Pathcost-standard | Method of calculating the MSTP path cost. |
| Timer-factor | Multiplier of Hello time. |
| Transmit-limit | Maximum number of BPDUs that the current interface can send each Hello time. For details, see stp transmit-limit. |
| Bridge-diameter | Network diameter of the MSTP. |
| CIST Bridge | Common and internal spanning tree (CIST) bridge ID.   * The 16 left-most bits represent the bridge's priority in the CIST. * The 48 right-most bits represent the bridge's MAC address. |
| CIST Root/ERPC | CIST root device ID/Cost of the external path (path from the local device to the CIST root device). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | ID of the CIST root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| CIST Global Information | CIST Global Information. |
| Mode | STP mode:   * STP. * RSTP. * MSTP. |
| Config Times | Manually configured BPDU parameters:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| Active Times | BPDUs parameters that are being used:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| BPDU-Protection | Whether BPDU protection is enabled:   * Disabled. * Enabled. |
| TC or TCN received | Number of received topology change (TC) or topology change notification (TCN) BPDUs. |
| TC count per hello | Number of TC BPDUs received each Hello time. |
| STP Converge Mode | Convergence mode of the Spanning Tree Protocol (STP), which can be fast or normal. |
| Share region-configuration | Whether the MST region configuration is shared. |
| Time since last TC | Period from the last topology change to now. |
| Number of TC | Number of topology changes. |
| Topo Change Flag | Flag indicating whether a topology change occurs:   * 0: No topology change occurs. * 1: A topology change occurs. |