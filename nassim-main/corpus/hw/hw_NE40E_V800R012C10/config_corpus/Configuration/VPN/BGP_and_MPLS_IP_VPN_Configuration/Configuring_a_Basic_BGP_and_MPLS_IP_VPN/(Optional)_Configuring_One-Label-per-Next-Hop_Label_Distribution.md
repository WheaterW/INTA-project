(Optional) Configuring One-Label-per-Next-Hop Label Distribution
================================================================

To save label resources on a PE, configure one-label-per-next-hop label distribution on the PE. Only one label is allocated to the VPNv4 routes that have the same next-hop address and outgoing label.

#### Context

In the scenario where multiple CEs access a PE, if the PE needs to send large numbers of VPNv4 routes to its peer but the MPLS labels are inadequate, configure one-label-per-next-hop label distribution on the PE. Then the PE allocates only one label to the VPNv4 routes that have the same next-hop address and outgoing label, which greatly saves label resources.

Perform the following steps on a PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family view is displayed.
4. Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   One-label-per-next-hop label distribution for VPNv4 routes is enabled on the PE.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After one-label-per-next-hop label distribution is enabled or disabled, the label allocated by the PE to a route changes, which leads to a transient loss of VPN packets.
5. (Optional) Run [**apply-label per-nexthop pop-go**](cmdqueryname=apply-label+per-nexthop+pop-go)
   
   
   
   The device is configured to assign a unique label to each next hop used by routes sent from its VPN instance IPv4 address family to its BGP VPNv4 peer and forward the data packets received from its BGP VPNv4 peer through outbound interfaces found in the local ILM.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In VPN instance IPv4 address family view, the [**apply-label per-nexthop pop-go**](cmdqueryname=apply-label+per-nexthop+pop-go) and [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop) commands are overwritten. The latest configuration overrides the previous one.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configurations, you can run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** to view details on VPN instances.