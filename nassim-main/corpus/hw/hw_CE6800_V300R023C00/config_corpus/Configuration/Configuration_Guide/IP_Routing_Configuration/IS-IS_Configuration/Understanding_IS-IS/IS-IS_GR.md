IS-IS GR
========

IS-IS GR is an HA technology that implements non-stop data forwarding. Without GR, no neighbor information is saved upon a master/slave main control board switchover on a routing device. As a result, the first IIH that the routing device sends to its neighbors after the switchover does not contain any neighbor information. After receiving the IIH, the neighbors detect that they are not in its neighbor list and consider their neighbor relationships with the routing device to be interrupted. The neighbor then generates new LSPs and floods the topology changes to all other devices in the area. The other devices in the area then calculate routes based on their new LSDBs, leading to routing interruptions or flapping. The IETF formulated a standard for IS-IS GR, which prevents route flapping and traffic forwarding interruptions during IS-IS process restarts.

#### Basic Concepts

GR restarter: a GR-capable device that restarts in GR mode.

GR helper: a GR-capable device that helps the GR restarter complete the GR process. The GR restarter must have the GR helper capability.

An IS-IS GR involves both a GR restarter and GR helper.

![](public_sys-resources/note_3.0-en-us.png) 

The routing device can function as a GR helper, but not as a GR restarter.



#### Restart TLV

