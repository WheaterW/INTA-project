Configuring the Device to Output Logs to the Log Buffer
=======================================================

Configuring the Device to Output Logs to the Log Buffer

#### Context

To view logs in the log buffer, configure the device to output logs to the log buffer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to output information to the log buffer.
   
   
   ```
   [info-center logbuffer](cmdqueryname=info-center+logbuffer)
   ```
3. Specify the channel used by the device to output logs to the log buffer.
   
   
   ```
   [info-center logbuffer channel](cmdqueryname=info-center+logbuffer+channel) { channel-number | channel-name } [ size logbuffersize ]
   ```
4. Configure the rule for outputting logs to the specified channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } log { state { off | on } | level severity } *
   ```
5. (Optional) Set the maximum number of logs in the log buffer.
   
   
   ```
   [info-center logbuffer](cmdqueryname=info-center+logbuffer) size buffersize
   ```
   
   By default, the log buffer can store a maximum of 512 logs.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```