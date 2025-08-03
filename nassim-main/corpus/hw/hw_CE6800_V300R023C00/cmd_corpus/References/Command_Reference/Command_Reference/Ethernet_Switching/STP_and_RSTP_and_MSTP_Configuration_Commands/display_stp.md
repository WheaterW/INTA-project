display stp
===========

display stp

Function
--------



The **display stp** command displays the status of and statistics about a spanning tree instance in a Multiple Spanning Tree Protocol (MSTP) process.




Format
------

**display stp** [ **instance** *instance-id* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* ] [ **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays the status of and statistics about a spanning tree instance.  If instance <instance-id> is not specified, the status of and statistics about all spanning tree instances will be displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| **interface** *interface-type* *interface-number* | Displays information of a spanning tree on a specified interface.  If interface <ifType> <ifNum> is not specified, the status of and statistics about all interfaces will be displayed in the sequence of the interface numbers. | - |
| **slot** *slot-id* | Specifies the number of the slot where the interface resides. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **brief** | Displays the brief status. | - |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The display stp command is used to check whether the spanning tree protocol is run on the specified MSTP process.

* If the Protocol Status field value is disabled, the spanning tree protocol is not run.
* If STP/RSTP/MSTP has been run, information such as the working mode of the spanning tree protocol will be displayed.When a network planner has deployed STP/RSTP/MSTP on the network, you can run the display stp command to check whether the configurations are correct and check the calculation result.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# When the stp enable command does not run, display the status of and statistics about STP on MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] display stp
Protocol Status       :Disabled
 Protocol Standard     :IEEE 802.1s
 Version               :3
 CIST Bridge Priority  :32768
 MAC address           :00e0-fc12-3456
 Max age(s)            :20
 Forward delay(s)      :15
 Hello time(s)         :2
 Max hops              :20

```

# After running the stp enable command, display the status of and statistics about STP of MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] display stp
CIST Global Information: 
  Mode                :MSTP
  CIST Bridge         :32768.200b-c739-1301
  Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  CIST Root/ERPC      :32768.0025-9e95-7c71 / 2000
  CIST RegRoot/IRPC   :32768.200b-c739-1301 / 0 (This bridge is the root)
  CIST RootPortId     :0.0
  BPDU-Protection     :Disabled
  TC or TCN received  :123
  TC count per hello  :0
  STP Converge Mode   :Normal
  Share region-configuration :Enabled
  Time since last TC  :0 days 17h:17m:39s
  Number of TC        :59
  Last TC occurred    :0
  Topo Change Flag    :0

```

**Table 1** Description of the **display stp** command output
| Item | Description |
| --- | --- |
| Protocol Status | Status of the protocol. |
| Protocol Standard | Standards of the protocol. |
| Version | Protocol version:   * 0: STP. * 2: RSTP. * 3: MSTP. |
| CIST Bridge Priority | Priority of the switch in CIST. |
| CIST Global Info | CIST global information. |
| CIST Bridge | ID of the CIST bridge.   * The 16 left-most bits are the priority of the switch in CIST. * The 48 right-most bits is the MAC address of the switch. |
| CIST Root/ERPC | CIST root bridge ID/External path cost (path cost from the switch to the CIST root bridge). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | CIST root port ID. "0.0" indicates that the switch is a root bridge and has no root port. |
| CIST Global Information | CIST Global Information. |
| MAC address | MAC address of the switch. |
| Max hops | Maximum hops in Multiple Spanning Tree (MST) region. |
| Max age(s) | Maximum lifecycle of the BPDU. |
| Forward delay(s) | Time interface status transition takes. |
| Hello time(s) | Interval at which BPDUs are sent from the root bridge. |
| Mode | The operation mode. The default mode is MSTP. |
| Config Times | Values configured manually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| Active Times | Values used actually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| BPDU-Protection | BPDU protection function:   * disabled. * enabled. |
| TC or TCN received | Number of received topology change (TC) or topology change notification (TCN) BPDUs. |
| TC count per hello | Number of TC BPDUs received within a hello interval. |
| TC or TCN send | Number of TC or TCN BPDUs sent by the port. |
| TC received | Number of received TC BPDUs. |
| STP Converge Mode | Convergence mode of the spanning tree protocol. |
| Share region-configuration | Whether the MST region configuration is shared. |
| Time since last TC | Period from the last topology change to now. |
| Number of TC | Number of topology changes. |
| Last TC occurred | Last TC occurred. |
| Topo Change Flag | Whether the topology is changed:   * 0: The topology is not changed. * 1: The topology is changed. |
| Port Protocol | The status of the port protocol:   * enable: STP is enabled on the port. * disable: STP is disabled on the port. |
| Port Role | Port role. In a CIST area, the port roles are as follows:   * CIST Disabled Port. * CIST Root Port. * CIST Designated Port. * CIST Alternate Port. * CIST Backup Port. |
| Port Priority | Priority of the port. |
| Port Edged | Edge port (specified by the administrator):   * Config: indicates the value configured using the stp edged-port command.   + Enabled: The current port is an edge port.   + Disabled: The current port is a non-edge port.   + Default: The edge port attribute of the current port is the default value. * Active: indicates the actual value obtained through dynamic negotiation.   + Enabled: The current port is an edge port.   + Disabled: The current port is a non-edge port. |
| Point-to-point | Link type of the port. Config indicates that the link type is configured using the stp point-to-point command. Active indicates the actual link type. |
| Transit Limit | Maximum number of the BPDUs sent by the current port before each Hello time expires. |
| Protection Type | Protection type , which can be:   * None: no protection. * LoopBack: self-loop detection. * BpduRoot: BPDU and root protection. * ROOT: root protection. * BPDU: BPDU protection. * Loop: loop protection. * BpduLoop: BPDU and loop protection. |
| Port STP Mode | STP mode on an interface. |
| Config-digest-snoop | Configuration digest snooping function: Displayed only after the stp config-digest-snoop command is configured to enable the configuration digest snooping function on the port. If the port does not have the function enabled, this field is not displayed.   * snooped=false: The configuration digest of the packets on the remote end is the same as that on the local end. * snooped=true: The configuration digest of the packets on the remote end is different from that on the local end. |
| Port Protocol Type | Format of the packets that the interface receives and sends:   * auto. * legacy. * dot1s.   The default value is auto.  Config indicates that the packet format is configured using the stp compliance command. Active indicates the actual packet format. |
| BPDU Encapsulation | Format of the BPDUs received and sent through a port. |
| PortTimes | Values in the BPDUs on the interface:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| BPDU Sent | Statistics about sent BPDUs:   * TCN: topology change notification. * Config: STP BPDUs. * RST: RSTP BPDUs. * MST: MSTP BPDUs. |
| BPDU Received | Statistics about received BPDUs. |
| Port Cost(Legacy) | Path cost of the port. It is calculated by dot1t algorithm.   * config: path cost manually configured. * active: actual path cost. |
| Port Id | Port ID. |
| Port Name | Port name. |
| Port State | Status of the port:   * Forwarding. * Discarding. * Down. * Disabled. * Learning. * Inactive. |
| Desg. Bridge/Port | ID of the designated switch and port. The 16 left-most bits of the switch ID represent the priority of the switch in the CIST region; the 48 right-most bits represent the MAC address of the switch. The left-most 4 bits of the port ID represent the priority and the right-most 12 bits represent the port number. |
| Message Age | BPDU lifetime. |
| MSTI Bridge ID | Multiple Spanning Tree instance (MSTI) bridge ID. |
| MSTI RegRoot/IRPC | MSTI root bridge ID/Internal path cost (path from the switch to the MSTI root). |
| MSTI RootPortId | ID of the MSTI root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| Master Bridge | ID of the bridge where the master interface resides.   * The 16 left-most bits represent the bridge's priority in the CIST. * The remaining 48 bits represent the bridge's MAC address. |
| Cost to Master | Cost of the path from the switch to the bridge where the master interface resides. 0 indicates that the master interface resides on the current bridge. |