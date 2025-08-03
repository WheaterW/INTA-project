Setting a Valid C-RP Address Range
==================================

You can create ACL rules on all Candidate-BootStrap Routers (C-BSRs) for filtering Candidate-Rendezvous Point (C-RP) addresses and the addresses of groups that C-RPs serve. A BSR accepts the Advertisement messages and adds C-RP information to the RP-Set only when C-RP addresses and the addresses of the groups that C-RPs serve in the Advertisement messages are within the valid address range. Thus, the C-RP spoofing is prevented.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   An advanced ACL is created, and the advanced ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
   
   
   
   Rules are configured for the advanced ACL.
   
   Run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a valid C-RP source address range, and set the **destination** parameter to a multicast group address range to be served by C-RPs.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**pim**](cmdqueryname=pim) [ **vpn-instance***vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
6. Run [**crp-policy**](cmdqueryname=crp-policy) { *advanced-acl-number* | **acl-name** *acl-name* }
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If an Advertisement message from a C-RP matches an ACL rule and the action is **permit**, the BSR permits this message.
   * If an Advertisement message from a C-RP matches an ACL rule and the action is **deny**, the BSR denies this message.
   * If an Advertisement message from a C-RP does not match any ACL rule, the BSR denies this message.
   * If a specified ACL does not exist or does not contain rules, the BSR denies all messages from any C-RP.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.