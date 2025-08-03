Configuring IPv6 Route Recursion to Remotely Leaked VPN Routes
==============================================================

After IPv6 route recursion to remotely leaked VPN routes is enabled, the labels and Tunnel IDs of the remotely leaked VPN routes can be inherited, which ensures correct traffic forwarding.

#### Usage Scenario

A route needs recursion if its next hop is unreachable. To allow IPv6 routes to recurse to remotely leaked VPN routes, run the [**ipv6 route recursive-lookup inherit-label-route enable**](cmdqueryname=ipv6+route+recursive-lookup+inherit-label-route+enable) command. After the command is run, IPv6 routes inherit the labels and tunnel IDs of the remotely leaked VPN routes, which ensures correct traffic forwarding. This command mainly applies to BGP/MPLS IPv6 VPN scenarios.

In [Figure 1](#EN-US_TASK_0172369687__fig_dc_vrp_cfg_00731901), PE1 and PE2 are IBGP peers, and CE1 and PE1 are IGP neighbors. PE2 learns the IP address of CE1's loopback interface, and an EBGP peer relationship is established between CE1 and PE2 using loopback interface IP addresses. By default, the BGP routes that PE2 learns from CE1 through the EBGP peer connection cannot recurse to remotely leaked VPN routes. As a result, traffic fails to be forwarded. To address this problem, run the [**ipv6 route recursive-lookup inherit-label-route enable**](cmdqueryname=ipv6+route+recursive-lookup+inherit-label-route+enable) command to allow the BGP4+ routes to recurse to remotely leaked VPN routes. After the BGP4+ routes inherit the labels and tunnel IDs of the remotely leaked VPN routes, traffic can be correctly forwarded.

**Figure 1** Basic BGP/MPLS IPv6 VPN networking  
![](images/fig_ip_route_recursive-lookup_inherit-label-route_enable.png)

#### Pre-configuration Tasks

Before configuring IPv6 route recursion to remotely leaked VPN routes, [configure basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2000.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route recursive-lookup inherit-label-route enable**](cmdqueryname=ipv6+route+recursive-lookup+inherit-label-route+enable)
   
   
   
   Recursion of all IPv6 routes to remotely leaked VPN routes is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view to check whether IPv6 route recursion to remotely leaked VPN routes is enabled.