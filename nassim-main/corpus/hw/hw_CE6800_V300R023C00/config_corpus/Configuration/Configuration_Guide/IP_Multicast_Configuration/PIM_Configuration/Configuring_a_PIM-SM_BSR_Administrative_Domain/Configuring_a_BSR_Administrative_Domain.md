Configuring a BSR Administrative Domain
=======================================

Configuring a BSR Administrative Domain

#### Context

A PIM domain can be divided into multiple BSR administrative domains and a global domain to facilitate PIM domain management. Each BSR administrative domain maintains one BSR, which serves multicast groups within a specific range. The global domain also maintains one BSR, which serves the other multicast groups. A device belongs to only one administrative domain. Therefore, multicast packet forwarding in one administrative domain is independent of that in other administrative domains. Multicast messages for the global domain can traverse any administrative domain.

The maximum range of multicast groups that a BSR administrative domain can serve is 239.0.0.0 to 239.255.255.255. Multicast addresses in this range can be used repeatedly and are equivalent to private group addresses of each BSR administrative domain.


#### Procedure

1. Enable the BSR administrative domain function on all devices in the PIM domain.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the PIM view.
      
      
      ```
      [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
      ```
   3. Enable the BSR administrative domain function.
      
      
      ```
      [c-bsr admin-scope](cmdqueryname=c-bsr+admin-scope)
      ```
2. Configure a BSR administrative domain boundary on each edge interface.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   3. Switch the interface working mode from Layer 2 to Layer 3.
      
      
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
      
      Determine whether to perform this step based on the current interface working mode.
   4. Configure a BSR administrative domain boundary.
      
      
      ```
      [multicast boundary](cmdqueryname=multicast+boundary) group-address { mask | mask-length }
      ```
      
      
      
      After the range of multicast group addresses is set, multicast packets that belong to this domain cannot be forwarded by this interface.
3. Configure a multicast group address range on each C-BSR in each BSR administrative domain.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the PIM view.
      
      
      ```
      [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
      ```
   1. Configure a multicast group address range on each C-BSR.
      
      
      ```
      [c-bsr group](cmdqueryname=c-bsr+group) group-address { mask | mask-length } [ hash-length hash-length | priority priority ] 
      ```
4. Configure a C-BSR for the global domain.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the PIM view.
      
      
      ```
      [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
      ```
   1. Configure a C-BSR for the global domain.
      
      
      ```
      [c-bsr global](cmdqueryname=c-bsr+global) [ hash-length hash-length | priority priority ] 
      ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```