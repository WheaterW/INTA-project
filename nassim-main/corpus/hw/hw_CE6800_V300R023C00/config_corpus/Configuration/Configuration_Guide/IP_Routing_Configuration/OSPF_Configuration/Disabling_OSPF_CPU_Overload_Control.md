Disabling OSPF CPU Overload Control
===================================

Disabling OSPF CPU Overload Control

#### Context

By default, OSPF CPU overload control is enabled. If a device's CPU is overloaded, each module takes necessary measures to control its own CPU usage accordingly. Upon receiving a CPU overload notification from the system, the OSPF module controls the speeds of some internal computing processes and the establishment of neighbor relationships based on the CPU overload condition to enhance the resilience of OSPF. In this case, new neighbor relationships cannot be established. For original neighbor relationships, if a neighbor relationship is in the Full state, it will be retained; if a neighbor relationship is in a non-Full state, establishment of the neighbor relationship is paused and can continue only after the CPU recovers from overload.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable OSPF CPU overload control.
   
   
   ```
   [ospf cpu-overload control disable](cmdqueryname=ospf+cpu-overload+control+disable)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   To minimize the impact of CPU overload upon services, you are advised not to disable OSPF CPU overload control.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```