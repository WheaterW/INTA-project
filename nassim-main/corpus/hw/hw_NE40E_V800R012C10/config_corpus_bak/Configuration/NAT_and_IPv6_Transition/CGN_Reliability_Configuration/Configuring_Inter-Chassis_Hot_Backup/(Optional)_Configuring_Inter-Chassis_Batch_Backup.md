(Optional) Configuring Inter-Chassis Batch Backup
=================================================

Configure inter-chassis batch backup between the master and backup devices to ensure their data consistency and normal user login after a master/backup device switchover.

#### Context

In CGN inter-chassis backup scenarios, if a fault occurs, a master/backup device switchover is triggered. However, if the address pools on the master and backup devices are inconsistent, users cannot go online after the switchover. To ensure data consistency between the master and backup devices and prevent user experience from being affected by network faults, configure inter-chassis batch backup between the master and backup devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**batch-backup service-type nat**](cmdqueryname=batch-backup+service-type+nat) **enable**
   
   
   
   The inter-chassis batch backup function is enabled.
   
   
   
   The batch backup function is enabled by default. If you need to enable this function again after it is disabled, perform this step.
3. Run [**batch-backup service-type nat**](cmdqueryname=batch-backup+service-type+nat) **timer-interval** *timer-interval*
   
   
   
   A batch backup interval is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.