Disabling OSPFv3 CPU Overload Control
=====================================

The OSPFv3 CPU overload control function is enabled by default. You can disable this function if necessary.

#### Context

By default, OSPFv3 CPU overload control is enabled. If a device's CPU is overloaded, each module takes necessary measures to control its own CPU usage accordingly. Upon receiving a CPU overload notification from the system, the OSPFv3 module controls the speeds of some internal computing processes and the establishment of neighbor relationships based on the CPU overload condition to enhance the resilience of OSPFv3. In this case, new neighbor relationships cannot be established. For original neighbor relationships, if a neighbor relationship is in the Full state, it will be retained; if a neighbor relationship is in a non-Full state, establishment of the neighbor relationship is paused and can continue only after the CPU recovers from overload.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf cpu-overload control disable**](cmdqueryname=ospf+cpu-overload+control+disable)
   
   
   
   OSPFv3 CPU overload control is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To minimize the impact of CPU overload upon services, you are advised not to disable OSPFv3 CPU overload control.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.