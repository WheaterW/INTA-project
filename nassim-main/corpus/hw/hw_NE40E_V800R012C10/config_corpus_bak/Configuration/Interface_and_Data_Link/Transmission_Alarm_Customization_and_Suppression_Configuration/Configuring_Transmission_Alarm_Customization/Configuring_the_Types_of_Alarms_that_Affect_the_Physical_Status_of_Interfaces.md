Configuring the Types of Alarms that Affect the Physical Status of Interfaces
=============================================================================

In the scenario where a router is connected to a transmission device, if the network is unstable, a large number of burr alarms may be generated. As a result, the physical status of interfaces will frequently change between up and down. To specify the alarms that can trigger the physical status of an interface to go down, you can configure transmission alarm customization.

#### Context

Transmission alarm customization can be used to control the impact of transmission alarms on the physical interface status. Perform the following steps globally or on the interface connected to a transmission device:

Transmission alarm filtering intervals can be configured globally or on an interface. The global configuration takes effect on interfaces supporting the function. The relationship is as follows:

* If the alarm customization is configured globally and a non-default alarm customization configuration exists on an interface, the configuration on the interface preferentially takes effect.
* If the alarm customization is configured globally but is not configured on an interface, the global configuration takes effect on the interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, global transmission alarm customization is supported only by the admin VS.



#### Procedure

* Configure transmission alarm customization globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **wan** | **pos** } { **auais** | **b1tca** | **b2tca** | **b3tca** | **lais** | **lcd** | **lof** | **lom** | **lop** | **los** | **lrdi** | **lrei** | **oof** | **pais** | **pplm** | **prdi** | **prei** | **puneq** | **rdool** | **rrool** | **sdbere** | **sfbere** | **trool** } \*
     
     
     
     The types of transmission alarms whose generation causes 10GE WAN and POS interfaces to go down physically are customized globally.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure transmission alarm customization on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* or [**controller**](cmdqueryname=controller) *interface-type* *interface-number*
     
     
     
     The corresponding interface view is displayed.
  3. Run the following commands as required:
     
     
     + To customize the types of transmission alarms whose generation causes the POS or 10GE WAN interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **auais** | **b1tca** | **b2tca** | **b3tca** | **lais** | **lcd** | **lof** | **lom** | **lop** | **los** | **lrdi** | **lrei** | **oof** | **pais** | **pplm** | **prdi** | **prei** | **puneq** | **rdool** | **rrool** | **sdbere** | **sfbere** | **trool** } \* command.
     + To customize the types of transmission alarms whose generation causes the WDM interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **odu-ais** | **odu-lck** | **odu-oci** | **otu-ais** | **otu-lom** | **otu-sd-ber** | **otu-sf-ber** | **pm-bdi** | **pm-tim** | **r-lof** | **r-los** | **r-oof** | **sm-bdi** | **sm-iae** | **sm-tim** | **prefec-tca** | **local-fault** | **remote-fault** } \* command.
     + To customize the types of transmission alarms whose generation causes the CPOS interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **los** | **lof** | **oof** | **lais** | **lrdi** | **lrei** | **b1tca** | **b2tca** | **b3tca** | **sdbere** | **sfbere** | **rrool** | **pais** | **auais** | **prdi** | **prei** | **lop** | **pplm** | **puneq** | **lom** } \* command.
     + To customize the types of transmission alarms whose generation causes the ATM interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **los** | **lof** | **oof** | **lais** | **lrdi** | **lrei** | **b1tca** | **b2tca** | **b3tca** | **sdbere** | **sfbere** | **rrool** | **pais** | **auais** | **prdi** | **prei** | **lop** | **pplm** | **puneq** | **lom** } \* command.
     + To customize the types of transmission alarms whose generation causes the E1 interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **lof** | **los** | **pais** | **prdi** } \* command.
     + To customize the types of transmission alarms whose generation causes the E3 interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **lof** | **los** | **pais** | **prdi** } \* command.
     + To customize the types of transmission alarms whose generation causes the trunk serial interface or serial interface to go down physically, run the [**transmission-alarm down**](cmdqueryname=transmission-alarm+down) { **pais** | **prdi** | **oof** } \* command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Not all interfaces support the preceding alarms because the alarm types supported may vary with subcards. If you attempt to customize an alarm type that is not supported by an interface for the interface, the customization fails, and a message is displayed, telling you which alarm types are not supported by this interface.
     + WLNK alarms can be viewed only and cannot be customized. The WLNK alarms are always enabled, and their generation causes interfaces to go down physically. To view the status and statistics on WLNK alarms, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) command.
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     By default, the LAIS, LOF, and LOS alarms can change interface status. If these alarms are disabled, forwarding of service data may be adversely affected. Therefore, you are advised to keep these alarms enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.