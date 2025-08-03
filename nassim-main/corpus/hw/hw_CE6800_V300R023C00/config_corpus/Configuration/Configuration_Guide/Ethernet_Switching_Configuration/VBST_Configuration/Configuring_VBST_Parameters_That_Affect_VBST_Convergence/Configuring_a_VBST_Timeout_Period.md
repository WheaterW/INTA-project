Configuring a VBST Timeout Period
=================================

Configuring a VBST Timeout Period

#### Context

If a device on a VBST network does not receive BPDUs from an upstream device within the timeout period, it will determine the upstream device as faulty and recalculate the spanning tree.

In some cases, however, if the upstream device is not faulty, but busy processing services, the device may still fail to receive BPDUs within the timeout period. In this case, to prevent spanning tree recalculation, you can set a long timeout period on a stable network to avoid wasting network resources. The timeout period is calculated as follows: Timeout period = Hello Time x 3 x Timer Factor


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set a timeout period for the device to wait to receive BPDUs from the upstream device.
   
   
   ```
   [stp timer-factor](cmdqueryname=stp+timer-factor) factor
   ```
   
   By default, the timeout period is nine times the Hello Time timer.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** [ **global** ] command and check the Timer-factor field for the timeout period setting.