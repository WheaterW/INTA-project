Enabling OSPF for a Multi-area Adjacency Interface
==================================================

Enabling OSPF for a Multi-area Adjacency Interface

#### Prerequisites

Before enabling OSPF for a multi-area adjacency interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Enabling OSPF for multi-area adjacency interfaces implements basic functions of the multi-area adjacency interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Enable OSPF for an interface.
   1. Return to the OSPF view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   3. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   4. Enable OSPF on the interface.
      
      
      ```
      [ospf enable](cmdqueryname=ospf+enable) [ process-id ] area area-id
      ```
5. Configure a multi-area adjacency interface and enable OSPF for it.
   
   
   ```
   [ospf enable multi-area](cmdqueryname=ospf+enable+multi-area) area-id
   ```
6. Enable the multi-area adjacency interface to fill in DD packets with its actual MTU before packet advertisement and check whether the MTU in a DD packet received from a neighbor exceeds the local MTU.
   
   
   ```
   [ospf mtu-enable multi-area](cmdqueryname=ospf+mtu-enable+multi-area) area-id
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   After this command is run, the involved neighbor relationship will be re-established.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```