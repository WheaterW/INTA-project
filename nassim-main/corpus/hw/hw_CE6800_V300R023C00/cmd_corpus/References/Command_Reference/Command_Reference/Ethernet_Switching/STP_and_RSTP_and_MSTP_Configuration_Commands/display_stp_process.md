display stp process
===================

display stp process

Function
--------



The **display stp process** command displays the status of and statistics about the specify ID of a Multiple Spanning Tree Protocol (MSTP) process.




Format
------

**display stp process** *process-id* [ **instance** *instance-id* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* ] [ **brief** ]

**display stp process** *process-id* [ **instance** *instance-id* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* ] **tc-bpdu** **statistics** [ **history** ]

**display stp process** *process-id* [ **instance** *instance-id* ] **topology-change**

**display stp process** *process-id* **active**

**display stp process** *process-id* **bridge** { **local** | **root** }

**display stp process** *process-id* **global**

**display stp process** *process-id* [ **instance** *instance-id* ] **abnormal-interface**

**display stp process** *process-id* **v-stp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a Multiple Spanning Tree Protocol (MSTP) process. | The value is a decimal integer ranging from 1 to 256. |
| **instance** *instance-id* | Displays statistics about the topology changes of a specified STP instance.  If instance <instanceId> is not specified, the status of and statistics about all spanning tree instances will be displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates Common and Internal Spanning Tree (CIST). |
| **interface** *interface-type* *interface-number* | Displays information of a spanning tree on a specified interface.  If interface <ifType> <ifNum> is not specified, the status of and statistics about all interfaces will be displayed in the sequence of the interface numbers. | - |
| **slot** *slot-id* | Specifies the number of the slot where the interface resides. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **brief** | Displays the brief status. | - |
| **tc-bpdu** | Displays the statistics about sent and received topology change (TC) and topology change notification (TCN) BPDUs on interfaces. | - |
| **statistics** | Displays the statistics about sent and received topology change (TC) and topology change notification (TCN) BPDUs on interfaces. | - |
| **history** | Displays historical TC/TCN statistics on an interface. | - |
| **topology-change** | Displays statistics about Multiple Spanning Tree Protocol (MSTP) topology changes. | - |
| **active** | Displays the status of and statistics on spanning trees of all Up interfaces.  To view information about spanning trees on all Up interfaces, run the display stp active command. | - |
| **bridge** | Displays detailed information about the spanning tree of a bridge.  To view detailed information about the spanning trees of the root and local bridges, run the display stp bridge command. | - |
| **local** | Displays detailed information about the spanning tree of the local bridge. | - |
| **root** | Displays detailed information about the spanning tree of the root bridge. | - |
| **global** | Displays global Spanning Tree Protocol (STP) information. | - |
| **abnormal-interface** | Displays information about abnormal interfaces running the Spanning Tree Protocol (STP).  Run the display stp abnormal-interface command can query information about abnormal STP interfaces quickly. | - |
| **v-stp** | Displays V-STP status and statistics. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

* The **display stp process** command displays the status and statistics of the spanning tree of a specified MSTP process.
* If Protocol Status is Disabled, it indicates that the spanning tree protocol is not running.
* If the spanning tree protocol is running, the corresponding information is displayed, such as the working mode of the spanning tree.
* The **display stp process brief** command displays the spanning tree status of the port with the specified MSTP process ID. The global information cannot be displayed.
* The **display stp process global** command displays brief information about the spanning tree protocol of a specified MSTP process.
* The **display stp process tc-bpdu statistics** command displays the number of sent and received TC (Topology Change) /TCN (Topology Change Notification) on the port of a specified MSTP process.
* To determine whether a fault has occurred on interfaces that send and receive TC/TCN BPDUs, run this command and locate the fault source based on port information.
* The **display stp process topology-change** command displays statistics about the MSTP process (Multiple Spanning Tree Protocol) topology changes in a specified MSTP process.
* On a Layer 2 network running the MSTP process, a device clears ARP entries and MAC address entries after receiving TC BPDUs. If a device receives a large number of TC BPDUs and frequently clears ARP and MAC address entries, the CPU usage of the device becomes high. As a result, network traffic is unstable.
* You can run this command to view statistics about topology changes in an MSTP process. If the number of topology changes increases, network flapping occurs.
* The **display stp process active** command displays the spanning tree status of the interfaces in Up state in the specified MSTP process. The spanning tree status of the interfaces in Down state is not displayed.
* The **display stp process bridge** command displays the spanning tree status of the local bridge and root bridge in a specified MSTP process.
* The **display stp process abnormal-interface** command displays information about abnormal ports running a spanning tree protocol in a specified MSTP process.
* The display stp process v-stp command displays the status and statistics of the V-STP process with a specified MSTP process ID, including bridge information, peer-link port information, and virtual port information. Users can learn about the status of the V-STP process.

