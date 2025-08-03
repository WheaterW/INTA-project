(Optional) Setting a Router ID for a BGP VPN Instance
=====================================================

To distinguish a BGP VPN instance from the other BGP VPN instances on the same device, specify a unique router ID for the BGP VPN instance.

#### Context

By default, all BGP-VPN instances on a device use the BGP router ID as their router ID. In this case, different BGP-VPN instances on the same device have the same router ID. Using the same router ID for all BGP VPN instances sometimes creates inconveniences. For example, it is impossible to establish a BGP peer relationship between two BGP VPN instances that use the same router ID on a PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
   
   
   
   A BGP VPN instance is created, and the BGP VPN instance view is displayed.
4. Run [**router-id**](cmdqueryname=router-id) { *ipv4-address* | **auto-select** }
   
   
   
   A router ID is manually set or automatically selected for the BGP VPN instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.