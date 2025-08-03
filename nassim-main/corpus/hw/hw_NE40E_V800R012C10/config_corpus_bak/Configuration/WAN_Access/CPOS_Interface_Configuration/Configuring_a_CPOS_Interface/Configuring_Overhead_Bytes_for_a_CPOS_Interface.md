Configuring Overhead Bytes for a CPOS Interface
===============================================

SDH provides a variety of overhead bytes. You can configure overhead bytes for CPOS interfaces to implement layered monitoring.

#### Context

The overhead bytes provided by SDH are used to implement layered monitoring. J1, J0, and C2 are used for interworking between devices of different countries, regions, or vendors.

* C2, the path signal label byte, is contained in the higher-order path overhead. C2 is used to indicate the multiplexing structure of a virtual container (VC) frame and the properties of payload.
* J0, the regenerator section trace byte, is contained in the section overhead to repeatedly send a section access point identifier, which is used to check the continued connection between two ports at the section layer.
* J1, the higher-order VC-N path trace byte, is used to repeatedly send a higher-order path access point identifier for checking the continued connection between two ports.
* J2, the lower-order VC-N path trace byte, is used to repeatedly send a lower-order path access point identifier for checking the continued connection between two ports.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command to enter the view of the specified CPOS interface.
3. Perform any of the following operations as required:
   
   
   * Run the [**flag j0**](cmdqueryname=flag+j0) **sdh** *j0-trace* command to configure the regenerator section trace byte J0 for the CPOS interface.
   * Run the [**flag j1**](cmdqueryname=flag+j1) { **1byte-mode** *1byte-value* | **16byte-mode** *16byte-value* | **64byte-mode** *64byte-value* } command to configure the path trace byte J1 for the CPOS interface.
   * Run the [**flag c2**](cmdqueryname=flag+c2) *c2* command to configure the path signal label byte C2 for the CPOS interface.
   * Run the [**flag v5 1byte-mode e1**](cmdqueryname=flag+v5+1byte-mode+e1) *e1-list* *v5* command to configure the lower-order path signal label byte V5 for the CPOS interface.
   * Run the [**flag j2 16byte-mode e1**](cmdqueryname=flag+j2+16byte-mode+e1) *e1-list* *j2* command to configure the lower-order path trace byte J2 for the CPOS interface.
   * Run the **flag space-padding disable** command to disable the function of automatically padding spaces at the end of the 16-byte J0 and J2 or the end of the 16-byte or 64-byte J1 configured on a CPOS interface.
4. (Optional) Run the [**flag j0-j1-j2 check disable**](cmdqueryname=flag+j0-j1-j2+check+disable) command to disable the reporting of J0, J1, and J2 check alarms.
   
   
   
   The sender and receiver must use the same overhead byte. Otherwise, an alarm is generated. In particular, when a large number of devices are migrated, many J0, J1, and J2 mismatch alarms are generated on the devices. In this scenario, these alarms are informational only. You can run this command to disable the alarm reporting function as required. After the migration is complete, run the [**undo flag j0-j1-j2 check disable**](cmdqueryname=undo+flag+j0-j1-j2+check+disable) command to enable this function again.
   
   The involved alarms are hwJ0TimAlarm, hwPtimAlarm, and hwLpTimVc12Alarm.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.