Manually Performing a Primary/Secondary Link Switchover in a Smart Link Group
=============================================================================

Manually Performing a Primary/Secondary Link Switchover in a Smart Link Group

#### Context

Once the original primary link recovers, data traffic is switched back after the WTR time expires. The default WTR time is 60 seconds, and the value ranges from 0 to 1200. To speed up link switchovers, you can manually switch data flows back to the original primary link.

The following conditions must be met for a successful primary/secondary link switchover:

* Both the master and slave interfaces exist and are in the Up state.
* The **[**smart-link**](cmdqueryname=smart-link)** { ****lock****| ****force****} command is not run in order to lock data flows.
* The Smart Link group has been enabled.

This command can be repeatedly run in the Smart Link group view. Each time the command is run, a link switchover is performed. Millisecond-level packet loss will occur during the switchover.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Perform a link switchover.
   
   
   ```
   [smart-link manual switch](cmdqueryname=smart-link+manual+switch)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```