Configuring a BSR RP
====================

Select several Routers and configure them as Candidate-BootStrap Routers (C-BSRs) and Candidate-Rendezvous Points (C-RPs). A BSR is dynamically elected from C-BSRs. The BSR collects C-RP information and summarizes C-RP information into an RP-Set. The RP-Set is encapsulated in a Bootstrap message and advertised to all the Routers in the PIM domain. Then, the C-RPs elect a BSR RP based on a uniform election rule.

#### Context

If a network is divided into several PIM-SM domains and the BSR RP needs to be used, [configure a BSR boundary](dc_vrp_multicast_cfg_0020.html) on the interfaces of edge Routers in PIM-SM domains to limit the range of each PIM-SM domain. Then, configure C-BSRs and C-RPs in each PIM-SM domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL or a named ACL as needed.
   
   
   * Configure a basic numbered ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL is created, and the basic numbered ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic numbered ACL.
   * Configure a named ACL.
     
     1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL is created, and the named ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the named ACL.
   
   If a basic numbered ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the multicast group range to be served by the C-RP.
   
   If a named ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **destination** parameter to the multicast group range to be served by the C-RP.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**c-bsr**](cmdqueryname=c-bsr) *interface-type* *interface-number* [ *hash-length* [ *priority* ] ]
   
   
   
   The C-BSR is configured.
   
   
   
   * *interface-type* *interface-number*: specifies the interface where the C-BSR resides. The interface must be configured with PIM-SM.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, using loopback interfaces is recommended.
   * *hash-length*: specifies the length of the hash mask.
     
     Based on the group address G, C-RP addresses, and value of *hash-length*, the Router calculates the hash value of the C-RPs that have the same priority and want to serve group G. The C-RP with the largest hash value is elected as the RP for group G.
     
     When a multicast network is overloaded or traffic congests on an RP, the RP may be overburdened. In this situation, you can configure *hash-length* to enable different RPs to transmit services for different multicast groups and implement load balancing.
   * *priority*: specifies the C-BSR priority for BSR election. A larger *priority* value indicates a higher priority.
     
     In a BSR election, the C-BSR with the highest priority wins. If all C-BSRs have the same priority, the C-BSR with the largest IP address wins.
6. Run [**c-rp**](cmdqueryname=c-rp) *interface-type* *interface-number* [ **group-policy** { *basic-acl-number* | **acl-name** *acl-name* } | **priority** *priority* | **holdtime** *hold-interval* | **advertisement-interval** *adv-interval* ] \*
   
   
   * A C-RP is configured. *interface-type* *interface-number*: specifies the interface where the C-RP resides. The interface must be configured with PIM-SM.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, using loopback interfaces is recommended.
     
     If IP address unnumbered is enabled, do not configure the interfaces with the same address as C-RPs simultaneously. If the priorities of C-RPs are different, the BSR considers that the C-RP configuration is frequently modified.
   * **group-policy** *basic-acl-number*: specifies that the C-RP serves only the multicast groups matching the ACL.
   * **priority** *priority*: specifies the C-RP priority for RP election. A larger *priority* value indicates a higher priority.
     
     The RP election rules are as follows:
     
     + If interfaces have the same address mask, the C-RP with the highest priority wins.
     + If interfaces have the same priority, the hash function is used and the C-RP with the largest hash value wins.
     + If interfaces have the same priority and the same hash value, the C-RP with the largest IP address wins.
   * **holdtime** *hold-interval*: specifies the timeout period for the BSR to wait for an Advertisement message from the C-RP.
   * **advertisement-interval** *adv-interval*: specifies the interval for the C-RP to send Advertisement messages.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the C-RP serves all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to filter multicast groups to be served by the C-RP.
     + If a multicast group matches an ACL rule and the action is **permit**, the C-RP serves this multicast group.
     + If a multicast group matches an ACL rule and the action is **deny**, the C-RP does not serve this multicast group.
     + If a multicast group does not match any ACL rule or if a specified ACL does not exist or does not contain rules, the C-RP serves all multicast groups.
7. (Optional) Run [**bsm semantic fragmentation**](cmdqueryname=bsm+semantic+fragmentation)
   
   
   
   BSR packet fragmentation is enabled.
   
   Enabling BSR packet fragmentation on all devices is recommended because BSR packet fragmentation can solve the problem faced by IP fragmentation that all fragments become unavailable due to loss of fragment information.
8. (Optional) Run [**auto-rp listening enable**](cmdqueryname=auto-rp+listening+enable)
   
   
   
   Auto-RP listening is enabled.
   
   Configure this command if the Router needs to interwork with a device that supports Auto-RPs.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.