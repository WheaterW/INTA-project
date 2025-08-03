Configuring a User Level and Authentication Mode for VTY User Interfaces
========================================================================

Configuring a User Level and Authentication Mode for VTY User Interfaces

#### Context

Other attributes on the VTY user interface have default values. Generally, you do not need to modify them. You can also modify these attributes as required. For details, see [Configuring VTY User Interfaces](dc_vrp_basic_cfg_0013.html).


#### Procedure

* Configure a user level for the VTY user interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
     
     The VTY user interface is displayed.
  3. Run the [**user privilege**](cmdqueryname=user+privilege) **level** *level* command to set the user level. [Table 1](#EN-US_TASK_0172359817__en-us_task_0172359804_tab_1) lists the mapping between user levels and command levels in the VTY user interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The value of *level* ranges from 0 to 15 when the [**command-privilege level rearrange**](cmdqueryname=command-privilege+level+rearrange) configuration exists.
     
     The value of *level* ranges from 0 to 3 when the [**command-privilege level rearrange**](cmdqueryname=command-privilege+level+rearrange) configuration does not exist.
     
     
     **Table 1** Mapping between user levels and command levels
     | User Level (0 to 3) | User Level (0 to 15) | Command Level | Permission | Description |
     | --- | --- | --- | --- | --- |
     | 0 | 0 | 0 | Visit | Diagnostic commands, such as ping and tracert, and commands that are used to access a remote device such as a Telnet client. |
     | 1 | 1-9 | 0, 1 | Monitoring | Commands of this level are used for system maintenance, including display commands. NOTE:  Not all display commands are of the monitoring level. For example, the [**display current-configuration**](cmdqueryname=display+current-configuration) command is of management level (3). For details about command levels, see *HUAWEI NE40E-M2 series Command Reference*. |
     | 2 | 10 to 14 | 0, 1, and 2 | Configuration level | Service configuration commands |
     | 3 | 15 | 0, 1, 2, and 3 | Management level | Commands of the management level are used for basic system operation to support services, including file system, FTP, TFTP, and configuration file switching commands, slave board control commands, user management commands, command level configuration commands, reboot commands, and debugging commands. |
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + User levels correspond to command levels. After a user logs in to a device, the user can use only commands of the corresponding level or lower, which improves device security.
     + If the user level configured for a user interface conflicts with the user level configured for a user, the user level configured for the user takes precedence.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure aaa authentication mode for the VTY user interfaces.
  
  
  
  When the authentication mode is set to AAA authentication, you must specify the access type of a local user.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**crypto password irreversible-algorithm hmac-sha256**](cmdqueryname=crypto+password+irreversible-algorithm+hmac-sha256)
     
     The HMAC-SHA256 ciphertext password encryption algorithm is set.
  3. Run [**aaa**](cmdqueryname=aaa)
     
     The AAA view is displayed.
  4. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     A local user name and a password are set.
     
     + If **cipher** or **irreversible-cipher** is not specified, a password is entered in man-machine interaction mode and the system does not display the entered password.
       
       When the user security policy is configured, the value is a string of 8 to 128 case-sensitive characters without spaces. When the user security policy is not configured, the value is a string of 1 to 128 case-sensitive characters without spaces. When the user security policy is configured, the password cannot be the same as the user name or its reverse. The password must contain the following characters: upper-case character, lower-case character, digit, and special character.![](../../../../public_sys-resources/note_3.0-en-us.png) Special characters do not include question marks (?) or spaces. However, when double quotation marks are used around a password, spaces are allowed in the password.
       - Double quotation marks cannot contain double quotation marks if spaces are used in a password.
       - Double quotation marks can contain double quotation marks if no space is used in a password.
       
       For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
     + If **cipher** is specified, a password can be entered in either simple text or cipher text.
       
       If a password is entered in simple text, the password requirements are the same as those when **cipher** is not specified. When you input a password in simple text, the system displays the password in simple text mode, which brings risks.
       
       A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or cipher text.
     + If **irreversible-cipher** is specified, a password can be entered in either simple text or irreversible cipher text.
       
       If a password is entered in simple text, the password requirements are the same as those when **irreversible-cipher** is not specified.
       
       A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or irreversible cipher text.
  5. Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **ssh**
     
     The access type of the local user is set to SSH.
  6. Run [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *user-group-name*
     
     The local user is added to a user group.
  7. Run [**quit**](cmdqueryname=quit)
     
     Exit the AAA view.
  8. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-index* [ *last-index* ]
     
     One or more VTY user interface views are displayed.
  9. Run [**authentication-mode**](cmdqueryname=authentication-mode) **aaa**
     
     The authentication mode is set to AAA authentication.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.