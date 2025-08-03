Manually Running a Python Script
================================

Manually Running a Python Script

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
3. Execute the Python script.
   
   
   ```
   [ops run python](cmdqueryname=ops+run+python) [ background ] script-name [ arguments ]
   ```
   
   
   
   If you specify **background**, the Python script is executed in the background. Otherwise, the script is executed in the foreground.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```