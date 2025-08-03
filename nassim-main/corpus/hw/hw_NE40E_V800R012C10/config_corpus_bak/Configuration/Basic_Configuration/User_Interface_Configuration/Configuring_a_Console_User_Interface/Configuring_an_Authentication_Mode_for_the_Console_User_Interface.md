Configuring an Authentication Mode for the Console User Interface
=================================================================

The system provides AAA authentication and password authentication to improve system security.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The password authentication mode is not secure, and it is strongly recommended to use AAA authentication mode.



#### Procedure

* Configure AAA authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**user-interface**](cmdqueryname=user-interface){ *ui-type* | **console***first-ui-number* }
     
     
     
     The console user interface view is displayed.
  3. Run [**authentication-mode**](cmdqueryname=authentication-mode) **aaa**
     
     
     
     The authentication mode is set to AAA authentication.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the console user interface view.
  5. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  6. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     
     
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
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure password authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**user-interface**](cmdqueryname=user-interface){ *ui-type* | **console***first-ui-number* } [ *last-ui-number* ]
     
     
     
     The console user interface view is displayed.
  3. Run [**authentication-mode**](cmdqueryname=authentication-mode) **password**
     
     
     
     The authentication mode is set to password authentication.
  4. Run [**set authentication password**](cmdqueryname=set+authentication+password) [ **cipher** *password* ]
     
     
     
     The authentication password is changed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If **cipher** is not specified, a password is entered in man-machine interaction mode and the system does not display the entered password.
     + A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
     + Special characters exclude question marks (?) and spaces. However, when quotation marks (") are used around the password, spaces are allowed in the password.
       - Double quotation marks cannot contain double quotation marks if spaces are used in a password.
       - Double quotation marks can contain double quotation marks if no space is used in a password.
       
       For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
     + If **cipher** is specified, a password can be entered in either simple text or cipher text.
       
       - If a password is entered in simple text, the password requirements are the same as those when **cipher** is not specified. When you input a password in simple text, the system displays the password in simple text mode, which brings risks.
       - A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or cipher text.
     
     If you have run the [**undo authentication-mode**](cmdqueryname=undo+authentication-mode) command to delete the authentication mode configured for the console user interface, you cannot run the [**set authentication password**](cmdqueryname=set+authentication+password) [ **cipher** *password* ] command to change the authentication password.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.