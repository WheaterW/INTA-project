Using XPL to Filter the BGP Routes to Be Advertised
===================================================

A BGP device can use a route-filter to filter the routes to be advertised and modify route attributes to control the network traffic forwarding path.

#### Usage Scenario

BGP is used to transmit routing information between ASs, and route advertisement directly affects traffic forwarding.

In most cases, a BGP routing table has a large number of routes. Transmitting them will intensify the load of a device. To address this problem, configure the device to advertise only desired routes.

In addition, multiple routes to the same destination may exist and travel through different ASs. To direct routes to specific ASs, you also need to filter the routes to be advertised.

You can use XPL route-filters to control the BGP routes to be advertised to all peers or peer groups or to a specified peer or peer group.


#### Pre-configuration Tasks

Before using XPL to filter the BGP routes to be advertised, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

* Configure BGP to filter the routes to be advertised globally.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  BGP advertisement policies take effect in the following sequence:
  
  1. Globally advertised routes:
     + Basic ACL-based advertisement policy configured using the [**filter-policy**](cmdqueryname=filter-policy+acl-name+export+direct+isis+ospf+rip+static) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command
     + IP prefix list-based advertisement policy configured using the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+export+direct+isis+ospf+rip+static) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command
     + XPL-based advertisement policy configured using the [**route-filter**](cmdqueryname=route-filter+export+direct+isis+ospf+rip+static) *route-filter-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] command
  2. IP address list-based policy for advertising routes to a specific peer or peer group, configured using the [**peer**](cmdqueryname=peer+advertise+dependent-filter+condition-filter) { *ipv4-address* | *group-name* } **advertise dependent-filter** *dependent-filter-list* *outDependType* [ **condition-filter** *condition-filter-list* | **condition-ip-filter** *ip-prefix-name* ] command
  3. XPL-based policy for advertising routes to a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+route-filter+export) { *group-name* | *ipv4-address* } **route-filter** *route-filter-name* **export** command
  
  
  
  Perform the following steps on the BGP device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**route-filter**](cmdqueryname=route-filter+export+direct+isis+ospf+rip+static) *route-filter-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ]
     
     
     
     The device is configured to filter the routes to be advertised.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP to filter the routes to be advertised to a specified peer or peer group.
  
  
  
  Perform the following steps on the BGP device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-filter+export) { *group-name* | *ipv4-address* } **route-filter** *route-filter-name* **export**
     
     
     
     The device is configured to filter the routes to be advertised to the specified peer or peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring BGP to control route advertisement, check the configuration.

* Run the [**display xpl**](cmdqueryname=display+xpl+route-filter+state+attached+unattached) **route-filter** **state** [ **attached** | **unattached** ] command to check information about the configured route-filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+peer+advertised-routes+statistics) [ **peer** *ipv4-address* **advertised-routes** [ **statistics** ] ] command to check the routes in the BGP routing table.