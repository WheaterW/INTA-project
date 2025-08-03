Configuring Optical Parameters
==============================

Optical parameters are configured in the WDM interface view to allow the WDM interfaces at both ends of an optical fiber to communicate at the physical layer.

#### Context

Optical parameters of WDM interfaces must be configured to allow the WDM interfaces at both ends of an optical fiber to communicate at the physical layer. Service parameters can be configured only after optical parameters are configured. Currently, optical parameters of WDM interfaces on the NE40E are FEC and TTI.

* FEC contained in the OTU overhead of the OTN frame is used for data error correction by using algorithms.
* TTI is a byte string in the overhead of an OTU and or an ODU. Like the J byte in the SDH segment overhead, the TTI identifies the source and destination stations to which each optical fiber is connected to prevent incorrect connection. If the received TTI differs from the expected value, a TIM alarm is generated.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**set transfer-mode otn**](cmdqueryname=set+transfer-mode+otn)
   
   
   
   The interface is configured to work in OTN mode.
4. Run [**optical-tx-power**](cmdqueryname=optical-tx-power) **target** *target-value*
   
   
   
   The attenuation value and optical power for an optical module is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**controller wdm**](cmdqueryname=controller+wdm) *interface-number*
   
   
   
   The interface view is displayed.
7. Run [**fec**](cmdqueryname=fec) { **standard** | **none** | **enhanced-i-4** | **enhanced-i-7** | **enhanced** | **lhaul-sd** | **lhaul-sd-pid** | **enhanced-pid** }
   
   
   
   The FEC mode is configured for the WDM interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Two interconnected WDM interfaces must have the same FEC configurations.
8. Run [**tti**](cmdqueryname=tti) { **otu** | **odu-pm** } { **expected** | **sent** } **64byte-mode** *value*
   
   
   
   The TTI is configured for the OTU or ODU.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value on the sending end must be the same as the expected value set on the peer end of an optical fiber.
9. Run [**otn**](cmdqueryname=otn) **sd-threshold** *sd-threshold*
   
   
   
   The alarm thresholds on attenuation of optical transmission signals are set.
10. (Optional) Run [**otn prefec-tca**](cmdqueryname=otn+prefec-tca) **trigger-threshold** *trigger-coefficient* *trigger-power* **trigger-interval** *trigger-time-interval* [ **recover-threshold** *recover-coefficient* *recover-power* ] [ **recover-interval** *recover-time-interval* ]
    
    
    
    Configure an alarm threshold and detection interval for FEC bit error ratio detection on an optical transport network (OTN).
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To configure an alarm threshold and detection interval for FEC bit error ratio detection on an OTN, run the otn prefec-tca command. By default, FEC bit error ratio detection is enabled. The default alarm thresholds and detection intervals are used. If the FEC bit error ratio exceeds a specified threshold, the device reports an FEC bit error ratio alarm to the NMS. When the FEC bit error ratio falls below a specified threshold, the device reports an FEC bit error ratio clear alarm to the NMS.
11. Run [**span**](cmdqueryname=span) *span-value*
    
    
    
    The span to estimate the OSNR of a line are set.
    
    When an optical amplifier (OA) resides between two connected OTN interfaces, run the [**span**](cmdqueryname=span) command to set a span based on the network situation, so that the non-linear OSNR of a line can be more accurately estimated to facilitate line adjustment.
12. Run [**mapping-path**](cmdqueryname=mapping-path) { **opu2-standard** | **opu2-non-standard** | **opu2e** }
    
    
    
    A mapping mode for client signals is configured.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * The **undo shutdown**, **loopback**, **clock**, and **ptp** command configurations have been cleared from the Ethernet interface that the WDM interface corresponds to.
    * Interfaces that have different mapping modes cannot communicate with each other. The **mapping-path** command can be run only on 10GE OTN subcards.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.