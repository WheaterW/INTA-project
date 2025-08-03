(Optional) Creating a Default MD
================================

This section describes how to create a default maintenance domain (MD).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm default md**](cmdqueryname=cfm+default+md) [ **level** *level* ]
   
   
   
   A default MD is created, and the default MD view is displayed.
   
   
   
   You can create only one default MD on each device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The default MD must have a higher level than all MDs to which maintenance association end points (MEPs) configured on the local device belong. In addition, the default MD must have the same level as a high-level MD. The default MD is used to transmit high-level continuity check messages (CCMs) and create maintenance association intermediate points (MIPs) to send linktrace reply (LTR) messages.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.