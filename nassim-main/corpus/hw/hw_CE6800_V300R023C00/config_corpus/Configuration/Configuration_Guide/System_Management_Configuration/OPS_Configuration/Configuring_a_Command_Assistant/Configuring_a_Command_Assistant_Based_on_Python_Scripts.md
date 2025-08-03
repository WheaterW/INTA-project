Configuring a Command Assistant Based on Python Scripts
=======================================================

Configuring a Command Assistant Based on Python Scripts

#### Context

To test whether a Python script runs normally, or if you do not want to bind a Python script to a trigger condition but want to run this script, manually trigger the execution of this script using a command.


#### Procedure

1. Upload a Python script file to the device. 
   
   
   
   For details about how to upload a file to the device, see [File System Management](vrp_file_cfg_0001.html).
   
   In the script, you can define the management actions to be performed using commands. You can also use OPS APIs to define management actions to be performed. For details, see [Compiling OPS API-based Scripts](vrp_ops_cfg_0023.html).
2. Install the script file in the user view.
   
   
   ```
   [ops install file](cmdqueryname=ops+install+file) scrFile [ destination directory ]
   ```
   If you do not specify **destination** *directory* in the command, the script is installed in flash:/$\_user/ by default. If this parameter is specified, the script is installed in flash:/$\_user/*directory*/.![](public_sys-resources/note_3.0-en-us.png) 
   
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
7. Specify the Python script that the assistant runs.
   
   
   ```
   [execute](cmdqueryname=execute) priority python file-name[arguments]
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```