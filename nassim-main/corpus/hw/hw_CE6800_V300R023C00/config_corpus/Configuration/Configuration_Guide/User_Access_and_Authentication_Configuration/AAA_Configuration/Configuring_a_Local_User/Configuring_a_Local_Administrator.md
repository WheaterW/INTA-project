Configuring a Local Administrator
=================================

Configuring a Local Administrator

#### Context

When an administrator uses local authentication and authorization, you need to configure a local administrator.

![](public_sys-resources/note_3.0-en-us.png) 

* When logging in to the device for the first time, the local administrator must change the password. To configure a local administrator with a specified user name not to change the password upon the first login, run the **local-user** *user-name* **password-force-change disable** command.
* After the permissions (such as the password, access type, FTP directory, and privilege level) of a local account are changed, the permissions of online users remain unchanged, and new users obtain new permissions when they go online.
* If the user name configured after the **local-user** command is run conflicts with the command keyword, the command keyword takes effect first.
* Telnet and FTP login modes pose security risks, and STelnet and SFTP login modes are recommended. If the STelnet or SFTP login mode is used, you need to set the user access type to SSH.
* After the FIPS mode is enabled, protocols and algorithms with low security cannot be used. The following describes the impact on the configuration of local administrators:
  + The **telnet** and **ftp** parameters in the [**local-user service-type**](cmdqueryname=local-user+service-type) command are unavailable.
  + The **ftp-directory** parameter in the [**local-user**](cmdqueryname=local-user) command is unavailable.
