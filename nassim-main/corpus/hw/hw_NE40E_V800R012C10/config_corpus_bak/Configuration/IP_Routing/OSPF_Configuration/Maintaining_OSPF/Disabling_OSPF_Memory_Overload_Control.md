Disabling OSPF Memory Overload Control
======================================

The OSPF memory overload control function is enabled by default. You can disable this function if necessary.

#### Context

By default, OSPF memory overload control is enabled. When the system memory is overloaded, each module needs to take necessary measures to control the memory usage. Upon receiving a memory overload notification from the system, the OSPF module no longer imports new routes and starts to control neighbor relationship establishment based on the memory overload condition to enhance OSPF resilience. In this case, new neighbor relationships cannot be established. For existing neighbor relationships, if they are in the Full state, they will be retained; if they are in a non-Full state, they are not reestablished until the memory recovers from overload.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ospf memory-overload control disable**](cmdqueryname=ospf+memory-overload+control+disable) command to disable OSPF memory overload control.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To reduce the impact of memory overload on services, you are advised not to disable OSPF memory overload control.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.