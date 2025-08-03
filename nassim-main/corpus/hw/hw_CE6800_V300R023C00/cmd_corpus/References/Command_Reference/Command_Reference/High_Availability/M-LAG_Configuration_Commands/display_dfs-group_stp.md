display dfs-group stp
=====================

display dfs-group stp

Function
--------



The **display dfs-group stp** command displays STP information about all nodes in a DFS group.




Format
------

**display dfs-group** *dfs-group-id* **node** *node-id* **stp** **global**

**display dfs-group** *dfs-group-id* **node** *node-id* **stp** **brief**

**display dfs-group** *dfs-group-id* **node** *node-id* **stp** **m-lag** *m-lag-id*

**display dfs-group** *dfs-group-id* **node** *node-id* **stp** **m-lag** *m-lag-id* **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |
| **node** *node-id* | Specifies the ID of a node. | The value is an integer that ranges from 1 to 2. |
| **global** | Displays global information. | - |
| **brief** | Displays brief information. | - |
| **m-lag** *m-lag-id* | Specifies the ID of an M-LAG. | The value is an integer that ranges from 1 to 2048. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **display dfs-group stp** command to check STP information about all nodes in a DFS group or STP information about an M-LAG user-side interface.

**Precautions**



An M-LAG in VBST mode does not support STP configuration check or commands used to check STP configurations.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display global STP information about node 1 in DFS group 1.
```
<HUAWEI> display dfs-group 1 node 1 stp global
Protocol Status            :Enabled
Bpdu-filter default        :Disabled
Tc-protection              :Enabled
Tc-protection threshold    :1
Tc-protection interval     :2s
Edged port default         :Disabled
Pathcost-standard          :Dot1T
Timer-factor               :3
Transmit-limit             :6
Bridge-address             :00e0-fc12-3456                                                                                          
Priority                   :32768 
CIST Global Information:
  BPDU-Protection     :Disabled
  STP Converge Mode   :Normal

```

# Display brief STP information about node 1 in DFS group 1 of M-LAG 1.
```
<HUAWEI> display dfs-group 1 node 1 stp m-lag 1 brief
M-Lag ID     Interface      Port Protocol
       1     Eth-Trunk 47   Enabled

```

**Table 1** Description of the **display dfs-group stp** command output
| Item | Description |
| --- | --- |
| Protocol Status | Spanning Tree Protocol (STP) status:  Enabled.  Disabled. |
| Bpdu-filter default | Whether the function of configuring device interfaces as Bridge Protocol Data Unit (BPDU) filter interfaces is enabled:  Enabled.  Disabled. |
| Tc-protection | Topology change (TC) protection status:  Enabled.  Disabled. |
| Tc-protection threshold | Threshold of TC packets that the device can handle and immediately refresh forwarding entries in a given period. |
| Tc-protection interval | Time the device takes to handle a given number of TC packets and immediately refresh forwarding entries. |
| Edged port default | Whether the function of configuring all ports of the switch as edge ports is enabled:  Enabled.  Disabled. |
| Pathcost-standard | Method of calculating the MSTP path cost. |
| Timer-factor | Multiplier of Hello time. |
| Transmit-limit | Maximum number of BPDUs that the current interface can send per Hello time. |
| Bridge-address | STP bridge MAC address. |
| Priority | STP priority. |
| CIST Global Information | CIST global information. |
| BPDU-Protection | Whether BPDU protection is enabled:  Disabled.  Enabled. |
| STP Converge Mode | Convergence mode of STP, which can be fast or normal. |
| M-Lag ID | ID of the M-LAG. |
| Interface | User-side Eth-Trunk. |
| Port Protocol | STP protocol status of the interface:  Enabled.  Disabled. |