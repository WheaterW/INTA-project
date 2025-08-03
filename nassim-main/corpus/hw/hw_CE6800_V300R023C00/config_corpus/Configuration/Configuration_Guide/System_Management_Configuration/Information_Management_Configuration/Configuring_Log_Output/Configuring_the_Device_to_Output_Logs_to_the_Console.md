Configuring the Device to Output Logs to the Console
====================================================

Configuring the Device to Output Logs to the Console

#### Context

After logs are output to the console, you can view logs on the console (the host from which you can log in to the device through the console interface) to monitor device operation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify a channel through which logs are output to the console.
   
   
   ```
   [info-center console channel](cmdqueryname=info-center+console+channel) { channel-number | channel-name }
   ```
3. Configure a rule for outputting logs to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } log { state { off | on } | level severity } *
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
7. Enable the log display function of the terminal.
   
   
   ```
   [terminal logging](cmdqueryname=terminal+logging)
   ```