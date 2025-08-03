Configuring an STP/RSTP/MSTP Timeout Period
===========================================

Configuring an STP/RSTP/MSTP Timeout Period

#### Context

If a device on an STP, RSTP, or MSTP network does not receive BPDUs from an upstream device within the timeout period, the device will determine the upstream device as faulty and recalculate the spanning tree. The timeout period is calculated as follows: Timeout period = Hello Time x 3 x Timer Factor.

In some cases, however, if the upstream device is not faulty, but busy processing services, the device may still fail to receive BPDUs within the timeout period. In this case, to prevent spanning tree recalculation, you can set a long timeout period on a stable network to avoid wasting network resources.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the MSTP process view.
   
   
   
   Perform this step to set system parameters only when the MSTP process ID is not 0. Skip this step if the MSTP process ID is 0.
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Set a timeout period for the device to wait to receive BPDUs from the uplink device.
   
   
   ```
   [stp timer-factor](cmdqueryname=stp+timer-factor) factor
   ```
   
   By default, the timeout period is nine times the Hello Time timer.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp global**](cmdqueryname=display+stp+global) command and check the Timer-factor field for the timeout period setting.