Configuring Split Horizon in a Bridge Domain
============================================

A bridge domain is a broadcast domain, in which bridge domain members broadcast received unknown unicast, multicast, or broadcast packets within the domain. To reduce the broadcast traffic volume, enable split horizon in the bridge domain, which isolates bridge domain member interfaces from one another if they do not need to communicate.

#### Context

Split horizon can be configured in either bridge domain or EVC Layer 2 sub-interface view:

* If split horizon is configured in the bridge domain view, this function takes effect on all bridge domain member interfaces. All bridge domain member interfaces are isolated from one another.
* If split horizon is configured in the EVC Layer 2 sub-interface view, this function takes effect only on the specified interface. The split horizon-enabled EVC Layer 2 sub-interface is isolated with other EVC Layer 2 sub-interfaces.
  
  Split horizon must be configured on each EVC Layer 2 sub-interface that needs to be isolated.


#### Procedure

* Configure split horizon in the bridge domain view.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The bridge domain view is displayed.
  3. Run [**split-horizon enable**](cmdqueryname=split-horizon+enable)
     
     Split horizon is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure split horizon in the EVC Layer 2 sub-interface view.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
     
     An EVC Layer 2 sub-interface is created, and the sub-interface view is displayed.
  3. Run [**split-horizon**](cmdqueryname=split-horizon)
     
     Split horizon is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.