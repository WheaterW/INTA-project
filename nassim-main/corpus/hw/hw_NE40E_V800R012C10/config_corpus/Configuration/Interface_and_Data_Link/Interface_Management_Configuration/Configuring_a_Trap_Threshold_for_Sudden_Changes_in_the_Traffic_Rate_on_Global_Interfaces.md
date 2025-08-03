Configuring a Trap Threshold for Sudden Changes in the Traffic Rate on Global Interfaces
========================================================================================

You can configure a trap threshold for sudden changes in the traffic rate to adjust the frequency of triggering traps.

#### Usage Scenario

To detect sudden changes in the traffic rate, you can configure a trap threshold for them on interfaces. After the configuration is complete, the device reports a trap if the percentage of change in the traffic rate exceeds the trap threshold. To prevent the device from frequently reporting traps, do not set the trap threshold too low.

The formula for calculating the percentage of change in the traffic rate on interfaces is as follows:

Percentage of change in the traffic rate = Difference between the interface rates in the current and previous traffic statistics collection intervals/Interface rate in the previous traffic statistics collection interval

To configure a traffic statistics collection interval on an interface, run the [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) command. The default interval is 300 seconds.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set flow-change-ratio**](cmdqueryname=set+flow-change-ratio) { **input-threshold** | **output-threshold** } **upper-limit** **threshold**
   
   
   
   A trap threshold is configured for sudden changes in the traffic rate on interfaces.
   
   
   
   After this command is run, if you enable the trap function for sudden changes in the traffic rate (configured using the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) **port trap-name hwinputratechangeoverthresholdnotice** or [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) **port trap-name hwoutputratechangeoverthresholdnotice** command) and the percentage of change in the traffic rate exceeds the configured trap threshold, the following traps are generated:
   
   * PORT\_1.3.6.1.4.1.2011.5.25.157.2.219 hwInputRateChangeOverThresholdNotice
   * PORT\_1.3.6.1.4.1.2011.5.25.157.2.220hwOutputRateChangeOverThresholdNotice
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.