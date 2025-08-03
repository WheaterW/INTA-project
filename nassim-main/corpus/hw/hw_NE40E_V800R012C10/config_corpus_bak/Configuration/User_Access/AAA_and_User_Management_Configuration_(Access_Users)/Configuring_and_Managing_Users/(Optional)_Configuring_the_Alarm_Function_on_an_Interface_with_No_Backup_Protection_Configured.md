(Optional) Configuring the Alarm Function on an Interface with No Backup Protection Configured
==============================================================================================

This section describes how to configure the backup detection interval, number of detections, and minor and major alarm thresholds for the number of users on an interface with no backup protection configured.

#### Context

The Router detects the number of users on interfaces at configured intervals. If backup protection is not configured on any of the following interfaces, a large number of users may fail to go online in case of a board fault:

* Physical interfaces that perform dual-device hot backup, including sub-interfaces
* Intra-board Eth-Trunk interfaces, including sub-interfaces
* Interfaces on which access response delay based on odd or even MAC addresses is configured but load imbalance occurs (for example, the access response delay function fails to take effect due to an interface fault)

In this case, you need to configure the alarm function to prevent impact on user services.

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**access backup-check**](cmdqueryname=access+backup-check) **detect-interval** *detect-interval* **detect-count** *detect-count* **fail-count** *fail-count*
   
   
   
   The interface backup detection interval and number of detections are configured.
4. Run [**access backup-check interface-type**](cmdqueryname=access+backup-check+interface-type) *interface-type* **minor-trap-usernum** *minor-trap-usernum* **major-trap-usernum** *major-trap-usernum*
   
   
   
   The minor and major alarm thresholds for the number of users on the interface with no backup protection configured are set for interface backup detection.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.