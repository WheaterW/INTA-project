Configuring MBGP Load Balancing
===============================

MBGP load balancing improves network resource usage.

#### Usage Scenario

Traffic can be balanced among MBGP routes only when the first nine attributes described in "BGP Route Selection Rules" and the AS\_Path of the routes are the same.


#### Pre-configuration Tasks

Before configuring MBGP load balancing, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).


#### Procedure

* Configure MBGP peer or peer group-based load balancing.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **load-balancing** [ **as-path-ignore** | **as-path-relax** ]
     
     Peer or peer group-based MBGP route load balancing is configured.
     
     After the **peer load-balancing** command is run, BGP peer-based load balancing is implemented only
     when the following conditions are met:
     + The routes are received from the specified peer or peer group.
     + The optimal route and optimal equal-cost routes exist.
     + The AS\_Path attribute is the same as that of the optimal route,
       or **as-path-ignore** or **as-path-relax** is specified in the **peer load-balancing** command.
       - If **as-path-ignore** is specified, the
         device ignores comparing AS\_Path attributes when selecting routes
         for load balancing. In this case, routes can participate in load balancing
         even if their AS\_Path attributes are different.
       - If **as-path-relax** is specified, the
         device ignores comparing the AS\_Path attributes of the same length
         when selecting routes for load balancing. In this case, routes cannot
         participate in load balancing if their AS\_Path attributes are of different
         lengths. For example, the AS\_Path attribute of route A is **10**, and the AS\_Path attribute of route B is **10, 20**. Because
         the two AS\_Path attributes are of different lengths, the two routes
         cannot participate in load balancing.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure global MBGP load balancing.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) [ **ebgp** | **ibgp** ] *number*
     
     The maximum number of MBGP routes for load balancing is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Checking the Configurations

After the configuration is complete, verify the configuration.

* Run the [**display bgp multicast routing-table**](cmdqueryname=display+bgp+multicast+routing-table) command to check the information about the MBGP routing table.