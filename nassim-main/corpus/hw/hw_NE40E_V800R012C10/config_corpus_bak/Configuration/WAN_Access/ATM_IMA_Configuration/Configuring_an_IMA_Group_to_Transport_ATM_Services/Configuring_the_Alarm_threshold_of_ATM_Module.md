Configuring the Alarm threshold of ATM Module
=============================================

After configuring the ATM module to report alarms to the NMS, you can monitor the alarm status of the ATM module on the NMS interface.

#### Procedure

1. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The view of the specified serial interface is displayed.
2. Run [**link-protocol**](cmdqueryname=link-protocol) **atm**
   
   
   
   ATM is configured as the link layer protocol of the serial interface.
3. Run [**trap-threshold**](cmdqueryname=trap-threshold) { **atmpw-lospkt-exc** | **atmpw-misorderpkt-exc** | **atmpw-unknowncell-exc** } **trigger-threshold** *trigger-threshold* **resume-threshold** *resume-threshold*
   
   
   
   The alarm generation and clearing thresholds for ATM service transport performance are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.