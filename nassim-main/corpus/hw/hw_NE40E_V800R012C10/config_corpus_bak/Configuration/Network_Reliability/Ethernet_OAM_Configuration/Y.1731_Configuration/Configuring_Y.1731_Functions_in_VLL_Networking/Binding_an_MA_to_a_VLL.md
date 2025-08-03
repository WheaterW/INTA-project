Binding an MA to a VLL
======================

Binding an MA to a VLL is a prerequisite for configuring single-ended packet loss measurement, dual-ended packet loss measurement, one-way packet delay measurement, two-way packet delay measurement.

#### Context

VLL-based performance monitoring is L2VC-specific. Therefore, when deploying performance monitoring defined in Y.1731 on a VLL, bind an MA to a specified L2VC, and then collect performance statistics about the MA. Then, performance statistics about a specified PW or AC will be available.

* To collect performance statistics about a PW, do as follows on the PEs at both ends of a VLL.
* To collect performance statistics about an AC between a PE and a CE, do as follows on the PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
4. Associate the MA with a service.
   
   
   * LDP VLL scenarios
     
     Run [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** }
     
     The MA is bound to a specified L2VC.
   * BGP VLL scenarios
     
     Run [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id*
     
     The MA is bound to a specified PW.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   MA cannot be associated with backup VC in 802.1ag.
   
   
   The interface of the **raw** type and the interface of the **tagged** type process packets in different manners, as shown in [Table 1](#EN-US_TASK_0172362062__tab_dc_vrp_cfg_01151401) and [Table 2](#EN-US_TASK_0172362062__tab_dc_vrp_cfg_01151402).
   
   **Table 1** Packet processing on an inbound interface
   | Inbound Interface Type | Raw Encapsulation (Ethernet Encapsulation) | Tagged Encapsulation (VLAN Encapsulation) |
   | --- | --- | --- |
   | Dot1q sub-interface | Removes one tag. | Keeps the tag unchanged. |
   | Dot1q termination sub-interface | Removes one tag. | Keeps the tag unchanged. |
   | QinQ termination sub-interface (in symmetry mode) | Removes the outer tag. | Keeps both inner and outer tags unchanged. |
   | QinQ termination sub-interface (in asymmetry mode) | Removes both the inner and outer tags. | Removes both inner and outer tags, and then adds another tag. |
   
   
   **Table 2** Packet processing on an outbound interface
   | Outbound Interface Type | Raw Encapsulation (Ethernet Encapsulation) | Tagged Encapsulation (VLAN Encapsulation) |
   | --- | --- | --- |
   | Dot1q sub-interface | Adds one tag. | Replaces the VLAN ID in the tag contained in a packet with the local VLAN ID. |
   | Dot1q termination sub-interface | Adds one tag. | Replaces the VLAN ID in the tag contained in a packet with the local VLAN ID. |
   | QinQ termination sub-interface (in symmetry mode) | Adds an outer tag. | Replaces the VLAN ID in the outer tag contained in a packet with the local VLAN ID. |
   | QinQ termination sub-interface (in asymmetry mode) | Adds two tags. | Removes the outer tag and then adds two tags. |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.