(Optional) Configuring a Delay for Link Switchovers in a Smart Link Group
=========================================================================

(Optional) Configuring a Delay for Link Switchovers in a Smart Link Group

#### Context

Intermittent link disconnection can affect packet forwarding and system performance as Smart Link switchovers are performed. To address this problem, you can configure a delay for link switchovers in a Smart Link group. When a member interface of a Smart Link group alternates between up and down, the Smart Link group will not perform a link switchover immediately. Instead, it will wait for the delay to expire and then performs the switchover if the interface is still down. This configuration suppresses link switchovers due to intermittent link disconnections.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Configure a delay for link switchovers in the Smart Link group.
   
   
   ```
   [smart-link hold-time](cmdqueryname=smart-link+hold-time) hold-time
   ```
   
   By default, the delay is 0s. That is, a switchover is performed immediately.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```