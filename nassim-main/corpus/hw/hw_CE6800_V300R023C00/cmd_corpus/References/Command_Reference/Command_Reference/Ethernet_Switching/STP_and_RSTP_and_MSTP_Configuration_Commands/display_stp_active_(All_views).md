display stp active (All views)
==============================

display stp active (All views)

Function
--------



The **display stp active** command displays the status of and statistics on spanning trees of all Up interfaces.




Format
------

**display stp active**


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



To view information about spanning trees on all Up interfaces, run the display stp active command.



**Precautions**



In a multi-instance scenario, a PW interface's STP state does not take effect for any MSTP instance with a non-0 ID. For such an instance, its actual STP state is the same as instance 0's STP state.The actual STP state of an interface bound to a process in link-share mode is the same as that of the interface bound to a process in no-link-share mode.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about spanning trees on all Up interfaces.
```
<HUAWEI> display stp active
CIST Global Information: 
  Mode                :MSTP
  CIST Bridge         :32768.38ba-38b1-5302
  Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  CIST Root/ERPC      :32768.38ba-38b1-5302 / 0 (This bridge is the root)
  CIST RegRoot/IRPC   :32768.38ba-38b1-5302 / 0 (This bridge is the root)
  CIST RootPortId     :0.0
  BPDU-Protection     :Disabled
  TC or TCN received  :0
  TC count per hello  :0
  STP Converge Mode   :Normal
  Share region-configuration :Enabled
  Time since last TC  :0 days 0h:0m:0s
  Number of TC        :0
  Topo Change Flag    :0

CIST Port Information: 
  Port Id             :1
  Port Name           :100GE1/0/1
  Port State          :Discarding
  Port Protocol       :Enabled
  Port Role           :Designated Port
  Port Priority       :128
  Port Cost(Dot1T)    :Config=auto / Active=200
  Designated Bridge/Port   :32768.38ba-38b1-5302 / 128.1
  Port Edged          :Config=default / Active=disabled
  Point-to-point      :Config=auto / Active=true
  Transit Limit       :6 packets/s         
  Protection Type     :LoopBack
  Port STP Mode       :MSTP
  Port Protocol Type  :Config=auto / Active=dot1s
  BPDU Encapsulation  :Config=stp / Active=stp
  PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
  TC or TCN send      :0
  TC or TCN received  :0
  BPDU Sent           :120
           TCN: 0, Config: 0, RST: 0, MST: 120
  BPDU Received       :120
           TCN: 0, Config: 0, RST: 0, MST: 120
  Message Age         :0

MSTI 1 Global Information:
  MSTI Bridge ID      :32768.38ba-38b1-5302
  MSTI RegRoot/IRPC   :32768.38ba-38b1-5302 / 0 (This bridge is the root)
  MSTI RootPortId     :0.0
  Master Bridge       :32768.38ba-38b1-5302
  Cost to Master      :0
  TC received         :0
  TC count per hello  :0
  Time since last TC  :0 days 0h:0m:0s
  Number of TC        :0
  Topo Change Flag    :0

MSTI 1 Port Information:
  Port Id             :1
  Port Name           :100GE1/0/1
  Port State          :Discarding
  Port Role           :Designated Port
  Port Priority       :128
  Port Cost(Dot1T)    :Config=auto / Active=200
  Desg. Bridge/Port   :32768.38ba-38b1-5302 / 128.1
  Port Times          :RemHops 20
  TC or TCN send      :0
  TC or TCN received  :0

```

