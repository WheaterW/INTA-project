Configuring BGP A-D Multicast VPN
=================================

The configuration of BGP A-D multicast VPN enables the Auto Discovery (AD) of PEs on the same VPN and allows multicast VPN services to run in public network tunnels based on PIM-SSM distribution trees.

#### Usage Scenario

Before the BGP A-D MVPN is introduced, MD MVPNs can establish only PIM-SM MDTs. This is because PEs belonging to the same VPN cannot detect each other's peer information. As a result, PEs belonging to the same VPN cannot detect the multicast source, and therefore are unable to send PIM-SSM Join messages to the multicast source to establish a PIM-SSM MDT.

After the BGP A-D MVPN is introduced, MD MVPNs can also establish PIM-SSM MDTs. On a BGP A-D MVPN, PEs obtain and record peer information about a VPN by exchanging BGP Update packets that carry A-D route information. Then, these PEs send PIM-SSM Join messages directly to the multicast source to establish a PIM-SSM MDT. After the PIM-SSM MDT is established, the BGP A-D MVPN transmits multicast services over a public network tunnel based on the PIM-SSM MDT.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If multicast VPN is implemented in BGP A-D mode, the configured A-D mode must be consistent with the A-D address family type configured in the BGP view.



#### Pre-configuration Tasks

Before configuring BGP A-D Multicast VPN, [configure an MD VPN](dc_vrp_multicast_cfg_2121.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mdt**
   
   
   
   The BGP-MDT address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **enable**
   
   
   
   Route exchange with a specific peer or peer group is enabled in the BGP-MDT address family view.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP-MDT address family view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
7. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
8. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family is enabled and its view is displayed.
9. Run [**auto-discovery**](cmdqueryname=auto-discovery) **mdt** [ **import route-policy** *route-policy-name* ]
   
   
   
   The MDT-SAFI A-D mode is configured for the VPN instance IPv4 address family.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After the BGP A-D multicast VPN is configured, run the following commands to check the configurations:

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check the PIM routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] | *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } ] \* [ **outgoing-interface-number** [ *number* ] ] command to check the multicast routing table.
* Run the [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **share-group** [ **local** | **remote** ] command to check the Share-Group information of a specified VPN instance in a multicast domain.