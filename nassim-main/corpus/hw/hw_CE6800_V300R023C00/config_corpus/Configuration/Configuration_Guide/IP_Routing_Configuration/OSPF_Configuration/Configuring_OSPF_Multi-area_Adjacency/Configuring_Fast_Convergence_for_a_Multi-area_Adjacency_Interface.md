Configuring Fast Convergence for a Multi-area Adjacency Interface
=================================================================

Configuring Fast Convergence for a Multi-area Adjacency Interface

#### Prerequisites

Before configuring fast convergence for a multi-area adjacency interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Configuring fast convergence for a multi-area adjacency interface improves network performance.


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
5. Configure fast convergence for the multi-area adjacency interface as needed.
   
   
   * Set an interval at which the multi-area adjacency interface sends Hello packets.
     
     ```
     [ospf timer hello](cmdqueryname=ospf+timer+hello) interval multi-area area-id
     ```
   * Set a dead interval for OSPF neighbors of the multi-area adjacency interface.
     
     ```
     [ospf timer dead](cmdqueryname=ospf+timer+dead) interval multi-area area-id
     ```
   * Set an interval at which the multi-area adjacency interface retransmits LSAs.
     
     ```
     [ospf timer retransmit](cmdqueryname=ospf+timer+retransmit) interval multi-area area-id
     ```
   * Set a delay for the multi-area adjacency interface to transmit LSAs.
     ```
     [ospf trans-delay](cmdqueryname=ospf+trans-delay) delayValue multi-area { area-id | area-id }
     ```
   * Enable the Smart-discover function on the multi-area adjacency interface.
     ```
     [ospf smart-discover](cmdqueryname=ospf+smart-discover) multi-area area-id
     ```
     
     If the neighbor status of a device or the DR/BDR on a multi-access network (broadcast or NBMA network) changes, the device waits until the Hello timer expires before sending Hello packets to its neighbor. This means that establishing a neighbor relationship takes longer to complete. To resolve this problem, configure Smart-discover. When configured, Smart-discover allows the device to send Hello packets to its neighbors immediately without waiting for the Hello timer of the multi-area adjacency interface to expire. This speeds up neighbor relationship establishment and network convergence.
   * Configure the multi-area adjacency interface to filter the LSAs to be sent.
     ```
     [ospf filter-lsa-out](cmdqueryname=ospf+filter-lsa-out) { all | { ase [ acl { ase-acl-num | ase-acl-name } ] | nssa [ acl { nssa-acl-num | nssa-acl-name } ] | summary [ acl { sum-acl-num | sum-acl-name } ] } * } multi-area { area-id-integer | area-id-ipv4 }
     ```
     
     If multiple links exist between two devices, you can configure this filtering function on some links to ensure that the matched LSAs are not transmitted through these links. This prevents unnecessary retransmissions and saves bandwidth resources.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```