Configuring CLI-to-XML Translation
==================================

Configuring CLI-to-XML Translation

#### Context

CLI and NETCONF are two device management models, which have a mapping relationship. To quickly obtain NETCONF YANG model packets corresponding to configuration commands, perform the following steps.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the CLI-to-XML translation mode.
   ```
   [xml-translate begin](cmdqueryname=xml-translate+begin)
   ```
3. Run the configuration commands to be translated.
4. Run either of the following commands as needed:
   * To translate the configuration commands into NETCONF YANG model packets, run the following command:
     ```
     [xml-translate end](cmdqueryname=xml-translate+end)
     ```
   * To abort the CLI-to-XML translation and exit the translation mode, run the following command:
     ```
     [xml-translate abort](cmdqueryname=xml-translate+abort)
     ```