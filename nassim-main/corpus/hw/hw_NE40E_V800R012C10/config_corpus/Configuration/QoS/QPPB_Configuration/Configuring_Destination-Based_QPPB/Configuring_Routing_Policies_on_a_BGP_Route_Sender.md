Configuring Routing Policies on a BGP Route Sender
==================================================

This section describes how to configure a route-policy on a route sender.

#### Context

Perform the following operations on a BGP route sender:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Create a basic ACL and configure a rule for it.
   
   
   1. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** }]
      
      A basic ACL is created, and the basic ACL view is displayed.
   2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ]\*
      
      A rule is configured for the basic ACL.The system processes packets based on the ACL rule as follows:
   * If packets match the ACL rule and the action of the rule is permit, the system permits the packets.
   * If packets match the ACL rule and the action of the rule is deny, the system discards the packets.
   * If packets do not match the ACL rule, the system does not apply the action to the packets. Instead, it forwards them.
   * If the referenced ACL does not exist or an existent ACL in which no rule is defined is referenced, the system does not apply any action to the packets. Instead, it forwards them.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* *matchMode* **node** *node*
   
   
   
   A route-policy with a node is created, and the route-policy view is displayed.
5. Configure a matching rule for the route-policy as required:
   
   
   * To match routes against an ACL, run the [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* } command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Route-policies support only basic ACLs (with the number ranging from 2000 to 2999).
   * To match BGP routes against an AS\_Path filter, run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } &<1-16> command.
   * To match BGP routes against a community filter, run the [**if-match community-filter**](cmdqueryname=if-match+community-filter) { *basic-comm-filter-num* [ **whole-match** ] | *adv-comm-filter-num* }\* &<1-16> or [**if-match community-filter**](cmdqueryname=if-match+community-filter) *comm-filter-name* [ **whole-match** ] command.
   * To match routes against a route cost, run the [**if-match cost**](cmdqueryname=if-match+cost) *cost* command.
   * To match routes against an IP prefix list, run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix* command.
6. Set route attributes for matched BGP routes as required.
   
   
   * To set the AS\_Path attribute, run the [**apply as-path**](cmdqueryname=apply+as-path) *as-number* &<1-128> [ **additive** ] command.
   * To set a community attribute, run the [**apply community**](cmdqueryname=apply+community) { [ *community-number* | *aa:nn* ] &<1-32> | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } \* [ **additive** ] command.
   * To set a route cost, run the [**apply cost**](cmdqueryname=apply+cost) { [ **+** | **-** ] *cost* | **inherit** } command.
   
   You can set one BGP attribute, such as the AS\_Path, community attribute, or extended community attribute, for the matched BGP routes as required.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
9. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
   
   
   
   The route-policy is applied to the routes to be advertised to the specified peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the BGP peer relationship has been established before applying the route-policy.
10. Run [**peer**](cmdqueryname=peer) *peerIpv4Addr* **advertise-community**
    
    
    
    The device is configured to advertise community attributes to the peer.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.