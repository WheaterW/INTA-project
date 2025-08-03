Configuring the Device to Output Logs to a Terminal
===================================================

Configuring the Device to Output Logs to a Terminal

#### Context

After logs are output to a user terminal, you can view logs on the user terminal (the host from which you log in to the device through VTY or SSH) to monitor device operation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify a channel through which logs are output to a user terminal.
   
   
   ```
   [info-center monitor channel](cmdqueryname=info-center+monitor+channel) { channel-number | channel-name }
   ```
3. Configure the rule for outputting logs to the specified channel.
   
   
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