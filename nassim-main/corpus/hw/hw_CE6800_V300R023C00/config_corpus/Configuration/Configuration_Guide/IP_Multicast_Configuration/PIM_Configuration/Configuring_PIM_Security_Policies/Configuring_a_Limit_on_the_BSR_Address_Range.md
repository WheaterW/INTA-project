Configuring a Limit on the BSR Address Range
============================================

Configuring a Limit on the BSR Address Range

#### Context

On a PIM-SM network that applies the BSR mechanism, any device can be configured as a C-BSR to participate in BSR election. The winner is responsible for advertising RP information on the network. When a device on the network is controlled by an attacker or an unauthorized attacker accesses the network, the attacker can set the device as a C-BSR and make the device win the election to obtain the right to advertise RP information on the network. To prevent such attacks, run the **bsr-policy** command on each device on the network to set the range of valid BSR addresses. For example, if only 1.1.1.1/32 and 1.1.1.2/32 are eligible to compete for the BSR, the device does not accept or forward messages from other BSR addresses.


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
5. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
6. Set the range of valid BSR addresses.
   
   
   ```
   [bsr-policy](cmdqueryname=bsr-policy) { bsrPolicyAclNum | acl-name acl-name }
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```