Locking the System Configuration
================================

This section describes how to lock the system configuration when multiple users manage a device at the same time. This operation avoids the inconsistency between the controller and forwarder.

#### Context

Multiple users can access a device and manage it. A user can be a controller or another type of user. If the configuration of a forwarder is modified by a non-controller user, the configurations of the controller and forwarder may be inconsistent. The following steps can be used to specify the controller to lock the system configuration of a forwarder to avoid the inconsistency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**configuration exclusive by-user-name**](cmdqueryname=configuration+exclusive+by-user-name) *user-name*
   
   
   
   The system configuration is locked by a specified user.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**display configuration exclusive by-user-name**](cmdqueryname=display+configuration+exclusive+by-user-name) command to view lock information of the system configuration locked based on user name.