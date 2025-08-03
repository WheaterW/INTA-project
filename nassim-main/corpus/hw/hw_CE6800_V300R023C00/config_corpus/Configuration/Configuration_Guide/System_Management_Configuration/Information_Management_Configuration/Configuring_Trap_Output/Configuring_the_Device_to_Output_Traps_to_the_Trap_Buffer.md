Configuring the Device to Output Traps to the Trap Buffer
=========================================================

Configuring the Device to Output Traps to the Trap Buffer

#### Context

To view traps in the trap buffer, configure the device to output traps to the trap buffer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to output traps to the trap buffer.
   
   
   ```
   [info-center trapbuffer](cmdqueryname=info-center+trapbuffer)
   ```
3. Specify the channel used by the device to output traps to the trap buffer.
   
   
   ```
   [info-center trapbuffer channel](cmdqueryname=info-center+trapbuffer+channel) { channel-number | channel-name } [ size size ]
   ```
4. Set a rule for outputting traps to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } trap { state { off | on } | level severity } *
   ```
5. (Optional) Set the maximum number of traps in the trap buffer.
   
   
   ```
   [info-center trapbuffer size](cmdqueryname=info-center+trapbuffer+size) size channel { channel-number | channel-name }
   ```
   
   By default, a trap buffer allows a maximum of 256 traps.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```