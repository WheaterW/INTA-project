Configuring a Blacklist
=======================

This section describes how to configure a blacklist. Insecure packets that match ACL rules can be added to the blacklist and then provided with lower bandwidth.

#### Prerequisites

The ACL bound to the blacklist must be a configured one. You can bind a non-existing ACL to the blacklist. When the ACL is bound to the blacklist, all the packets that match the ACL rules are added to the blacklist automatically. The blacklist function must be enabled. Otherwise, the self-defined blacklist does not take effect although you can configure a self-defined blacklist.


#### Context

If you determine that certain packets cannot be sent to the CPU or are invalid, you can add them to the blacklist by setting ACL rules. In this manner, you can discard these packets. All the users in the blacklist need to be manually configured. There is no default user in the blacklist.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**blacklist**](cmdqueryname=blacklist+ipv6+acl+name) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }
   
   
   
   A self-defined blacklist is created.
   
   A self-define blacklist can be bound to only one ACL. If you bind a self-define blacklist to several ACLs, only the latest configuration takes effect. An address or port pool can be specified in an ACL rule, and the ACL rule can be delivered.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The address pool function can be delivered in the attack defense policy only when the [**cp-acl ip-pool enable**](cmdqueryname=cp-acl+ip-pool+enable) command is configured.
   * By default, the IPv6 address pool function is disabled in an attack defense policy. If this function is disabled, the device can only deliver source address pool rules of the BGP IPv6 peer type based on a blacklist. To enable the device to support other types of IPv6 address pool rules, run the **cp-acl ipv6-pool enable** command.
   * The **vpn-instance** field in an ACL configured in an attack defense policy can be delivered and takes effect only when the [**cp-acl vpn-instance enable**](cmdqueryname=cp-acl+vpn-instance+enable) command is configured.
   * If the ACL rule in which both a port pool and a TTL range are specified is delivered, the TTL range does not take effect.
   * ACL rules with the **neq** parameter are not supported.
   * If the address pool function is not enabled, the ACL rule in which both address and port pools are specified cannot be delivered.
4. (Optional) Run the [**ipv6-enhance acl enable**](cmdqueryname=ipv6-enhance+acl+enable) command to enable some IPv6 packets to be sent to the CPU to match the ACL rules specified in a blacklist, whitelist, or user-defined flow of the attack defense policy.
5. (Optional) Run the [**cp-acl ip-pool enable**](cmdqueryname=cp-acl+ip-pool+enable) command to enable the IPv4 address pool function for the attack defense policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before enabling the IPv4 address pool function for an attack defense policy, configure an IPv4 address pool and bind an ACL to the address pool.
6. (Optional) Run the [**cp-acl ipv6-pool enable**](cmdqueryname=cp-acl+ipv6-pool+enable) command to enable the IPv6 address pool function for the attack defense policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before enabling the IPv6 address pool function for an attack defense policy, configure an IPv6 address pool and bind an ACL to the address pool.
7. (Optional) Run the **[**cp-acl ipv6-fragment enable**](cmdqueryname=cp-acl+ipv6-fragment+enable)** command to enable the device to match IPv6 fragmented packets against CPACL rules.
8. (Optional) Run the [**cp-acl vpn-instance enable**](cmdqueryname=cp-acl+vpn-instance+enable) command to enable the **vpn-instance** field in the ACL rule bound to the attack defense policy to take effect.
9. (Optional) Run the [**acl ipv4-multicast-fib-miss enable**](cmdqueryname=acl+ipv4-multicast-fib-miss+enable) command to enable the device to match IPv4 MFIB-MISS packets against the ACL rules specified in a blacklist, whitelist, or user-defined flow of the attack defense policy.
10. (Optional) Run the **acl dhcp-discover enable** command to enable the device to match DHCP DISCOVER packets against the ACL rules specified in a blacklist, whitelist, or user-defined flow of the attack defense policy.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.