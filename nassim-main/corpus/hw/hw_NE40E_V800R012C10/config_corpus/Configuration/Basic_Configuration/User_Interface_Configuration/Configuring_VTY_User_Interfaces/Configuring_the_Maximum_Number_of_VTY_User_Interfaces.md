Configuring the Maximum Number of VTY User Interfaces
=====================================================

You can configure the maximum number of VTY user interfaces to limit the number of concurrent login users.

#### Context

The maximum number of VTY user interfaces is the total number of users who use Telnet and SSH to log in.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If the maximum number of VTY user interfaces is set to 0 on a router, no user can log in to the router using VTY.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface maximum-vty**](cmdqueryname=user-interface+maximum-vty) *number*
   
   
   
   The maximum number of VTY user interfaces is set.
   
   
   
   * If the configured maximum number is less than the current number, online users are not affected and no additional configuration is needed.
   * If the configured maximum number is greater than the current number, configure the authentication mode and password for additional users. The system uses password authentication to authenticate users who log in through newly added user interfaces.
     
     For example, run the [**authentication-mode**](cmdqueryname=authentication-mode) commands to increase the maximum number of allowed online users from 5 to 18. A password is entered in man-machine interaction mode. The system does not display the entered password. A password must meet the following requirements:
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] user-interface maximum-vty 18
     ```
     ```
     [*HUAWEI] user-interface vty 5 17
     ```
     ```
     [*HUAWEI-ui-vty5-17] authentication-mode password
     ```
     ```
     [*HUAWEI-ui-vty5-17] set authentication-mode password
     ```
     ```
     Please configure the login password (8-16)
     Enter Password:
     Confirm Password:
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The password must meet the following requirements:
     
     + The password is entered in man-machine interaction mode. The system does not display the entered password.
     + A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
     + Special characters exclude question marks (?) and spaces. However, spaces are allowed in the password if the password is enclosed in quotation marks.
       - Double quotation marks cannot contain double quotation marks if spaces are used in a password.
       - Double quotation marks can contain double quotation marks if no space is used in a password.
       
       For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
     
     The configured password is displayed in ciphertext in the configuration file.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.