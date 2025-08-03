Configuring a Local FTP User
============================

You can configure authentication information, authorization mode, and authorized directory to prevent unauthorized FTP users from accessing a specified directory.

#### Context

To use FTP to operate files, configure a local user name and a password on a device that functions as an FTP server, and specify a service type and an authorized directory. If you do not perform these operations, you cannot use FTP to access the device.

Perform the following steps on the device that functions as an FTP server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**crypto password irreversible-algorithm hmac-sha256**](cmdqueryname=crypto+password+irreversible-algorithm+hmac-sha256)
   
   
   
   The HMAC-SHA256 ciphertext password encryption algorithm is set.
3. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
4. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
   
   
   
   A local user name and a password are set.
   
   
   
   * If **cipher** or **irreversible-cipher** is not specified, a password is entered in man-machine interaction mode and the system does not display the entered password.
     
     When the user security policy is configured, the value is a string of 8 to 128 case-sensitive characters without spaces. When the user security policy is not configured, the value is a string of 1 to 128 case-sensitive characters without spaces. When the user security policy is configured, the password cannot be the same as the user name or its reverse. The password must contain the following characters: upper-case character, lower-case character, digit, and special character.![](../../../../public_sys-resources/note_3.0-en-us.png) Special characters do not include question marks (?) or spaces. However, when double quotation marks are used around a password, spaces are allowed in the password.
     + Double quotation marks cannot contain double quotation marks if spaces are used in a password.
     + Double quotation marks can contain double quotation marks if no space is used in a password.
     
     For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
   * If **cipher** is specified, a password can be entered in either simple text or cipher text.
     
     If a password is entered in simple text, the password requirements are the same as those when **cipher** is not specified. When you input a password in simple text, the system displays the password in simple text mode, which brings risks.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or cipher text.
   * If **irreversible-cipher** is specified, a password can be entered in either simple text or irreversible cipher text.
     
     If a password is entered in simple text, the password requirements are the same as those when **irreversible-cipher** is not specified.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or irreversible cipher text.
5. Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type ftp**
   
   
   
   The service type is set to FTP for the local user.
6. Run [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* [ **access-permission** { **read-only** | **read-write** } ]
   
   
   
   An authorized FTP directory and corresponding operation permission are configured for the local user.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   FTP users are classified as local AAA authentication users or remote authentication (RADIUS and HWTACACS) users.
   
   * The [**local-user ftp-directory**](cmdqueryname=local-user+ftp-directory) command must be run to specify the FTP working directory for local authentication users. Otherwise, local authentication users cannot use FTP to access the device.
   * The FTP working directory for remote authentication users can be specified using the HWTACACS server. The [**set default ftp-directory**](cmdqueryname=set+default+ftp-directory) command can be used to specify the default FTP working directory for remote authentication users.
   * A user group or user level needs to be configured on the AAA server for remote authentication users. For details about the configuration, see the configuration guide provided by the associated vendor.
7. Run [**local-user**](cmdqueryname=local-user) *user-name* [**level**](cmdqueryname=level) *level*
   
   
   
   A level is set for the local user.
   
   
   
   To access the FTP server, you must set the level of the local user to Level 3 or higher.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.