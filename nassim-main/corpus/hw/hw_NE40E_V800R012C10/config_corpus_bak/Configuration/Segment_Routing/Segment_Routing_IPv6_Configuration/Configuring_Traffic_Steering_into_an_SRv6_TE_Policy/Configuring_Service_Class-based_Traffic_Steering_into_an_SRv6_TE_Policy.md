Configuring Service Class-based Traffic Steering into an SRv6 TE Policy
=======================================================================

You can configure service class-based traffic steering to recurse a route to an SRv6 TE Policy based on service class values, so that traffic can be forwarded through a path in the SRv6 TE Policy.

#### Prerequisites

Before configuring service class-based traffic steering into an SRv6 TE Policy, complete the following task:

* Configure an SRv6 TE Policy.

#### Context

After an SRv6 TE Policy is configured, traffic needs to be steered into it for forwarding. This process is called traffic steering. Currently, SRv6 TE Policies can be used for various services, such as BGP L3VPN and EVPN services. This section describes how to configure services to recurse to an SRv6 TE Policy through a specified tunnel policy.

During service class-based traffic steering, nodes use SRv6 mapping policies to dynamically create SRv6 TE flow groups.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   The SRv6 view is displayed.
3. Run [**mapping-policy**](cmdqueryname=mapping-policy)*name-value* **color***color-value*
   
   
   
   An SRv6 mapping policy is created, and the SRv6 mapping policy view is displayed.
4. (Optional) Run [**description**](cmdqueryname=description) *description-value*
   
   
   
   A description is configured for the SRv6 mapping policy.
5. Run [**match-type service-class**](cmdqueryname=match-type+service-class)
   
   
   
   The mapping type of the SRv6 mapping policy is set to service class.
6. Run **index** *index-value* **service-class** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } \* **match** { **srv6-te-policy** **color** *color-value* | **native-ip** } or **default** **match** { **srv6-te-policy** **color** *color-value* | **native-ip** }
   
   
   
   A rule is configured for the mapping between the color values of SRv6 TE Policies in an SRv6 TE flow group and the service class values of packets or for the mapping between native IP links in an SRv6 TE flow group and the service class values of packets.
   
   
   
   In an SRv6 mapping policy, you can specify a rule for the mapping between the color values of SRv6 TE Policies and the service class values of packets or for the mapping between native IP links and the service class values of packets. Each service class value can be associated with only one SRv6 TE Policy or native IP link. Furthermore, such a mapping rule can be configured for an SRv6 TE Policy only if this policy is up.
   
   When packets with service class values enter an SRv6 TE flow group, they are matched against the following rules in sequence to achieve forwarding:
   
   1. The packets are first strictly matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the corresponding service class value.
   
   2. If the matching fails, the packets are matched against the SRv6 TE Policy-specific or native IP link-specific rule configured with the **default** priority.
   
   3. If the rule configured with the **default** priority does not exist or it fails to go up, the packets are matched against the SRv6 mapping policy rule that is configured with the smallest index and remains up. As such, it is recommended that low-priority service classes (BE < AF1 < AF2 < AF3 < AF4 < EF < CS6 < CS7) be specified in the SRv6 mapping policy rule with a small index. This ensures that unmatched traffic preferentially preempts the low-priority bandwidth instead of the high-priority bandwidth.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the SRv6 view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
   
   
   
   A tunnel policy is created, and its view is displayed.
10. (Optional) Run [**description**](cmdqueryname=description) *description-text*
    
    
    
    A description is configured for the tunnel policy.
11. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6** **srv6-te-flow-group** **load-balance-number** *loadBalanceNumber*
    
    
    
    A tunnel selection policy is configured.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Because there can be only one effective SRv6 TE Policy with the endpoint and color specified, load balancing is not involved.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.