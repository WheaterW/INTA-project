Configuring Route Exchange Between a PE and a CE
================================================

The routing protocol running between a PE and a CE can be BGP or IGP. A static route (including the default route) can also run between them. You can choose any of them as required.

#### Context

The routing protocol run between a Spoke-PE and a Spoke-CE is related to the routing protocol run between a Hub-PE and a Hub-CE. EBGP, IGP, and the static route (including the default route) can run between a Hub-PE and a Hub-CE. You can choose any of them as required.


#### Procedure

* Configure EBGP between a Hub-PE and a Hub-CE.
  
  
  
  For detailed configuration procedures, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
  
  In this mode, EBGP, IGP, or static route (including the default route) can be run between a Spoke-PE and a Spoke-CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If EBGP is run both between the Spoke-PE and the Spoke-CE and between the Hub-PE and the Hub-CE, you need to run the [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ] command in the BGP-VPN instance IPv6 address family view of the Hub-PE to allow route loops. If *number* is set to 1, it indicates that the route with the AS numbers in the AS\_Path list repeated once is allowed.
* Configure IGP between a Hub-PE and a Hub-CE.
  
  
  
  For detailed configuration procedures, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
  
  In this mode, only IGP or static route (including the default route) can be run between a Spoke-PE and a Spoke-CE. BGP cannot be used. For details, see the chapter "BGP/MPLS IP VPN" in *HUAWEI NE40E-M2 seriesUniversal Service Router Feature Description* - *VPN*.
* Configure a static route (including the default route) between a Hub-PE and a Hub-CE.
  
  
  
  For detailed configuration procedures, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
  
  In this mode, EBGP, IGP, or static route (including the default route) can be run between a Spoke-PE and a Spoke-CE.
  
  If a Hub-CE adopts the default route to access the Hub-PE, to enable the Hub-PE to advertise the default route to all the Spoke-PEs, you need to run the following commands on the Hub-PE:
  
  + Run the [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* **::** **0** *nexthop-address* [ **tag** *tag* ] [ **description** *text* ] command in the system view.
    
    In this example, *vpn-instance-name* specifies VPN-out and *nexthop-address* specifies the IPv6 address of the Hub-CE interface that connects to the PE interface bound to VPN-out.
  + Run the [**network**](cmdqueryname=network) **::** **0** command in the BGP-VPN instance IPv6 address family view to advertise the default route to all the Spoke-PEs through MP-BGP.