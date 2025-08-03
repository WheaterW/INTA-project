display stp vlan information
============================

display stp vlan information

Function
--------



The **display stp vlan information** command displays the spanning tree status of an interface that joins a VLAN.




Format
------

**display stp vlan** [ *vlan-id* ] **information** [ **brief** | **global** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays the spanning tree status of an interface that joins a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **brief** | Displays the status of and brief information about the spanning tree. | - |
| **global** | Displays global brief information about the spanning tree. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a VLAN is configured on an interface and the VBST function is enabled, you can run this command to check the spanning tree status of an interface that joins the VLAN. At this time, you do not need to pay attention to the mapping between VLANs and instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of and brief information about the spanning tree of the device running VBST.
```
<HUAWEI> display stp vlan 10 information

VLAN 10 information:
--------------------------------------------------------------------------------
Global information:
    Protocol Status            : Enabled
    Bpdu-filter Default        : Disabled
    Bpdu-protection            : Disabled
    Tc-protection              : Disabled
    Tc-protection Threshold    : 1
    Tc-protection Interval(s)  : 10
    Edged Port Default         : Disabled
    Path Cost Standard         : Dot1T
    Timer Factor               : 3
    Transit Limit              : 6
    Bridge Diameter            : 7
    Bridge ID                  : 4106.0025-9e95-7c21
    Config Times               : Hello 2s MaxAge 20s FwDly 15s 
    Active Times               : Hello 2s MaxAge 20s FwDly 15s 
    Root ID/RPC                : 4106.0025-9e95-7c21 / 0
    RootPortId(InterfaceName)  : 0.0 (This bridge is the root)
    Root Type                  : Secondary
Port information:
    Port ID   : 58
    Interface : 100GE1/0/1
        STP State                      : Forwarding
        Port Role                      : Designated Port
        Port Priority                  : 128
        Path Cost Standard             : Dot1T
        Port Cost(Config/Active)       : 0 / 200
        Desg. Bridge/Port              : 4106.0025-9e95-7c21 / 128.58
        Port Edged(Config/Active)      : Default / Enabled
        Point-to-point(Config/Active)  : Auto / True
        Port Revert Slow               : Disabled
        Port Agreement Legacy          : Disabled
        Transit Limit                  : 6 packets/hello
        Protection Type                : None
    Port ID   : 63
    Interface : 100GE1/0/2
        STP State                      : Forwarding
        Port Role                      : Designated Port
        Port Priority                  : 128
        Path Cost Standard             : Dot1T
        Port Cost(Config/Active)       : 0 / 200
        Desg. Bridge/Port              : 4106.0025-9e95-7c21 / 128.63
        Port Edged(Config/Active)      : Default / Disabled
        Point-to-point(Config/Active)  : Auto / True
        Port Revert Slow               : Disabled
        Port Agreement Legacy          : Disabled
        Transit Limit                  : 6 packets/hello
        Protection Type                : None
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display stp vlan information** command output
| Item | Description |
| --- | --- |
| VLAN | VLAN ID. |
| Protocol Status | Protocol status.   * Enabled: The protocol is enabled. * Disabled: The protocol is disabled. |
| Bpdu-filter Default | Indicates whether to specify all ports of a device as BPDU filter ports. For details, see stp bpdu-filter default.   * Enabled: All ports of a device are specified as BPDU filter ports. * Disabled: All ports of a device are specified as non-BPDU filter ports. |
| Bpdu-protection | Indicates whether to enable the BPDU protection function. For details, see stp bpdu-protection.   * Enabled: The BPDU protection function is enabled. * Disabled: The BPDU protection function is disabled. |
| Tc-protection | Indicates whether to enable the TC protection function. For details, see stp tc-protection.   * Enabled: The TC protection function is enabled. * Disabled: The TC protection function is disabled. |
| Tc-protection Threshold | Maximum number of TC BPDUs that a device processes within a specified period. For details, see stp tc-protection threshold. |
| Tc-protection Interval(s) | Time for a device to process the maximum number of TC BPDUs. For details, see stp tc-protection interval. |
| Edged Port Default | Indicates whether to configure ports on a device as edge ports. For details, see stp edged-port default.   * Enabled: Ports on a device are configured as edge ports. * Disabled: Ports on a device are configured as non-edge ports. |
| Port ID | Port ID. |
| Port Role | Role of the port. In the CIST region, the roles of ports are as follows:   * Root port. * Designated port. * Alternate port. * Backup port. |
| Port Priority | Priority of the port. To set the priority of the port, run the stp port priority command. |
| Port Cost(Config/Active) | Interface path cost value:   * Config indicates the manually configured path cost value. * Active indicates the actual path cost value. |
| Port Edged(Config/Active) | Edge port specified by the administrator:   * Enabled: indicates that the edge port is enabled. * Disabled: indicates that the edge port is not enabled.   Config indicates the value configured by the stp edged-port command; Active indicates the actual value. |
| Port Revert Slow | The delay in revertive switching during VBST calculation on a port:   * Enabled: The delay in revertive switching is enabled. * Disabled: The delay in revertive switching is disabled.   To specify the parameter, run the stp revertive slow command. |
| Port Agreement Legacy | Whether the interface discards non-standard STP/RSTP packets sent by the HanDreamnet switch:   * Enabled: The interface discards non-standard STP/RSTP packets sent by the HanDreamnet switch. * Disabled: The interface does not discard non-standard STP/RSTP packets sent by the HanDreamnet switch. |
| Path Cost Standard | Standard for calculating the path cost:   * dot1d-1998. * Dot1T. * legacy. |
| Timer Factor | Timer factor of the timeout period of a device to the Hello Time. For details, see stp timer-factor. |
| Transit Limit | Maximum number of BPDUs that each interface sends per second. For details, see stp transmit-limit (system view) and stp transmit-limit (interface view). |
| Bridge ID | Bridge ID:  The value consists of the device priority add VLAN ID and MAC address, which are separated by a dot. |
| Bridge Diameter | Bridge Diameter. |
| Config Times | Time values in manually configured bridge protocol information:   * Hello: indicates the interval for sending BPDUs. * MaxAge: indicates the maximum lifetime of BPDUs. * FwDly: indicates the delay for interface status transition. |
| Active Times | Time values in actual bridge protocol information:   * Hello: indicates the interval for sending BPDUs. * MaxAge: indicates the maximum lifetime of BPDUs. * FwDly: indicates the delay for interface status transition. |
| Root ID/RPC | CIST root device ID or external cost of the path from the device to the CIST root device. |
| Root Type | Root bridge type.   * Normal. * Secondary. * Primary. |
| RootPortId(InterfaceName) | ID of the CIST root port.  "0.0" indicates that the device is the root device without the root port. |
| Interface | Interface number. |
| STP State | Interface status. In the CIST region, the statuses of interfaces are as follows:   * FORWARDING. * LEARNING. * DISCARDING. |
| Desg. Bridge/Port | Designated switch ID and designated port ID. Desg.Bridge indicates "device priority + VLAN ID"."MAC address of the local switch". Port indicates "port priority"."port number". |
| Point-to-point(Config/Active) | Link type of the port. Config indicates the link type configured by the stp point-to-point command; Active indicates the actual link type. |
| Protection Type | Protection type:   * root-protection. * loop-protection. * loopback. * bpdu. * bpdu/root. * bpdu/loop. * pvidconsistency. |