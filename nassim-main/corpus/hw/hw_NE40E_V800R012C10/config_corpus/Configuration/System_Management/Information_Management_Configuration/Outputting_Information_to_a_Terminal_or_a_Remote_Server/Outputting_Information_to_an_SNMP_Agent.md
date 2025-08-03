Outputting Information to an SNMP Agent
=======================================

This section describes how to output information to an SNMP agent. Users can learn the device operation by using an NMS to view information.

#### Context

When a system fault or an emergent event (such as the restart of a managed device) occurs, the device generates a log and also sends a trap through an SNMP agent to the NMS server. The information can be output to an SNMP agent, and can be further output to a network management terminal. Users can check the information on the network management terminal to monitor the device operation in real time or collect information about the device operation.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, traps are output to an SNMP agent.



#### Procedure

1. Configure information to be output through channels.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**info-center enable**](cmdqueryname=info-center+enable)
      
      
      
      Information management is enabled to output information to a terminal or remote server.
   3. (Optional) Run [**info-center channel**](cmdqueryname=info-center+channel) *channel-number* **name** *channel-name*
      
      
      
      The information channel specified by *channel-number* is named *channel-name*.
   4. (Optional) Run [**info-center snmp channel**](cmdqueryname=info-center+snmp+channel) { *channel-number* | *channel-name* }
      
      
      
      The channel through which information is output to an SNMP agent is configured.
   5. Run [**info-center source**](cmdqueryname=info-center+source) { *module-name* | **default** } **channel** { *channel-number* | *channel-name* } [ **log** { **state** { **off** | **on** } | **level** *log-level* } \* | **trap** { **state** { **off** | **on** } | **level** *trap-level* } \* | **debug** { **state** { **off** | **on** } | **level** *dbg-level* } \* ] \*
      
      
      
      Rules for outputting information through information channels are configured.
2. Run [**snmp-agent**](cmdqueryname=snmp-agent)
   
   
   
   The SNMP agent function is enabled.
   
   The SNMP agent can receive information normally only after the SNMP agent function is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details on how to configure the SNMP agent, see the chapter "SNMP Configuration" in the *Configuration Guide*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.