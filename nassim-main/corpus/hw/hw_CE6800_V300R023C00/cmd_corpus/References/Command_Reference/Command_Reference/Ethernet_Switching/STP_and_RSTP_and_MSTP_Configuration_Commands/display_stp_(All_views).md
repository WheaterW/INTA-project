display stp (All views)
=======================

display stp (All views)

Function
--------



The **display stp** command displays the status of and statistics about a spanning tree instance.




Format
------

**display stp** [ **instance** *instance-id* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* ] [ **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays the status of and statistics about a spanning tree instance.  If instance <instanceId> is not specified, the status of and statistics about all spanning tree instances will be displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| **interface** *interface-type* *interface-number* | Displays information of a spanning tree on a specified interface.  If interface <ifType> <ifNum> is not specified, the status of and statistics about all interfaces will be displayed in the sequence of the interface numbers. | - |
| **slot** *slot-id* | Specifies the number of the slot where the interface resides. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |
| **brief** | Displays the brief status. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The display stp command is used to check whether the spanning tree protocol is run on the existingdevice or specified interface.

* If the Protocol Status field value is Disabled, the spanning tree protocol is not run.
* If STP/RSTP/MSTP has been run, information such as the working mode of the spanning tree protocol will be displayed.When a network planner has deployed STP/RSTP/MSTP on the network, you can run the display stp command to check whether the configurations are correct and check the calculation result.

**Precautions**



In a multi-instance scenario, a PW interface's STP state does not take effect for any MSTP instance with a non-0 ID. For such an instance, its actual STP state is the same as instance 0's STP state.The actual STP state of an interface bound to a process in link-share mode is the same as that of the interface bound to a process in no-link-share mode.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# When the stp enable command does not run, display the status of and statistics about STP.
```
<HUAWEI> display stp
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

# Display brief information about the spanning tree when the STP mode is VBST.
```
<HUAWEI> display stp brief
--------------------------------------------------------------------------------
VLANID Interface              Role STPState    Protection           Cost Edged  
--------------------------------------------------------------------------------
     1 100GE1/0/1             DESI forwarding  none                 800 enable 
   100 100GE1/0/2             DESI forwarding  none                 2000 enable 
--------------------------------------------------------------------------------

```

# Display the status of and statistics about spanning tree instance 0 on interface.
```
<HUAWEI> display stp instance 0 interface 100ge 1/0/1
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

# After running the stp enable command, display the status of and statistics about STP.
```
<HUAWEI> display stp
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

**Table 1** Description of the **display stp (All views)** command output
| Item | Description |
| --- | --- |
| Protocol Status | Status of the protocol. |
| Protocol Standard | Standards of the protocol. |
| Version | Protocol version:   * 0: STP. * 2: RSTP. * 3: MSTP. |
| CIST Bridge Priority | Priority of the switch in CIST. |
| CIST Global Info | Global CIST information. |
| CIST Bridge | ID of the CIST bridge.   * The 16 left-most bits are the priority of the switch in CIST. * The 48 right-most bits is the MAC address of the switch. |
| CIST Root/ERPC | CIST root device ID/Cost of the external path (path from the local device to the CIST root device). |
| CIST RegRoot/IRPC | ID of the CIST region root bridge/Cost of the internal path (path from the switch to the CIST region root bridge). |
| CIST RootPortId | ID of the CIST root port. 0.0 indicates that the switch is the root bridge and does not provide any root port. |
| CIST Global Information | CIST Global Information. |
| CIST Port Information | CIST Port Information. |
| MAC address | MAC address of the switch. |
| Max hops | Maximum hops in Multiple Spanning Tree (MST) region. |
| Max age(s) | Maximum lifecycle of the BPDU. |
| Forward delay(s) | Time interface status transition takes. |
| Hello time(s) | Interval at which BPDUs are sent from the root bridge. |
| Protection Type | Protection type , which can be:   * None: no protection. * LoopBack: self-loop detection. * BpduRoot: BPDU and root protection. * ROOT: root protection. * BPDU: BPDU protection. * Loop: loop protection. * BpduLoop: BPDU and loop protection. |
| Cost to Master | Cost of the path from the local device to the bridge where the master interface is located. 0 indicates that the master interface is located at the current bridge. |
| Mode | The operation mode. The default mode is MSTP. For the detailed configuration, see stp mode. |
| Config Times | Values configured manually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| Active Times | Values used actually in the BPDU:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |
| BPDU-Protection | BPDU protection function:   * disabled. * enabled. |
| TC or TCN received | Number of received topology change (TC) or topology change notification (TCN) BPDUs. |
| TC count per hello | Number of TC BPDUs received each Hello time. |
| TC or TCN send | Number of TC or TCN BPDUs sent by the port. |
| TC received | Number of received TC BPDUs. |
| STP Converge Mode | Convergence mode of the spanning tree protocol. |
| STP State | Status of the port:   * Forwarding. * Discarding. * Down. * Disabled. * Learning. * Inactive. |
| Share region-configuration | Whether the MST region configuration is shared. |
| Time since last TC | Period from the last topology change to now. |
| Number of TC | Number of topology changes. |
| Topo Change Flag | Flag indicating whether a topology change occurs:   * 0: No topology change occurs. * 1: A topology change occurs. |
| Port Protocol | The status of the port protocol:   * enable: STP is enabled on the port. * disable: STP is disabled on the port. |
| Port Role | Port role:   * CIST Disabled Port. * CIST Root Port. * CIST Designated Port. * CIST Alternate Port. * CIST Backup Port. |
| Port Priority | Priority of the port. To set the priority of the port, run the stp port priority command. |
| Port Edged | Status of an edge port that is specified by the administrator.   * enabled. * disabled.   Config indicates that the value is configured by using the stp edged-port command. Active indicates the actual value. |
| Port STP Mode | STP mode on an interface. |
| Port Protocol Type | Format of the packets that the interface receives and sends:   * auto. * legacy. * dot1s.   The default value is auto.  Config indicates that the packet format is configured using the stp compliance command. Active indicates the actual packet format. |
| Port Id | Port ID. |
| Port Name | Interface name. |
| Port State | Status of the port:   * Forwarding. * Discarding. * Down. * Disabled. * Learning. * Inactive. |
| Designated Bridge/Port | ID of the designated switch and port. The 16 left-most bits of the switch ID represent the priority of the switch in the CIST region; the 48 right-most bits represent the MAC address of the switch. The left-most 4 bits of the port ID represent the priority and the right-most 12 bits represent the port number. |
| Point-to-point | Link type of the port. Config indicates the link type configured by the stp point-to-point command; Active indicates the actual link type. |
| Transit Limit | Maximum number of BPDUs that the current interface can send each Hello time. For details, see stp transmit-limit. |
| BPDU Encapsulation | Format of the BPDUs received and sent through a port. |
| BPDU Sent | Statistics on sent BPDUs, including:   * TCN: TCN BPDUs. * Config: STP BPDUs. * RST: Rapid Spanning Tree Protocol (RSTP) BPDUs. * MST: MST BPDUs. |
| BPDU Received | Statistics about received BPDUs. |
| Message Age | Life time of the BPDU. |
| MSTI Bridge ID | MSTI bridge ID. |
| MSTI RegRoot/IRPC | MSTI root bridge ID/Internal path cost (path from the switch to the MSTI root). |
| MSTI RootPortId | ID of the MSTI root interface. "0.0" indicates that the device is a root device and does not have a root port. |
| MSTI 1 Global Information | All information about MSTI 1. |
| MSTI 1 Port Information | MSTI 1 Port Information. |
| Master Bridge | ID of the bridge where the master interface resides.   * The 16 left-most bits represent the bridge's priority in the CIST. * The remaining 48 bits represent the bridge's MAC address. |
| Desg. Bridge/Port | ID of the designated switch and port. The 16 left-most bits of the switch ID represent the priority of the switch in the CIST region; the 48 right-most bits represent the MAC address of the switch. The left-most 4 bits of the port ID represent the priority and the right-most 12 bits represent the port number. |
| Last TC occurred | Last TC occurred. |
| PortTimes/Port Times | Values in the BPDUs on the interface:   * Hello: interval at which BPDUs are sent. * MaxAge: maximum lifecycle of the BPDU. * FwDly: forwarding delay timer. * MaxHop: maximum hops in the MST region. |