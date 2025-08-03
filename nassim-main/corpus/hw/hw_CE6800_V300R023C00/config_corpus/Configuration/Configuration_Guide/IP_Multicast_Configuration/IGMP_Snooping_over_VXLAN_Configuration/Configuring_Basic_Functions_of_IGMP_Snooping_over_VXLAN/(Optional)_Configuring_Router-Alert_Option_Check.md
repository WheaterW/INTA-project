(Optional) Configuring Router-Alert Option Check
================================================

(Optional) Configuring Router-Alert Option Check

#### Context

For compatibility purposes, a device does not check the Router-Alert option by default. When receiving an IGMP message, it sends the message to the upper-layer protocol for processing, regardless of whether the message carries the Router-Alert option in the IP header. To improve system performance, reduce costs, and improve protocol security, you can configure the Router-Alert option check function. After the function is configured, the device checks the Router-Alert option in each received IGMP message and discards those that do not contain this option.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure the device to check the Router-Alert option in received IGMP messages and discard those that do not contain this option.
   
   
   ```
   [igmp snooping require-router-alert](cmdqueryname=igmp+snooping+require-router-alert)
   ```
4. Configure the device to send IGMP messages carrying the Router-Alert option.
   
   
   ```
   [undo igmp snooping send-router-alert disable](cmdqueryname=undo+igmp+snooping+send-router-alert+disable)
   ```
   
   The IGMP snooping-enabled devices on the same network segment must have the same configuration of whether the Router-Alert option is carried in the IGMP messages to be sent. If the receiver end is configured to check the Router-Alert option, the IGMP messages sent by the transmit end must carry the Router-Alert option. By default, IGMP messages sent by a device to a BD carry the Router-Alert option.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```