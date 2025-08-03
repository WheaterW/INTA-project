Setting a Cost for a Multi-area Adjacency Interface
===================================================

Setting a Cost for a Multi-area Adjacency Interface

#### Prerequisites

Before setting a cost for a multi-area adjacency interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

You can adjust and optimize route selection by setting a cost for a multi-area adjacency interface.


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
5. Set a cost for the multi-area adjacency interface.
   
   
   ```
   [ospf cost](cmdqueryname=ospf+cost) cost multi-area area-id
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```