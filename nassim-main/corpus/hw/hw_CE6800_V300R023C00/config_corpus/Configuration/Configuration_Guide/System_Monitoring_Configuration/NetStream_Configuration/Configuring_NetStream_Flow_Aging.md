Configuring NetStream Flow Aging
================================

Configuring NetStream Flow Aging

#### Context

When a NetStream flow is aged out, the device sends the flow statistics in its cache to the NSC. You can configure the aging mode of NetStream flows.


#### Procedure

* Configure active flow aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the active flow aging time.
     
     
     ```
     [netstream timeout](cmdqueryname=netstream+timeout) { ip | ipv6 | vxlan inner-ip } active active-interval
     ```
     
     By default, the active flow aging time is 1800 seconds.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure inactive flow aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the inactive flow aging time.
     
     
     ```
     [netstream timeout](cmdqueryname=netstream+timeout) { ip | ipv6 | vxlan inner-ip } inactive inactive-interval
     ```
     
     By default, the inactive flow aging time is 15 seconds.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure FIN- and RST-based aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the aging of NetStream flows according to the FIN or RST flag in the TCP header.
     
     
     ```
     [netstream timeout](cmdqueryname=netstream+timeout) { ip | ipv6 | vxlan inner-ip } tcp-session
     ```
     
     By default, FIN- and RST-based aging of NetStream flows is disabled.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure forced aging.
  1. Configure the device to forcibly age out NetStream flows in the user view.
     
     
     ```
     [reset netstream cache](cmdqueryname=reset+netstream+cache) { ip | ipv6 | vxlan inner-ip } slot slot-id
     ```