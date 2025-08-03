(Optional) Restricting the Flooding of OSPF Update LSAs
=======================================================

To maintain stable OSPF neighbor relationships, you can restrict the flooding of update LSAs on a local device, so that its neighbors will not discard Hello packets due to a great number of update LSAs.

#### Context

If a local device has a large number of neighbors or needs to flood a large number of update LSAs, neighbor routers will receive a large number of update packets within a short time. In this case, neighbor routers are busy with processing the burst update packets and discard the Hello packets that are used to maintain neighbor relationships. As a result, the established OSPF neighbor relationships will be terminated. Then, the neighbor routers will exchange more packets to re-establish the neighbor relationships, exacerbating the problem of excessive packets.

To prevent this problem and ensure the stability of neighbor relationships, you can configure OSPF to restrict the flooding of update LSAs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The parameter settings of this command directly affect the flooding speed. If the parameters are improperly set, LSAs may not be synchronized in time, which affects the routing of the entire network. Therefore, this function is not recommended unless otherwise required.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**flooding-control**](cmdqueryname=flooding-control) [ **number** *number-value* | **timer-interval** *timer-interval-value* ] \*
   
   
   
   OSPF is configured to restrict the flooding of update LSAs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.