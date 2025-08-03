Configuring MBGP to Import Unicast Routes from a VPN Instance
=============================================================

Configuring_MBGP_to_Import_Unicast_Routes_from_a_VPN_Instance

#### Context

By default, a device does not import BGP routes from a VPN instance into an MVPN BGP routing table. To import unicast routes from a VPN instance into an MVPN routing table, perform the following steps. The following configurations do not take effect for locally leaked non-labeled routes or the routes imported in import or network mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run **[**vpn-instance**](cmdqueryname=vpn-instance)** **vpn-instance-name**
   
   
   
   A BGP-VPN instance is created, and the BGP-VPN instance view is displayed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
5. Run **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name**
   
   
   
   The BGP-Multicast VPN instance IPv4 address family view is displayed.
6. Run [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   The device is enabled to import BGP routes from a VPN instance into the MVPN BGP routing table.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display bgp multicast routing-table**](cmdqueryname=display+bgp+multicast+routing-table) command to check the MBGP routing table.