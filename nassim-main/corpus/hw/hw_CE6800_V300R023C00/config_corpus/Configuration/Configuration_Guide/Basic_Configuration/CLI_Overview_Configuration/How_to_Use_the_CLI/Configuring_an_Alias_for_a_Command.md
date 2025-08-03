Configuring an Alias for a Command
==================================

Configuring an Alias for a Command

#### Context

The command alias function allows you to define your preferred character strings for commands to facilitate command usage.

You can use the **alias** command to achieve the following:

* Configure an easy-to-remember string of characters as the alias for a command or command keyword. By doing this, you only need to enter the alias when you want to run the command. For example, if you define the alias for **display** as **show**, you only need to enter the **show** command instead of **display**.
* Adjust the order of parameters to cater for your need. Parameters start with a dollar sign ($). For example, after you configure the **alias showif parameter $ifnum $iftype command "display interface $iftype $ifnum"** command, you can enter **showif 1 Eth-Trunk** to substitute **display interface Eth-Trunk 1**.

To enable the command alias function for the current terminal, run the [**terminal command alias**](cmdqueryname=terminal+command+alias) command. To disable the command alias function for the current terminal, run the [**undo terminal command alias**](cmdqueryname=undo+terminal+command+alias) command. Disabling the command alias function does not delete the existing alias configuration. Therefore, the existing alias configuration will continue to take effect after you enable the command alias function again for the current terminal. To check whether or not the command alias function is enabled, you can run the [**display terminal command alias**](cmdqueryname=display+terminal+command+alias) command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the command alias view.
   
   
   ```
   [command alias](cmdqueryname=command+alias)
   ```
3. Configure an alias for a command.
   
   
   ```
   [alias](cmdqueryname=alias) alias-string [ parameter parameter &<1-32> ] command command
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display command alias**](cmdqueryname=display+command+alias) command to view the configuration of the command alias.

```
<HUAWEI> display command alias
  show = display
  showif $ifnum $iftype = display interface $iftype $ifnum
```