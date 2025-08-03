Configuring the VTY User Interface to Support SSH
=================================================

Configuring the VTY User Interface to Support SSH

#### Context

Before logging in to the device through SSH, configure the VTY user interface that will be used to support SSH.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Enter the VTY user interface view.
   
   
   ```
   [user-interface](cmdqueryname=user-interface) vty first-ui-number [ last-ui-number ]
   ```
   
   By default, no user interface view is displayed.
3. Configure the AAA authentication mode for the VTY user interface.
   
   
   ```
   [authentication-mode](cmdqueryname=authentication-mode) aaa
   ```
   
   By default, no authentication mode is used on a VTY user interface.
   
   Configure the AAA authentication mode on the VTY user interface to enable SSH support. If the AAA authentication mode is not set, the [**protocol inbound**](cmdqueryname=protocol+inbound) **ssh** command does not take effect.
4. Configure the VTY user interface to support SSH.
   
   
   ```
   [protocol inbound](cmdqueryname=protocol+inbound) { all | ssh }
   ```
   
   By default, the VTY user interface supports all protocols, including SSH.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```