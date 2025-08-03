(Optional) Configuring Parameters for Automatic Clock Source Selection
======================================================================

(Optional)_Configuring_Parameters_for_Automatic_Clock_Source_Selection

#### Context

When the NE40E works in automatic clock source selection mode, the configurable parameters include:

* SSM level mapped to the clock source with an SSM level of **unk**
* Maximum output SSM level of clock signals
* Reversion mode of the clock source selection algorithm
* Holdoff time after clock source signals are lost
* Wait to restore (WTR) time for a status change after the clock source is restored

You can configure the function or parameters to improve the synchronization quality of a clock synchronization network and keep stable clock signals.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**clock board-freq-switch enable**](cmdqueryname=clock+board-freq-switch+enable) command to enable frequency deviation-triggered clock source switching.
   
   
   
   After this function is enabled, if the system detects that the frequency deviation of the clock source is abnormal, it notifies the interface board where the clock source resides, triggering the interface board to select the optimal clock source for use.
3. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
4. Run the [**clock freq-deviation recover**](cmdqueryname=clock+freq-deviation+recover) command to enable frequency deviation status recovery for clock sources.
   
   
   
   A clock source can participate in reference clock source selection only when its frequency deviation status is normal.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In scenarios where frequency deviation detection and frequency deviation-triggered clock source switching are both enabled, if the frequency deviation of a clock source is detected to be abnormal, then the clock source frequency deviation status is set to be abnormal. When selecting the reference clock source, the interface board excludes this clock source from the candidate clock source list. After determining that the frequency deviation of the clock source has recovered, you can run this command to recover its frequency deviation status, so that the clock source can participate in reference clock source selection again.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run the [**clock map unk**](cmdqueryname=clock+map+unk) { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **prtc** | **eprtc** | **esec** | **eprc** } command to map an SSM level to the clock source with an SSM level of **unk**.
   
   
   
   **unk** indicates that the clock source has an unknown SSM level. The clock source with an SSM level of **unk** cannot participate in clock source selection. To enable this type of clock source to participate in clock source selection, map a valid SSM level to it.
7. Run the [**clock**](cmdqueryname=clock) **max-out-ssm** { **prc** | **sec** | **ssua** | **ssub** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure the maximum output SSM level for clock signals.
8. Run the [**clock switch**](cmdqueryname=clock+switch) { **revertive** | **non-revertive** } command to configure a reversion mode for the clock source selection algorithm.
   
   
   
   The NE40E supports the following reversion modes:
   
   * Revertive mode: If the optimal clock source is faulty, the system uses the clock source selection algorithm to select the second optimal clock source. If the optimal clock source is restored, the system automatically retraces it.
   * Non-revertive mode: If the optimal clock source is faulty, the system uses the clock source selection algorithm to select the second optimal clock source. If the optimal clock source is restored, the system continues to trace the second optimal clock source. If there is no the second optimal clock source to select, the system selects the optimal clock source.
9. Run the [**clock source-lost holdoff-time**](cmdqueryname=clock+source-lost+holdoff-time) **holdoff-time-value** command to configure a holdoff time after clock source signals are lost.
   
   
   
   When clock source signals are lost, the system reports status changes only after a holdoff time to instruct the clock source selection algorithm to reselect a clock source. This processing mechanism prevents the clock source selection algorithm from frequently reselecting a clock source when clock source signals are lost for a short time.
10. Run the [**clock wtr**](cmdqueryname=clock+wtr) *wtr-time* command to configure a WTR time for a status change after the clock source is restored.
    
    
    
    You can configure an appropriate WTR time to minimize the impact of frequent clock source status changes on clock source selection. You are advised not to set the WTR time to 0.
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.