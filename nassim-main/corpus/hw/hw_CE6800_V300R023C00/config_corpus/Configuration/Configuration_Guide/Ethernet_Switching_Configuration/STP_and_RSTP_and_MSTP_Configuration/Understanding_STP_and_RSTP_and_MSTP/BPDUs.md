BPDUs
=====

STP, RSTP, or MSTP determines the network topology and calculates the spanning tree by exchanging bridge protocol data units (BPDUs) between devices. A BPDU is encapsulated in an Ethernet frame and has a destination MAC address of 01-80-C2-00-00-00.

#### BPDU Classification

BPDUs are classified into the following types:

* Configuration BPDU: used to calculate and maintain the spanning tree topology in STP.
* Rapid spanning tree BPDU (RST BPDU): used to calculate and maintain the spanning tree topology in RSTP.
* Multiple spanning tree BPDU (MST BPDU): used to calculate and maintain the spanning tree topology in MSTP.
* Topology Change Notification BPDU (TCN BPDU): used to notify devices that the network topology changes.

#### BPDU Format

The BPDU type is determined by the Protocol Version Identifier and BPDU Type fields, as shown in the [Table 1](#EN-US_CONCEPT_0000001345158073__table164583673913).

**Table 1** BPDU types
| Protocol Version Identifier | BPDU Type | BPDU Type |
| --- | --- | --- |
| 0 | 0x00 | Configuration BPDU |
| 2 | 0x02 | RST BPDU |
| 3 | 0x02 | MST BPDU |
| 0 | 0x80 | TCN BPDU |

* The first 35 bytes in [Figure 1](#EN-US_CONCEPT_0000001345158073__fig17998727121212) are used in a configuration BPDU. The Root Identifier, Root Path Cost, Bridge Identifier, and Port Identifier fields are the main fields of a configuration BPDU and form a BPDU priority vector {root BID, root path cost, sender BID, port ID}.
  + Root Identifier: indicates the BID of the root bridge. A BID is composed of a bridge priority and a bridge MAC address. The bridge priority occupies the leftmost 16 bits and the MAC address occupies the rightmost 48 bits. The device with the smallest BID is elected as the root bridge.
  + Root Path Cost (RPC): The path cost is a port variable used for link selection. STP, RSTP, and MSTP calculate path costs to select effective links, block redundant links, and trim the network into a loop-free tree topology. The RPC is the accumulated path cost from a port to the root bridge.
  + Bridge Identifier: indicates the BID of the device that sends BPDUs.
  + Port Identifier: indicates the ID of the port that sends BPDUs. A PID is composed of a port priority (leftmost 4 bits) and a port number (rightmost 12 bits).
* RST BPDUs retain the basic configuration BPDU format defined in STP with minor changes. In an RST BPDU, the Version 1 Length field is added, and the middle six bits (except the least and most significant bits) in the Flags field are used. In contrast, configuration BPDUs in STP use only the least and most significant bits in the Flags field, and the six bits in the middle are reserved. [Figure 2](#EN-US_CONCEPT_0000001345158073__fig1061018101115) shows the middle six bits used by RST BPDUs.
* The first 36 bytes of an MST BPDU are the same as those of an RST BPDU. Fields from the 37th byte of an MST BPDU are MSTP-specific. The Multiple Spanning Tree Instance (MSTI) Configuration Messages field consists of configuration BPDUs of multiple MSTIs.
* A TCN BPDU is 4 bytes long and uses only the first three fields in [Figure 1](#EN-US_CONCEPT_0000001345158073__fig17998727121212). That is, a TCN BPDU contains only the Protocol Identifier, Protocol Version Identifier, and BPDU Type fields.

[Table 2](#EN-US_CONCEPT_0000001345158073__tab_dc_fd_stp_000601) describes the fields in a BPDU.

**Figure 1** BPDU format  
![](figure/en-us_image_0000001291918996.png)
**Figure 2** Flags field  
![](figure/en-us_image_0000001345238525.png)

**Table 2** Fields in a BPDU
| Field | Length (Bytes) | Description |
| --- | --- | --- |
| Protocol Identifier | 2 | Identifies a protocol. |
| Protocol Version Identifier | 1 | Indicates the protocol version identifier:   * 0: STP * 2: RSTP * 3: MSTP |
| BPDU Type | 1 | Indicates the BPDU types:  * 0x00: Configuration BPDU * 0x80: TCN BPDU * 0x02: If the value in the Protocol Version Identifier field is 2, the BPDU is an RST BPDU. If the value in the Protocol Version Identifier field is 3, the BPDU is an MST BPDU. |
| Flags | 1 | Indicates whether the network topology has changed. This field identifies the Common and Internal Spanning Tree (CIST) in MSTP.  * The rightmost bit is the Topology Change (TC) flag. * The leftmost bit is the Topology Change Acknowledgment (TCA) flag. |
| Root Identifier | 8 | Indicates the BID of the root bridge and identifies the CIST root bridge ID in MSTP. |
| Root Path Cost | 4 | Indicates the accumulated path cost from a port to the root bridge. This field is CIST External Root Path Cost in MSTP, which is the total path cost from the MST region where the local device resides to the MST region where the CIST root resides. This value is calculated based on link bandwidth. |
| Bridge Identifier | 8 | Indicates the BID of the local device. This field is CIST Regional Root Identifier in MSTP, which is the ID of the internal spanning tree (IST) master in a region. If the CIST root is in this region, the CIST Regional Root Identifier is the same as the CIST Root Identifier. |
| Port Identifier | 2 | Indicates the ID of the port that sends the BPDU. This field indicates the ID of the designated port in the IST. |
| Message Age | 2 | Indicates the lifecycle of the BPDU.  If the configuration BPDU is sent from the root bridge, the Message Age value is 0. Otherwise, the Message Age value is the total time required to transmit the BPDU from the root bridge to the local bridge, including the transmission delay. The Message Age value of a configuration BPDU is incremented by 1 each time the configuration BPDU passes through a bridge. |
| Max Age | 2 | Indicates the maximum lifecycle of the BPDU. If the Max Age timer expires, the link to the root bridge is considered faulty. |
| Hello Time | 2 | Indicates the interval at which BPDUs are sent. The default value is 2 seconds. |
| Forward Delay | 2 | Indicates the Forward Delay timer (the period during which a port stays in Listening and Learning states). The default value is 15 seconds. |
| Version 1 Length | 1 | Indicates the BPDUv1 length, which has a fixed value of 0. |
| Version 3 Length | 2 | Indicates the BPDUv3 length. |
| MST Configuration Identifier | 51 | Indicates the Minimum Spanning Tree (MST) configuration identifier, which has four fields. |
| CIST Internal Root Path Cost | 4 | Indicates the total path costs from the local port to the IST master. This value is calculated based on link bandwidth. |
| CIST Bridge Identifier | 8 | Indicates the ID of the designated device on the CIST. |
| CIST Remaining Hops | 1 | Indicates the number of remaining hops of the BPDU in the CIST. |
| MSTI Configuration Messages(may be absent) | 16 | Indicates an MSTI configuration message, each occupying 16 bytes. If there are *n* MSTIs, MSTI configuration messages are *n* x 16 bytes long. |