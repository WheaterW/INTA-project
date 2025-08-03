Configuring the Device to Output Debugging Messages to the Console
==================================================================

Configuring the Device to Output Debugging Messages to the Console

#### Context

After debugging messages are output to the console, you can view debugging messages on the console (host from which you can log in to the device through the console interface) to monitor device running.

![](public_sys-resources/caution_3.0-en-us.png) 

Debugging occupies a device's CPU resources and affects system running. You are advised to immediately run the **undo debugging all** command to disable debugging after this function is performed.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify a channel through which debugging messages are output to the console.
   
   
   ```
   [info-center console channel](cmdqueryname=info-center+console+channel) { channel-number | channel-name }
   ```
3. Set a rule for outputting debugging messages to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } debug { state { off | on } | level severity } *
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
7. Enable the debugging message display function of the terminal.
   
   
   ```
   [terminal debugging](cmdqueryname=terminal+debugging)
   ```