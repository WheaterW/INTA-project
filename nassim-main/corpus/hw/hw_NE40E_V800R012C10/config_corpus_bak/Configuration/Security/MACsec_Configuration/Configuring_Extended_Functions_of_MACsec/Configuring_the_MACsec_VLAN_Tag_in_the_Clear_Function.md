Configuring the MACsec VLAN Tag in the Clear Function
=====================================================

Configuring_the_MACsec_VLAN_Tag_in_the_Clear_Function

#### Context

The MACsec VLAN tag in the clear function allows MACsec not to encrypt VLAN tags. The hub site router uses a Layer 3 (IP) sub-interface of each VLAN that is associated with each remote site branch. The result is a highly flexible MACsec hub/spoke design that eliminates the older solutions that require a physical interface "per remote site" on the hub router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*.*subinterface-number*
   
   
   
   The sub-interface view is displayed.
3. Run [**macsec**](cmdqueryname=macsec) { **dot1q-in-clear** | **qinq-in-clear** }
   
   
   
   The MACsec VLAN tag in the clear function is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed