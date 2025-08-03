Enabling Multicast Routing
==========================

Enable multicast routing on a Router before you configure other multicast features on the Router.

#### Context

VPN-instance-related configurations need to be performed only on Provider Edges (PEs). If a PE has a VPN instance interface connected to user hosts, you must perform Steps 3 to 6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled in the public network instance.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo multicast routing-enable**](cmdqueryname=undo+multicast+routing-enable) command will delete all the multicast configurations of the public network or VPN instance and interrupt the multicast service running in the instance. If you want to restore the multicast service in the instance, re-configure multicast commands for which configurations have been deleted.
3. (Optional) Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
4. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
5. (Optional) Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   A Route Distinguisher (RD) is configured for the VPN instance IPv4 address family.
6. (Optional) Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled in the VPN instance.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.