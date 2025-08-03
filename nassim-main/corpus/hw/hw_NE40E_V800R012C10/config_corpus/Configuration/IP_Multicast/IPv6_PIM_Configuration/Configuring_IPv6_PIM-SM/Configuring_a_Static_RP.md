Configuring a Static RP
=======================

To use a static Rendezvous Point (RP) in an IPv6 PIM-SM domain, configure the same RP address and same address arrange of multicast groups that the RP serves on all Routers in the IPv6 PIM-SM domain.

#### Context

Devices that are not configured with static RPs do not forward multicast packets in the local IPv6 PIM-SM domain.

If an IPv6 PIM-SM network is divided into multiple IPv6 PIM-SM domains and the static RP needs to be used, configure the same static RP address on all the Routers in one IPv6 PIM-SM domain to specify the range of each IPv6 PIM-SM domain.


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
   
   You can use the **source** parameter in the [**rule**](cmdqueryname=rule) command to define a multicast group range.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**static-rp**](cmdqueryname=static-rp) *rp-address* [ *basic-acl6-number* | **acl6-name** *acl6-name* ] [ **preferred** ]
   
   
   
   A static RP is configured.
   
   Multiple static RPs can be configured for the Router by using this command repeatedly, but an IPv6 ACL cannot correspond to multiple static RPs. If no IPv6 ACL is referenced, only one static RP can be configured.
   
   * *rp-address*: specifies the address of a static RP.
   * *basic-acl6-number* | **acl6-name** *acl6-name*: specifies the number of a basic IPv6 ACL. This basic IPv6 ACL defines the range of IPv6 groups served by a static RP. When the IPv6 multicast group ranges to which multiple static RPs correspond overlap, the static RP with the largest IPv6 address serves IPv6 multicast groups.
   * **preferred**: indicates that a static RP is preferred. If a BootStrap router (BSR) RP and a static RP exist on a network, after **preferred** is set, the Routers on the network prefer the static RP. Otherwise, the Routers prefer the BSR RP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the static RP serves all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to filter multicast groups to be served by the static RP.
     + If a multicast group matches an ACL rule and the action is **permit**, the static RP serves this multicast group.
     + If a multicast group matches an ACL rule and the action is **deny**, the static RP does not serve this multicast group.
     + If a multicast group does not match any ACL rule or if a specified ACL does not exist or does not contain rules, the static RP serves all multicast groups.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.