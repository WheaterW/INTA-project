Comparing Configuration Files
=============================

Comparing Configuration Files

#### Context

You can compare the current configuration file with the specified configuration file to check whether they are consistent and determine whether to use the specified configuration file for the next startup.

![](public_sys-resources/note_3.0-en-us.png) 

The configuration file name extension must be .cfg or .zip.



#### Procedure

**Table 1** Comparing configuration files
| Operation | Command | Description |
| --- | --- | --- |
| Check whether the current configurations are consistent with those in the specified configuration file. | [**display configuration changes**](cmdqueryname=display+configuration+changes) [ **running file** *file-name* | **file** *file-name* **running** ] | These two commands can only compare the current running configuration file with a specified configuration file. When you run these commands, the first specified configuration file is called source configuration, and the later specified configuration file is called target configuration. If the target configuration is different from the source configuration, the difference is displayed based on the following rules:  * A command that exists in the target configuration rather than the source configuration is prefixed with "+". * A command that exists in the source configuration rather than the target configuration is prefixed with "-". * If a command is modified in the target configuration, the original command is prefixed with "-" and the new command is prefixed with "+". |
| Check whether the current configurations are consistent with those of a specified user label. | [**display configuration changes**](cmdqueryname=display+configuration+changes) { **running**  **label** *label* | **label** *label* **running** } |
| Check whether the current configurations are the same as those in the configuration file for the next startup or a specified configuration file. | [**compare configuration**](cmdqueryname=compare+configuration) [ *configuration-file* ] | After completing a series of configuration operations, you can compare whether the current configurations are the same as those in the configuration file for the next startup, or a specified configuration file starting from the first line. Based on the comparison result, you can determine whether to save the current configurations in the configuration file and specify it as that used for the next startup.  If there are differences between the configurations, the system displays a maximum of nine lines starting from the first line with differences. If there are fewer than nine lines from that line to the end of the file, the system will display the remaining lines. |