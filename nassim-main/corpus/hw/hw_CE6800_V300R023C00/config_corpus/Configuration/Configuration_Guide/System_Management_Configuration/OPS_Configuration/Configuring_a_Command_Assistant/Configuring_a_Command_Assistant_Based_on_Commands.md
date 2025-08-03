Configuring a Command Assistant Based on Commands
=================================================

Configuring a Command Assistant Based on Commands

#### Context

If you want a device to run a few commands automatically in a specific condition to implement a function, bind the commands to a command assistant.

![](public_sys-resources/note_3.0-en-us.png) 

* Ensure that the specified commands are correct and complete. The system does not provide help information or check the correctness of the commands bound to a command assistant.
* Because command assistants are executed in the background, you are advised not to bind interactive or jump commands, such as [**telnet**](cmdqueryname=telnet) and [**stelnet**](cmdqueryname=stelnet), to a command assistant.
* When executing an interactive command that requires a Y/N choice, the system automatically selects Y. When executing an interactive command that requires input of a character string, the system waits for the input and proceeds to run the next command when the wait period expires.
* The system switches to the user view by default to run the specified commands. If a command must be executed in the system view, run the [**execute**](cmdqueryname=execute) *priority* **command** **system-view** command first. Otherwise, the command configuration does not take effect.
* A command assistant cannot be configured based on both commands and batch files.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OPS view.
   
   
   ```
   [ops](cmdqueryname=ops)
   ```
3. Create an assistant.
   
   
   ```
   [assistant](cmdqueryname=assistant) assistant-name
   ```
4. Configure a trigger condition for the assistant.
   
   
   
   **Table 1** Trigger conditions for an assistant
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the severity of an alarm that triggers the assistant execution. | [**condition alarm level**](cmdqueryname=condition+alarm+level) { **eq** | **ge** | **gt** | **le** | **lt** | **ne** } { **critical** | **major** | **minor** | **warning** } | A command assistant can match only one trigger condition.  If the alarm or event in the condition is deleted due to upgrade or patch installation, the command assistant cannot be triggered. In this case, you are advised to adjust the trigger condition. |
   | Set the name of an alarm or event that triggers the assistant execution. | [**condition**](cmdqueryname=condition) { **alarm** [ *alarm-type* ] | **event** } **feature** *feature-name* **name** *event-name* [ *para-name* *para-optype* *para-value* ] &<1-4> [ **occurs** *occur-number* [ **period** *period-value* ] ] |
   | Set the OID of an SNMP trap that triggers the assistant execution. | [**condition snmp-notification**](cmdqueryname=condition+snmp-notification) **oid** *oid-string* [ *optype* *oid-value* ] |
   | Set a log that triggers the assistant execution. | [**condition syslog pattern**](cmdqueryname=condition+syslog+pattern) *reg-express* [ **occurs** *occur-number* [ **period** *period-value* ] ] |
   | Set the time when an assistant is executed. | [**condition timer**](cmdqueryname=condition+timer) *cron* *minutes* *hours* *daysOfMonth* *months* *daysOfWeek* [ *years* ] |
5. Specify the commands that the command assistant runs. 
   
   
   ```
   [execute](cmdqueryname=execute) priority command command-string
   ```
   
   
   
   You can run the command multiple times to specify multiple commands to run.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```