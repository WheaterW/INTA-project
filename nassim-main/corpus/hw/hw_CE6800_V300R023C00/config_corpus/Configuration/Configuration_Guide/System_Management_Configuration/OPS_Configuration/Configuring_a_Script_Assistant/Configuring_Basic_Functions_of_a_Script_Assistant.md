Configuring Basic Functions of a Script Assistant
=================================================

Configuring Basic Functions of a Script Assistant

#### Context

In a script assistant, trigger conditions and tasks must be defined using the Python ops\_condition() and ops\_execute() functions, respectively. A script assistant can be triggered by command line, timer, and route change events.


#### Procedure

1. Upload a Python script file to the device. 
   
   
   
   For details about how to upload a file to the device, see [File System Management](vrp_file_cfg_0001.html).
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
5. (Optional) Configure an environment variable.
   
   
   ```
   [environment](cmdqueryname=environment) env-name env-value
   ```
   The OPS supports the following environment variables:
   * System environment variables: environment variables that are automatically generated during system running.
   * User environment variables: environment variables that are configured using the [**environment**](cmdqueryname=environment) command.
   
   Intermediate data generated during Python script running is lost after the Python is shut down. You can configure the Python script's running variable as an environment variable so that data can be saved and used by other users.
6. Create a script assistant.
   
   
   ```
   [script-assistant python](cmdqueryname=script-assistant+python) script-name
   ```
   
   A script assistant is enabled by default after being created. When the trigger condition specified in a Python script is met, the tasks specified in the script will be automatically executed.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```