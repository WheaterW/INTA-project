Configuring a User-Defined Flow
===============================

This section describes how to configure a user-defined flow and add the specified traffic to the flow based on ACL rules. In this way, traffic policing can be performed on the packets as required.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number* command to enter the attack defense policy view.
3. Run the [**user-defined-flow**](cmdqueryname=user-defined-flow+acl+name+prior+ipv6+acl+name) *flow-id* **acl** { *acl-number* | **name** *acl-name* } [ **prior** ] or [**user-defined-flow**](cmdqueryname=user-defined-flow+ipv6+acl+name) *flow-id* **ipv6** **acl** { *acl-number* | **name** *acl-name* } command to configure a user-defined flow.
   
   
   
   An address or port pool can be specified in an ACL rule, and the ACL rule can be delivered.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The IPv4 address pool function can be delivered in an attack defense policy only after the [**cp-acl ip-pool enable**](cmdqueryname=cp-acl+ip-pool+enable) command is run.
   * By default, the IPv6 address pool function is disabled in an attack defense policy. If this function is disabled, the device can only deliver source address pool rules of the BGP IPv6 peer type through the user-defined flow function. To enable other IPv6 address pool functions, run the [**cp-acl ipv6-pool enable**](cmdqueryname=cp-acl+ipv6-pool+enable) command.
   * The **vpn-instance** field in the ACL rule bound to an attack defense policy takes effect only after the [**cp-acl vpn-instance enable**](cmdqueryname=cp-acl+vpn-instance+enable) command is run.
   * If both a port pool and a TTL range are specified in an ACL rule, the TTL range does not take effect.
   * A port pool does not support the delivery of ACL rules configured with the **neq** parameter.
   * If the address pool function is not enabled, an ACL rule in which both address and port pools are specified cannot be delivered.
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
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.