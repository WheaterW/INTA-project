(Optional) Configuring OSPF to Restrict the Flooding of Update LSAs
===================================================================

(Optional) Configuring OSPF to Restrict the Flooding of Update LSAs

#### Context

If a local device has multiple neighbors or needs to flood a large number of update LSAs, an OSPF neighbor will receive a large number of Update LSAs within a short time. As a result, the established OSPF neighbor relationships may be terminated, because the neighbor may discard the Hello packets used to maintain neighbor relationships if it is busy processing the burst update LSAs. In this case, OSPF neighbors will exchange more packets to re-establish their neighbor relationships, exacerbating the problem of excessive packets.

To prevent this problem and ensure the stability of neighbor relationships, you can configure OSPF to restrict the flooding of update LSAs.

![](../public_sys-resources/note_3.0-en-us.png) 

The parameter settings of this command directly affect the flooding speed. If the parameters are improperly set, LSAs may not be synchronized in time, which affects the routing of the entire network. Therefore, this function is not recommended unless otherwise required.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Configure OSPF to restrict the flooding of update LSAs.
   
   
   ```
   [flooding-control](cmdqueryname=flooding-control) [ number number-value | timer-interval timer-interval-value ] *
   ```
   
   By default, OSPF is not configured to restrict the flooding of update LSAs.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```