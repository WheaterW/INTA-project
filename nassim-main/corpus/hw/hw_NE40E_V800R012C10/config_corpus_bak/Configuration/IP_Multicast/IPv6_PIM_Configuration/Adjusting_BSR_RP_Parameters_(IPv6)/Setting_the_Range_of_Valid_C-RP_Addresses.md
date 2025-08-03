Setting the Range of Valid C-RP Addresses
=========================================

The range of valid Candidate-Rendezvous Point (C-RP) addresses and range of IPv6 multicast groups that each C-RP serves can be configured to filter packets on all Candidate-BootStrap Routers (C-BSRs) by using an IPv6 ACL. The BSR adds the C-RP information contained in an Advertisement message received from a C-RP to the RP-Set only when the address of the C-RP and IPv6 multicast groups that the C-RP serves are within the configured ranges respectively. This prevents C-RP spoofing.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   An advanced ACL6 is created, and the advanced ACL6 view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
   
   
   
   Rules are configured for the advanced ACL6.
   
   
   
   Run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a valid C-RP source address range, and set the **destination** parameter to a multicast group address range to be served by C-RPs.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
6. Run [**crp-policy**](cmdqueryname=crp-policy) { *advanced-acl6-number* | **acl6-name** *acl6-name* }
   
   
   
   The range of valid C-RP addresses and the range of IPv6 multicast groups that a C-RP serves are set.
   
   
   
   * If the C-RP address or the address of a multicast group that a C-RP serves contained in an Advertisement message is not within the range defined by an IPv6 ACL or no action is defined in the IPv6 ACL for processing such an Advertisement message, the BSR discards the Advertisement message and does not add the C-RP information carried by the Advertisement message to the RP-Set.
   * If only *advanced-acl6-number* or **acl6-name** *acl6-name* is set but no ACL6 is set, the BSR denies all Advertisement messages, and all RP information cannot be added to the RP-set.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If an Advertisement message from a C-RP matches an ACL rule and the action is **permit**, the BSR permits this message.
   * If an Advertisement message from a C-RP matches an ACL rule and the action is **deny**, the BSR denies this message.
   * If an Advertisement message from a C-RP does not match any ACL rule, the BSR denies this message.
   * If a specified ACL does not exist or does not contain rules, the BSR denies all messages from any C-RP.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.