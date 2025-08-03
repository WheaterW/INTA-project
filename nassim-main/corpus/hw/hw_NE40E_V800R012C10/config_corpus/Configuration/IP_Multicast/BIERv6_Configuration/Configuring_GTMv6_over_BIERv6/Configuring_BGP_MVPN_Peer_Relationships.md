Configuring BGP MVPN Peer Relationships
=======================================

BGP MVPN peer relationships between PEs on the network-side public network allow the PEs to exchange MVPN A-D routes and C-multicast routes.

#### Context

In the typical GTMv6 over BIERv6 networking shown in [Figure 1](#EN-US_TASK_0000001188702493__fig12181260228), one sender PE and multiple receiver PEs are deployed. Because multicast traffic is transmitted between the multicast source and receivers, BGP MVPN peer relationships must be established between the sender PE and all receiver PEs.

**Figure 1** GTMv6 over BIERv6 networking  
![](figure/en-us_image_0000001142822536.png "Click to enlarge")
#### Procedure

1. Configure the sender PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family unicast**](cmdqueryname=ipv6-family+unicast)
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) { **ipv4-address** | **ipv6-address** } [**enable**](cmdqueryname=enable)
      
      
      
      The device is enabled to exchange routes with the specified IPv4/IPv6 peer.
      
      
      
      You can configure the sender PE to exchange routes with a specified IPv4 or IPv6 peer or with both IPv4 and IPv6 peers. If the sender PE is configured to exchange routes with both IPv4 and IPv6 peers, you can configure a PrefVal on the corresponding receiver PE for the routes received from each type of peer (IPv4 or IPv6) so that the receiver PE selects routes accordingly.
   5. Run [**peer**](cmdqueryname=peer) { **i***pv4-address* | **peerIpv6Addr** } [**advertise-ext-community**](cmdqueryname=advertise-ext-community)
      
      
      
      BGP is configured to advertise routes with extended community attributes to the specified peer.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   7. Run [**ipv6-family mvpn**](cmdqueryname=ipv6-family+mvpn)
      
      
      
      The IPv6 BGP-MVPN address family view is displayed.
   8. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The device is enabled to establish a BGP MVPN peer relationship with a specified receiver PE. You need to run this command repeatedly as needed to establish a BGP MVPN peer relationship between the device and each receiver PE.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of each receiver PE.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IPv6 BGP-MVPN address family view.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-IPv6 unicast address family view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure a receiver PE.
   
   
   
   Perform the following operations on all receiver PEs.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family unicast**](cmdqueryname=ipv6-family+unicast)
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) { **ipv4-address** | **ipv6-address** } [**enable**](cmdqueryname=enable)
      
      
      
      The device is enabled to exchange routes with the specified IPv4/IPv6 peer.
      
      
      
      You can configure the sender PE to exchange routes with a specified IPv4 or IPv6 peer or with both IPv4 and IPv6 peers. If the sender PE is configured to exchange routes with both IPv4 and IPv6 peers, you can configure a PrefVal on the corresponding receiver PE for the routes received from each type of peer (IPv4 or IPv6) so that the receiver PE selects routes accordingly.
   5. Run [**peer**](cmdqueryname=peer) { **i***pv4-address* | **peerIpv6Addr** } [**advertise-ext-community**](cmdqueryname=advertise-ext-community)
      
      
      
      BGP is configured to advertise routes with extended community attributes to the specified peer.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   7. Run [**ipv6-family mvpn**](cmdqueryname=ipv6-family+mvpn)
      
      
      
      The IPv6 BGP-MVPN address family view is displayed.
   8. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The device is enabled to establish a BGP MVPN peer relationship with the sender PE.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of the sender PE.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IPv6 BGP-MVPN address family view.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-IPv6 unicast address family view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.