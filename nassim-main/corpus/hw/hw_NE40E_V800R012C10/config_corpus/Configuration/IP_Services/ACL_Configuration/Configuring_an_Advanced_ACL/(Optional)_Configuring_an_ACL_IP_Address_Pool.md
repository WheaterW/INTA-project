(Optional) Configuring an ACL IP Address Pool
=============================================

An ACL IP address pool is applicable to the scenario in which multiple IP addresses need to be matched and reduces the configuration workload.

#### Context

In typical ACL usage scenarios, for example, in the policy-based routing scenario, multiple IP addresses need to be matched. To implement policy-based routing using ACL rules to match both source and destination IP addresses carried in packets, specify all possible combinations of source IP addresses and destination IP addresses when configuring ACL rules. However, these combinations are over 10 thousands on a large-scale network. It is unreasonable to configure manually all ACL rules that match both source and destination IP addresses carried in packets.

To reduce the configuration workload, configure an ACL IP address pool. After an ACL IP address pool is configured, you only need to configure an ACL rule with a specified IP address pool name (*pool-name*) to match multiple IP addresses carried in packets.![](../../../../public_sys-resources/note_3.0-en-us.png) 

In scenarios in which ACL rules are used to match both source and destination IP addresses carried in packets, run the [**acl ip-pool**](cmdqueryname=acl+ip-pool) command to create an ACL source IP address pool (which includes all needed IP addresses) and an ACL destination IP address pool (which includes all needed destination IP addresses), respectively.


If you need to filter packets with the source address being the IP address of a BGP peer, run the [**apply bgp-peer**](cmdqueryname=apply+bgp-peer) command to associate the IP address of the BGP peer with the ACL address pool. Then configure QoS or security services to reference the ACL to filter traffic of the BGP peer.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ip-pool**](cmdqueryname=acl+ip-pool) *pool-name*
   
   
   
   An ACL IP address pool is created and the IP address pool view is displayed.
3. Add an IP address to the ACL IP address pool, associate IP addresses of BGP peers with the address pool, or associate interface IP addresses with the address pool.
   
   
   * Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to add an IP address to the ACL IP address pool.
     
     If the command is run more than once, all configurations take effect.
   * Run the [**apply bgp-peer**](cmdqueryname=apply+bgp-peer+public-vpn+all-private-vpn+vpn-instance) [ **public-vpn** | **all-private-vpn** | **vpn-instance** *vpn-instance-name* ] command to associate IP addresses of BGP peers with the ACL IP address pool.
   * Run the [**apply interface-address**](cmdqueryname=apply+interface-address+main-interface+sub-interface) { **main-interface** | **sub-interface** | **all-interface** } [ **public-vpn** | **all-private-vpn** | **vpn-instance** *VpnInstanceName* ] command to associate interface IP addresses with the address pool.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is applicable only to QoS or device security services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.