(Optional) Configuring a Switch-MDT
===================================

A switch-multicast distribution tree (MDT) is set up for multicast traffic flowing from a private network to the public network. Multicast packets can be switched from the share-MDT to the switch-MDT. This reduces the pressure on PEs and bandwidth consumption and allows multicast data to be transmitted on demand.

#### Context

In a multicast domain (MD) VPN, a share-MDT is set up between PEs. All PEs that belong to the same MD receive multicast packets, irrespective of whether they have receivers connected to them. This wastes bandwidth resources and imposes an extra burden on PEs. A switch-MDT optimizes MDT and allows on-demand multicast transmission. Traffic will be switched from the share-MDT to the switch-MDT if multicast traffic on PEs reaches the maximum. Only the PEs that have receivers connected to them will receive multicast data from the switch-MDT. This reduces the pressure on PEs and bandwidth consumption.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If you do not configure a switch-MDT, VPN multicast data will always be transmitted along the share-MDT.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
4. Run [**multicast-domain switch-group-pool**](cmdqueryname=multicast-domain+switch-group-pool) *switch-group-pool* { *network-mask* | *network-mask-length* } [ **threshold** *threshold-value* | **acl** { *advanced-acl-number* | *acl-name* } ] \*
   
   
   
   The switching group pool of a switch-MDT and conditions for the switch-MDT switching are configured.
   
   
   
   * *switch-group-pool* indicates a start address of the Switch-Group-pool. The same *switch-group-pool* value must be configured for the same VPN instance IPv4 address family on different PEs. The value range of the Switch-Group address for a VPN instance IPv4 address family cannot overlap with that for another VPN instance IPv4 address family on the same PE.
   * *threshold-value* indicates the switching threshold.
   * { *advanced-acl-number* | *acl-name* } indicates an advanced ACL.
5. (Optional) Run [**multicast-domain switch-delay**](cmdqueryname=multicast-domain+switch-delay) *switch-delay*
   
   
   
   A delay for switching to the switch-MDT is configured.
6. (Optional) Run [**multicast-domain holddown-time**](cmdqueryname=multicast-domain+holddown-time) *interval*
   
   
   
   The delay for switching back VPN multicast traffic from the switch-MDT to the share-MDT is set.
7. (Optional) Run [**multicast-domain switch-without-register**](cmdqueryname=multicast-domain+switch-without-register)
   
   
   
   The source PE is disabled from sending Register packets to the Rendezvous Point (RP) to establish the shortest path tree (SPT) on the public network before the Switch-Group address is used to encapsulate VPN data.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.