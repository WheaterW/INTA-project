Configuring an AC Interface
===========================

In MPLS E-Line scenarios, a Layer 2 sub-interface can function as an AC interface, and traffic encapsulation can be configured on the AC interface to transmit different types of data packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   A Layer 2 sub-interface is created, and its view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If the configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete it.
   
   In addition to a Layer 2 sub-interface, an Ethernet main interface, Layer 3 sub-interface, or Eth-Trunk interface can also function as an AC interface.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   The encapsulation type of packets allowed to pass through the Layer 2 sub-interface is specified.
4. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   The Layer 2 sub-interface is bound to an EVPL instance.
5. (Optional) Run [**evpn-vpws ignore-ac-state**](cmdqueryname=evpn-vpws+ignore-ac-state)
   
   
   
   The function to ignore the AC status on an interface is enabled.
   
   This step can be performed to ensure EVPN VPWS service continuity after the AC interface is configured with the CFM and interface association function in a primary/secondary link networking scenario. In this case, if a primary/secondary link switchover is triggered after the AC status of the interface is changed to down, the AC status of the interface is ignored, and the EVPN VPWS service does not need to be re-established during a primary/secondary link switchover.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.