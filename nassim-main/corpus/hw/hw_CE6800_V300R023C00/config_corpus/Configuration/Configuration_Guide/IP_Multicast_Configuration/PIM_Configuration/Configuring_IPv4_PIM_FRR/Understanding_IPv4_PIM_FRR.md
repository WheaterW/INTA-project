Understanding IPv4 PIM FRR
==========================

PIM FRR establishes primary and backup links through unicast backup FRR paths to provide link protection for PIM-SM or PIM-SSM shortest path trees (SPTs). This and implements fast switchover after a link fault occurs, reducing multicast traffic loss.

#### Background

The setup of an MDT depends on unicast routes. If a link on the network fails, a new MDT can be set up only after unicast route convergence is completed; however, this process takes a long time and causes excessive multicast traffic loss.

PIM FRR solves this problem. It allows a device to send Join messages to the multicast source based on primary and backup unicast FRR routes to establish primary and backup MDTs. In this case, the cross-connect nodes of the primary and backup links receive multicast traffic from both the primary and backup links. The forwarding plane accepts traffic from the primary link and discards traffic from the backup link. However, if the primary link fails, the forwarding plane immediately accepts traffic from the backup link, reducing multicast traffic loss.


#### Implementation

PIM FRR implementation involves three steps:

1. Establishment of primary and backup MDTs
   
   After the primary inbound interface is added to the PIM-SM (S, G) entries in which SPT switchover information has been updated or added to PIM-SSM (S, G) entries according to unicast routes, the device checks whether a backup FRR route exists. If it exists, the system also adds the backup inbound interface to the entries. The device then sends a PIM Join message along both the primary and backup routes to the multicast source to set up primary and backup MDTs. [Figure 1](#EN-US_CONCEPT_0000001314140801__fig_dc_vrp_feature_new_00727106) shows the process of setting up primary and backup MDTs.
   
   **Figure 1** Setting up primary and backup MDTs  
   ![](figure/en-us_image_0000001314065453.png "Click to enlarge")
2. Fault detection and protection
   
   After the primary and backup MDTs are set up, each device with primary and backup routes (such as DeviceA) receives two copies of multicast traffic. In normal cases, the forwarding plane accepts traffic from the primary link and discards traffic from the backup link. If the primary link fails, the forwarding plane detects that the primary link is down and accepts traffic from the backup link immediately. If two devices are connected through a link that passes through another device (such as a multiplexer/demultiplexer device), the link may still be up after the link fails. In this case, PIM FRR cannot trigger a fast switchover through link state detection. In this case, you can deploy single-hop BFD to solve the problem. If Eth-Trunk is used, you are advised to configure BFD link-bundle. After a multicast inbound interface is bound to a BFD session, PIM FRR can detect the BFD session to implement fast switchover.
   
   In [Figure 2](#EN-US_CONCEPT_0000001314140801__fig115225916260), DeviceA accepts traffic from the primary link and discards traffic from the backup link.
   
   **Figure 2** PIM FRR implementation before the failure occurs  
   ![](figure/en-us_image_0000001375889514.png "Click to enlarge")
   
   In [Figure 3](#EN-US_CONCEPT_0000001314140801__fig14130103202611), DeviceA accepts multicast traffic from the backup link (DeviceB -> DeviceD -> DeviceA) immediately after detecting the failure on the local primary link.
   
   **Figure 3** PIM FRR implementation after the failure occurs  
   ![](figure/en-us_image_0000001375729950.png "Click to enlarge")
3. Switchback process
   
   After a link fault is rectified, the PIM protocol layer starts route switchback upon detection of the route change. To ensure sufficient time for forwarding entry restoration, the forwarding plane enters the WTR state for a delayed switchback. After the WTR time expires, traffic is smoothly converged to the optimal primary path.

#### Benefits

PIM FRR provides link protection for multicast services with high requirements on real-time transmission.


#### Usage Limitations

PIM FRR has the following limitations:

* It applies only to IPv4 networks.
* Node protection cannot be preferentially used in equal-cost multiple path (ECMP) scenarios because IGPs cannot compute backup paths in these scenarios.
* PIM FRR has the following limitations in non-ECMP scenarios:
  + On an IGP network with PIM FRR deployed, the IGP does not back up information about the backup link. After a primary/backup link switchover occurs, the multicast backup link may be deleted during data smoothing. As a result, rapid switchover cannot be implemented if the primary link fails.
  + Only LFA FRR-based non-ECMP PIM FRR is supported, but not remote FRR-based non-ECMP PIM FRR.
* If PIM FRR is deployed on a network with LFA FRR configured, PIM FRR inherits the limitations of IGP LFA FRR.
* If PIM FRR is deployed on a network with LFA FRR configured, rapid primary/backup link switchover is not supported if the backup link is an ECMP one.
* PIM FRR supports only PIM-SM SPT (S, G) entries. Backup paths and PIM-SSM entries are generated only when multicast traffic is available.
* The primary and secondary inbound interfaces supported by PIM FRR can be physical interfaces, physical sub-interfaces, Eth-Trunk interfaces, Eth-Trunk sub-interfaces, or VLANIF interfaces (the primary and secondary inbound interfaces cannot be both VLANIF interfaces).
* PIM FRR cannot be used in IPv4 Layer 3 multicast over VXLAN scenarios.