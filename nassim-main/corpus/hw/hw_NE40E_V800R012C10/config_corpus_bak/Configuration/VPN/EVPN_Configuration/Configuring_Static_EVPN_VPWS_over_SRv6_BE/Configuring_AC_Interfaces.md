Configuring AC Interfaces
=========================

In an EVPN VPWS scenario, you can configure Layer 2 sub-interfaces to function as AC interfaces and configure traffic encapsulation on these Layer 2 sub-interfaces, so that they can transmit different types of data packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   A Layer 2 sub-interface is created, and the sub-interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the involved Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If this configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete the configuration.
   
   In addition to Layer 2 sub-interfaces, Ethernet main interfaces, Layer 3 sub-interfaces, and Eth-Trunk interfaces can also function as AC interfaces.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   A packet encapsulation type is configured, so that the Layer 2 sub-interface can transmit data packets of the specified encapsulation type.
4. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   The Layer 2 sub-interface is bound to an EVPL instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.