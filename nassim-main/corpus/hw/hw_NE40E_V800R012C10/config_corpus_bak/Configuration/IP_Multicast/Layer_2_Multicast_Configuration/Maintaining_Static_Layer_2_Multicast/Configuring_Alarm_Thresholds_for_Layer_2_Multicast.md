Configuring Alarm Thresholds for Layer 2 Multicast
==================================================

This section describes how to configure alarm thresholds for Layer 2 multicast.

#### Context

To configure alarm thresholds for the total number of global entries in all VSIs of Layer 2 multicast, the total number of listened users on each board, and the total number of users in each multicast group, run the [**l2-multicast all-vsi limit threshold-alarm**](cmdqueryname=l2-multicast+all-vsi+limit+threshold-alarm) command. The default alarm trigger and clear thresholds are 75% and 70% for all VSIs of Layer 2 multicast, respectively.


#### Procedure

* Configure alarm thresholds for the total number of global entries in all VSIs of Layer 2 multicast.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2-multicast all-vsi global-entry limit threshold-alarm upper-limit**](cmdqueryname=l2-multicast+all-vsi+global-entry+limit+threshold-alarm+upper-limit) *upper-limit-value* **lower-limit** *lower-limit-value*
     
     
     
     Alarm thresholds are configured for the total number of global entries in all VSIs of Layer 2 multicast.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure alarm thresholds for the total number of listened users on each board of Layer 2 multicast.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2-multicast all-vsi listened-user-per-group limit threshold-alarm upper-limit**](cmdqueryname=l2-multicast+all-vsi+listened-user-per-group+limit+threshold-alarm+upper-limit) *upper-limit-value* **lower-limit** *lower-limit-value*
     
     
     
     Alarm thresholds are configured for the total number of listened users on each board of Layer 2 multicast.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure alarm thresholds for the total number of listened users in each multicast group of Layer 2 multicast.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2-multicast all-vsi listened-user-per-slot limit threshold-alarm upper-limit**](cmdqueryname=l2-multicast+all-vsi+listened-user-per-slot+limit+threshold-alarm+upper-limit) *upper-limit-value* **lower-limit** *lower-limit-value*
     
     
     
     Alarm thresholds are configured for the total number of listened users in each multicast group of Layer 2 multicast.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.