* After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary (which can be queried using the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command) cannot be specified in the following commands for configuring local administrators:
  + [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *ir-password*
  + [**local-user**](cmdqueryname=local-user) *user-name* **password**
  + **local-user change-password**


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. (Optional) Enable user name complexity check for local administrators.
   
   
   ```
   [undo local-aaa-user user-name complexity-check disable](cmdqueryname=undo+local-aaa-user+user-name+complexity-check+disable)
   ```
   
   By default, user name complexity check is enabled for local administrators.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * To prevent accounts from being stolen due to simple passwords, run this command to set the minimum length for the user name of a local administrator to six characters.
   * To disable user name complexity check, run the [**local-aaa-user user-name complexity-check disable**](cmdqueryname=local-aaa-user+user-name+complexity-check+disable) command. After this function is disabled, you can configure a user name with less than six characters. A simple user name, however, has security risks.
4. Create a local administrator and configure a password for the local administrator. Use either of the following methods:
   
   
   * Configure the password directly.
     ```
     [local-user](cmdqueryname=local-user) user-name password irreversible-cipher ir-password
     ```
   * Enter the password in interactive mode.
     ```
     [local-user](cmdqueryname=local-user) user-name password
     ```
5. Configure an access type for the local administrator.
   
   
   ```
   [local-user](cmdqueryname=local-user) user-name service-type { none | { http | ftp | ssh | telnet | terminal | snmp | md-cli }* }
   ```
6. (Optional) Configure other information about the local administrator as required.
   
   
   
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set a privilege level for the local administrator. | [**local-user**](cmdqueryname=local-user) *user-name* **privilege** **level** *level* | By default, no privilege level is configured for a local administrator. |
   | Configure the FTP directory to which the specified FTP user is allowed access. | [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* [ **read** **execute** [ **write** ] ] | By default, the FTP directory to which an FTP user is allowed access is not specified.  If the access type of a local user is set to FTP, the FTP directory must be configured for the local user and the privilege level of the local user cannot be lower than the management level. Otherwise, the FTP user will be unable to log in to the device.  If the **read** **execute** and **write** parameters are not set, the user has the read, write, and execute permissions by default. |
   | Set the state of the local administrator. | [**local-user**](cmdqueryname=local-user) *user-name* **state** { **active** | **block** } | By default, a local administrator is in active state.  The following describes how the device handles authentication requests of users in active or block state:  * active state: The device accepts the authentication request of the user and performs further processing. * block state: The device rejects the authentication request of the user. |
   | Configure the validity period of the local administrator account. | [**local-user**](cmdqueryname=local-user) *user-name* **expire-date** *expire-date* | By default, a local administrator account is valid permanently. |
   | Configure an access time range for the local administrator. | **[**local-user**](cmdqueryname=local-user)** *user-name* **time-range** *time-name* | By default, no access time range is configured for local administrators. In this case, local administrators are allowed access to the network anytime. |
   | Set the idle timeout period for the local administrator. | [**local-user**](cmdqueryname=local-user) *user-name* **idle-timeout** *minutes* [ *seconds* ] | You can set the timeout period of a user interface. If local administrators have been idle for longer than the specified period, they automatically go offline.  If *minutes* [ *seconds* ] is set to 0, the idle disconnection function is disabled.  If the idle timeout period of a user connection is set to 0 or a large value, the terminal will remain connected to a device. This poses security risks. In such cases, you are advised to run the [**lock**](cmdqueryname=lock) command to lock out the connection. |
   | Set the maximum number of connections that can be established by the specified local administrator. | [**local-user**](cmdqueryname=local-user) *user-name* **access-limit** *max-number* | By default, the number of connections that can be established by local administrators is not limited. It is determined by the device specifications.  To configure a local user to log in through only one terminal, set *max-number* to 1. |
7. (Optional) Configure a password policy for local administrators.
   
   
   1. Enable the password policy for local administrators and enter the local administrator password policy view.
      ```
      [local-aaa-user password policy administrator](cmdqueryname=local-aaa-user+password+policy+administrator)
      ```
      
      By default, the password policy for local administrators is enabled.
   2. Enable the password expiry notification function and set the number of days in advance users are notified that their passwords are about to expire.
      ```
      [password alert before-expire](cmdqueryname=password+alert+before-expire) days
      ```
      
      By default, the device prompts users to change their passwords 30 days before their passwords expire.
   3. Enable the function of prompting users to change the password (configured during the creation of the users).
      ```
      [password alert original](cmdqueryname=password+alert+original)
      ```
      
      By default, the function of prompting users to change the password (configured during the creation of the users) is enabled.
      
      By default, when a local administrator logs in for the first time, the system prompts the administrator to change the password. The administrator must change the password configured for the first time. To configure a local administrator with a specified user name not to change the password upon the first login, run the **local-user** *user-name* **password-force-change disable** command.
      
      After you run the **undo password alert original** command to disable the function of prompting users to change the password upon the first login, the **undo local-user** *user-name* **password-force-change disable** command does not take effect. That is, administrators are not configured to change the password.
   4. Enable the password expiry notification function and set the password validity period.
      ```
      [password expire](cmdqueryname=password+expire) days
      ```
      
      By default, the password validity period is 90 days.
   5. Enable the function of checking the similarity between the local administrator password and user name.
      ```
      [undo password similar-to-name-check disable](cmdqueryname=undo+password+similar-to-name-check+disable)
      ```
      
      By default, the function of checking the similarity between the local administrator password and user name is enabled.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * To prevent security problems such as simple user names and account theft, run this command to set the password of a local administrator. The password cannot repeat or reverse the user name.
      * To disable the function of checking the similarity between the local administrator password and user name, run the [**password similar-to-name-check disable**](cmdqueryname=password+similar-to-name-check+disable) command. After this function is disabled, you can configure a password that is similar to the user name. Such a password, however, is too simple and has security risks.
   6. Enable password complexity check.
      ```
      [password complexity](cmdqueryname=password+complexity) { two-of-kinds | three-of-kinds | four-of-kinds }
      ```
      
      By default, the device checks whether a password contains at least four types of characters.
      
      If the password complexity is low, the device has security risks. You are advised to set the password according to highest password complexity. That is, the password contains four types of the following characters: uppercase letters, lowercase letters, digits, and special characters. In addition, you need to change the password periodically.
   7. Set the maximum number of historical passwords recorded for each user.
      ```
      [password history record number](cmdqueryname=password+history+record+number) number
      ```
      
      By default, a maximum of 10 historical passwords are recorded for each user. That is, the new password cannot be the same as the last 10 passwords.
      
      * When a user changes the password, the device compares the new password against the historical passwords stored on the device. If the new password is the same as a stored password, the device displays an error message to prompt the user that password change fails.
      * When the number of recorded historical passwords reaches the maximum value, the later password will overwrite the earliest password on the device.
      * After the historical password recording function is disabled (that is, the maximum number of historical passwords recorded for each user is 0), the device does not record historical passwords; however, the passwords that have been stored are retained.
   8. Set the minimum length of a local user password.
      ```
      [password min-length](cmdqueryname=password+min-length) password-min-length
      ```
      
      By default, the minimum length of a local user password is 8.
   9. Return to the AAA view.
      ```
      [quit](cmdqueryname=quit)
      ```
8. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **[**display local-user**](cmdqueryname=display+local-user)** [ **domain** *domain-name* | **username** *user-name* | **state** { **active** | **block** } ] \* command to check the attributes of local administrators.
* Run the **[**display local-aaa-user password policy**](cmdqueryname=display+local-aaa-user+password+policy)** **administrator** command to check the password policy of local administrators.
* Run the **[**display local-user expire-time**](cmdqueryname=display+local-user+expire-time)** command to check the expiry time of local administrators.