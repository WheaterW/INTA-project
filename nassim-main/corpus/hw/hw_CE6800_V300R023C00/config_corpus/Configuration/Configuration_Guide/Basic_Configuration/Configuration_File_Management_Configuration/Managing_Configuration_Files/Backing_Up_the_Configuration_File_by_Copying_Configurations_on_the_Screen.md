Backing Up the Configuration File by Copying Configurations on the Screen
=========================================================================

Backing Up the Configuration File by Copying Configurations on the Screen

#### Context

You can copy configurations on the screen to back up them as a configuration file to the hard disk of the PC. The backup configuration file can be used if the configuration file restoration fails due to unexpected device damage.


#### Procedure

1. Copy configurations on the screen. Specifically, run the following command and copy all command output to a .txt file on the PC. The configurations are then saved on the PC.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the configuration of a single command is too long, the configuration may be displayed in multiple lines on the terminal screen, depending on the terminal software. When copying a multi-line configuration from the screen to a .txt file, ensure that the configuration occupies one line in the .txt file. Otherwise, such a configuration may fail to be restored when the .txt file is used.