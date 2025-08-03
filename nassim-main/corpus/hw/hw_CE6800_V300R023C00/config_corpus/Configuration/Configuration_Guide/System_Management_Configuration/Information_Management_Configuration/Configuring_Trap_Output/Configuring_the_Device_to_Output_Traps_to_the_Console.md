Configuring the Device to Output Traps to the Console
=====================================================

Configuring the Device to Output Traps to the Console

#### Context

After traps are output to the console, you can view traps on the console (host from which you can log in to the device through the console interface) to monitor device running.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify a channel through which traps are output to the console.
   
   
   ```
   [info-center console channel](cmdqueryname=info-center+console+channel) { channel-number | channel-name }
   ```
3. Set a rule for outputting traps to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } trap { state { off | on } | level severity } *
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
5. Return to the user view.
   
   
   ```
   [quit](cmdqueryname=quit) 
   ```
6. Enable the display of logs, traps, and debugging messages on the user terminal.
   
   
   ```
   [terminal monitor](cmdqueryname=terminal+monitor)
   ```
7. Enable the trap display function of the terminal.
   
   
   ```
   [terminal trapping](cmdqueryname=terminal+trapping)
   ```