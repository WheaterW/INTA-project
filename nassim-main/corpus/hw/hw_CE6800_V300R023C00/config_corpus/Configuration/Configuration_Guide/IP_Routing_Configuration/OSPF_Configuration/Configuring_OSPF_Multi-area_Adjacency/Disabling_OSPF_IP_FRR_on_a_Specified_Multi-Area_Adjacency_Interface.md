Disabling OSPF IP FRR on a Specified Multi-Area Adjacency Interface
===================================================================

Disabling OSPF IP FRR on a Specified Multi-Area Adjacency Interface

#### Prerequisites

Before disabling OSPF IP FRR on a specified multi-area adjacency interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If an OSPF multi-area adjacency interface is connected to a link carrying key services, you can prevent FRR from using the connected link as a backup link by disabling OSPF IP FRR on the interface. This reduces the impact on services.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable OSPF on the interface.
   
   
   ```
   [ospf enable](cmdqueryname=ospf+enable) [ process-id ] area area-id
   ```
4. Configure a multi-area adjacency interface and enable OSPF for it.
   
   
   ```
   [ospf enable multi-area](cmdqueryname=ospf+enable+multi-area) area-id
   ```
5. Disable OSPF IP FRR on the multi-area adjacency interface.
   
   
   ```
   [ospf frr block](cmdqueryname=ospf+frr+block) multi-area area-id
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```