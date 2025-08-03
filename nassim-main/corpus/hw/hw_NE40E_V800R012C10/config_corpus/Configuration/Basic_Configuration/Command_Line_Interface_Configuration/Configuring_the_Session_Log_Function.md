Configuring the Session Log Function
====================================

By default, the global session log function is disabled, and the session log function of a single connection is enabled. You can perform the following steps to configure the session log function.

#### Context

The global session log function is disabled by default. You can enable the global session log function if you need to save the input, device screen output, and the time when the device executes commands to the **sessionlog** folder in the root directory.

The session log function of a single connection is enabled by default. After the global session log function is enabled, information such as the input and screen output of all connections on the device is recorded in the log file. If session logs do not need to be generated for some connections, you can run the [**terminal session-log disable**](cmdqueryname=terminal+session-log+disable) command to disable the session log function for these connections.


#### Procedure

* Enable the global session log function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**undo info-center session log disable**](cmdqueryname=undo+info-center+session+log+disable)
     
     
     
     The global session log function is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable the session log function for the current connection.
  
  
  
  Run [**display info-center session log status**](cmdqueryname=display+info-center+session+log+status)
  
  The status of the global session log function and the status of the session log function of all online connections are displayed.
  
  + If the global session log function is enabled, perform the following steps:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**terminal session-log disable**](cmdqueryname=terminal+session-log+disable) command to disable the session log function of the current connection.
    3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + If the global session log function is disabled, no further action is required.

#### Checking the Configurations

Run the [**display info-center session log status**](cmdqueryname=display+info-center+session+log+status) command to view the status of the global session log function and the session log function of all online connections.