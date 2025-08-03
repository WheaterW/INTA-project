Disabling IS-IS CPU Overload Control
====================================

IS-IS CPU overload control is enabled by default and can be disabled.

#### Context

By default, IS-IS CPU overload control is enabled. If a device's CPU is overloaded, each module takes necessary measures to control its own CPU usage accordingly. Upon receiving a CPU overload notification from the system, the IS-IS module controls the speeds of some internal computing processes and the establishment of neighbor relationships based on the CPU overload condition to enhance the resilience of IS-IS. In this case, new neighbor relationships cannot be established, and the established neighbor relationships are not affected.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis cpu-overload control disable**](cmdqueryname=isis+cpu-overload+control+disable)
   
   
   
   IS-IS CPU overload control is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To minimize the impact of CPU overload upon services, you are advised to keep IS-IS CPU overload control enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.