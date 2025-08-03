Configuring an Alias for a Command
==================================

To facilitate operations, you can use the command alias function to configure a character string as an alias for a command.

#### Context

To enable the command alias function for the current terminal, run the [**terminal command alias**](cmdqueryname=terminal+command+alias) command. To disable the command alias function for the current terminal, run the [**undo terminal command alias**](cmdqueryname=undo+terminal+command+alias) command. Disabling the command alias function does not delete the existing alias configuration. Therefore, the existing alias configuration continues to take effect if you enable the command alias function again for the current terminal. You can run the [**display terminal command alias**](cmdqueryname=display+terminal+command+alias) command to view the status of the command alias function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**command alias**](cmdqueryname=command+alias)
   
   
   
   The command alias view is displayed.
3. Run [**alias**](cmdqueryname=alias) *alias-string* [ **parameter** { *parameter* } &<1-32> ] **command** *command*
   
   
   
   An alias is configured for a command.

#### Follow-up Procedure

* Run the [**display command alias**](cmdqueryname=display+command+alias) command to view the alias configuration.