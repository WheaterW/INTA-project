Configuring the MSTP Mode
=========================

Before configuring basic Multiple Spanning Tree Protocol (MSTP) functions, you need to configure the working mode of a device to MSTP. MSTP is compatible with STP and Rapid Spanning Tree Protocol (RSTP).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp mode**](cmdqueryname=stp+mode) **mstp**
   
   
   
   The working mode of the device is configured as MSTP.
   
   
   
   STP and MSTP cannot recognize packets of each other. If an MSTP-enabled local interface is connected to an STP-enabled interface, the MSTP working mode of the local interface automatically changes to the STP working mode. This enables devices running STP and MSTP to communicate with each other.
   
   RSTP and MSTP can recognize packets of each other. If an MSTP-enabled local interface is connected to an RSTP-enabled interface, the local interface remains to work in MSTP mode.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.