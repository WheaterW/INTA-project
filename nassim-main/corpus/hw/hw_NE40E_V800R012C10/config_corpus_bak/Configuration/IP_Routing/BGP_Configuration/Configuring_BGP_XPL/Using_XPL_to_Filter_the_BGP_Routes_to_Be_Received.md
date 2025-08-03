Using XPL to Filter the BGP Routes to Be Received
=================================================

A BGP device can use a route-filter to filter the routes to be received and modify route attributes to control the network traffic forwarding path.

#### Usage Scenario

BGP is used to transmit routing information between ASs, and route advertisement directly affects traffic forwarding.

A BGP device may receive multiple routes to the same destination network from different peers. To control the network traffic forwarding path, filter the routes to be received.

In addition, a BGP device may receive a large number of routes during an attack, which may consume lots of device resources. Regardless of whether malicious attacks or incorrect configurations result in the reception of numerous BGP routes, the administrator must limit the device resources to be consumed based on the network planning and device capacity.

You can use XPL route-filters to control the BGP routes to be received from all peers or peer groups or from a specified peer or peer group.


#### Pre-configuration Tasks

Before using XPL to filter the BGP routes to be received, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

* Configure BGP to filter the routes to be received globally.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  BGP acceptance policies take effect in the following sequence:
  
  1. Globally received routes:
     + Basic ACL-based acceptance policy configured using the [**filter-policy**](cmdqueryname=filter-policy+acl-name+import) { *acl-number* | **acl-name** *acl-name* } **import** command
     + IP prefix list-based acceptance policy configured using the [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+import) **ip-prefix** *ip-prefix-name* **import** command
     + XPL-based acceptance policy configured using the [**route-filter**](cmdqueryname=route-filter+import) *route-filter-name* **import** command
  2. XPL-based policy for accepting routes from a specified peer or peer group, configured using the [**peer**](cmdqueryname=peer+route-filter+import) { *group-name* | *ipv4-address* } **route-filter** *route-filter-name* **import** command
  
  
  
  Perform the following steps on the BGP device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**route-filter**](cmdqueryname=route-filter+import) *route-filter-name* **import**
     
     
     
     The device is configured to filter the routes to be received.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP to filter the routes to be received from a specified peer or peer group.
  
  
  
  Perform the following steps on the BGP device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-filter+import) { *group-name* | *ipv4-address* } **route-filter** *route-filter-name* **import**
     
     
     
     The device is configured to filter the routes to be received from the specified peer or peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring BGP to control route acceptance, check the configuration.

* Run the [**display xpl**](cmdqueryname=display+xpl+route-filter+state+attached+unattached) **route-filter** **state** [ **attached** | **unattached** ] command to check information about the configured route-filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+peer+received-routes+statistics) [ **peer** *ipv4-address* **received-routes** [ **statistics** ] ] command to check the routes in the BGP routing table.