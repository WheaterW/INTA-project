Understanding MSTP Multi-Process
================================

MSTP multi-process is an enhancement to MSTP. The MSTP multi-process mechanism allows ports on devices to be bound to different processes, based on which MSTP calculation is performed. In this manner, only ports that are bound to a process participate in the MSTP calculation for this process. With the MSTP multi-process mechanism, spanning trees of different processes are calculated independently and do not affect each other.

#### Context

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001345318765__fig151220144355):

* User-facing Provider Edges (UPEs) are deployed at the aggregation layer, running MSTP.
* UPE1 and UPE2 are connected by a Layer 2 link.
* Multiple rings are connected to UPE1 and UPE2 through different ports.
* Devices on the rings are access devices running STP or RSTP. Because UPE1 and UPE2 are provided by different carriers, they reside on different spanning trees so that their topology changes do not affect each other.

UPE1 and UPE2 are connected to multiple independent access rings. Neither STP nor RSTP can calculate a single spanning tree for all devices. Instead, one of them must be enabled on each ring to calculate a separate spanning tree.

MSTP supports MSTIs, but these MSTIs must belong to one MST region and devices in the region must have the same configurations. If devices belong to different regions, MSTP calculates a spanning tree based on only one instance. If this is the case, the status change of any device on the network affects the stability of the entire network. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001345318765__fig151220144355), access devices connected to UPEs support STP or RSTP only, not MSTP. When MSTP-enabled UPEs receive BPDUs from the access devices, the UPEs consider that both they and the access devices belong to different regions. As a result, only one spanning tree is calculated for the rings formed by the UPEs and access devices, and in this case, the access rings are not independent of each other.

MSTP multi-process can prevent this problem. This is a mechanism that allows ports on devices to be added to different processes, based on which MSTP calculation is performed. In this manner, only ports added to the same process participate in the MSTP calculation in this process. The network shown in [Figure 1](#EN-US_CONCEPT_0000001345318765__fig151220144355) can be divided into multiple MSTP processes by using MSTP multi-process; ports on each of the rings are added to the same process. The MSTP processes have the same functions and support MSTIs, and the calculation for one process does not affect that of another process.

![](public_sys-resources/note_3.0-en-us.png) 

MSTP multi-process is applicable to MSTP, RSTP, and STP.


**Figure 1** Application of both MSTP and STP/RSTP  
![](figure/en-us_image_0000001345158177.png)

#### Purpose

MSTP multi-process provides the following benefits:

* Greatly improves the applicability of spanning tree protocols to different networking conditions.
  
  On a network running different spanning tree protocols, ports on devices that run different spanning tree protocols can be added to different processes, allowing every process to calculate a separate, independent spanning tree.
* Improves networking reliability.
  
  A network topology is calculated for each process so that, if a device fails, only the topology corresponding to the process that the device belongs to is affected.
* Reduces the network administrator workload during network expansion.
  
  To expand a network, a network administrator must not only configure new MSTP processes, but also add the ports that connect new devices to existing devices to the new MSTP processes, and keep the existing MSTP processes unchanged. If device expansion is performed in a process, then only this process needs to be modified.
* Implements separate Layer 2 port management
  
  An MSTP process manages separate ports on a device. Layer 2 ports on a device are separately managed by multiple MSTP processes.


#### Fundamentals

**Shared Link Status**

In [Figure 1](#EN-US_CONCEPT_0000001345318765__fig151220144355), ports on the shared link between UPE1 and UPE2 need to participate in the calculation of multiple access rings and MSTP processes. The UPEs must identify the process from which MSTP BPDUs are sent.

In addition, a port on the shared link participates in the calculation for multiple MSTP processes, and obtains a different status, and so cannot determine its own status.

To prevent this, the port always adopts its status in MSTP process 0 when participating in the calculation for multiple MSTP processes.

![](public_sys-resources/note_3.0-en-us.png) 

By default, MSTP process 0 is created when a device starts, and MSTP configurations in the system view and interface view belong to this process.

**Reliability**

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001345318765__fig1825411534322), after the topology of access devices changes, the MSTP multi-process mechanism helps UPEs flood a TC BPDU to all devices on the ring and not to devices on other rings. UPE1 and UPE2 update MAC address and ARP entries on the ports corresponding to the changed spanning tree.

**Figure 2** MSTP multi-process topology change  
![](figure/en-us_image_0000001292078976.png "Click to enlarge")

**Shared Link Faults and Solutions**

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001345318765__fig1981142310155), if the shared link between UPE1 and UPE2 fails, multiple devices may unblock their blocked ports on the access ring. Assume that UPE1 is configured with the highest priority, UPE2 with the second highest priority, and all other access devices with default or lower priorities. After the shared link between UPE1 and UPE2 fails, the blocked ports (backup ports for the root ports) on access devices no longer receive BPDUs with higher priorities, triggering spanning tree calculation. If this calculation changes the blocked ports to designated ports, a permanent loop forms.

**Figure 3** Loop between access rings  
![](figure/en-us_image_0000001292238804.png "Click to enlarge")

To prevent a loop between access rings, use either of the following solutions:

* Configure an Eth-Trunk between UPE1 and UPE2 as a shared link to improve link reliability, as shown in [Figure 4](#EN-US_CONCEPT_0000001345318765__fig88171142185818).**Figure 4** Eth-Trunk as a shared link  
  ![](figure/en-us_image_0000001345318845.png)
* Configure root protection between UPE1 and UPE2.
  
  On the network shown in [Figure 5](#EN-US_CONCEPT_0000001345318765__fig72061423191717), UPE1 is configured with the highest priority, UPE2 with the second highest priority, and devices on access rings with default or lower priorities. Root protection is enabled on UPE1 and UPE2.
  
  For example, if BP 1 on DeviceB is blocked on the yellow ring, when the shared link between UPE1 and UPE2 fails, DeviceB starts to calculate the spanning tree because BP 1 no longer receives higher-priority BPDUs. After calculation, BP 1 becomes a designated port and performs P/A negotiation with the downstream device.
  
  After DeviceB sends higher-priority BPDUs to the UPE2 port enabled with root protection, the port is blocked, and remains so because it continues to receive BPDUs of higher priorities. This prevents a network loop.
  
  **Figure 5** MSTP multi-process with root protection  
  ![](figure/en-us_image_0000001345158189.png)