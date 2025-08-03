Basic Concepts of ERPS
======================

ERPS prevents loops at the Ethernet link layer. ERPS works for ERPS rings. It blocks the ring protection link (RPL) owner port and controls other common ports to switch the port status between Forwarding and Discarding to eliminate loops. There are two versions of ERPS: ERPSv1 and ERPSv2. ERPSv2 is fully compatible with ERPSv1 and extends ERPSv1 functions.

In [Figure 1](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000301), DeviceA through DeviceD constitute a ring and are connected to the upstream network. This connection mode will cause a loop on the entire network. To eliminate loops on the network and ensure link connectivity, a loop prevention mechanism needs to be used.

**Figure 1** ERPS single-ring networking  
![](figure/en-us_image_0000001216729804.png)

ERPS can be deployed on the network shown in [Figure 1](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000301). The following describes basic concepts of ERPS based on the figure:

#### ERPS Ring

An ERPS ring consists of connected Layer 2 switching devices that are configured with the same control VLAN. An ERPS ring is the basic unit of ERPS. An ERPS ring can be a major ring or a sub-ring. By default, an ERPS ring is a major ring. A major ring is a closed ring, whereas a sub-ring is an open ring. Both of them are configured using commands. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000304), DeviceA through DeviceD constitute a major ring, and DeviceC through DeviceF constitute a sub-ring. Only ERPSv2 supports sub-rings, while ERPSv1 does not.

**Figure 2** ERPS major ring and sub-ring networking  
![](figure/en-us_image_0000001142188108.png)

#### ERPS Port

ERPS defines three types of ports: RPL owner port, RPL neighbour port, and common port. Only ERPSv2 supports the RPL neighbour port, while ERPSv1 does not.

* RPL owner port
  
  An RPL owner port is manually specified. Once specified, it is blocked to prevent loops on the ERPS ring where it resides. An ERPS ring has only one RPL owner port. When the device where the RPL owner port resides receives a message indicating a node or link fault on the ERPS ring, the device unblocks the RPL owner port so that the port resumes sending and receiving traffic, thus ensuring nonstop traffic forwarding. The link where the RPL owner port resides is the RPL.
* RPL neighbour port
  
  An RPL neighbour port is directly connected to an RPL owner port. The RPL neighbour port reduces the number of FDB entry updates on the device where the RPL neighbour port resides. Both the RPL owner port and RPL neighbour port are blocked to prevent loops under normal circumstances, and are unblocked if the ERPS ring fails.
* Common port
  
  In an ERPS ring, all ports except the RPL owner port and RPL neighbour port are common ports. A common port monitors the status of the directly connected ERPS link and sends messages to notify the other ports of link status changes.

An ERPS port can be in either of the following states:

* Forwarding: In this state, the port forwards user traffic and sends and receives R-APS PDUs.
* Discarding: In this state, the port can only send and receive R-APS PDUs.


#### VLAN

ERPS has two types of VLANs: data VLAN and control VLAN. A data VLAN is used to transmit data packets, and a control VLAN is used to transmit R-APS PDUs. Each ERPS ring must be configured with a control VLAN. After a port is added to an ERPS ring configured with a control VLAN, the port is automatically added to the control VLAN. Different ERPS rings cannot be configured with the same control VLAN.


#### ERP Instance

On a Layer 2 device running ERPS, the VLANs in which R-APS PDUs and data packets are transmitted must be mapped to an Ethernet Ring Protection (ERP) instance so that ERPS forwards or blocks these packets based on blocking rules. If the VLAN is not mapped to an ERP instance, a broadcast storm may occur on the ring network, causing the ring network to become unavailable.


#### Timers

ERPS defines four timers: Guard timer, wait to restore (WTR) timer, Holdoff timer, and wait to block (WTB) timer. Only ERPSv2 supports the WTB timer, whereas ERPSv1 does not.

* Guard timer
  
  After a faulty link or node recovers or a clear operation is performed, the device sends R-APS No Request (NR) messages to notify other devices of the link or node recovery and starts the Guard timer. Before the Guard timer expires, the device does not process any R-APS NR message to avoid receiving out-of-date R-APS NR messages. If the device still receives an R-APS NR message after the timer expires, the local port enters the Forwarding state.
* WTR timer
  
  If a device or link fails, the RPL owner port is unblocked. After the fault is rectified, the faulty port may have not changed from down to up. To prevent network flapping caused by immediate blocking of the RPL owner port, the device starts the WTR timer after the RPL owner port receives an R-APS NR message. If the device receives an R-APS Signal Failed (SF) message before the WTR timer expires, the device disables the WTR timer and does not block the RPL owner port. If the device does not receive any R-APS SF message before the WTR timer expires, the device blocks the RPL owner port when the WTR timer expires and sends an R-APS No Request RPL Blocked (NRRB) message. After receiving the R-APS NRRB message, the other ports set their forwarding status to Forwarding.
* Holdoff timer
  
  Layer 2 networks running ERPS may have different requirements on the protection switching sequence. For example, if a server fails on a network that provides multi-layer services, users may require a period of time to restore the server, during which clients are unaware of the fault. That is, protection switching is not performed immediately. You can set a proper Holdoff timer value. If a fault occurs, the fault is not immediately reported to ERPS. Instead, the fault is reported only when the Holdoff timer expires and the fault persists.
* WTB timer
  
  When the switching status (Forced Switch or Manual Switch) of a port is cleared, the WTB timer is started. Because multiple ports on an ERPS ring may be manually blocked, the clear operation takes effect only after the WTB timer expires. This prevents the RPL owner port from being blocked immediately.
  
  The WTB timer cannot be manually specified but depends on the Guard timer configuration. The value of the WTB timer is the value of the Guard timer plus 5s. The default value of the WTB timer is 7s.


