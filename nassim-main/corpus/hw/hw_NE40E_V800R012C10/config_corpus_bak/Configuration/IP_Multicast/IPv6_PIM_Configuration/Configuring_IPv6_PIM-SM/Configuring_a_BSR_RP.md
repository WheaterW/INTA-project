Configuring a BSR RP
====================

Select several Routers and configure them as Candidate-BootStrap Routers (C-BSRs) and Candidate-Rendezvous Points (C-RPs). A BSR is dynamically elected from C-BSRs. The BSR collects C-RP information and summarizes C-RP information into an RP-Set. The RP-Set is encapsulated in a Bootstrap message and advertised to all the Routers in the IPv6 PIM domain. Then, the C-RPs elect a BSR RP based on a uniform election rule.

#### Context

If an IPv6 PIM-SM network is divided into multiple IPv6 PIM-SM domains and a dynamic RP needs to used, [configure a BSR boundary](dc_vrp_multicast_cfg_2015.html) on the interfaces of edge Routers in IPv6 PIM-SM domains to limit the range of each IPv6 PIM-SSM domain. Then, configure C-BSRs and C-RPs in each IPv6 PIM-SM domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL6 or a named ACL6 as needed.
   
   
   * Configure a basic numbered ACL6.
     
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL6 is created, and the basic numbered ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the basic numbered ACL6.
   * Configure a named ACL6.
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL6 is created, and the named ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the named ACL6.
   
   You can use the **source** parameter in the [**rule**](cmdqueryname=rule) command to define the range of multicast groups served by the C-RP.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**c-bsr**](cmdqueryname=c-bsr) *ipv6-address* [ *hash-length* ]
   
   
   
   A C-BSR is configured.
   
   
   
   * *ipv6-address*: specifies the IPv6 address of the interface where a C-BSR resides. The interface must be enabled with IPv6 PIM-SM.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, use the loopback interface address as the global IPv6 unicast address of the C-BSR.
   * *hash-length*: specifies the hash mask length.
     
     Based on the group address G, C-RP address, and the value of *hash-length*, Routers use hash functions to calculate the C-RPs that have the same priority and want to serve G, and then compare the calculation results. The C-RP that has the largest calculated value is elected as the RP for group G.
     
     When a multicast network is overloaded or traffic congests on an RP, the RP may be overburdened. In this situation, you can configure *hash-length* to enable different RPs to transmit services for different multicast groups and implement load balancing.
6. Run [**c-rp**](cmdqueryname=c-rp) *ipv6-address* [ **advertisement-interval** *adv-interval* | **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* } | **holdtime** *hold-interval* | **priority** *priority* ] \*
   
   
   
   A C-RP is configured.
   
   
   
   * *ipv6-address*: specifies the IPv6 address of the interface where a C-RP resides. The interface must be enabled with IPv6 PIM-SM.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, use the loopback interface address as the global IPv6 unicast address of the C-RP.
   * **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }: indicates that a C-RP serves only IPv6 multicast groups within the IPv6 multicast group range defined by a specified IPv6 ACL. By default, a C-RP serves all IPv6 multicast groups.
   * **priority** *priority*: specifies the priority of a C-RP. A larger **priority** value indicates a lower priority.
     
     An RP is elected based on the following rules:
     
     + The C-RP with the highest priority wins.
     + If interfaces have the same priority, the hash function is used and the C-RP with the largest hash value wins.
     + If interfaces have the same priority and the same hash value, the C-RP with the highest IPv6 address wins.
   * **holdtime** *hold-interval*: specifies the timeout period during which the BSR waits to receive Advertisement message from a C-RP.
   * **advertisement-interval** *adv-interval*: specifies the interval at which a C-RP sends Advertisement messages.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the C-RP serves all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to filter multicast groups to be served by the C-RP.
     + If a multicast group matches an ACL rule and the action is **permit**, the C-RP serves this multicast group.
     + If a multicast group matches an ACL rule and the action is **deny**, the C-RP does not serve this multicast group.
     + If a multicast group does not match any ACL rule or if a specified ACL does not exist or does not contain rules, the C-RP serves all multicast groups.
7. (Optional) Run [**bsm semantic fragmentation**](cmdqueryname=bsm+semantic+fragmentation)
   
   
   
   BSR packet fragmentation is enabled.
   
   
   
   Enabling BSR packet fragmentation on all devices is recommended because BSR packet fragmentation can solve the problem faced by IP fragmentation that all fragments become unavailable due to loss of fragment information.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.