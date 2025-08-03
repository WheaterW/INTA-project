Configuring the Device to Output Logs to a Log File
===================================================

Configuring the Device to Output Logs to a Log File

#### Context

After a device is configured to output logs to a log file, the logs are saved as a file on the device. If a fault occurs on the device, you can export and analyze the log file to locate the fault.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify a channel through which logs are output to a log file.
   
   
   ```
   [info-center logfile channel](cmdqueryname=info-center+logfile+channel) { channel-number | channel-name }
   ```
3. Configure a rule for outputting logs to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } log { state { off | on } | level severity } *
   ```
4. (Optional) Enable event log recording globally.
   
   
   ```
   [info-center event logging all](cmdqueryname=info-center+event+logging+all)
   ```
   
   
   
   By default, event log recording is disabled globally.
5. (Optional) Set the log file size.
   
   
   ```
   [info-center logfile](cmdqueryname=info-center+logfile) [ security ] size size
   ```
   
   If the size of a log file exceeds the configuration, the system automatically compresses the log file into a .zip file.
6. (Optional) Set the maximum number of log files that can be saved.
   
   
   ```
   [info-center max-logfile-number](cmdqueryname=info-center+max-logfile-number) [ security ] filenumbers
   ```
   
   If the number of log files generated on the device exceeds this limit, the system deletes the earliest log files.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
8. Return to the user view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. (Optional) Configure the device to save information in the log buffer to a log file.
   
   
   ```
   [save logfile](cmdqueryname=save+logfile)
   ```
   
   Logs are cached in the system memory before being written into log files. When the buffer is full or if the log saving timer expires, the device immediately writes the cached logs into log files. If the buffer is not full or the timer does not expire, run this command to manually write logs in the memory into information files.

#### Follow-up Procedure

After a log file is generated, you can run the [**display logfile**](cmdqueryname=display+logfile) command to view its content. The format of the log file is log.log.

To delete log files, run the **delete** *filename* command in the user view.