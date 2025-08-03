Outputting Information to a Remote Terminal
===========================================

Information can be output to a console for the query of users logging in to the device through the Virtual Type Terminal (VTY) or Telnet. This allows users to learn the operating status of the device.

#### Context

When a device is working, the system records the operating status of the device in real time and generates certain information. After the information management function is enabled, the information can be output to a remote terminal. This enables the administrator to monitor the device operation and diagnose network faults remotely.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, logs, traps, and debugging information are output to a remote terminal.



#### Procedure

1. Configure information to be output through channels.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**info-center enable**](cmdqueryname=info-center+enable)
      
      
      
      Information management is enabled to output information to a terminal or remote server.
   3. (Optional) Run [**info-center channel**](cmdqueryname=info-center+channel) *channel-number* **name** *channel-name*
      
      
      
      The information channel specified by *channel-number* is named *channel-name*.
   4. (Optional) Run [**info-center monitor channel**](cmdqueryname=info-center+monitor+channel) { *channel-number* | *channel-name* }
      
      
      
      The channel through which information is output to the remote terminal is configured.
   5. Run [**info-center source**](cmdqueryname=info-center+source) { *module-name* | **default** } **channel** { *channel-number* | *channel-name* } [ **log** { **state** { **off** | **on** } | **level** *log-level* } \* | **trap** { **state** { **off** | **on** } | **level** *trap-level* } \* | **debug** { **state** { **off** | **on** } | **level** *dbg-level* } \* ] \*
      
      
      
      Rules for outputting information through information channels are configured.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the user view.
2. The display function is enabled on a remote terminal.
   
   
   
   Information is displayed on the screen of the remote terminal only after this function is enabled.
   
   
   
   1. In the user view, run [**terminal monitor**](cmdqueryname=terminal+monitor)
      
      
      
      Displaying logs, traps, and debugging information on the remote terminal is enabled.
   2. In the user view, run [**terminal logging**](cmdqueryname=terminal+logging)
      
      
      
      Displaying logs on the remote terminal is enabled.
   3. (Optional) In the user view, run [**terminal echo synchronous**](cmdqueryname=terminal+echo+synchronous)
      
      
      
      Display debugging, log, or trap information synchronously on a terminal is enabled.
   4. In the user view, run [**terminal debugging**](cmdqueryname=terminal+debugging)
      
      
      
      Displaying debugging information on the remote terminal is enabled.
   5. In the user view, run [**terminal alarm**](cmdqueryname=terminal+alarm)
      
      
      
      Displaying traps on the remote terminal is enabled.