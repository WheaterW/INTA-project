Configuring BGP MVPN Peer Relationships
=======================================

BGP MVPN peer relationships between PEs in the same MVPN allow the PEs to exchange MVPN A-D routes and C-multicast routes.

#### Prerequisites

Before configuring BGP MVPN peers, configure L3VPNv6/EVPN L3VPNv6 over SRv6. For details, see the configuration examples in this document.


#### Context

In the typical MVPNv6 over BIERv6 networking shown in [Figure 1](#EN-US_TASK_0271431868__fig12181260228), one sender PE and multiple receiver PEs are deployed. Because multicast traffic is transmitted between the multicast source and receivers, BGP MVPN peer relationships must be established between the sender PE and all receiver PEs.

**Figure 1** MVPNv6 over BIERv6 networking  
![](figure/en-us_image_0283039348.png "Click to enlarge")
#### Procedure

1. Configure the sender PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family mvpn**](cmdqueryname=ipv6-family+mvpn)
      
      
      
      The BGP-IPv6 MVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The sender PE is enabled to establish a BGP MVPN peer relationship with a specified receiver PE. You need to run this command for each receiver PE with which the sender PE needs to establish a BGP MVPN peer relationship.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of each receiver PE.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-IPv6 MVPN address family view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a receiver PE.
   
   
   
   Perform the following operations on all receiver PEs.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family mvpn**](cmdqueryname=ipv6-family+mvpn)
      
      
      
      The BGP-IPv6 MVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The receiver PE is enabled to establish a BGP MVPN peer relationship with the sender PE.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of the sender PE.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-IPv6 MVPN address family view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.