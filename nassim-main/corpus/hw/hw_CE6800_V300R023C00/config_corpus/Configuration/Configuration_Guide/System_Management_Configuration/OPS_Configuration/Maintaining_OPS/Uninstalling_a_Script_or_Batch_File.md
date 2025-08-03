Uninstalling a Script or Batch File
===================================

Uninstalling a Script or Batch File

#### Context

You can uninstall unwanted scripts or batch files to release storage space on a device. If an installed script or batch file needs to be updated, uninstall it first and then reinstall it after the modification.

![](public_sys-resources/note_3.0-en-us.png) 

* If a file name is specified, the **ops uninstall file** command uninstalls the specified file. If a directory is specified, the **ops uninstall file** command uninstalls all files in the directory and its subdirectories.
* The **ops uninstall file** command cannot uninstall a script that has been bound to an assistant. To uninstall such a script, unbind it from the assistant first.
* If the script bound to an assistant calls other scripts, the called scripts may be uninstalled when the **ops uninstall file** command is run. Therefore, you are advised to use only one script to implement required functions.
* The asterisk (\*) is supported. If **/** or **/\*** is specified, all files in the **$\_user** directory are deleted. If **/\*** is specified after a folder name, all files in the folder are deleted. If **\*.py** is specified, all Python files in the **$\_user** directory are deleted.


#### Procedure

1. Uninstall a script or batch file.
   
   
   ```
   [ops uninstall file](cmdqueryname=ops+uninstall+file) file-name-or-dir
   ```