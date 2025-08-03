Enabling Secure Synchronization
===============================

Enabling Secure Synchronization

#### Prerequisites

Before enabling secure synchronization, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

For a short moment when devices in an area finish synchronizing their LSDBs, each LSDB differs from the others. As a result, route flapping occurs. You can enable secure synchronization to solve this problem; however, it may delay the establishment of an OSPF adjacency.


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
3. Enable secure synchronization.
   
   
   ```
   [safe-sync enable](cmdqueryname=safe-sync+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```