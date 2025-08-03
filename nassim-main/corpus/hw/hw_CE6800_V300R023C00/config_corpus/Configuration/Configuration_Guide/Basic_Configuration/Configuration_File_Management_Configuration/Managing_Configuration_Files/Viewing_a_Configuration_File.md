Viewing a Configuration File
============================

Viewing a Configuration File

#### Procedure

**Table 1** Viewing a configuration file
| Operation | Command | Description |
| --- | --- | --- |
| Check the configuration file in the storage medium. | [**dir**](cmdqueryname=dir) | - |
| Check the configuration files for the current and next startup. | [**display startup**](cmdqueryname=display+startup) | - |
| Check configurations in a specified configuration file. | [**display configuration**](cmdqueryname=display+configuration) *configuration-file* | - |
| Check configurations in the configuration file for the next startup. | [**display saved-configuration**](cmdqueryname=display+saved-configuration) | - |
| Check the system configurations saved last time. | [**display saved-configuration last**](cmdqueryname=display+saved-configuration+last) | - |
| Check the time when the configurations are saved last time. | [**display saved-configuration time**](cmdqueryname=display+saved-configuration+time) | - |
| Check all configurations that take effect on the device. | [**display current-configuration**](cmdqueryname=display+current-configuration) [ **include-default** ] | If **include-default** is not specified, only configured information is displayed. If **include-default** is specified, both configured information and default configurations are displayed. |
| Check the configurations that take effect in the current view. | [**display this**](cmdqueryname=display+this) [ **include-default** ] | This command displays the configurations in the view where this command is executed.  If **include-default** is not specified, only configured information in the current view is displayed. If **include-default** is specified, both configured information and default configurations in the current view are displayed. |