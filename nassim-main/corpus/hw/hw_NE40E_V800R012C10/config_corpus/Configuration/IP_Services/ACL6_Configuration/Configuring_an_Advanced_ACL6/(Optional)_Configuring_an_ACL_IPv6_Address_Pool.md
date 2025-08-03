(Optional) Configuring an ACL IPv6 Address Pool
===============================================

This section describes how to configure an ACL IPv6 address pool to filter packets based on the source IPv6 addresses of BGP peers.

#### Context

In some typical ACL6 application scenarios, multiple IPv6 addresses need to be matched. To use an ACL6 to match multiple source and destination IPv6 addresses, you must specify all possible combinations of source and destination IPv6 addresses when configuring ACL6 rules. However, these combinations are over 10 thousands on a large-scale network. It is unreasonable to manually configure all ACL6 rules that match both source and destination IPv6 addresses carried in packets.

To reduce the configuration workload, configure an ACL6 IPv6 address pool. After an ACL6 IPv6 address pool is configured, you only need to configure an ACL6 rule with a specified ACL6 IPv6 address pool name (*pool-name*) to match multiple IPv6 addresses.![](../../../../public_sys-resources/note_3.0-en-us.png) 

In scenarios in which ACL6 rules are used to match both source and destination IPv6 addresses carried in packets, run the [**acl ipv6-pool**](cmdqueryname=acl+ipv6-pool) command to create an ACL6 source IPv6 address pool (which includes all needed source IPv6 addresses) and an ACL6 destination IPv6 address pool (which includes all needed destination IPv6 addresses).


In some typical ACL6 application scenarios, such as QoS or security service scenarios, to filter traffic with the source IPv6 address being the address of a BGP peer, create an ACL IPv6 address pool, associate the address of the BGP peer with this address pool, and then configure the QoS or security service to reference the ACL6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6-pool**](cmdqueryname=acl+ipv6-pool) *pool-name*
   
   
   
   An ACL IPv6 address pool is created, and the ACL IPv6 address pool view is displayed.
3. Add an IPv6 address to the ACL IPv6 address pool, associate IPv6 addresses of BGP peers with the address pool, or associate interface IPv6 addresses with the address pool.
   
   
   * Run the [**ipv6 address**](cmdqueryname=ipv6+address) *ipv6-address* { *ipv6-mask* | *mask-length* } command to add an IPv6 address to the ACL IPv6 address pool.
     
     If the command is run more than once, all configurations take effect.
   * Run the [**apply bgp-peer**](cmdqueryname=apply+bgp-peer+public-vpn+all-private-vpn+vpn-instance) [ **public-vpn** | **all-private-vpn** | **vpn-instance** *vpn-instance-name* ] command to associate the addresses of BGP peers with the address pool.
   * Run the [**apply interface-address**](cmdqueryname=apply+interface-address+main-interface+sub-interface) { **main-interface** | **sub-interface** | **all-interface** } [ **public-vpn** | **all-private-vpn** | **vpn-instance** *VpnInstanceName* ] command to associate interface IPv6 addresses with the address pool.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command is applicable only to QoS or device security services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.