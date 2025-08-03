Configuring the STP/RSTP Mode
=============================

Before configuring basic STP/Rapid Spanning Tree Protocol (RSTP) functions, you need to configure the working mode of a device to STP/RSTP. RSTP is compatible with STP.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp mode**](cmdqueryname=stp+mode) { **mstp** | **stp** | **rstp** }
   
   
   
   The working mode of the device is configured as STP/RSTP.
   
   
   
   On a ring network running only STP, the working mode of a device is configured as STP; on a ring network running RSTP, the working mode of a device is configured as RSTP. In other cases, the working mode of a device is configured as MSTP by default.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.