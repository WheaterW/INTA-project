Configuring a Static RP
=======================

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain.

#### Context

If a network is divided into multiple PIM-SM domains and the static RP needs to be used, configure the same static RP address on all the CEs and PEs in one PIM-SM domain to specify the range of each PIM-SM domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL or a naming ACL as needed.
   
   
   * Configure a basic numbered ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL is created, and the basic numbered ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic numbered ACL.
   * Configure a naming ACL.
     
     1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A naming ACL is created, and the naming ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the naming ACL.
   
   Run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the multicast group range to be served by the static RP.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**static-rp**](cmdqueryname=static-rp) *rp-address* [ *basic-acl-number* | **acl-name** *acl-name* ] [ **preferred** ]
   
   
   
   A static RP is specified.
   
   You can run this command repeatedly to configure multiple static RPs for the router.
   
   * *rp-address*: specifies the static RP address.
   * *basic-acl-number*: specifies an access control list. Such a list defines the range of multicast groups that the static RP serves. If a multicast group is in the service range of more than one static RP, the multicast group is served by the static RP with the largest IP address.
   * **preferred**: indicates that the static RP takes precedence. If Candidate-Rendezvous Points (C-RPs) are also configured and **preferred** is specified in the [**static-rp**](cmdqueryname=static-rp) command, routers prefer the statically specified RP; otherwise, C-RPs are preferred.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the static RP serves all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to filter multicast groups to be served by the static RP.
     + If a multicast group matches an ACL rule and the action is **permit**, the static RP serves this multicast group.
     + If a multicast group matches an ACL rule and the action is **deny**, the static RP does not serve this multicast group.
     + If a multicast group does not match any ACL rule or if a specified ACL does not exist or does not contain rules, the static RP serves all multicast groups.
6. (Optional) Run [**source-lifetime**](cmdqueryname=source-lifetime) *interval*
   
   
   
   The timeout period of multicast source entries is specified.
   
   Each a (S,G) entry has a timer. When the router receives a multicast packet from the source, it will reset the timer of the corresponding entry. If no multicast packet of the source is received with the timeout period, the (S,G) entry is considered invalid.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.