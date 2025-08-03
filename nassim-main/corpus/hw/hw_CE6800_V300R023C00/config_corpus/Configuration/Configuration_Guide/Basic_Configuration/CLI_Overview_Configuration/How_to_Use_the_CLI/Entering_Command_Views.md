Entering Command Views
======================

Devices provide rich functions and a variety of configuration and query commands for device configuration, management, and maintenance. To simplify the use of such commands on the Huawei devices, these commands are registered in different command views based on their functions. To configure a function, you need to enter the required command view and run the required commands.

A device provides various command views. The following describes the most commonly used command views. For instructions on how to enter command views not listed below, see the *Command Reference*.

#### Common Command Views

* User view
  
  The user view allows you to check statistics and view the operating status of the device.
  
  You automatically enter the user view after logging in to the device, and the following prompt is displayed:
  
  ```
  <HUAWEI>
  ```
* System view
  
  The system view allows you to set the device's system parameters and enter other function views.
  
  To enter the system view, run the [**system-view**](cmdqueryname=system-view) command and press **Enter** while in the user view.
  
  ```
  <HUAWEI> system-view
  Enter system view, return user view with return command.
  [~HUAWEI]
  ```
* Interface view
  
  You can configure interface parameters in the interface view. Interface parameters include physical attributes, link layer protocols, and IP addresses.
  
  To enter the interface view, run the [**interface**](cmdqueryname=interface) command and specify an interface type and number. A 100GE interface is used here as an example.
  
  ```
  [~HUAWEI] interface 100ge X/Y/Z 
  [*HUAWEI-100GEX/Y/Z] 
  ```
  
  *X/Y/Z* indicates the interface number that needs to be specified, and is displayed in the following format: slot number/subcard number/interface sequence number.
* Routing protocol view
  
  Routing protocol views enable you to configure most routing protocol parameters. The routing protocol views include the IS-IS view, the OSPF view, and the RIP view.
  
  To enter a routing protocol view, run a specific command to activate a routing protocol process in the system view.
  
  ```
  [~HUAWEI] isis
  [*HUAWEI-isis-1] 
  ```

The command line prompt HUAWEI is the default host name (sysname), and the prompt indicates the current view. For example, <> indicates the user view and [] indicates all other views.

To add comments, enter ! or # followed by a character string in any view. All the entered content (including ! and #) is displayed as comments and no corresponding configuration will be generated.

![](public_sys-resources/note_3.0-en-us.png) 

* Some commands can be executed in multiple views, while their functions depend on the views these commands are executed.
* In the system view, you can run the [**diagnose**](cmdqueryname=diagnose) command to enter the diagnostic view. Diagnostic commands (level-3 management commands) are used for device fault diagnosis, and running certain commands in this view may cause the device unable to work properly or interrupt services. To use these diagnostic commands, contact technical support.


#### Exiting Command Views

To return from the current view to an upper-level view, run the [**quit**](cmdqueryname=quit) command.

For example, run the [**quit**](cmdqueryname=quit) command to return from the AAA view to the system view, and then run the [**quit**](cmdqueryname=quit) command again to return from the system view to the user view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[*HUAWEI-aaa] quit
[*HUAWEI] quit
<HUAWEI>
```

To return from the AAA view directly to the user view, press **Ctrl+Z** or run the [**return**](cmdqueryname=return) command.

# Press **Ctrl+Z** to return directly to the user view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[*HUAWEI-aaa]           //Enter Ctrl+Z.
<HUAWEI> 
```

# Run the [**return**](cmdqueryname=return) command to return directly to the user view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[*HUAWEI-aaa] return
<HUAWEI> 
```