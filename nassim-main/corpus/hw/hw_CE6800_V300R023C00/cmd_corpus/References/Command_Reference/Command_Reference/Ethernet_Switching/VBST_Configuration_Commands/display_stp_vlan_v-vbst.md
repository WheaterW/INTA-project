display stp vlan v-vbst
=======================

display stp vlan v-vbst

Function
--------



The **display stp vlan v-vbst** command displays the virtual VBST calculation result of the spanning tree in a specified VLAN.




Format
------

**display stp vlan** *vlan-id* **v-vbst**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays the virtual VBST calculation result of the spanning tree in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Display the virtual VBST calculation result of the spanning tree in a specified VLAN.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the virtual VBST calculation result of the spanning tree in a specified VLAN.
```
<HUAWEI> display stp vlan 100 v-vbst
Bridge Information:
  V-VBST Mode            : True
  Bridge Mac             : Config=00e0-fc87-8787 / Active= 00e0-fcaa-3333
  Peer-link Name         : Eth-Trunk1

CIST Global Information:
  Priority               : Config=12288 / Active=32768
  Peer-link State        : Discarding
  CIST Root Times        : Hello 2s MaxAge 20s FwDly 15s MaxHop 20
  CIST Root/ERPC         : 32779.00e0-fcaa-3333 / 0
  Designated Bridge/Port : 32779.00e0-fcaa-3333 / 0.0
  CIST RootPortId        : 0.0 (M-lag: Invalid / MAC: 00e0-fcfe-6c01)
  Virtual Port State     : Active
  Packet Sent            : 7037
  Packet Received        : 7044
  TC(Sent/Received)      : 0 / 0

CIST M-lag Port Information:
  Port Id                : 3
  Port Name              : Eth-Trunk10
  M-lag Id               : 3
  Port State             : Forwarding
  Port Role              : Designated Port
  Port Cost(Dot1T)       : Config=auto / Active=2000
  Send Port Id           : 4092

CIST M-lag Port Information:
  Port Id                : 5
  Port Name              : Eth-Trunk20
  M-lag Id               : 20
  Port State             : Down
  Port Role              : Disabled Port
  Port Cost(Dot1T)       : Config=auto / Active=2000
  Send Port Id           : 0

```

**Table 1** Description of the **display stp vlan v-vbst** command output
| Item | Description |
| --- | --- |
| Bridge Mac | Bridge MAC address. config indicates the configured value, and active indicates the running value. |
| V-VBST Mode | Whether to enter the V-VBST mode. The value can be true or false. |
| Peer-link Name | Peer-link interface name. |
| Peer-link State | Peer-link interface status, which can be:  Down.  Disabled.  Forwarding.  Learning.  Discarding.  Inacive. |
| CIST Root Times | Time values in bridge protocol information:  Hello: indicates the interval for sending BPDUs.  MaxAge: indicates the maximum lifetime of a BPDU.  FwDly: indicates the delay for port status transition.  MaxHop: indicates the maximum number of hops in the MST region. |
| CIST Root/ERPC | CIST root switch ID/external path cost (path cost from the switch to the CIST root switch). |
| CIST RootPortId | Root port ID. The priority is synchronized. The M-LAG ID of the root port and the MAC address of the peer device are also displayed. |
| Priority | Instance priority. config indicates the configured value, and active indicates the running value. |
| Designated Bridge/Port | ID of the designated switch and designated port ID. |
| Virtual Port State | Status of the virtual interface:  Active.  Inactive. |
| Port Id | Interface number. |
| Port Name | M-LAG interface name. |
| Port State | Port status. |
| Port Role | Port role. In a CIST region, there are three port roles:  CIST Root Port: root port.  CIST Designated Port: designated port.  CIST Alternate Port: alternate root port. |
| Port Cost(Dot1T) | Path cost of the port, which is calculated using the dot1t algorithm. Config indicates the manually configured path cost and Active indicates the actual path cost. |
| Packet Sent | Statistics about sent proprietary V-VBST packets. |
| Packet Received | Statistics about received proprietary V-VBST packets. |
| TC(Sent/Received) | Statistics about sent and received TC BPDUs. |
| M-lag Id | M-LAG ID of the M-LAG interface. 4294967295 is an invalid value and "Invalid" is displayed. |
| Send Port Id | Port number used by the M-LAG interface to send BPDUs. |