The Restart TLV is included in the extension part of an IS-to-IS Hello (IIH) PDU. All IIH packets of a device that supports IS-IS GR contain the Restart TLV. The Restart TLV carries some parameters for the protocol restart. [Figure 1](#EN-US_CONCEPT_0000001176743779__fig18987143216129) shows the restart TLV format.

**Figure 1** Restart TLV format  
![](figure/en-us_image_0000001176663913.png)

[Table 1](#EN-US_CONCEPT_0000001176743779__table63171116457) describes the fields in the restart TLV.

**Table 1** Fields in the restart TLV
| Field | Length | Description |
| --- | --- | --- |
| Type | 1 octet | TLV type. Type value 211 indicates the restart TLV. |
| Length | 1 octet | Length of the TLV. |
| RR | 1 bit | Restart request (RR) bit. A GR restarter sends an IIH with the RR bit set to 1 to notify the GR helper that it is starting or restarting, and to instruct the GR helper to retain the current IS-IS neighbor relationship and respond with a CSNP. |
| RA | 1 bit | Restart acknowledgement (RA) bit. An IIH with the RA bit set to 1 is used to acknowledge the reception of an IIH with the RR bit set to 1. |
| SA | 1 bit | Suppress adjacency advertisement (SA) bit. It is used by a starting device to request its neighbors to suppress the broadcast of the neighbor relationships with the starting device to prevent routing black holes. |
| Remaining Time | 2 octets | Period (in seconds) during which the neighbor relationship is not reset. |



#### Timers

IS-IS GR has three timers: T1, T2, and T3.

T1: If the GR restarter has sent an IIH with the RR bit set to 1 but has not received any IIH carrying the restart TLV with the RA bit set to 1 from the GR helper when the T1 timer expires, the GR restarter resets the T1 timer and resends the IIH with the RR bit set to 1. When the GR restarter receives an IIH with the RA bit set to 1 from the GR helper, or when the T1 timer expires three times, the GR restarter cancels the T1 timer. Any interface enabled with IS-IS GR maintains a T1 timer. On Level-1-2 routing devices, broadcast interfaces maintain a T1 timer for each level of neighbor relationships.

T2: This timer specifies the period from when the GR restarter restarts, to when the LSDBs on all devices with the same level as the GR restarter are synchronized. The T2 timer is the maximum time for the system to wait for the LSDB synchronization at both Level-1 and Level-2. Level-1 and Level-2 LSDBs maintain their respective T2 timers.

T3: This timer specifies the maximum time allowed for the GR restarter to finish GR. The initial value of the T3 timer is 65535 seconds. After the IIH packet in which the RA is set is received from the neighbor, the value of the T3 timer becomes the smallest value among the Remaining Time fields of the IIH packets. If the T3 timer expires, GR fails. The entire system maintains only one T3 timer.


#### Session Mechanism

GR minimizes the impact of control plane faults on the network and prevents route flapping, which ensures high reliability. For differentiation, the GR process triggered by a master/slave main control board switchover or by an IS-IS process restart is referred to as restarting. Throughout this process, the forwarding table remains unchanged. The GR process triggered by a device restart is referred to as starting, and the forwarding table is updated during this process. The IS-IS GR restarting and starting processes are described in the following section.

[Figure 2](#EN-US_CONCEPT_0000001176743779__fig1535713317176) shows the IS-IS restarting process.**Figure 2** IS-IS restarting process  
![](figure/en-us_image_0000001176663909.png)

1. After the GR restarter performs a master/slave main control board switchover, it starts the T1, T2, and T3 timers and sends an IIH containing the restart TLV through all interfaces. In the IIH, the RR bit is set to 1, and the RA and SA bits remain at 0.
2. After receiving the IIH, the GR helper maintains the neighbor relationship with the GR restarter, updates the current holdtime, and replies with an IIH carrying the restart TLV. In this IIH, the RR bit is set to 0, the RA bit is set to 1, and the Remaining Time is the time left before the holdtime expires. In addition, the GR helper sends a CSNP and all LSPs to the GR restarter.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   On a P2P link, the GR helper must reply with a CSNP in the preceding scenario. On a broadcast link network, CSNPs are sent by the DIS. If the DIS is a GR restarter, a temporary DIS is elected from the other routing devices on the broadcast link network. If a neighbor does not have the GR helper capability, it ignores the restart TLV, returns to normal IS-IS processing, and resets the neighbor relationship with the GR restarter.
3. After receiving the IIH in which the RR bit is set to 0 and the RA bit is set to 1 from the GR helper, the GR restarter performs the following operations:
   
   * Compares the current value of the T3 timer with the Remaining Time in the IIH and uses the smaller value as the new T3 timer value.
   * Cancels the T1 timer maintained by the local interface if the interface receives an acknowledgement packet and CSNP from the GR helper.
   * Repeatedly resets the T1 timer and resends the IIH that contains the restart TLV if the interface receives no acknowledgement packet or CSNP from the GR helper. If the timeout count of the T1 timer exceeds the threshold, the GR restarter forcibly cancels the T1 timer and switches to normal IS-IS processing.
4. After canceling the T1 timers on all its interfaces, clearing the CSNP list, and collecting all LSPs, the GR restarter considers LSDB synchronization with all neighbors as finished, and then cancels the T2 timer.
5. When the T2 timer is canceled, LSDBs of the corresponding level are synchronized. If the GR restarter is a Level-1 or Level-2 device, it directly performs SPF calculation. If the GR restarter is a Level-1-2 device, it checks whether the T2 timer of the other level is also canceled. If both T2 timers are canceled, the GR restarter performs SPF calculation. Otherwise, the GR restarter waits for the T2 timer of the other level to expire.
6. When both T2 timers are canceled, the GR restarter cancels the T3 timer and updates the FIB. In addition, the GR restarter re-generates the LSPs of each level and floods them. During LSDB synchronization, if the GR restarter receives the LSPs generated by itself before its restart, it deletes them.
7. The GR restarter's IS-IS restarting process is now complete.

Regarding the starting process, the starting device does not retain FIB entries. As a result, it expects the GR helper to reset their neighbor relationship that is up before the starting device starts, and not to advertise their neighbor relationship within a certain period. The IS-IS starting process, as shown in [Figure 3](#EN-US_CONCEPT_0000001176743779__fig1150854673412), is different from the IS-IS restarting process.**Figure 3** IS-IS starting process  
![](figure/en-us_image_0000001176663911.png)

1. After the GR restarter starts, it starts the T2 timers for LSDB synchronization at each level and sends IIHs carrying the restart TLV through all interfaces. In the IIHs, the RR bit is set to 0, and the SA bit is set to 1.
2. After receiving the IIH carrying the restart TLV, a neighbor performs the following operations based on whether GR is supported:
   
   If the neighbor supports GR, it re-initiates the neighbor relationship with the GR restarter, deletes the description of the neighbor relationship from the LSPs to be sent, and ignores the link connected to the GR restarter when performing SPF calculation until it receives an IIH in which the SA bit is set to 0 from the GR restarter.
   
   If the neighbor does not support GR, it ignores the restart TLV, resets the neighbor relationship with the GR restarter, replies with an IIH without the restart TLV, and switches to normal IS-IS processing. In this case, the neighbor still advertises its neighbor relationship with the GR restarter. If the link between the two ends is a P2P link, the neighbor also replies with a CSNP.
3. After neighbor relationships are re-initiated, the GR restarter re-establishes them with its neighbors through all its interfaces. When a neighbor relationship set on an interface goes up, the GR restarter starts the T1 timer for the interface.
4. When the T1 timer expires, the GR restarter sends an IIH in which both the RR and SA bits are set to 1.
5. After the neighbor receives the IIH, it replies with an IIH in which the RR bit is set to 0 and the RA bit is set to 1, as well as a CSNP.
6. After the GR restarter receives the IIH and CSNP from the neighbor, it cancels the T1 timer. If the GR restarter does not receive the IIH or CSNP, it repeatedly resets the T1 timer and resends the IIH in which both the RR and SA bits are set to 1. If the timeout count of the T1 timer exceeds the threshold, the GR restarter forcibly cancels the T1 timer and switches to normal IS-IS processing to complete LSDB synchronization.
7. After receiving the CSNP from the GR helper, the GR restarter starts LSDB synchronization.
8. After LSDBs of the corresponding level are synchronized, the GR restarter cancels the T2 timer.
9. After T2 timers of both levels are canceled, the GR restarter performs SPF calculation and re-generates and floods LSPs.
10. The GR restarter's IS-IS starting process is now complete.