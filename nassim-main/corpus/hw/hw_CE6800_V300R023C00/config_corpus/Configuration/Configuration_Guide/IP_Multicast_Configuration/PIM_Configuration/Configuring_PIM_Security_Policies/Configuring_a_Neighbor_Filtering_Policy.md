Configuring a Neighbor Filtering Policy
=======================================

Configuring a Neighbor Filtering Policy

#### Context

A neighbor filtering policy defines the range of permitted neighbor addresses. A device with such a policy discards Hello messages from neighbors that are not in this address range.


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
7. Configure a neighbor filtering policy.
   
   
   ```
   [pim neighbor-policy](cmdqueryname=pim+neighbor-policy) { basic-acl-number | acl-name acl-name }
   ```
   
   A neighbor filtering policy defines the range of permitted neighbor addresses. A device with such a policy discards Hello messages from neighbors that are not in this address range.
   
   * If an ACL rule is matched and the action is **permit**, the device establishes neighbor relationships with the addresses in this range.
   * If an ACL rule is matched and the action is **deny**, the device does not set up any neighbor relationships with the addresses in this range.
   * If an ACL rule is not matched, the device does not set up any neighbor relationships with the addresses in this range.
   * If the applied ACL or rule does not exist, the device does not set up neighbor relationships with any addresses.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```