**Table 1** Description of the **display stp active (All views)** command output
| Item | Description |
| --- | --- |
| CIST Bridge | Common and internal spanning tree (CIST) bridge ID.   * The 16 left-most bits represent the bridge's priority in the CIST. * The 48 right-most bits represent the bridge's MAC address. |
| CIST Root/ERPC | CIST root bridge ID/Cost of the external path (path from the switch to the CIST root bridge). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | ID of the CIST root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| CIST Global Information | CIST Global Information. |
| CIST Port Information | CIST Port Information. |
| Mode | Mode of the spanning tree protocol:   * STP. * RSTP. * MSTP. |
| Config Times | Manually configured BPDU parameters:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| Active Times | BPDUs parameters that are actually used:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * MaxHop: maximum number of hops in the MST region. |
| BPDU-Protection | Whether BPDU protection is enabled:   * disabled. * enabled. |
| TC or TCN received | Number of received topology change (TC) or topology change notification (TCN) BPDUs. |
| TC count per hello | Number of TC BPDUs received each Hello time. |
| TC or TCN send | Number of TC or TCN BPDUs sent on the interface. |
| TC received | Number of received TC BPDU. |
| STP Converge Mode | Convergence mode of the Spanning Tree Protocol (STP), which can be fast or normal. |
| Time since last TC | Time past since the last topology changed. |
| Number of TC | Number of topology changes. |
| Topo Change Flag | Whether a topology change occurs:   * 0: No topology change occurs. * 1: A topology change occurs. |
| Port Protocol | STP status on the interface:   * Enabled: STP is enabled on the interface. * Disabled: STP is disabled on the interface. |
| Port Role | Role of an interface. In the CIST region, the roles of interfaces are as follows:   * Root Port. * Designated Port. * Alternate Port. * Backup Port. |
| Port Priority | Interface priority. For details, see stp port priority. |
| Port Edged | Whether the edge port (specified by the administrator) is enabled:   * enabled. * disabled. Config indicates the value configured using the.  stp edged-port command, and.  Active indicates the value in use. |
| Port STP Mode | STP mode of the interface. |
| Port Protocol Type | Format of packets sent and received by the interface:   * auto. * legacy. * dot1s. The default value is. auto.  Config indicates the packet format configured using the.  stp compliance command, and.  Active indicates the packet format in use. |
| Port Cost(Dot1T) | Path cost (calculated by dot1t) of an interface:   * Config: configured path cost. * Active: path cost that is being used. |
| Port Id | Interface ID. |
| Port Name | Interface name. |
| Port State | Interface status:  -Forwarding.  -Discarding.  -Down.  -Disabled.  -Learning.  -Inactive. |
| Designated Bridge/Port | Designated bridge ID/Port ID. The 16 left-most bits represent the bridge's priority in the CIST region, and the 48 right-most bits represent the bridge's MAC address. The first 4 bits of the port ID represent the port's priority, and the last 12 bits represent the port number. |
| Point-to-point | Link type of the interface. Config indicates the link type configured using the stp point-to-point command, and Active indicates the link type in use. |
| Transit Limit | Maximum number of BPDUs that the current interface can send every second. For details, see stp transmit-limit. |
| Protection Type | Protection type:   * root-protection: Protection takes effect only on the designated interface. * loop-protection: Protection takes effect only on the root port or alternate interface. |
| BPDU Sent | Statistics about sent BPDUs:   * TCN: TCN packet. * Config: STP packet. * RST: RSTP packet. * MST: MSTP packet. |
| BPDU Received | Statistics on received BPDUs. |
| BPDU Encapsulation | Format of BPDUs that are sent and received on the interface. |
| Message Age | Life time of the BPDU. |
| MSTI Bridge ID | MSTI bridge ID. |
| MSTI RegRoot/IRPC | MSTI root bridge ID/Cost of the internal path (path from the switch to the MSTI root bridge). |
| MSTI RootPortId | ID of the MSTI root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| MSTI 1 Global Information | All information about MSTI 1. |
| MSTI 1 Port Information | MSTI 1 Port Information. |
| Master Bridge | ID of the bridge where the master interface resides.   * The 16 left-most bits represent the bridge's priority in the CIST. * The 48 right-most bits represent the bridge's MAC address. |
| Cost to Master | Cost of the path from the local device to the bridge where the master interface is located. 0 indicates that the master interface is located at the current bridge. |
| Desg. Bridge/Port | Designated bridge ID/Port ID. The 16 left-most bits represent the bridge's priority in the CIST region, and the 48 right-most bits represent the bridge's MAC address. The first 4 bits of the port ID represent the port's priority, and the last 12 bits represent the port number. |
| PortTimes/Port Times | BPDU parameters of the interface:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifetime of a BPDU. * FwDly: time interface status transition takes. * Remhop: maximum number of hops in the MST region. |