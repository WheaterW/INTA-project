Configuring Route Exchange Between a PE and a CE
================================================

The routing protocol running between a PE and a CE can
be BGP or an IGP. A static route (including the default route) can
also run between them. You can choose any of them as required.

#### Context

The routing protocol running between a Spoke-PE and a
Spoke-CE is related to the routing protocol running between a Hub-PE
and a Hub-CE. EBGP, an IGP, or a static route (including the default
route) can run between a Hub-PE and a Hub-CE. You can choose any of
them as required.


#### Procedure

* Configure EBGP between a Hub-PE and a Hub-CE.
  
  
  
  For configuration details, see [Configuring Route Exchange
  Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
  
  In this mode, EBGP, an IGP, or a
  static route (including the default route) can run between a Spoke-PE
  and a Spoke-CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If EBGP runs both between
  the Spoke-PE and Spoke-CE and between the Hub-PE and Hub-CE, you must
  run the [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ] command
  in the BGP-VPN instance IPv4 address family view of the Hub-PE
  to allow routing loops. If *number* is set to 1,
  the route with the AS numbers in the AS-path list repeated once is
  allowed.
* Configure IGP between a Hub-PE and a Hub-CE.
  
  
  
  For configuration details, see [Configuring Route Exchange
  Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
  
  In this mode, only an IGP or a static
  route (including the default route) can run between a Spoke-PE and
  a Spoke-CE. For details, see "BGP/MPLS IP VPN" in the *HUAWEI NE40E-M2 seriesUniversal Service RouterFeature Description* - *VPN*.
* Configure a static route (including the default route)
  between a Hub-PE and a Hub-CE.
  
  
  
  For configuration details, see [Configuring Route Exchange
  Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
  
  In this mode, EBGP, an IGP, or a
  static route (including the default route) can run between a Spoke-PE
  and a Spoke-CE.
  
  In a scenario where a Hub-CE accesses a Hub-PE
  through dual links, if the Hub-CE uses the default route to access
  the Hub-PE, to enable the Hub-PE to advertise the default route to
  all the Spoke-PEs, run the following commands on the Hub-PE:
  1. Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** **0.0.0.0** *nexthop-address* [ **tag** *tag* ] [ **description** *text* ] command in the
     system view.
     
     In this example, *vpn-instance-name* specifies VPN-out and *nexthop-address* specifies
     the IP address of the Hub-CE interface that connects to the PE interface
     bound to VPN-out.
  2. Run the [**network**](cmdqueryname=network) **0.0.0.0** **0** command in the BGP-VPN instance IPv4 address
     family view to advertise the default route to all the Spoke-PEs
     through MP-BGP.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  In a scenario where a Hub-CE accesses a Hub-PE through
  a single link, if the Hub-CE uses the default route to access the
  Hub-PE, run the [**peer**](cmdqueryname=peer) *ipv4-address* **default-route-advertise** [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ **conditional-route-match-all** { *ipv4-address1* { *mask1* | *mask-length1* } } &<1-4> | **conditional-route-match-any** { *ipv4-address2* { *mask2* | *mask-length2* } } &<1-4> ] command in the BGP view
  on the Hub-CE to enable the Hub-CE to advertise default routes to
  the Hub-PE.