**Prerequisites**



For a non-0 process, it has been configured using the **stp process** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about spanning trees on all Up interfaces in MSTP process 0.
```
<HUAWEI> display stp process 0 active
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

# Display detailed information about the spanning tree of the root bridge of MSTP process 0.
```
<HUAWEI> display stp process 0 bridge root
MSTID RootID               RootCost HelloTime MaxAge ForwardDelay RootPort
--------------------------------------------------------------------------
    0 61440.00e0-fc12-3456        0         2     20           15                         
    1 61440.00e0-fc12-3456        0         2     20           15

```

# Display brief STP information about MSTP process 0.
```
<HUAWEI> display stp process 0 global
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

**Table 1** Description of the **display stp process** command output
| Item | Description |
| --- | --- |
| CIST Bridge Priority | Priority of the switch in CIST. |
| CIST Global Info | CIST global information. |
| CIST Bridge | ID of the CIST bridge.   * The 16 left-most bits are the priority of the switch in CIST. * The 48 right-most bits is the MAC address of the switch. |
| CIST Root/ERPC | CIST root device ID/Cost of the external path (path from the local device to the CIST root device). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | ID of the CIST root port. "0.0" indicates that the device is a root device and does not have a root port. |
| CIST Global Information | CIST Global Information. |
| CIST Port Information | CIST Port Information. |
| Mode | The operation mode. The default mode is MSTP. For the detailed configuration, see stp mode. |
| Config Times | Values configured manually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| Active Times | Values used actually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| BPDU-Protection | BPDU protection:   * disabled: BPDU protection is disabled. * enabled: BPDU protection is enabled. |
| TC or TCN received | Number of received TC or TCN packets. |
| TC count per hello | Number of TC packets received per Hello time. |
| TC or TCN send | Number of TC or TCN BPDUs sent by the port. |
| TC received | Number of received TC BPDUs. |
| STP Converge Mode | Convergence mode of the spanning tree protocol. |
| Share region-configuration | Whether the MST region configuration is shared. |
| Time since last Topology Change | Time past since the last topology changed. |
| Time since last TC | Time since the last topology change. |
| Number of Topology Changes | Total number of topology changes since MSTP initialization. |
| Number of TC | Number of topology changes. |
| Topo Change Flag | Flag indicating whether a topology change occurs:   * 0: No topology change occurs. * 1: A topology change occurs. |
| Port | Interface name. |
| Port Protocol | The status of the port protocol:   * enable: STP is enabled on the port. * disable: STP is disabled on the port. |
| Port Role | Port role:   * CIST Disabled Port. * CIST Root Port. * CIST Designated Port. * CIST Alternate Port. * CIST Backup Port. |
| Port Priority | Interface priority. For details on how to configure the interface priority, see stp port priority. |
| Port Edged | Status of an edge port that is specified by the administrator.   * enabled. * disabled. Config indicates that the value is configured by using the stp edged-port command. Active indicates the actual value. |
| Port STP Mode | STP mode on an interface. |
| Port Protocol Type | Format of the packets that the interface receives and sends:   * auto. * legacy. * dot1s. The default value is auto.  Config indicates that the packet format is configured using the stp compliance command. Active indicates the actual packet format. |
| Port Cost(Legacy) | Path cost of the port. It is calculated by dot1t algorithm.   * config: path cost manually configured. * active: actual path cost. |
| Port Id | Interface ID. |
| Port Name | Interface name. |
| Port State | Status of the port:   * Forwarding. * Discarding. * Down. * Disabled. * Learning. * Inactive. |
| Port Cost(Dot1T) | Path cost (calculated by dot1t) of an interface:   * Config: configured path cost. * Active: path cost that is being used. |
| Designated Bridge/Port | ID of the designated switch and port. The 16 left-most bits of the switch ID represent the priority of the switch in the CIST region; the 48 right-most bits represent the MAC address of the switch. The left-most 4 bits of the port ID represent the priority and the right-most 12 bits represent the port number. |
| Edged port default | Whether the function of configuring all ports of the switch as edge ports is enabled:   * Enabled. * Disabled. |
| Point-to-point | Link type of the port. Config indicates the link type configured using the stp point-to-point command, and Active indicates the actual link type. |
| Transit Limit | Maximum number of BPDUs that the current interface can send per Hello time. For details, see stp transmit-limit. |
| Protection Type | Protection type , which can be:   * None: no protection. * LoopBack: self-loop detection. * BpduRoot: BPDU and root protection. * ROOT: root protection. * BPDU: BPDU protection. * Loop: loop protection. * BpduLoop: BPDU and loop protection. |
| BPDU Encapsulation | Format of BPDUs that are sent and received by the interface. |
| BPDU Sent | Statistics on sent BPDUs, including:   * TCN: TCN BPDUs. * Config: STP BPDUs. * RST: RSTP BPDUs. * MST: MST BPDUs. |
| BPDU Received | Statistics on received BPDUs. |
| Message Age | BPDU lifetime. |
| MSTI Bridge ID | Multiple Spanning Tree instance (MSTI) bridge ID. |
| MSTI RegRoot/IRPC | ID of the MSTI root bridge/Cost of the internal path (path from the local device to the MSTI root bridge). |
| MSTI RootPortId | ID of the MSTI root interface. "0.0" indicates that the device is a root device and does not have a root port. |
| MSTI 1 Global Information | All MSTI 1 information. |
| MSTI 1 Port Information | MSTI 1 Port Information. |
| Master Bridge | ID of the bridge where the master interface is located.   * The first 16 bits represent the priority of the device in the CIST. * The last 48 bits are the MAC address of the device. |
| Cost to Master | Cost of the path from the device to the bridge where the master interface resides. 0 indicates that the master interface resides on the current bridge. |
| Desg. Bridge/Port | ID of the designated switch and port. The 16 left-most bits of the switch ID represent the priority of the switch in the CIST region; the 48 right-most bits represent the MAC address of the switch. The left-most 4 bits of the port ID represent the priority and the right-most 12 bits represent the port number. |
| MSTID | MSTP instance ID. |
| Hello time(s) | Interval at which BPDUs are sent from the root bridge. |
| Max hops | Maximum hops in Multiple Spanning Tree (MST) region. |
| Max age(s) | Maximum lifecycle of the BPDU. |
| Forward delay(s) | Time interface status transition takes. |
| RootID | MSTP root bridge ID. |
| RootCost | MSTP root path cost. |
| HelloTime | Interval at which Bridge Protocol Data Units (BPDUs) are sent from the root bridge. |
| ForwardDelay | Delay in interface status transition. |
| RootPort | Root port. |
| Bpdu-filter default | Whether the function of configuring a port as a BPDU filter port is enabled:   * Enabled: The function of configuring a port as a BPDU filter port is enabled. * Disabled: The function of configuring a port as a BPDU filter port is disabled. |
| Tc-protection | TC protection status:   * Enabled: TC protection is enabled. * Disabled: TC protection function is disabled. |
| Tc-protection threshold | Threshold for MSTP to process TC BPDUs and immediately refresh forwarding entries per unit time. |
| Tc-protection interval | Time taken by MSTP to process the maximum number of TC BPDUs and immediately refresh forwarding entries. |
| Pathcost-standard | Method of calculating the MSTP path cost. |
| Timer-factor | Multiplier of Hello time. |
| Transmit-limit | Maximum number of BPDUs that the current interface can send per Hello time. For details, see stp transmit-limit. |
| Bridge-diameter | Network diameter of the MSTP. |
| TC(Send/Receive) | Statistics about sent and received TC BPDUs. |
| TCN(Send/Receive) | Statistics about sent and received TCN BPDUs (A hyphen (-) indicates that only MSTI 0 has TCN BPDUs sent and received). |
| Topology Change initiator(detected) | Interface that triggers the topology change because the interface status changes to DETECTED after the interface status changes from blocked to unblocked. |
| Topology Change initiator(notified) | Port that initiates a topology change after receiving a TC BPDU. |
| Topology Change last received from | Bridge MAC address of the source of topology change BPDUs. |
| MAC address | MAC address of a device. |
| PortTimes/Port Times | Values in the BPDUs on the interface:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |