CP-CAR Configuration Method and Procedure
=========================================

The following example uses CP-CAR configuration to describe how to add a trusted network segment to a whitelist.

1. Run **system-view**
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { [ **number** ] *acl-number* | **name** *acl-name* [ **number** *acl-number* ] } [ **match-order** { **auto** | **config** } ]
   
   The advanced ACL is configured.
3. Run **rule** [ *rule-id* ] **permit** [ **fragment-type** *fragment-type-name* | **source** { *source-ip-address* *source-wildcard* | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   The trusted network segment is specified in an ACL rule.
4. Run **rule** [ *rule-id* ] **deny** [ **fragment-type** *fragment-type-name* | **source** { *source-ip-address* *source-wildcard* | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   The untrusted network segment is specified in an ACL rule.
5. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.
6. Run **quit**
   
   Return to the system view.
7. Run **cpu-defend policy** *policy-number*
   
   An attack defense policy is created.
8. Run **whitelist acl** *acl-number*
   
   A whitelist is created.
   
   To disable the whitelist function, run the [**whitelist disable**](cmdqueryname=whitelist+disable) command.
9. Run **car whitelist** { **cir** *cir-value* | **cbs** *cbs-value* } \*
   
   The bandwidth for incoming packets to be sent to the CPU is configured in the whitelist.
10. Run **priority whitelist** { **high** | **middle** | **low** }
    
    The priority of incoming packets to be sent to the CPU is configured in the whitelist.
11. Run [**commit**](cmdqueryname=commit)
    
    The configuration is committed.
12. Run **quit**
    
    Exit from the policy view.
13. Run **slot** *slotl-number*
    
    The interface board view is displayed.
14. Run **cpu-defend-policy** *policy-number*
    
    The attack defense policy is bound to the interface board.
    
    The attack defense function takes effect on an interface board only after the interface board is bound to an attack defense policy.
15. Run [**commit**](cmdqueryname=commit)
    
    The configuration is committed.

#### Verifying the Security Hardening Result

Run the **display current-configuration configuration cpu-defend-policy** command to check the configuration of the attack defense policy.