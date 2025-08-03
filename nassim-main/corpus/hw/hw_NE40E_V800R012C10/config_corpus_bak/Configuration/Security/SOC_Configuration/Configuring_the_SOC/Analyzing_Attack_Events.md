Analyzing Attack Events
=======================

The SOC determines whether an attack event has occurred by analyzing attack event reports and statistics. If attack defense is enabled, you can also check packet loss statistics of the interface under attack.

#### Context

If an exception occurs or an attack event alarm is generated on the NE40E, perform the following procedures to determine whether an attack event has occurred:

1. Check attack event reports and identify the attack event to be analyzed.
2. Check the **Location** and **Reasons** fields in attack event reports to find out the slot ID and protocol of the attack event and check the historical statistics. Historical statistics include the CPCAR statistics and protocol statistics. Determine whether the attack event is caused by protocol packets sent to the CPU or invalid packets or sessions on a protocol module.
3. After the attack event is determined, enable attack defense. Then the NE40E uses the configured attack defense policies to defend against subsequent attack packets. You can also check packet loss statistics of the interface under attack.

Perform the following steps in any view.


#### Procedure

1. Check attack event reports.
   1. Run the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command to check a summary of attack events.
   2. Run the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) [ { **slot** *slot-id* [ **event-number** *event-number* ] [ **verbose** ] | **event-number** *event-number* [ **verbose** ] } ] command to check information about attack events on the board in a specified slot.
      
      
      
      The specified slot is identified by checking the **Location** field in the attack event summary. Detailed information about attack events is displayed if **verbose** is configured.
2. Check historical statistics.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the following commands, *slot-id* must be the same as the *slot-id* specified in the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command, and *protocol-name* must be the same as the **Reasons** field value in the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) command output.
   
   
   
   Check CPCAR statistics.
   
   
   
   1. Run the [**display soc attack-detect statistics car**](cmdqueryname=display+soc+attack-detect+statistics+car) **slot** *slot-id* **protocol** *protocol-name* command to check all CPCAR statistics monitored by the SOC. Identify **CarName** of the CPCAR with the highest packet loss rate or the largest number of lost packets.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      CAR is a traffic policing instance. CPCAR functions for packets to be sent to the CPU.
   2. Run the [**display soc attack-detect statistics car**](cmdqueryname=display+soc+attack-detect+statistics+car) **slot** *slot-id* **protocol** *protocol-name* [ *cpcar-name* **history** { **15-minutes** | **60-minutes** | **72-hours** } ] command to check the packet loss rate of the protocol packets identified by *cpcar-name* within a specified period.
   3. Run the [**display soc attack-detect cpu-usage**](cmdqueryname=display+soc+attack-detect+cpu-usage) **slot** *slot-id* **history** { **15-minutes** | **60-minutes** | **72-hours** } command to check the CPU usage within a specified period. If the CPU usage and packet loss rate within a specified period have similar tendencies, the CPU overload is caused by the protocol packets identified by *cpcar-name*.
   
   
   
   Check protocol statistics.
   
   
   
   1. Run the [**display soc attack-detect statistics application**](cmdqueryname=display+soc+attack-detect+statistics+application) **slot** *slot-id* command to check statistics about the protocol packets and sessions on the board in a specified slot. Identify the protocol module that has the largest percentage of the number of invalid packets or sessions to the total number of packets or sessions. This protocol module can be considered to have the poorest security.
   2. Run the [**display soc attack-detect statistics application**](cmdqueryname=display+soc+attack-detect+statistics+application) **slot** *slot-id* **protocol** *protocol-name* **history** { **15-minutes** | **60-minutes** | **72-hours** } command to check statistics about the protocol packets and sessions and the average CPU usage within the last 15 minutes, 1 hour, or 72 hours. If the CPU usage is high while the percentage of the number of invalid packets or sessions to the total number of packets or sessions is high, attacks to the protocol module cause the CPU overload. If you cannot identify the problem by querying the average CPU usage, run the following command to check detailed information about the CPU usage within the specified period.
   3. (Optional) Run the [**display soc attack-detect cpu-usage**](cmdqueryname=display+soc+attack-detect+cpu-usage) **slot** *slot-id* **history** { **15-minutes** | **60-minutes** | **72-hours** } command to check detailed information about the CPU usage within a specified period.
3. (Optional) Run the [**display soc attack-defend statistics**](cmdqueryname=display+soc+attack-defend+statistics) **slot** *slot-id* **port-vlan-car** command to check statistics about the packets that pass through or are discarded by interfaces being attacked on the board in a specified slot.
   
   
   
   After attack defense is enabled and the NE40E is being attacked, you can run this command.