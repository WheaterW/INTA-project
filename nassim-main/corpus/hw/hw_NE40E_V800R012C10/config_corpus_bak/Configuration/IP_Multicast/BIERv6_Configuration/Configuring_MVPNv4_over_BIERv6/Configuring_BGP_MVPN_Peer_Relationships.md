Configuring BGP MVPN Peer Relationships
=======================================

BGP MVPN peer relationships between PEs in the same MVPN allow the PEs to exchange MVPN Auto-Discovery (A-D) routes and C-multicast routes.

#### Prerequisites

Before configuring BGP MVPN peers, configure L3VPNv4/EVPN L3VPNv4 over SRv6. For details, see the configuration examples in this document.


#### Context

In the typical MVPNv4 over BIERv6 networking shown in [Figure 1](#EN-US_TASK_0271431864__fig12181260228), one sender PE and multiple receiver PEs are deployed. Because multicast traffic is transmitted between the multicast source and receivers, BGP MVPN peer relationships must be established between the sender PE and all receiver PEs.

**Figure 1** MVPNv4 over BIERv6 networking  
![](figure/en-us_image_0282751846.png "Click to enlarge")
#### Procedure

1. Configure the sender PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family mvpn**](cmdqueryname=ipv4-family+mvpn)
      
      
      
      The BGP-MVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The sender PE is enabled to establish a BGP MVPN peer relationship with a specified receiver PE. You need to run this command for each receiver PE with which the sender PE needs to establish a BGP MVPN peer relationship.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of each receiver PE.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-MVPN address family view.
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
   3. Run [**ipv4-family mvpn**](cmdqueryname=ipv4-family+mvpn)
      
      
      
      The BGP-MVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv6-address* **enable**
      
      
      
      The receiver PE is enabled to establish a BGP MVPN peer relationship with the sender PE.
      
      
      
      It is recommended that the IPv6 address be set to the loopback interface address of the sender PE.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-MVPN address family view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.