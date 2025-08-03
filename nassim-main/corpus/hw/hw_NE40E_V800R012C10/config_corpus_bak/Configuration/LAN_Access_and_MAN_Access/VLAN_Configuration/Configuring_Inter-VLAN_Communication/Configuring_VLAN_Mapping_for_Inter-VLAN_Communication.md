Configuring VLAN Mapping for Inter-VLAN Communication
=====================================================

The configuration of VLAN mapping is simple and independent of Layer 3 routing.

#### Context

VLAN mapping is also called VLAN translation. With VLAN mapping, a device maps the VLAN ID of a frame to another VLAN ID after receiving the frame and before sending the frame. On the network shown in [Figure 1](#EN-US_TASK_0172363110__fig_dc_vrp_vlan_cfg_005901), ports connecting CE 1 to users are added to VLAN 2 and ports connecting CE 2 to users are added to VLAN 3. To allow users in VLAN 2 and VLAN 3 to communicate with each other, configure VLAN mapping on the uplink interface interface1 of CE1.

* Before sending a frame to VLAN 3, interface1 on CE 1 replaces the VLAN ID 2 in the frame with the VLAN ID 3.
* After receiving a frame from VLAN 3, interface1 on CE 1 replaces the VLAN ID 3 in the frame with the VLAN ID 2.

**Figure 1** Configuring VLAN mapping for inter-VLAN communication  
![](figure/en-us_image_0000001623111040.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring VLAN mapping to allow PCs in two VLANs to communicate, IP addresses of the PCs must belong to the same network segment. Otherwise, communication between these devices must be implemented using Layer 3 routes, making VLAN mapping invalid.


Currently, the NE40E supports the following mapping modes:

* 1 to 1 VLAN mapping
  
  After receiving a single-tagged frame, the device replaces the tag with a specified tag.
  
  1 to 1 VLAN mapping is applicable to the networking environment shown in [Figure 2](#EN-US_TASK_0172363110__fig_dc_vrp_vlan_cfg_005902).
  
  **Figure 2** 1 to 1 VLAN mapping  
  ![](figure/en-us_image_0000001591309738.png)
  
  On the network shown in [Figure 2](#EN-US_TASK_0172363110__fig_dc_vrp_vlan_cfg_005902), different types of services (Internet, IPTV, and VoIP) of each household are transmitted in separate VLANs. To differentiate between households, you need to configure 1 to 1 VLAN mapping on each corridor switch to transmit the same type of services for different households in separate VLANs. In this case, the aggregation switch must provide a large number of VLAN IDs to separate services of different households. As the number of available VLAN IDs on the aggregation switch is limited, you need to implement VLAN aggregation to transmit the same type of services for different households in one VLAN.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Add the ports connected to users to the specified VLANs.
3. Configure the Layer 2 port type.
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of an Ethernet port to be configured with VLAN mapping.
   2. Run the [**port link-type**](cmdqueryname=port+link-type) **trunk** command to configure the Layer 2 Ethernet port as a trunk port.
4. Run [**port vlan-mapping**](cmdqueryname=port+vlan-mapping) **vlan** *vlan-id1* [ **to** *vlan-id2* ] **map-vlan** *vlan-id3*
   
   
   
   VLAN mapping is configured to change the outer VLAN tag to *vlan-id3*.
5. Run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command to specify the VLAN IDs permitted by the port configured with VLAN mapping.
   
   
   
   The VLAN ID specified in this command must be private VLAN IDs and cannot be public VLAN IDs.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.