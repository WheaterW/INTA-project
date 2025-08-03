Changing the Password of the BootLoader Menu
============================================

Changing the Password of the BootLoader Menu

#### Context

When you log in to the BootLoader system for the first time, the device requires you to set a password for the BootLoader menu. To change the password, perform the following operations:


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Change the password of the BootLoader menu.
   
   
   ```
   [set boot password](cmdqueryname=set+boot+password) slot slot-id
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If you enter an incorrect password for three consecutive times when changing the BootLoader menu password, you need to wait for 600s before changing the password again.
   * When you log in to a new device for the first time through the console port, you need to immediately set the BootLoader password to prevent the console port password from being cleared without authorization. If the BootLoader password is not set, unauthorized users may attempt to log in to a device through the BootLoader and clear the console port password, which will cause security risks.