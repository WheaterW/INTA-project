(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces
=================================================================

If the MAC address of the L2VE or L3VE interface is the same as that of another interface on a vBRAS-pUP, configure a new MAC address for the L2VE or L3VE interface for proper communication.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**set l2ve-mac**](cmdqueryname=set+l2ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L2VE interface.
   
   
   
   You can change the MAC address of an L2VE interface to prevent MAC address conflicts.
   
   An L2VE interface has only one MAC address.
4. Run [**set access-ve-mac**](cmdqueryname=set+access-ve-mac) *mac-address*
   
   
   
   A MAC address is configured for the L3VE interface.
   
   
   
   Perform this step to change the MAC address of the L3VE interface if an L2VE interface is bound to the same BD as an Eth-Trunk interface or a sub-interface of an interface on which the **portswitch** command is run, and the preceding Eth-Trunk interface or sub-interface needs to communicate with the L3VE interface at Layer 3. The L3VE interface uses a bridge MAC address as an interface MAC address. If the same bridge MAC address is also used by an Eth-Trunk interface or an interface on which the **portswitch** command is run, the Layer 2 interface incorrectly discards packets before the packets are sent to the L3VE interface.
   
   An L3VE interface has only one MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.