#### Revertive and Non-revertive Switching Modes

After a link fault on an ERPS ring is rectified, re-blocking the RPL owner port depends on the configured revertive or non-revertive switching mode.

* In revertive switching mode, if the faulty link recovers, the RPL owner port is re-blocked after the WTR timer expires. The blocked link is switched back to the RPL.
* In non-revertive switching mode, if the faulty link recovers, the WTR timer is not started and the original faulty link is still blocked.

By default, an ERPS ring works in revertive switching mode.

ERPSv1 supports only revertive switching mode, whereas ERPSv2 supports both revertive and non-revertive switching modes.


#### Port Blocking Modes

Because the RPL on which the RPL owner port resides may have higher bandwidth, you can block a low-bandwidth link so that user traffic can be transmitted on the RPL. ERPS supports Forced Switch (FS) and Manual Switch (MS) modes for blocking a port:

* FS: A port configured with FS is immediately blocked regardless of whether other links on the ring are faulty.
* MS: The process of performing an MS operation on a port on an ERPS ring is similar to that of performing an FS operation on a port. The difference is that the MS operation does not take effect if the ERPS ring is not in Idle or Pending state.

In addition to FS and MS operations, ERPS also supports the clear operation. The clear operation applies to the following scenarios:

* Clears the local MS and FS configurations.
* Triggers revertive switching before the WTB or WTR timer expires when the ERPS ring is in revertive switching mode.
* Triggers revertive switching when the ERPS ring is in non-revertive switching mode.

Only ERPSv2 supports port blocking modes, whereas ERPSv1 does not.


#### R-APS PDU Transmission Mode in a Sub-ring

ERPSv2 supports single-ring and multi-ring topologies. In multi-ring topologies, R-APS PDUs from sub-rings can be transmitted in virtual channel (VC) and non-virtual channel (NVC) modes.

* VC mode: R-APS PDUs from a sub-ring are transmitted to the major ring through interconnected nodes. That is, interconnected nodes do not terminate R-APS PDUs from a sub-ring. A blocked port on the sub-ring blocks both R-APS PDUs and data traffic on the sub-ring.
* NVC mode: R-APS PDUs from a sub-ring are terminated on interconnection nodes. A blocked port on the sub-ring blocks data traffic but not R-APS PDUs on the sub-ring.

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000302), a major ring is interconnected with two sub-rings. The sub-ring on the left transmits R-APS PDUs in VC mode, and the sub-ring on the right transmits R-APS PDUs in NVC mode.

**Figure 3** Interconnected rings using VC and NVC modes  
![](figure/en-us_image_0000001142188106.png)

By default, R-APS PDUs from a sub-ring are transmitted in NVC mode. In a special networking scenario shown in [Figure 4](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000303) where sub-ring links are discontinuous, the VC mode must be used. In other scenarios, the default NVC mode is recommended. On the network shown in [Figure 4](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000303), links b and d belong to major rings 1 and 2 respectively, and links a and c belong to a sub-ring. Links a and c are independent of each other and cannot detect the status change of each other. Therefore, VCs must be used to transmit R-APS PDUs.

**Figure 4** Network diagram of a special scenario where virtual channels are used  
![](figure/en-us_image_0000001187948247.png)
[Table 1](#EN-US_CONCEPT_0000001141619014__tab_dc_fd_erps_000301) lists the advantages and disadvantages of R-APS PDU transmission modes on sub-rings using VC and NVC modes.

**Table 1** Comparison between VC and NVC modes
| R-APS PDU Transmission Mode in a Sub-ring | Advantage | Disadvantage |
| --- | --- | --- |
| VC | This mode can be applied to the special networking scenario shown in [Figure 4](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000303). | R-APS virtual channels on a sub-ring are affected by the topology of adjacent rings. Resources need to be reserved and control VLAN IDs need to be allocated for R-APS virtual channels on the network where these virtual channels reside. |
| NVC | This mode does not require resource reservation and control VLAN ID assignment from adjacent rings. | This mode cannot be applied to the special networking scenario shown in [Figure 4](#EN-US_CONCEPT_0000001141619014__fig_dc_fd_erps_000303). |




#### ERPSv1 and ERPSv2

ERPS has two versions: ERPSv1 and ERPSv2. ERPSv1 was released by the ITU-T in June 2008, and ERPSv2 was released by the ITU-T in August 2010. ERPSv2 is fully compatible with ERPSv1 and extends ERPSv1 functions. [Table 2](#EN-US_CONCEPT_0000001141619014__tab_dc_vrp_erps_cfg_000203) lists the differences between ERPSv1 and ERPSv2.

**Table 2** Comparison between ERPSv1 and ERPSv2
| Function | ERPSv1 | ERPSv2 |
| --- | --- | --- |
| Ring creation | Only a single ring can be created. Sub-rings cannot be configured. | Multiple rings can be created, that is, major rings and sub-rings can be configured. |
| Port role configuration | The RPL owner port and common ports can be configured. | The RPL owner port, the RPL neighbour port, and common ports can be configured. |
| Topology change notification | This function is not supported. | This function is supported. |
| Transmitting R-APS PDUs from sub-rings in VC and NVC modes | This function is not supported. | This function is supported. |
| Revertive and non-revertive switching mode | The revertive switching mode is used by default and cannot be configured. The non-revertive switching mode is not supported. | Both the revertive switching and non-revertive switching modes can be configured. |
| Manually switching blocked ports | This function is not supported. | This function is supported. Both FS and MS modes are supported. |


![](public_sys-resources/note_3.0-en-us.png) 

ERPSv2 is fully compatible with ERPSv1. If all devices on an ERPS ring support both ERPSv1 and ERPSv2, configuring ERPSv2 is recommended.