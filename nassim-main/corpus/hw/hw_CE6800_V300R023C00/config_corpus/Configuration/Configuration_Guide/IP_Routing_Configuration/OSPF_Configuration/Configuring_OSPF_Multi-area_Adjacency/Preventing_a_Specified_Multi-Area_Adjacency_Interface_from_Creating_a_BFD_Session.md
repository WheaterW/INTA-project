Preventing a Specified Multi-Area Adjacency Interface from Creating a BFD Session
=================================================================================

Preventing a Specified Multi-Area Adjacency Interface from Creating a BFD Session

#### Prerequisites

Before preventing a specified multi-area adjacency interface from creating a BFD session, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* [Configure BFD for OSPF](vrp_ospf_cfg_0090.html).

#### Context

After BFD for OSPF is configured, all interfaces on which neighbor relationships are in the Full state in the OSPF process will create BFD sessions. If BFD is not required on specific interfaces, disable these interfaces from dynamically creating BFD sessions.


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
5. Prevent the multi-area adjacency interface from creating a BFD session.
   
   
   ```
   [ospf bfd block](cmdqueryname=ospf+bfd+block) multi-area area-id
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```