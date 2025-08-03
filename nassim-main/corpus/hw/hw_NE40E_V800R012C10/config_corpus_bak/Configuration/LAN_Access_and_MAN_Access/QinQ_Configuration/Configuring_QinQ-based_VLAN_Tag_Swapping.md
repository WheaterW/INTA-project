Configuring QinQ-based VLAN Tag Swapping
========================================

This section describes how to configure QinQ-based virtual local area network (VLAN) tag swapping. This configuration enables a device to swap the inner tag with the outer tag in a double-tagged packet. QinQ-based VLAN tag swapping applies only on double-tagged packets.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172363250__fig_dc_vrp_qinq_cfg_004701), the user-end provider edge (UPE) is connected to multiple customer edges (CEs), and each packet that the UPE receives from the CEs carries two VLAN tags. The outer tag indicates the user, and the inner tag indicates the service. The UPE, however, can only forward packets whose outer tags indicate services and inner tags indicate users. To address this problem, the UPE needs to swap the inner tag with the outer tag in double-tagged packets.

In this situation, configure QinQ-based VLAN tag swapping on the UPE.

**Figure 1** Networking for QinQ-based VLAN tag swapping  
![](figure/en-us_image_0000001559167570.png)
#### Pre-configuration Tasks

Before configuring QinQ-based VLAN tag swapping, configure user VLANs so that packets received by an interface or sub-interface carry two VLAN tags.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)*interface-type interface-number*
   
   
   
   The view of the Ethernet interface on which QinQ-based VLAN tag swapping is to be configured is displayed.
3. Run [**vlan-swap enable**](cmdqueryname=vlan-swap+enable)
   
   
   
   VLAN tag swapping is enabled.
   
   
   
   After BA classification based on 802.1p values is configured on a VLAN-swap-capable interface, BA classification is implemented based on the 802.1p values of the swapped outer VLAN tag.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring QinQ-based VLAN tag swapping, check the configurations.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether QinQ-based VLAN tag swapping is configured.