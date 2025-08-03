Configuring the Buffer Size
===========================

Configuring the Buffer Size

#### Context

If the device's current buffer cannot meet requirements, you can manually divide the buffer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Configure the queue-level service buffer for outbound queues.
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ, run the following command:
   ```
   [qos buffer queue](cmdqueryname=qos+buffer+queue) queue-index shared-threshold { static static-value { bytes | kbytes | mbytes } | dynamic dynamic-value }
   ```
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, run the following command:
   ```
   [qos buffer queue](cmdqueryname=qos+buffer+queue) queue-index shared-threshold dynamic dynamic-value
   ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the [**qos burst-mode**](cmdqueryname=qos+burst-mode) command is not configured in the system view or interface view.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```