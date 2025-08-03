Binding a Global Static Address Pool to a NAT Load-Balancing Group
==================================================================

You can bind a global static address pool to a NAT load balancing instance to implement CGN load balancing.

#### Context

If one NAT service can be bound to only one service board CPU, the service board of a single NAT instance may reach the performance threshold when the number of users goes up. In this situation, service boards are added. After a global static address pool is bound to a NAT instance, multiple service boards share the pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Run [**nat ip-address**](cmdqueryname=nat+ip-address) *ip-address* *mask-len* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   An IP address is configured for inter-chassis traffic diversion.
   
   
   
   In centralized scenarios with dual-device hot backup load balancing, service traffic needs to be diverted to CGN service boards. Therefore, this command must be run.
4. Run [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* **group-id** *group-id* **bind-ip-pool** *pool-name*
   
   
   
   The global static address pool is bound to the NAT instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.