(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces
=================================================================

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. (Optional) Run [**set l2ve-mac**](cmdqueryname=set+l2ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L2VE interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can modify the MAC address of an L2VE interface on an NPE if the MAC address of the interface is the same as the MAC address of a UPE interface that connects to the NPE. An L2VE interface can have only one MAC address.
4. (Optional) Run [**set access-ve-mac**](cmdqueryname=set+access-ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L3VE interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An L3VE interface uses the bridge MAC address as its MAC address and an Eth-Trunk or portswitch interface also uses the bridge MAC address. If an L2VE interface is bound to the same local VSI as a sub-interface of the Eth-Trunk or portswitch interface and Layer 3 interworking is implemented between the L3VE interface and the sub-interface, packets sent to the L3VE interface may be incorrectly dropped at the Layer 2 interface. To prevent incorrect packet drop, you can modify the MAC address of the L3VE interface. Note that an L3VE interface can have only one MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.