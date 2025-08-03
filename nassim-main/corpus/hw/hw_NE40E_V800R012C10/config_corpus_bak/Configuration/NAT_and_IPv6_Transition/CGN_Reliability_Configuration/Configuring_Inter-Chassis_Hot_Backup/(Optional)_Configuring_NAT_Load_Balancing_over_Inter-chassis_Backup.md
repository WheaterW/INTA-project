(Optional) Configuring NAT Load Balancing over Inter-chassis Backup
===================================================================

This section describes how to configure NAT load balancing over inter-chassis backup.

#### Context

In centralized NAT load balancing, when the master device becomes faulty, services may be interrupted. To ensure normal service operation, configure inter-chassis backup on the basis of load balancing.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* **group-id** *group-id* **bind-ip-pool** *pool-name*
   
   
   
   The NAT instance is bound to a global static address pool.
4. Run [**nat ip-address**](cmdqueryname=nat+ip-address) *ip-address* *mask-len* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IP address for distributing traffic between the master and slave chassis is configured.
   
   This command is mandatory for achieving NAT load balancing and inter-chassis backup.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.