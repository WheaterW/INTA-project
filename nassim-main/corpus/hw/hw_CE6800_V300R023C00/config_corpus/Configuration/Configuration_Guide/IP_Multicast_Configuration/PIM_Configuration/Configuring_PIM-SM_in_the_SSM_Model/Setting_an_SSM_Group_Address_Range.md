Setting an SSM Group Address Range
==================================

Setting an SSM Group Address Range

#### Context

The group address ranges of SSM and ASM models are different. If the address of the multicast group that a user joins is within the SSM group address range, the SSM forwarding mode is used. Otherwise, the ASM forwarding mode is used. The default SSM group address range is 232.0.0.0/8, which is modifiable. When changing the SSM group address range, ensure that the SSM group address ranges configured on all devices on the network are the same. Otherwise, network faults may occur.


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
3. Configure a rule for the basic ACL.
   
   
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
6. Configure an SSM group address range.
   
   
   ```
   [ssm-policy](cmdqueryname=ssm-policy) { basic-acl-number | acl-name acl-name }
   ```
   
   
   
   The ACL takes effect as follows:
   
   * If a multicast group address matches the ACL rule and the action is **permit**, the device forwards the packets corresponding to the multicast group address in SSM mode.
   * If a multicast group address matches the ACL rule and the action is **deny**, the device refuses to forward the packets corresponding to the multicast group address in SSM mode.
   * If a multicast group address does not match the ACL rule, the device refuses to forward the packets corresponding to the multicast group address in SSM mode.
   * If a specified ACL does not exist or does not contain rules, no SSM group address range is configured.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```