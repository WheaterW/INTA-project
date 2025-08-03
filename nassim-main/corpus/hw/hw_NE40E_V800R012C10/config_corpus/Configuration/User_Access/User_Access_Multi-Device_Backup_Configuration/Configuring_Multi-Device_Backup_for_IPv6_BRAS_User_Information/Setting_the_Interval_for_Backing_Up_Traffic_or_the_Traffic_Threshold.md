Setting the Interval for Backing Up Traffic or the Traffic Threshold
====================================================================

If the traffic backup interval and traffic threshold are both set to 0, user traffic is not backed up.

#### Context

To ensure that user traffic can be backed up in real time, perform the following operations on devices that back up each other:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP view is displayed.
3. Run [**traffic backup**](cmdqueryname=traffic+backup) { **interval** *interval-value* [ **threshold** *threshold-value* ] | **threshold** *threshold-value* [ **interval** *interval-value* ] }
   
   
   
   A traffic backup interval or traffic threshold is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.