SOC Configuration Method and Procedure
======================================

SOC Configuration Method and Procedure

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**soc**](cmdqueryname=soc)
3. (Optional) Run [**attack-defend enable**](cmdqueryname=attack-defend+enable)
   
   
   
   Attack defense is enabled.
   
   If the SOC determines that an attack event has occurred, enable attack defense.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. (Optional) Run the [**display soc attack-defend statistics**](cmdqueryname=display+soc+attack-defend+statistics) **slot** *slot-id* **port-vlan-car** command to check statistics about the packets that pass through or are discarded by interfaces being attacked on the board in a specified slot.
   
   
   
   After attack defense is enabled and the NE40E is being attacked, you can run this command.
6. Configure thresholds for determining attack events.
   * To configure the threshold for determining the location of an attack event, run the [**attack-trace location-type**](cmdqueryname=attack-trace+location-type) { **interface** | **qinq** | **source-ip** | **source-mac** | **sub-interface** | **vlan** } **threshold** *threshold-value* command.
   * To configure the threshold for determining the probability of an attack event, run the [**attack-trace probability**](cmdqueryname=attack-trace+probability) { **top5-user** | **top5-source-mac** | **top5-source-ip** | **broadcast-flood** | **app-error-percent** } { **determined** | **notification** | **suspicion** } *threshold-value* command.
   * To configure the threshold for determining the cause of an attack event, run the [**attack-trace reason**](cmdqueryname=attack-trace+reason) { **app-packet** | **broadcast-flood** | **change-source-packet** } **percentage** *percentage-value* command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Security Hardening Result

1. Check attack event reports.
   1. Run the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command to check brief information about attack event reports.
   2. Run the ****display soc attack-event**** [ { **slot** *slot-id* [ **event-number** *event-number* ] [ **verbose** ] | **event-number** *event-number* [ **verbose** ] } ] command to check the attack event report about the board in a specified slot. The slot is identified by the **Location** field in the command output. To check detailed information, specify the **verbose** parameter.
   3. Run the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) **event-number** *event-number* [ **verbose** ] command to check information about the specified attack event report. The specified attack event is identified by checking the **Seq.** field in the attack event summary or information about attack events on the board in a specified slot.
2. Check historical statistics.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The *slot-id* and *protocol-name* parameters in the following commands correspond to the *slot-id* parameter in the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command and the **Reasons** parameter in the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command output, respectively.
   
   Check CPCAR statistics.
   
   1. Run the [**display soc attack-detect statistics car**](cmdqueryname=display+soc+attack-detect+statistics+car) **slot** *slot-id* **protocol** *protocol-name* command to check all CPCAR statistics monitored by the SOC. Identify **CarName** of the CPCAR with the highest packet loss rate or the largest number of lost packets. CAR is a traffic policing instance. CPCAR functions for packets to be sent to the CPU.
   2. Run the [**display soc attack-detect statistics car**](cmdqueryname=display+soc+attack-detect+statistics+car) **slot** *slot-id* **protocol** *protocol-name* [ *cpcar-name* **history** { **15-minute** | **60-minutes** | **72-hour** } ] command to check the packet loss rate of the protocol packets identified by *cpcar-name* within a specified period.
   3. Run the [**display soc attack-detect cpu-usage**](cmdqueryname=display+soc+attack-detect+cpu-usage) **slot** *slot-id* **history** { **15-minutes** | **60-minutes** | **72-hours** } command to check the CPU usage within a specified period. If the CPU usage and packet loss rate within a specified period have similar tendencies, the CPU overload is caused by the protocol packets identified by *cpcar-name*.Check protocol statistics.
   1. Run the [**display soc attack-detect statistics application**](cmdqueryname=display+soc+attack-detect+statistics+application) **slot** *slot-id* command to check statistics about the protocol packets and sessions on the board in a specified slot. Identify the protocol module that has the largest percentage of the number of invalid packets or sessions to the total number of packets or sessions. This protocol module can be considered to have the poorest security.
   2. Run the [**display soc attack-detect statistics application**](cmdqueryname=display+soc+attack-detect+statistics+application) **slot** *slot-id* **protocol** *protocol-name* **history** { **15-minute** | **60-minutes** | **72-hour** } command to check statistics about the protocol packets and sessions and the average CPU usage within the last 15 minutes, 1 hour, or 72 hours. If the CPU usage is high while the percentage of the number of invalid packets or sessions to the total number of packets or sessions is high, attacks to the protocol module cause the CPU overload. If you cannot identify the problem by querying the average CPU usage, run the following command to check detailed information about the CPU usage within the specified period.
   3. (Optional) Run the [**display soc attack-detect cpu-usage**](cmdqueryname=display+soc+attack-detect+cpu-usage) **slot** *slot-id* **history** { **15-minutes** | **60-minutes** | **72-hours** } command to check detailed information about the CPU usage within a specified period.