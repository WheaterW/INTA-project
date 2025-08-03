Establishing Route Reflection for BGP VPNv6 Routes
==================================================

This section describes how to configure route reflection for BGP VPNv6 routes so that the RR can reflect the VPNv6 routes received from a client PE to other client PEs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
4. Run either of the following commands:
   
   
   * To enable route reflection if the RR has established an MP-IBGP connection to a peer group consisting of all the client PEs, run the [**peer**](cmdqueryname=peer) *group-name* **reflect-client** command.
   * To enable route reflection if the RR has established an MP-IBGP connection to each client PE rather than a peer group, run the [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client** command.
5. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function to filter received VPNv6 routes based on VPN targets is disabled.
6. (Optional) Run [**rr-filter**](cmdqueryname=rr-filter) *extcomm-filter-name*
   
   
   
   A reflection policy is configured for the RR.
   
   
   
   To allow an RR to filter routes to be reflected, run the [**rr-filter**](cmdqueryname=rr-filter) command. Only IBGP routes of which the RT extended community attribute matches the reflection policy can be reflected.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.