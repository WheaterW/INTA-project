Configuring a Join Information Filtering Policy
===============================================

Configuring a Join Information Filtering Policy

#### Context

To prevent unauthorized users from joining a multicast group, configure a join information filtering policy to specify a permitted source address range for join information in Join/Prune messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a type of ACL as required.
   
   
   * Configure a basic numbered ACL.
     ```
     [acl](cmdqueryname=acl) [ number ] basic-acl-number 
     ```
   * Configure a named ACL.
     ```
     [acl](cmdqueryname=acl) name acl-name basic 
     ```
3. Configure an ACL rule.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the PIM interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Configure a join information filtering policy to specify the permitted source address range of join information.
   
   
   ```
   [pim join-policy](cmdqueryname=pim+join-policy) { asm { basic-acl-number | acl-name acl-name }basic-acl-number | ssm { advanced-acl-number | acl-name acl-name }advanced-acl-number | advanced-acl-number | acl-name acl-name }
   ```
   
   When defining an ACL rule, you can use the **permit** parameter to enable the device to accept only the Join messages with addresses in the specified address range. If no ACL [**rule**](cmdqueryname=rule) is defined, the interface filters out join information of any address range in Join/Prune messages by default.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```