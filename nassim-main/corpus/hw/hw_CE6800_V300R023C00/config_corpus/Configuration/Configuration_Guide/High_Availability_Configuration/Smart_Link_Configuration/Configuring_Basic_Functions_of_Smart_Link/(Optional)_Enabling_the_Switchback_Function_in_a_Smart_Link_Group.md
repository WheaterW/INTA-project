(Optional) Enabling the Switchback Function in a Smart Link Group
=================================================================

(Optional) Enabling the Switchback Function in a Smart Link Group

#### Context

When the primary link in a Smart Link group fails, traffic is automatically switched to the secondary link. After the fault is rectified, the original primary link remains blocked to ensure that traffic transmission is stable. Traffic transmission can be resumed on the original primary link through either of the following methods:

* Enable the switchback function for the Smart Link group. Traffic will be automatically switched back to the original primary link when the WTR timer expires.
* Switch traffic to the primary link using the [**smart-link manual switch**](cmdqueryname=smart-link+manual+switch) command.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  + Traffic can be switched between links in a Smart Link group only when both member interfaces are in the Up state.
  + The switchback function must be configured before enabling the Smart Link group. If the Smart Link group has been enabled, disable it before configuring the switchback function.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Enable the switchback function in the Smart Link group.
   
   
   ```
   [restore enable](cmdqueryname=restore+enable)
   ```
   
   The switchback function in a Smart Link group is disabled by default.
4. Configure the WTR time for the Smart Link group.
   
   
   ```
   [timer wtr](cmdqueryname=timer+wtr) wtr-time
   ```
   
   The default WTR time of a Smart Link group is 60 seconds.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```