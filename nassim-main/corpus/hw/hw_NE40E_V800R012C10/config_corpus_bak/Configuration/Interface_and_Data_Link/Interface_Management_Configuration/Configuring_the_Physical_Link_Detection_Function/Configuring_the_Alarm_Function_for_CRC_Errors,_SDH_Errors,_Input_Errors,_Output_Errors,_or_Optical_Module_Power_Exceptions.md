Configuring the Alarm Function for CRC Errors, SDH Errors, Input Errors, Output Errors, or Optical Module Power Exceptions
==========================================================================================================================

This section describes how to configure the alarm function for CRC errors, SDH errors, input errors, output errors, or optical module power exceptions.

#### Context

If the alarm function for CRC errors, SDH errors, input errors, output errors, or optical module power exceptions is enabled on an interface, the system generates an alarm when the number of errors or exceptions exceeds or falls below the threshold set on the interface. If a large number of alarms are generated on links, the system will be busy processing them, which causes performance deterioration. To prevent this problem, properly configure the type of interface alarm, alarm thresholds, and detection interval.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snmp-agent trap enable port**](cmdqueryname=snmp-agent+trap+enable+port) { **crcexc-error** | **input-error** | **output-error** | **sdh-error-rising** | **optical-module-abnormal** }
   
   
   
   The alarm function is enabled on interfaces.
   
   
   
   The configuration takes effect on all physical interfaces supporting the alarm function.
   
   You can set a type of alarm as required.
   
   * **crcexc-error**: Enables the alarm function for CRC errors.
   * **sdh-error-rising**: Enables the alarm function for SDH errors.
   * **optical-module-abnormal**: Enables the alarm function for optical module power exceptions.
   
   In VS mode, this command is supported only by the admin VS.
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
4. Configure alarm thresholds and a detection interval.
   
   
   * Configure alarm thresholds for inbound and outbound bandwidth usage:
     + Run [**trap-threshold**](cmdqueryname=trap-threshold) { **input-rate** | **output-rate** } *bandwidth-in-use* [ **resume-rate** *resume-threshold* ]
       
       The inbound and outbound bandwidth usage threshold is set.
       
       To prevent alarms from being generated frequently, keep a large difference between *bandwidth-in-use* and *resume-threshold*.
     + Run [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) *interval*
       
       The traffic statistic collection interval is set for the interface, in seconds.
       
       The new interval takes effect after the original interval expires. If the interface is logical, traffic statistics about the interface are updated when the new interval takes effect for the second time. If the interface is physical, traffic statistics about the interface are updated immediately after the new interval takes effect.
       
       The traffic statistic collection interval set on an interface is effective only on the interface.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You can configure a global traffic statistic collection interval, which takes effect on all interfaces, including the interfaces on which no traffic statistic collection interval has been set. To configure a global traffic statistic collection interval, run the [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) *interval* command in the system view. The traffic statistic collection interval of an interface takes preference over a global traffic statistic collection interval.
   * Configure the CRC alarm function using either of the following methods:
     + Run [**trap-threshold crc-error**](cmdqueryname=trap-threshold+crc-error) *threshold* **interval-second** *interval* [ **shutdown** ]
       
       An alarm threshold and a detection interval are set for CRC errors.
     + Run [**trap-threshold crc-error**](cmdqueryname=trap-threshold+crc-error) **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval* [ **shutdown** ]
       
       The upper and lower alarm thresholds for CRC errors as well as the detection interval are set.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You can run the [**trap-threshold**](cmdqueryname=trap-threshold) **slot** *slot-id* **card** *card-id* **crc-error** **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval* command in the system view to configure global values for all interfaces on the specified subcard.
   * Configure the SDH alarm function using either of the following methods:
     + Run [**trap-threshold sdh-error**](cmdqueryname=trap-threshold+sdh-error) *threshold* **interval-second** *interval*
       
       An alarm threshold and a detection interval are set for SDH errors.
     + Run [**trap-threshold sdh-error**](cmdqueryname=trap-threshold+sdh-error) **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval*
       
       The upper and lower alarm thresholds for SDH errors as well as the detection interval are set.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You can run the [**trap-threshold**](cmdqueryname=trap-threshold) **slot** *slot-id* **card** *card-id* **sdh-error** **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval* command in the system view to configure global values for all interfaces on the specified subcard.
   * Configure the symbol alarm function.
     + Run [**trap-threshold symbol-error**](cmdqueryname=trap-threshold+symbol-error) **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval*
       
       The upper and lower alarm thresholds for symbol errors as well as the detection interval are set.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You can run the [**trap-threshold**](cmdqueryname=trap-threshold) **slot** *slot-id* **card** *card-id* **symbol-error** **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval* command in the system view to configure global values for all interfaces on the specified subcard.
   * Configure input/output alarm thresholds and a detection interval (for Ethernet interfaces and POS interfaces).
     + Run [**trap-threshold**](cmdqueryname=trap-threshold) { **input-error** | **output-error** } **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval*
       
       The upper and lower alarm thresholds for interface input or output errors are set.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You can run the [**trap-threshold**](cmdqueryname=trap-threshold) **slot** *slot-id* **card** *card-id* { **input-error** | **output-error** } **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval* command in the system view to configure global values for all interfaces on the specified subcard.
   * Configure an alarm threshold and a clear alarm threshold for the CRC error packet ratio:
     + Run [**trap-threshold crc-error**](cmdqueryname=trap-threshold+crc-error) **packet-error-ratio** **alarm-threshold** *alarm-coefficient-value* *alarm-power-value* [ **resume-threshold** *resume-coefficient-value* *resume-power-value* ] [ **trigger-lsp** | **trigger-section** ]
       
       An alarm threshold and a clear alarm threshold are configured for the CRC error packet ratio.
   * Configure parameters for the algorithm to calculate the CRC packet error ratio:
     + Run [**crc-error packet-error-ratio algorithm-parameter**](cmdqueryname=crc-error+packet-error-ratio+algorithm-parameter) *sample-window-factor* *child-window-max-number* *child-window-alarm-number* *child-window-resume-number*
       
       Parameters are configured for the algorithm to calculate the CRC packet error ratio.
     + Run [**crc-error packet-error-ratio algorithm-parameter realtime-factor**](cmdqueryname=crc-error+packet-error-ratio+algorithm-parameter+realtime-factor) *crcAlgTemplate*
       
       A template number is specified for factors affecting the algorithm used to calculate the CRC packet error ratio on the interface.
   * Configure CRC alarm threshold in percentages:
     + Run [**trap-threshold crc-error percent**](cmdqueryname=trap-threshold+crc-error+percent) *percent-val*
       
       The CRC alarm threshold in percentages is set.
5. (Optional) Run [**port-alarm down**](cmdqueryname=port-alarm+down) { **crc-error** | **sdh-error** | **symbol-error** | **input-error** | **output-error**}
   
   
   
   The interface is enabled to go Down when an error alarm is generated.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The Router also supports the [**port-alarm down**](cmdqueryname=port-alarm+down) **slot** *slot-id* **card** *card-id* { **crc-error** | **sdh-error** | **symbol-error** | **input-error** | **output-error** } command in the system view. This command takes effect on all interfaces on the subcard.
   * After the association function is enabled, you can run the [**port-alarm clear**](cmdqueryname=port-alarm+clear) { **crc-error** | **sdh-error** | **symbol-error** | **input-error** | **output-error** } command to manually clear the alarms generated on the physical interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.