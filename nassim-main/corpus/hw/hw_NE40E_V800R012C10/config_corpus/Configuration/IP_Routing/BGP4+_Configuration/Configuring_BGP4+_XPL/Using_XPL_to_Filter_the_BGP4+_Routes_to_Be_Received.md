Using XPL to Filter the BGP4+ Routes to Be Received
===================================================

BGP4+ uses XPL route-filters to filter the routes to be received from BGP4+ peers.

#### Context

A BGP4+ device can use a route-filter to filter the routes to be received from all its peers or peer groups or only from a specified peer or peer group.


#### Procedure

* Configure a BGP4+ device to filter the routes to be received from all its peers or peer groups.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  BGP4+ acceptance policies take effect in the following sequence:
  
  1. Globally received routes:
     + To configure a basic ACL6-based acceptance policy, run the [**filter-policy**](cmdqueryname=filter-policy+acl6-name+import) { *acl6-number* | **acl6-name** *acl6-name* } **import** command.
     + To configure an IP prefix list-based acceptance policy, run the [**filter-policy**](cmdqueryname=filter-policy+ipv6-prefix+import) **ipv6-prefix** *ipv6-prefix-name* **import** command.
     + To configure an XPL-based acceptance policy, run the [**route-filter**](cmdqueryname=route-filter+import) *route-filter-name* **import** command.
  2. To configure an XPL-based policy for accepting routes from a specified peer or peer group, run the [**peer**](cmdqueryname=peer+route-filter+import) *ipv6-address* **route-filter** *route-filter-name* **import** command.
  
  
  
  Perform the following steps on the BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**route-filter**](cmdqueryname=route-filter) *route-filter-name* **import**
     
     
     
     The device is configured to filter received routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a BGP4+ device to filter the routes to be received from a specified peer or peer group.
  
  
  
  Perform the following steps on the BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-filter+import) *ipv6-address* **route-filter** *route-filter-name* **import**
     
     
     
     The device is configured to filter the routes to be received from the specified peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.