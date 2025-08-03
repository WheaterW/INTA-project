Configuring a Traffic Behavior
==============================

If the routes between the interface where URPF check is performed and the source address of packets are symmetrical, you must perform strict URPF check. In other cases, you can perform loose URPF check.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is defined and its view is displayed.
   
   
   
   The traffic behavior specified by *behavior-name* cannot be a pre-defined one in the system. You can directly use the pre-defined traffic behaviors when defining traffic policies. For details about traffic behaviors, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - QoS*.
3. Run [**ip urpf**](cmdqueryname=ip+urpf) { **loose** | **strict** } [ **allow-default** ]
   
   
   
   URPF is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.