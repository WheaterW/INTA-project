Configuring DSCP-based Traffic Steering into an SRv6 TE Policy
==============================================================

You can configure DSCP-based traffic steering to recurse a route to an SRv6 TE Policy based on DSCP values, so that traffic can be forwarded through a path in the SRv6 TE Policy.

#### Prerequisites

Before configuring DSCP-based traffic steering into an SRv6 TE Policy, complete the following task:

* Configure an SRv6 TE Policy.

#### Context

After an SRv6 TE Policy is configured, traffic needs to be steered into it for forwarding. This process is called traffic steering. Currently, SRv6 TE Policies can be used for various services, such as BGP L3VPN and EVPN services. This section describes how to configure services to recurse to an SRv6 TE Policy through a specified tunnel policy.

During DSCP-based traffic steering, nodes use SRv6 mapping policies to dynamically create SRv6 TE flow groups.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

EVPN VPWS and EVPN VPLS packets do not support DSCP-based traffic steering because they do not carry DSCP values.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   The SRv6 view is displayed.
3. Run [**mapping-policy**](cmdqueryname=mapping-policy)*name-value* **color***color-value*
   
   
   
   An SRv6 mapping policy is created, and the SRv6 mapping policy view is displayed.
4. (Optional) Run [**description**](cmdqueryname=description) *description-value*
   
   
   
   A description is configured for the SRv6 mapping policy.
5. Run [**match-type dscp**](cmdqueryname=match-type+dscp)
   
   
   
   The mapping type of the SRv6 mapping policy is set to DSCP, and the SRv6 mapping policy DSCP view is displayed.
6. Run **index** *index-value* **dscp** { **ipv4** | **ipv6** } { { *dscpBegin* [ **to** *dscpEnd* ] } &<1-64> } **match** { **srv6-te-policy** **color** *color-value* | **native-ip** } or { **ipv4** | **ipv6** } **default** **match** { **srv6-te-policy** **color** *color-value* | **native-ip** }
   
   
   
   A rule is configured either for the mapping between the color values of SRv6 TE Policies in an SRv6 TE flow group and the DSCP values of packets or for the mapping between native IP links in an SRv6 TE flow group and the DSCP values of packets.
   
   
   
   In an SRv6 mapping policy, you can configure a separate color-DSCP mapping rule for both the IPv4 address family traffic and IPv6 address family traffic. In the same address family (IPv4 or IPv6), each DSCP value can be mapped to only one color value. Furthermore, such a mapping rule can be configured for an SRv6 TE Policy only if this policy is up.
   
   When IPv4/IPv6 packets with DSCP values enter an SRv6 TE flow group, they are matched against the following rules in sequence to achieve forwarding:
   
   1. The packets are first strictly matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with specified DSCP values in the corresponding address family.
   
   2. If the matching fails, the packets are matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the **default** priority in the local address family.
   
   3. If the matching fails, the packets are matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the smallest DSCP value in the local address family.
   
   4. If the matching fails, the packets are matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the **default** priority in the other address family.
   
   5. If the matching fails, the packets are matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the smallest DSCP value in the other address family.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the SRv6 mapping policy view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the SRv6 view.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
    
    
    
    A tunnel policy is created, and its view is displayed.
11. (Optional) Run [**description**](cmdqueryname=description) *description-text*
    
    
    
    A description is configured for the tunnel policy.
12. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6** **srv6-te-flow-group** **load-balance-number** *loadBalanceNumber*
    
    
    
    A tunnel selection policy is configured.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    After you complete the preceding configurations, the service route is associated with the specified SRv6 TE flow group according to the next hop address of the route.
    
    The DSCP value of a packet is associated with the specified color according to the mapping configured in the SRv6 mapping policy, and then associated with the corresponding SRv6 TE Policy in the SRv6 TE flow group. In this way, traffic is steered into this SRv6 TE Policy.
    
    Because there can be only one effective SRv6 TE Policy with the endpoint and color specified, load balancing is not involved.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.