Configuring a Command Assistant Based on Batch Files
====================================================

Configuring a Command Assistant Based on Batch Files

#### Context

If you want a device to run a few commands automatically in a specific condition to implement a function, write the commands one by one to a batch file with the file name extension \*.bat. Then, load the batch file and bind it to a command assistant. When the device runs the command assistant, it executes the commands in the batch file in sequence.

![](public_sys-resources/note_3.0-en-us.png) 

* A command assistant can be configured with only one batch file, and cannot be configured based on both commands and batch files.
* Ensure that the specified batch file is correct and complete. The system does not check the correctness of content in the batch file.
* Because command assistants are executed in the background, you are advised not to bind interactive or jump commands, such as [**telnet**](cmdqueryname=telnet) and [**stelnet**](cmdqueryname=stelnet), to a command assistant.
* The system switches to the user view by default to run commands in the batch file. If a command must be executed in the system view, run the [**system-view**](cmdqueryname=system-view) command to enter the system view. Otherwise, the command configuration does not take effect.


#### Procedure

1. Upload a batch file to the device. 
   
   
   
   For details about how to upload a file to the device, see [File System Management Configuration](vrp_file_cfg_0001.html).
2. Install the batch file in the user view.
   
   
   ```
   [ops install file](cmdqueryname=ops+install+file) scrFile [ destination directory ]
   ```
   
   If you do not specify **destination** *directory* in the command, the batch file is installed in flash:/$\_user/ by default. If this parameter is specified, the batch file is installed in flash:/$\_user/*directory*/.
   
   If the specified directory does not exist, the system automatically creates the directory. A maximum of seven levels of subdirectories can be created under flash:/$\_user/.
3. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
4. Enter the OPS view.
   
   
   ```
   [ops](cmdqueryname=ops)
   ```
5. Create an assistant.
   
   
   ```
   [assistant](cmdqueryname=assistant) assistant-name
   ```
6. Configure a trigger condition for the assistant.
   
   
   
   **Table 1** Trigger conditions for an assistant
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the severity of an alarm that triggers the assistant execution. | [**condition alarm level**](cmdqueryname=condition+alarm+level) { **eq** | **ge** | **gt** | **le** | **lt** | **ne** } { **critical** | **major** | **minor** | **warning** } | A command assistant can match only one trigger condition. |
   | Set the name of an alarm or event that triggers the assistant execution. | [**condition**](cmdqueryname=condition) { **alarm** [ *alarm-type* ] | **event** } **feature** *feature-name* **name** *event-name* [ *para-name* *para-optype* *para-value* ] &<1-4> [ **occurs** *occur-number* [ **period** *period-value* ] ] |
   | Set the OID of an SNMP trap that triggers the assistant execution. | [**condition snmp-notification**](cmdqueryname=condition+snmp-notification) **oid** *oid-string* [ *optype* *oid-value* ] |
   | Set a log that triggers the assistant execution. | [**condition syslog pattern**](cmdqueryname=condition+syslog+pattern) *reg-express* [ **occurs** *occur-number* [ **period** *period-value* ] ] |
   | Set the time when an assistant is executed. | [**condition timer**](cmdqueryname=condition+timer) *cron* *minutes* *hours* *daysOfMonth* *months* *daysOfWeek* [ *years* ] |
7. Specify the batch file that the command assistant runs. 
   
   
   ```
   [execute](cmdqueryname=execute) priority batch-file file-name
   ```
   
   A command assistant can be configured with only one batch file.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```