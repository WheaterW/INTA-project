(Optional) Configuring Load Balancing
=====================================

Load balancing needs to be deployed to achieve balanced network traffic distribution.

#### Procedure

* Configure PEs.
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
     
     
     + Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
     + Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) [ **ebgp** | **ibgp** ] *number* [ **ecmp-nexthop-changed** ]
     
     
     
     The maximum number of equal-cost routes for load balancing is set.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-VPN instance IPv4 or IPv6 address family view.
  5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  6. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path) { *ipv4-address* | *group-name* } **capability-advertise** **add-path** { **send** | **receive** | **both** }
     
     
     
     The function to send or receive Add-Path routes from a specified peer is enabled.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-EVPN address family view.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP view.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure DC GWs.
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
     
     
     + Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
     + Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) [ **ebgp** | **ibgp** ] *number* [ **ecmp-nexthop-changed** ]
     
     
     
     The maximum number of equal-cost routes for load balancing is set.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-VPN instance IPv4 or IPv6 address family view.
  5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  6. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path) { *ipv4-address* | *group-name* } **capability-advertise** **add-path** { **send** | **receive** | **both** }
     
     
     
     The function to send or receive Add-Path routes from a specified peer is enabled.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-EVPN address family view.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP view.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure L2GWs/L3GWs.
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
     
     
     + Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
     + Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) [ **ebgp** | **ibgp** ] *number* [ **ecmp-nexthop-changed** ]
     
     
     
     The maximum number of equal-cost routes for load balancing is set.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-VPN instance IPv4 or IPv6 address family view.
  5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  6. Run [**bestroute add-path**](cmdqueryname=bestroute+add-path) **path-number** *path-number*
     
     
     
     BGP Add-Path is enabled, and the number of preferred routes that can be selected is configured.
  7. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path) { *ipv4-address* | *group-name* } **capability-advertise** **add-path** { **send** | **receive** | **both** }
     
     
     
     The function to send or receive Add-Path routes from a specified peer is enabled.
  8. Run [**peer**](cmdqueryname=peer+advertise+add-path+path-number) { *ipv4-address* | *group-name* } **advertise add-path path-number** *path-number*
     
     
     
     The number of preferred routes that can be advertised to a specified peer is configured.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-EVPN address family view.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.