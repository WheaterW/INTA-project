Configuring a VPN Instance
==========================

A VPN instance can be configured on a PE to manage VPN routes.

#### Context

In the hub-spoke networking, the PE connected to a central site (Hub site) is called a Hub-PE and the PE connected to a non-central site (Spoke site) is called a Spoke-PE.

You need to configure a VPN instance on each Spoke-PE and two VPN instances (VPN-in and VPN-out) on each Hub-PE.

* VPN-in is used to receive and maintain the VPNv6 routes advertised by all the Spoke-PEs.
* VPN-out is used to maintain the routes of the Hub site and all the Spoke sites and advertise the routes to all Spoke-PEs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Steps 1 to 8 are performed to configure one VPN instance. Configurations of different VPN instances are similar. Note that the different VPN instances on the same device must have different names, RDs, and description.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is created and the VPN instance view is displayed.
   
   The name of a VPN instance is case sensitive. For example, **vpn1** and **VPN1** are considered different VPN instances.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   The description of the VPN instance is configured.
   
   The description is used to record the purpose of creating the VPN instance and the CEs connected to the VPN instance.
4. Run [**ipv6-family**](cmdqueryname=ipv6-family)
   
   
   
   The IPv6 address family is enabled for the VPN instance and the VPN instance IPv6 address family view is displayed.
5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is set for the VPN instance IPv6 address family.
   
   A VPN instance IPv6 address family takes effect only after being assigned an RD. Before setting the RD, you can configure only the description about the VPN instance. No other parameters can be configured.
6. (Optional) Run [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go)
   
   
   
   The device is configured to assign a unique label to each VPNv6 route sent to its BGP VPNv6 peer and forward the data packets received from its BGP VPNv6 peer through outbound interfaces found in the local ILM table.
   
   
   
   After the [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command is configured, the local device records in the ILM the mapping between the label assigned to each VPNv6 route and the outbound interface of the route. Then, after the local device receives a labeled data packet from its BGP VPNv6 peer, the local device directly searches the ILM for an outbound interface based on label information carried in the packet and forwards the packet through the found outbound interface after removing its label. This implementation significantly accelerates packet forwarding.
   
   The [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command is mutually exclusive with the [**apply-label per-instance**](cmdqueryname=apply-label+per-instance) command. If the two commands are both configured, the later configuration overrides the previous one.
7. (Optional) Run [**apply-label per-instance**](cmdqueryname=apply-label+per-instance)
   
   
   
   MPLS label allocation based on VPN instances IPv6 address family is configured. Then, all the routes of the VPN instance IPv6 address family use one label.
8. (Optional) Run [**prefix limit**](cmdqueryname=prefix+limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }
   
   
   
   The maximum number of prefixes of the VPN instance IPv6 address family is set.
   
   To prevent a PE from importing excessive prefixes, you can set the maximum number of prefixes supported by the VPN instance IPv6 address family.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.