Using XPL to Filter the BGP4+ Routes to Be Advertised
=====================================================

This section describes how to use XPL to filter the BGP4+ routes to be advertised to BGP4+ peers.

#### Context

A BGP4+ device can use a route-filter to filter the routes to be advertised to all peers or peer groups or only to a specified peer or peer group.


#### Procedure

* Configure a BGP4+ device to filter the routes to be advertised to all peers or peer groups.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  BGP4+ advertisement policies take effect in the following sequence:
  
  1. Globally advertised routes:
     + To configure a basic ACL6-based advertisement policy, run the [**filter-policy**](cmdqueryname=filter-policy+acl6-name) { *acl6-number* | **acl6-name** *acl6-name* } [**export**](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ] command.
     + To configure an IP prefix list-based advertisement policy, run the [**filter-policy**](cmdqueryname=filter-policy+ipv6-prefix) **ipv6-prefix** *ipv6-prefix-name* [**export**](cmdqueryname=export+direct+isis+ospfv3+ripng+static) [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ] command.
     + To configure an XPL-based advertisement policy, run the [**route-filter**](cmdqueryname=route-filter+export+direct+isis+ospfv3+ripng+static) *route-filter-name* **export** [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ] command.
  2. To configure an IP address list-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command.
  3. To configure an XPL-based policy for advertising routes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer+route-filter+export) *ipv6-address* **route-filter** *route-filter-name* **export** command.
  
  
  
  Perform the following steps on the BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**route-filter**](cmdqueryname=route-filter+export+direct+isis+ospfv3+ripng+static) *route-filter-name* **export** [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** | **unr** ]
     
     
     
     The device is configured to filter the routes to be advertised.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP4+ to filter the routes to be advertised to a specified peer or peer group.
  
  
  
  Perform the following steps on the BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-filter+export) *ipv6-address* **route-filter** *route-filter-name* **export**
     
     
     
     The device is configured to filter the routes to be advertised to the specified peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.