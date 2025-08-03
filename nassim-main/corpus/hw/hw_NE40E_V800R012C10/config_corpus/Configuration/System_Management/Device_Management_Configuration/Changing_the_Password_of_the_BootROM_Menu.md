Changing the Password of the BootROM Menu
=========================================

When you log in to the BootROM system for the first time, the device requires you to set a password for the BootROM menu. If you need to change the password, perform the following operations:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set boot password**](cmdqueryname=set+boot+password) **slot** *slot-id*
   
   
   
   The BootROM menu password is set for the main control board based on the slot ID.
   
   
   
   You can run the [**display device**](cmdqueryname=display+device) command to view slot information.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The BootROM menu consists of the **Ctrl+B** menu and **Ctrl+K** menu.
   
   For the **Ctrl+B** menu:
   
   * When the device starts, press **Ctrl+B** and use the password to enter the **Ctrl+B** menu to change the password.
   * When you log in to the **Ctrl+B** menu for the first time, you are required to set a password. If the password is not set, the **Ctrl+B** menu cannot be accessed.
   * After the device is upgraded, the password of the **Ctrl+B** menu before the upgrade is still valid. You are advised to change the password after the upgrade.
   * The password must be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   * You can press **Ctrl+R** to restore the factory settings and delete the configured password.
   
   For the **Ctrl+K** menu:
   
   * When the device starts, press **Ctrl+K** and use the password to enter the **Ctrl+K** menu to change the password.
   * When you log in to the **Ctrl+K** menu for the first time, you are required to set a password. If the password is not set, the **Ctrl+K** menu cannot be accessed.
   * After the device is upgraded, the password of the **Ctrl+K** menu before the upgrade is still valid. You are advised to change the password after the upgrade.
   * The password must be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   * You can press **Ctrl+R** to restore the factory settings and delete the configured password.
   * The support for this menu varies according to the device board.

#### Result

Run the [**display boot password status**](cmdqueryname=display+boot+password+status) command to check the password for logging in to the BootROM menu of the main control board.