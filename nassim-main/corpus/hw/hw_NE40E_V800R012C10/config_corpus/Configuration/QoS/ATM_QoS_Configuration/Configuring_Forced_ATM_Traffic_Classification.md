Configuring Forced ATM Traffic Classification
=============================================

ATM forced traffic classification can be configured on an upstream sub-interface, a PVP, or a PVC to classify traffic, mark the traffic with specific color, and perform queue scheduling based on the classification and color.

#### Usage Scenarios

Forced ATM traffic classification can be applied to the following situations:

* Transparent transmission of ATM cells
  
  As shown in [Figure 1](#EN-US_TASK_0172371658__fig_dc_ne_qos_cfg_01238302), transparent transmission of ATM cells needs to be set on DeviceA and DeviceB for ATM traffic accessed through DSLAM. DeviceA transmits the received ATM cells to DeviceB over a PW. DeviceB continues to forward the ATM cells over its ATM links.
  
  On the upstream sub-interface, PVP or PVC of DeviceA, forced traffic classification can be set to classify traffic and mark the traffic with specific color. Then the downstream interface, PVP or PVC of DeviceA can schedule queues on the basis of the forced classification and coloring.
  
  **Figure 1** Forced traffic classification for transparent transmission of ATM cells  
  ![](images/fig_dc_ne_qos_cfg_01238302.png)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Forced traffic classification based on PVC supports such services as transparent transmission of ATM cells, and IPoA.
* Forced traffic classification based on PVP supports such services as transparent transmission of ATM cells.
* Forced traffic classification based on sub-interface supports such services as transparent transmission of ATM cells, and IPoA.
* Forced traffic classification based on the main interface is valid to only PVC or PVP of the interface and supports transparent transmission of ATM cells and IPoA.


#### Pre-configuration Tasks

Before configuring forced ATM traffic classification, complete the following tasks:

* Configuring an L2VPN between PEs at both ends and binding the L2VPN to the two PEs' interfaces that connect to CEs
* Configuring PVCs on CEs and configuring transparent cell transmission at the ATM side on PEs

#### Configuration Procedures

**Figure 2** Flowchart for Configuring Forced ATM Traffic Classification  
![](images/fig_dc_ne_qos_cfg_01238301.png)


[Configuring ATM Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012385.html)

The ATM service can be transmitted through ATM cell relay, or IPoA.

[Configuring ATM Forced Traffic Classification](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012386.html)

This section describes how to configure asynchronous transfer mode (ATM) forced traffic classification. ATM forced traffic classification can be configured on ATM interfaces, ATM sub-interfaces, permanent virtual circuits (PVCs), and permanent virtual paths (PVPs).

[Verifying the Configuration of ATM Forced Traffic Classification](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012387.html)

After ATM forced traffic classification is configured, you can view that traffic is classified as defined.