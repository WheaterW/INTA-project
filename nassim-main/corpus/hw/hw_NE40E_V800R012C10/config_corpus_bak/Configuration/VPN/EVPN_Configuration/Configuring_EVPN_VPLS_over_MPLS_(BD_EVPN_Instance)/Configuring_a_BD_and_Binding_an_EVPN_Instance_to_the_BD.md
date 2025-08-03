Configuring a BD and Binding an EVPN Instance to the BD
=======================================================

An EVPN instance in BD mode is only bound to a BD instead of an interface.

#### Context

An EVPN instance can be bound to a BD in two ways: using a VXLAN Network Identifier (VNI) and using MPLS. In VNI mode, an EVPN instance is bound to a BD after a VNI is configured. In MPLS mode, an EVPN instance is bound to a BD directly in the BD view. If an EVPN instance needs to access a VPLS network, the EVPN instance must be bound to a BD in VNI mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The view of the BD to be bound to an EVPN instance is displayed.
3. (Optional) Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode**
   
   
   
   A VNI is created and associated with the BD, and split horizon is specified for packet forwarding.
4. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ]
   
   
   
   The BD is bound to the EVPN instance. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
5. (Optional) Configure the EVPN route learning mode as **qualify**.
   1. Run the [**mac-learn-style qualify**](cmdqueryname=mac-learn-style+qualify) command to configure the MAC address learning mode as **qualify**.
      
      
      
      If no MAC address learning mode is configured, each MAC address is unique in the BD, and the device learns MAC addresses based on BDs. VLAN-based differentiation is not needed in this case. If users need to be differentiated based on VLANs, perform this step to set the MAC address learning mode to **qualify**, so that each VLAN has its own MAC address space. The device learns MAC addresses based on both MAC addresses and VLAN tags carried in user Ethernet packets.
   2. Run the [**evpn qualify-compatible**](cmdqueryname=evpn+qualify-compatible) command to configure EVPN qualify enhancement.
      
      
      
      After this function is configured, EVPN Ethernet A-D per-EVI, EVPN inclusive, and EVPN UMR routes are generated based on VLANs.
   
   
   
   This step is recommended when the VLAN-aware service model is used on the user side for EVPN access.
6. (Optional) Run [**reserve-interface fast-switch enable**](cmdqueryname=reserve-interface+fast-switch+enable)
   
   
   
   The reserve-interface fast switching function is enabled.
   
   When the active interface board fails, you can perform this step to enable reserve-interface fast switching, so that broadcast traffic can be quickly switched to the standby interface board.
7. (Optional) Enable the function to apply the DF election result of a BD to all AC interfaces in the BD.
   
   
   1. Run the [**evpn df-result spread enable**](cmdqueryname=evpn+df-result+spread+enable) command to enable the function to apply the DF election result of a BD to all AC interfaces in the BD.
   2. Run the [**esi**](cmdqueryname=esi) *esi* command to configure an ESI for the BD.
   3. Run the [**timer es-recovery**](cmdqueryname=timer+es-recovery) *seconds* command to configure a delay after which Ethernet segment routes are advertised to prevent traffic loss during traffic switchback.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   A Layer 2 sub-interface is created, and the Layer 2 sub-interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the involved Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If the configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete it.
10. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }, 
    
    
    
    A traffic encapsulation type is specified for the Layer 2 sub-interface.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the MAC address learning mode is **qualify**, **ce-vid** used in QinQ encapsulation cannot be **default**.
11. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** }
    
    
    
    The function to remove VLAN tags from received packets is enabled.For single-tagged packets that a Layer 2 sub-interface receives, specify **single** to enable the sub-interface to remove single VLAN tags from these packets.
    
    If the encapsulation type of packets has been set to QinQ in the previous step, specify **double** to enable the sub-interface to remove double VLAN tags from the received packets.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the current MAC address learning mode is **qualify**, this step cannot be performed.
12. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
    
    
    
    The Layer 2 sub-interface is added to the BD to transmit data packets through this BD.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.