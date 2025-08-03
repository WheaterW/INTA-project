Monitoring the Usage of MAC Address Tables
==========================================

You can monitor MAC address table usage to ensure that the device runs stably, because a large number of MAC addresses are configured on or learned by the device.

#### Procedure

* Run the [**display mac-address-usage**](cmdqueryname=display+mac-address-usage) [ **slot** *slot-number* ] command to check the usage of a MAC address table.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  You can run the [**mac-address-usage threshold**](cmdqueryname=mac-address-usage+threshold) *threshold* [ **slot** *slot-number* ] command to set a usage threshold for a MAC address table as required.
  
  The [**display mac-address-usage**](cmdqueryname=display+mac-address-usage) and [**mac-address-usage threshold**](cmdqueryname=mac-address-usage+threshold) commands are supported only by the admin VS.