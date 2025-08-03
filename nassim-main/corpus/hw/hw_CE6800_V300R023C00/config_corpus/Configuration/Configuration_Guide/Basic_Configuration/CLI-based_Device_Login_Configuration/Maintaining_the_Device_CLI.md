Maintaining the Device CLI
==========================

Maintaining the Device CLI

#### Deleting Online Users

To disconnect a login user from a device, you can delete the user.

Run the [**kill user-interface**](cmdqueryname=kill+user-interface) { *ui-number* | *ui-type* *ui-number1* } command to delete online users.

Run the [**display users**](cmdqueryname=display+users) command to view information about users who have logged in to the device.


#### Locking Configuration Rights

When multiple users log in to the device to perform configurations at the same time, conflicts may occur. To avoid service exceptions, you can configure exclusive configuration rights to ensure that only one user can perform configurations at a time.

* Method 1: Lock configuration rights based on the session.
  1. Lock configuration rights for the current user.
     ```
     [configuration exclusive](cmdqueryname=configuration+exclusive)
     ```
     
     After the command is executed, the configuration rights are exclusive to the current user.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + This command applies to all views.
     + You can run the [**display configuration exclusive user**](cmdqueryname=display+configuration+exclusive+user) command to check information about a user who holds an exclusive lock on the configuration rights.
     + If the configuration rights have been locked, a message will be displayed when you attempt to lock the configuration rights again.
  2. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  3. (Optional) Configure the lockout period after which the system automatically unlocks the configuration rights.
     ```
     [configuration exclusive timeout](cmdqueryname=configuration+exclusive+timeout) timeout-value
     ```
     
     This command specifies the maximum period for locking the configuration rights for a specific user when no configuration command is delivered. After the specified period expires, the system automatically unlocks the configuration rights and other users can perform configurations.
     
     By default, the lockout period is 30 seconds.
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
* Method 2: Lock the configurations based on the user name.
  
  Multiple users can access a device in order to manage it. These users can be controller users or other types of users. If a non-controller user logs in to the device and modifies device configurations in a scenario where the controller is deployed, the configurations delivered by the controller may be different from those on the device. To avoid this, you can run the [**configuration exclusive by-user-name**](cmdqueryname=configuration+exclusive+by-user-name) command to lock the system configuration for a specified controller user.
  
  When multiple users manage a device, you can lock the device for a specified user name, so that only users who log in to the device using this user name can modify device configurations.
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Lock the system configuration for a specified user name.
     ```
     [configuration exclusive by-user-name](cmdqueryname=configuration+exclusive+by-user-name) user-name
     ```
     
     By default, the system configuration is not locked.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + The system configuration can be locked for one user name at a time.
     + Only users of the management privilege level can lock and unlock the system configuration.
     + After the system configuration is locked for a specified user name, only users with this user name can perform configuration operations. The configuration operations performed by other users cannot take effect. To make other users' configurations take effect, run the [**undo configuration exclusive by-user-name**](cmdqueryname=undo+configuration+exclusive+by-user-name) *user-name* command to unlock the configuration.
     + When running the [**undo configuration exclusive by-user-name**](cmdqueryname=undo+configuration+exclusive+by-user-name) *user-name* command, ensure that *user-name* is set to the user name for which the configuration is locked.
     + Run the [**display configuration exclusive by-user-name**](cmdqueryname=display+configuration+exclusive+by-user-name) command to view lock information about system configuration that is locked or unlocked based on the user name.
  3. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```

#### Locking a User Interface

When you need to temporarily stop operating the terminal, lock the user interface to prevent unauthorized users from operating it.

1. Run the [**lock**](cmdqueryname=lock) command to lock the user interface.
2. Enter the lock password and confirm it when prompted.
   ```
   <HUAWEI> lock
   Enter Password:
   Confirm Password:
   Info: The terminal is locked.
   ```
   
   After running the [**lock**](cmdqueryname=lock) command, you are prompted to enter and then confirm the lock password. If the two passwords are the same, the user interface is locked.
   
   To unlock the user interface, press **Enter**, and then enter the login password as prompted.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command) defined in the weak password dictionary cannot be specified in this command.

#### User Interface Communication

When multiple users concurrently log in to the device, the device supports message exchanges between user interfaces.

1. Run the [**send**](cmdqueryname=send) { **all** | *ui-type* *ui-number* } command to specify the user interface from which messages are to be sent.
2. Enter a message and send it as prompted.
   
   After entering a message on the current user interface, press **Enter** or **Ctrl**+**Z** to send the message. You can also press **Ctrl**+**C** to cancel message sending. After receiving the message, the target user interface immediately displays it.
   
   ```
   <HUAWEI> send all 
   Enter message, end with CTRL+Z or Enter; abort with CTRL+C: 
   hello~! 
   Send message? [Y/N]:Y
   ```