(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces
=================================================================

If the MAC address of an L2VE or L3VE interface is the same as that of another interface on a BNG, configure a new MAC address for the L2VE or L3VE interface to ensure normal communication.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**set l2ve-mac**](cmdqueryname=set+l2ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L2VE interface.
   
   
   
   You can modify the MAC address of an L2VE interface on a BNG if this MAC address is the same as that of an M-AGG interface connected to the BNG.
   
   An L2VE interface can have only one MAC address.
4. Run [**set access-ve-mac**](cmdqueryname=set+access-ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L3VE interface.
   
   
   
   Perform this step to change the MAC address of the L3VE interface if the L2VE interface is bound to the same EVPL instance as an Eth-Trunk interface or a sub-interface of an interface on which the **portswitch** command is run and the preceding Eth-Trunk interface or sub-interface needs to communicate with the L3VE interface at Layer 3. An L3VE interface can have only one MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.