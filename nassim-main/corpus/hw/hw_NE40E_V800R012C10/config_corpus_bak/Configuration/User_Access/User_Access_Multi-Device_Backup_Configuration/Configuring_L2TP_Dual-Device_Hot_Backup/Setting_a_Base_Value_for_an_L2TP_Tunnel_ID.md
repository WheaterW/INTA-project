Setting a Base Value for an L2TP Tunnel ID
==========================================

To implement L2TP dual-device hot backup in load balancing mode, a base value must be set on either of the master and backup Routers to ensure unique tunnel IDs on the Routers.

#### Context

An L2TP tunnel ID with an index value starting with 1 is assigned to each router. In a dual-device hot backup scenario for traffic load balancing, tunnel information is backed up from the master Router to the backup Router, which may cause a tunnel ID conflict. To prevent the conflict, a base value can be specified for one Router for tunnel ID generation (Tunnel ID = Base value + Index value starting with 1). The other Router uses the default base value 0. This ensures unique tunnel IDs on the Routers that back up each other.

Perform the following steps on either of the master and backup Routers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set l2tp tunnel base-id**](cmdqueryname=set+l2tp+tunnel+base-id) *base-id*
   
   
   
   A base value is set for an L2TP tunnel ID.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a tunnel backed up from the master Router to the backup Router has the same tunnel ID as the local tunnel on the backup Router, the backup Router deletes the existing local tunnel information and accepts the received tunnel information.
   * The [**set l2tp tunnel base-id**](cmdqueryname=set+l2tp+tunnel+base-id) *base-id* command cannot be used on aRouter that already has a tunnel ID.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.