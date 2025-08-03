(Optional) Configuring Attack Source Tracing Parameters
=======================================================

If attack event reports present incorrect or missing decisions on attack events, adjust attack source tracing parameters to allow attack source tracing to function precisely.

#### Context

As network configurations and traffic characteristics vary, the default attack source tracing thresholds may cause incorrect or missing decisions on attack events. You can adjust the attack source tracing parameters based on actual conditions. If an object under attack fails to be located, the attack source tracing thresholds are set high and need to be lowered. If an object not under attack is identified as being attacked, the attack source tracing threshold is set low and needs to be increased.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Each attack source tracing threshold has its default value. Adjust the thresholds based on your networking environment by referring to the default values and value ranges provided in the command reference. It is recommended that you adjust attack source tracing thresholds with assistance from Huawei engineers.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**soc**](cmdqueryname=soc)
   
   
   
   The SOC view is displayed.
3. Configure thresholds for determining attack events.
   * To configure the threshold for determining the location of an attack event, run the [**attack-trace location-type**](cmdqueryname=attack-trace+location-type) { **interface** | **qinq** | **source-ip** | **source-mac** | **sub-interface** | **vlan** | **vni** } **threshold** *threshold-value* command.
   * To configure the threshold for determining the probability of an attack event, run the [**attack-trace probability**](cmdqueryname=attack-trace+probability) { **top5-user** | **top5-source-mac** | **top5-source-ip** | **broadcast-flood** | **app-error-percent** } { **determined** | **notification** | **suspicion** } *threshold-value* command.
   * To configure the threshold for determining the cause of an attack event, run the **attack-trace reason** { **broadcast-flood** **percentage** *percentage-value1* | **change-source-packet** **percentage** *percentage-value2* | **app-packet** **percentage** *percentage-value3* } command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.