Configuring the STP/RSTP/MSTP Mode
==================================

Configuring the STP/RSTP/MSTP Mode

#### Context

The STP, RSTP, and MSTP modes are available. Select STP for devices on an STP-enabled ring network and RSTP for devices on an RSTP-enabled ring network.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to work in STP, RSTP, or MSTP mode.
   
   
   ```
   [stp mode](cmdqueryname=stp+mode) { stp | rstp | mstp }
   ```
   
   
   
   By default, a device works in MSTP mode.
   
   MSTP is compatible with STP and RSTP.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```