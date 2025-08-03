When AAA Local Authentication Is Used, a User Is Disconnected from the Device After Logging In to the Device Through Telnet or STelnet
======================================================================================================================================

When AAA Local Authentication Is Used, a User Is Disconnected from the Device After Logging In to the Device Through Telnet or STelnet

#### Fault Symptom

When AAA local authentication is used, a user logs in to the device through Telnet or STelnet. After the login, the user is not prompted to change the initial password and then disconnected from the device.


#### Possible Causes

* The function of prompting users to change the initial password is enabled by default. After a user logs in to the device, the user needs to change the initial password to continue the connection. If the user terminal does not support the change of the initial password, the connection will be disconnected.

#### Troubleshooting Procedure

* For a specific administrator, run the **local-user** *user-name* **password-force-change disable** command in the AAA view to disable the function of prompting users to change the initial password for the specified user.
* For all administrators, run the **undo password alert original** command in the administrator password policy view to disable the function of prompting users to change the initial password for all users.![](../public_sys-resources/note_3.0-en-us.png) 
  
  After the **undo password alert original** command is run, the function of prompting users to change the initial password does not take effect, which poses security risks.