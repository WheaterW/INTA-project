(Optional) Binding a Static Route Tag to the RBS
================================================

In a dual-device hot backup scenario, if IP addresses are allocated using a RADIUS server instead of an address pool, you need to bind a static route tag to the remote backup service (RBS) to switch traffic between the master and backup devices.

#### Context

In a dual-device hot backup scenario, if IP addresses are allocated using a RADIUS server instead of an address pool, you need to bind a static route tag to the RBS and specify a cost for the static route. If an NNI on the master device fails, the outbound interface of the static route can be directed to the protection tunnel to switch traffic to the backup device. This reduces the fault impact on user services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
   
   
   
   An RBS is created and the RBS view is displayed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**static-route if-match**](cmdqueryname=static-route+if-match) **null** *interface-number* **tag** *tag-num* [ **metric** *metric-num* ] [ **rui-slave** ]
   
   
   
   A static route tag is bound to the RBS, and a cost is specified for the static route.
   
   
   
   If **metric** *metric-num* is configured, the cost configured on the master
   device must be less than that configured on the backup device, so
   that the route on the master device is preferentially selected.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command must be run on both the master and backup devices.
   In addition, **rui-slave** must be configured
   on the backup device. Otherwise, traffic flaps between the two devices.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.