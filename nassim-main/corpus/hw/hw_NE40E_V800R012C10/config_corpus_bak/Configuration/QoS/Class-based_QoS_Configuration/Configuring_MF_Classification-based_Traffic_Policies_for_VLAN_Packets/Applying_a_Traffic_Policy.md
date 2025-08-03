Applying a Traffic Policy
=========================

A class-based policy does not take effect unless it is applied to an interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform the following operations based on the interfaces on which a traffic policy is used:
   
   
   * Apply an MF classification-based traffic policy to a Layer 3 interface.
     1. To enter the Layer 3 interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command.
     2. To apply a traffic policy to the Layer 3 interface, run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } [ **all-layer** | **link-layer** | **mpls-layer** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If **link-layer** is configured, the device performs MF classification based on Layer 2 information of packets.
        
        If **mpls-layer** is configured, the device performs MF classification based on MPLS packet header information.
        
        If **all-layer** is configured, the device first performs MF classification based on Layer 2 information of packets. If packets do not match any rule based on Layer 2 information, the device performs MF classification based on Layer 3 information of packets.
   * Apply an MF classification-based traffic policy to a Layer 2 interface, with a VLAN ID range specified.
     1. To enter the Layer 3 interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command.
     2. To change the interface mode from Layer 3 to Layer 2, run the [**portswitch**](cmdqueryname=portswitch) command.
     3. To add the Layer 2 interface to a specific VLAN in tagged mode, run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command.
     4. To apply a traffic policy to the Layer 2 interface, run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] | **all** } [ **all-layer** | **link-layer** | **mpls-layer** ] command.
   * Apply an MF classification-based traffic policy to an EVC Layer 2 sub-interface, with the bandwidth allocation mode specified.
     1. To enter the EVC Layer 2 sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command.
     2. To apply a traffic policy to the EVC Layer 2 sub-interface, run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } **identifier** { **none** | **vid** | **ce-vid** | **vid-ce-vid** } [ **all-layer** | **link-layer** | **mpls-layer** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The bandwidth allocation mode specified using the **identifier** parameter must be the same as the one configured on the EVC Layer 2 sub-interface.
   * Apply an MF classification-based traffic policy to a QinQ VLAN tag termination sub-interface, with the PVLAN ID and CVLAN ID ranges specified.
     1. To enter the sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number* command.
     2. To set a VLAN ID range for the sub-interface and configure the sub-interface to remove the tags from double-tagged packets, run the [**encapsulation**](cmdqueryname=encapsulation) **qinq-termination** [ **local-switch** | **rt-protocol** ] command.
     3. To configure the sub-interface as a QinQ VLAN tag termination sub-interface, run the [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ] command.
     4. To apply a traffic policy to the QinQ VLAN tag termination sub-interface, run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } **pe-vid** *pe-vid* **ce-vid** *ce-vid1* [ **to** *ce-vid2* ] [ **all-layer** | **link-layer** | **mpls-layer** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        You can directly run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } [ **all-layer** | **link-layer** | **mpls-layer** ] command to apply an MF classification-based traffic policy to a QinQ VLAN tag termination sub-interface without specifying PVLAN and CVLAN IDs.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.