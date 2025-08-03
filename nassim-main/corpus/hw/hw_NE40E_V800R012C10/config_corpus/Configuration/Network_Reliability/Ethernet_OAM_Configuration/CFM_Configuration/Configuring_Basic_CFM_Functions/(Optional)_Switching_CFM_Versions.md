(Optional) Switching CFM Versions
=================================

This section describes how to switch connectivity fault management (CFM) versions.

#### Context

You can perform the following steps to switch the CFM version between IEEE 802.1ag Draft 7 and IEEE Standard 802.1ag-2007.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm version**](cmdqueryname=cfm+version) { **draft7** | **standard** }
   
   
   
   CFM versions are switched.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Devices running different CFM versions cannot send CFM packets to each other. Therefore, the devices in a maintenance domain (MD) must run the same CFM version.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.