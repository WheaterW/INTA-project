display stp v-stp
=================

display stp v-stp

Function
--------



The **display stp v-stp** command displays V-STP status and statistics.




Format
------

**display stp v-stp**


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

To check V-STP status and statistics, run the **display stp v-stp** command. The command output shows bridge, peer-link interface, virtual interface, and M-LAG interface information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display V-STP information.
```
<HUAWEI> display stp v-stp
Bridge Information: 
   V-STP Mode          :True
   Bridge Mac          :Config=00e0-fc11-1200 / Active=00e0-fc12-1234
   Peer-link Name      :Eth-Trunk1

CIST Global Information: 
   Priority            :Config=0 / Active=0
   Peer-link State     :Forwarding
   CIST Root Times     :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   CIST Root/ERPC      :0.00e0-fc12-1234 / 0
   CIST RegRoot/IRPC   :0.00e0-fc12-1234 / 0
   Designated Bridge/Port   :0.00e0-fc12-1234 / 0.0
   CIST RootPortId     :0.0(M-lag: Invalid / MAC: 00e0-fc12-1234)
   Virtual Port State  :Active
   Packet Sent         :128
   Packet Received     :128
   TC(Sent/Received)    :1 / 0

CIST M-lag Port Information: 
   Port Id             :3
   Port Name           :Eth-Trunk2
   M-lag Id            :3
   Port State          :Forwarding
   Port Role           :Designated Port
   Port Cost(Dot1T)    :Config=auto / Active=2000
   BPDU Port-Id For V-STP   :2048

```

**Table 1** Description of the **display stp v-stp** command output
| Item | Description |
| --- | --- |
| Bridge Information | V-STP bridge information. |
| Bridge Mac | Remote device's priority and bridge MAC address.   * Config: configured MAC address. If a bridge MAC address is configured, its value is displayed. If no bridge MAC address is configured, the system MAC address is configured. * Active: MAC address in use, which can be the configured MAC address or synchronized MAC address from the master device. |
| V-STP Mode | V-STP mode.   * False: non-V-STP mode. * True: V-STP mode. |
| Peer-link Name | Name of the V-STP connected remote interface.  If no peer-link exists, hyphens (--) are displayed. |
| Peer-link State | Peer-link interface status.   * Down. * Forwarding. * Learning. * Discarding. * Inactive. |
| CIST Global Information | CIST global information. |
| CIST Root Times | Time information of the CIST root.   * Hello: interval at which BPDUs are sent. * MaxAge: maximum TTL of BPDUs. * FwDly: holdoff period for interface status transition. * MaxHop: maximum number of hops in the MST region. |
| CIST Root/ERPC | CIST root ID/external path cost. |
| CIST RegRoot/IRPC | CIST regional root ID/internal path cost. |
| CIST RootPortId | Root interface ID.  In a scenario where two devices running V-STP in an M-LAG are both root bridges, the M-LAG member interfaces on the devices are all designated ports instead of root ports. In this case, the value of this field is displayed as 0.0, with the M-LAG interface status being Invalid and the MAC address being the peer-link interface's MAC address. |
| CIST M-lag Port Information | V-STP-enabled M-LAG interface information. |
| Priority | Priority. |
| Designated Bridge/Port | ID of the designated switch and designated interface. |
| Virtual Port State | Virtual interface activation status:   * Active. * Inactive. |
| Port Id | Interface ID. |
| Port Name | Name of an interface. |
| Port State | Interface status. |
| Port Role | Interface role in a CIST region:   * CIST Root Port. * CIST Designated Port. * CIST Alternate Port. * Disabled Port. |
| Port Cost(Dot1T) | Interface's path cost (calculated using the dot1t algorithm):   * Config: configured path cost. * Active: path cost in use. |
| Packet Sent | Number of sent V-STP BPDUs. |
| Packet Received | Number of received V-STP BPDUs. |
| TC(Sent/Received) | Number of sent and received TC BPDUs. |
| M-lag Id | M-LAG ID. |
| BPDU Port-Id For V-STP | When a port sends packets, the port ID carried by the M-LAG port is updated. When the port does not send packets, the port ID in the last sent packet is retained. When the link of a port is faulty, Port ID is displayed as 0. |