Configuring User Login Prompt Information
=========================================

Configuring User Login Prompt Information

#### Context

To provide some prompts or alarms to users, you can configure such information as titles on the device. When a user logs in to the device, the configured titles will be displayed.

When a terminal connection is activated and a user attempts to log in, the terminal displays the title configured using the **header login** command. If the user successfully logs in, the terminal displays the title configured using the **header shell** command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the prompt upon a login attempt.
   
   
   ```
   [header login](cmdqueryname=header+login) { information text | file file-name }
   ```
3. Set the prompt upon successful login.
   
   
   ```
   [header shell](cmdqueryname=header+shell) { information text | file file-name }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```