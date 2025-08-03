(Optional) Configuring One-Label-per-Next-Hop Label Distribution on an ASBR
===========================================================================

To conserve label resources on an ASBR, configure one-label-per-next-hop label allocation on the ASBR. One-label-per-next-hop label allocation on ASBRs and one-label-per-instance label distribution on PEs must be used together.

#### Context

In an inter-AS VPN Option B scenario, after one-label-per-next-hop label distribution is configured on an ASBR, the ASBR assigns only one label to VPNv6 routes that share the same next hop and outgoing label. Compared with on-label-per-route label distribution, one-label-per-next-hop label distribution significantly saves label resources on the ASBR.

Perform the following steps on an ASBR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPNv6 address family view is displayed.
4. Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   One-label-per-next-hop label distribution for VPNv6 routes is enabled on the ASBR.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After one-label-per-next-hop label distribution is enabled or disabled on an ASBR, the labels assigned by the ASBR to routes change. As a result, packet loss occurs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.