Configuring an Embedded-RP
==========================

By default, the embedded-Rendezvous Point (RP) function is enabled. You can change the range of IPv6 multicast groups that an embedded RP serves or disable the embedded-RP function.

#### Context

The embedded-RP function can be applied either in an IPv6 PIM-SM domain or among PIM-SM domains. It solves the problem that IPv6 PIM-SM domains cannot learn RP information from each other because Multicast Source Discovery Protocol (MSDP) does not support IPv6 networks.

To avoid inconsistent results of RP elections, an RP obtained by using the embedded-RP function takes precedence over other RPs elected by using other mechanisms according to PIM-SM. The range of IPv6 groups that an embedded RP serves is FF70::/12. You can change the range of IPv6 multicast groups that an embedded RP serves.


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
   
   Use the **source** parameter in the [**rule**](cmdqueryname=rule) command to set a multicast group address.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**embedded-rp**](cmdqueryname=embedded-rp) [ *basic-acl6-number* | **acl6-name** *acl6-name* ]
   
   
   
   The range of IPv6 groups that an embedded-RP serves is configured.
   
   
   
   If the group range defined by an IPv6 ACL is wider than the default range of groups that an embedded RP serves, the embedded-RP is valid for the intersection part of the two address ranges.
   
   The same range of groups that an embedded-RP serves must be set on all Routers in an IPv6 PIM-SM domain.
   
   You can run the [**undo embedded-rp**](cmdqueryname=undo+embedded-rp) command to disable the embedded-RP function.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the embedded-RP is used. The embedded-RP group address range is FF7x::/12, where x is 0 or in the range of 3 to F.
   * If an ACL is configured on an interface, the interface uses configured ACL rules to filter multicast group addresses to be served by an embedded-RP.
     + If a multicast group matches an ACL rule and the action is **permit**, the RP that serves this group is an embedded-RP.
     + If a multicast group matches an ACL rule and the action is **deny**, the RP that serves this group is not an embedded-RP.
     + If a multicast group does not match any ACL rule, the RP that serves this group is not an embedded-RP.
     + If a specified ACL does not exist or does not contain rules, RPs that serve multicast groups are not embedded-RPs.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.