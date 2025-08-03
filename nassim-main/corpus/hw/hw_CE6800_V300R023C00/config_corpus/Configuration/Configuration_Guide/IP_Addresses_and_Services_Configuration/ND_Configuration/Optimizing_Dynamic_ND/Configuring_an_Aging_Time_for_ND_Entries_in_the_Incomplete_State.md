Configuring an Aging Time for ND Entries in the Incomplete State
================================================================

Configuring an Aging Time for ND Entries in the Incomplete State

#### Context

By default, ND probe is performed for ND entries in the Incomplete state. The status of an ND entry changes to Reachable when a neighbor is reachable. The local device ages out an ND entry after failing to receive a response to a probe packet from the peer device within a specified number of probes. If the rate at which NS messages are sent is limited, ND entries in the Incomplete state cannot be effectively probed for a long time, occupying entry resources. To speed up entry aging and release entry resources, configure a short aging time for ND entries in the Incomplete state.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure an aging time for ND entries in the Incomplete state.
   
   
   ```
   [ipv6 nd neighbor-incomplete expire-time](cmdqueryname=ipv6+nd+neighbor-incomplete+expire-time) expire-time-value
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```