Configuring a VLAN Tag Termination Sub-interface
================================================

A VLAN tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

#### Procedure

* Configure a dot1q VLAN tag termination sub-interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     The view of the PE's Ethernet sub-interface connecting to the user side is displayed.
  3. (Optional) Create a user VLAN group.
     
     1. Run [**vlan-group**](cmdqueryname=vlan-group) *group-id*
        
        A user VLAN group is created.
     2. Run [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** }
        
        The working mode of the VLAN group is configured.
        
        + **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets or deploy quality of service (QoS) policies based on a VLAN or a VLAN range.
        + **multiple**: VLANs and VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets or deploy QoS policies based on a VLAN or VLAN range to implement refined management.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the view of the PE's Ethernet sub-interface connecting to the user side.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configuring a VLAN group allows you to achieve the following purposes:
     
     + Deploy QoS policies based on services or users so that higher priority service traffic is preferentially forwarded, improving user experience.
     + View statistics about QinQ packets to check whether a device is functioning properly.
  4. Run [**control-vid**](cmdqueryname=control-vid) *vid* **dot1q-termination** [ **rt-protocol** ] or [**encapsulation**](cmdqueryname=encapsulation) **dot1q-termination** [ **rt-protocol** ]
     
     The encapsulation type is configured as dot1q VLAN tag termination for the sub-interface.
     
     Specify **rt-protocol** so that the dot1q VLAN tag termination sub-interface supports routing protocols.
     
     To enable the dot1q VLAN tag termination sub-interface to support routing protocols, specify **rt-protocol**.
  5. Run [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ]
     
     The VLAN tag termination function is configured for the dot1q VLAN tag termination sub-interface.
     
     After you specify **rt-protocol**, the dot1q VLAN tag termination sub-interface terminates packets carrying a fixed-value VLAN tag.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a QinQ VLAN tag termination sub-interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     The view of the PE's Ethernet sub-interface connecting to the user side is displayed.
  3. (Optional) Create a user VLAN group.
     
     1. Run [**vlan-group**](cmdqueryname=vlan-group) *group-id*
        
        A user VLAN group is created.
     2. Run [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** }
        
        The working mode of the VLAN group is configured.
        
        + **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets or deploy quality of service (QoS) policies based on a VLAN or a VLAN range.
        + **multiple**: VLANs and VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets or deploy QoS policies based on a VLAN or VLAN range to implement refined management.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the view of the PE's Ethernet sub-interface connecting to the user side.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configuring a VLAN group allows you to achieve the following purposes:
     
     + Deploy QoS policies based on services or users so that higher priority service traffic is preferentially forwarded, improving user experience.
     + View statistics about QinQ packets to check whether a device is functioning properly.
  4. Run [**control-vid**](cmdqueryname=control-vid) *vid* **qinq-termination** [ **local-switch** | **rt-protocol** ] or [**encapsulation**](cmdqueryname=encapsulation) **qinq-termination** [ **local-switch** | **rt-protocol** ]
     
     The encapsulation type is configured as QinQ VLAN tag termination for the sub-interface.
     
     + Specify **local-switch** so that the QinQ VLAN tag termination sub-interface supports local switching.
     + Specify **rt-protocol** so that the QinQ VLAN tag termination sub-interface supports routing protocols.
  5. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
     
     The VLAN tag termination function is configured for the QinQ VLAN tag termination sub-interface.
     
     After you specify **rt-protocol**, the QinQ VLAN tag termination sub-interface terminates packets carrying two fixed-value VLAN tags.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.