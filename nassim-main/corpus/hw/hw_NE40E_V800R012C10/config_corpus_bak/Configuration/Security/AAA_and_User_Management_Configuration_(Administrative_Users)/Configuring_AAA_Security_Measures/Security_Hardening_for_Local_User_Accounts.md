Security Hardening for Local User Accounts
==========================================

To enhance the security of local accounts, you can configure the maximum number of user login failures, password complexity restriction, and minimum password length.

#### Context

To prevent security issues such as account theft caused by simple usernames and passwords and excessive login failures, you can improve password complexity and limit the number of login failures. This helps enhance system security.

If the login password does not satisfy the security hardening policy, the system prompts you to change your password. Change your password based on the prompted message.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-security-policy enable**](cmdqueryname=user-security-policy+enable)
   
   
   
   A security policy is configured for local user accounts.
3. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
4. Perform the following configurations in the AAA view to improve user security as required.
   
   
   
   **Table 1** Configurations to improve user security in the AAA view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Enable forced change of initial password for local users. | [**undo user-password password-force-change**](cmdqueryname=undo+user-password+password-force-change) **disable** | * If the current device version supports forced change of initial password for local users, this function is enabled by default, and you do not need to run this command. When a local user created or reset by the administrator logs in for the first time, the user is forced to change the initial password. To ensure user security, you are advised not to disable this function. * If the device is upgraded from an earlier version that does not support forced change of initial password for local users to a later version that supports this function, this function is disabled by default. That is, the [**user-password password-force-change disable**](cmdqueryname=user-password+password-force-change+disable) command is delivered by default. In this case, you can run this command to enable forced change of initial password for local users to improve user security. * To disable forced change of initial password upon first login for a specified user, run the [**local-user**](cmdqueryname=local-user) *user-name* **password-force-change disable** command. This function may bring security risks. Exercise caution when performing this operation. |
   | Configure the minimum username length for local users. | [**user-name minimum-length**](cmdqueryname=user-name+minimum-length) *length* | After this command is run, the newly created local username must comply with the command configuration. Otherwise, the user cannot be created. |
   | Configure the minimum password length for local users. | [**user-password min-len**](cmdqueryname=user-password+min-len) *min-length* | This command applies to passwords in plain text only. |
   | Enable password complexity check for local users. | [**user-password complexity-check**](cmdqueryname=user-password+complexity-check) | - |
   | Configure the number of historical passwords that cannot be used as a new password for local users. | [**user-password history-password-check**](cmdqueryname=user-password+history-password-check) *historyPwdNum* | - |
   | Configure the function to prompt a local administrator to change the initial password upon the next login. | [**user-password change**](cmdqueryname=user-password+change) | - |
   | Configure the aging period of a local account. | * [**user-aging**](cmdqueryname=user-aging) *aging-period* * [**local-user**](cmdqueryname=local-user) *user-name* **aging** *aging-period* | To age a local user account that has been idle for a long time, run this command. If a user account remains idle for a configured aging period, the user account automatically ages.  The [**user-aging**](cmdqueryname=user-aging) command applies to all users in the system. The [**local-user**](cmdqueryname=local-user) **aging** command applies only to a specified user. When an aging period has been configured for all users using the [**user-aging**](cmdqueryname=user-aging) command: * If the [**local-user**](cmdqueryname=local-user) **aging** command is not run, the aging time configured using the [**user-aging**](cmdqueryname=user-aging) command takes effect. * If the [**local-user**](cmdqueryname=local-user) **aging** command is run, the aging time configured using the [**local-user**](cmdqueryname=local-user) **aging** command takes effect. |
   | Configure an expiration date for a local user account. | [**local-user**](cmdqueryname=local-user) *user-name* **expire** *date* | If all administrator users (terminal, Telnet, FTP, and SSH users) on a device have an expiration date configured for their accounts, the account that expires last (that is, the administrator whose account expires last) remains valid. This prevents all user accounts on the device from expiring. |
   | Configure the period after which a local user password expires. | [**local-user**](cmdqueryname=local-user) *user-name* **password expire** *days* | To harden network security, administrators can run the [**local-user password expire**](cmdqueryname=local-user+password+expire) command to configure the period after which a password expires.  When the password is changed, the system resets the period.  The command applies only to local users. After a password expires, reconfigure a new password for the user. Otherwise, user login fails. |
   | Set the password validity period and the period for advance warning before the password expires for administrators. | [**user-password expire**](cmdqueryname=user-password+expire) *expire-days* **prompt** *prompt-days* | To prevent administrator accounts from being stolen due to unchanged passwords and other security issues, run this command to set the password validity period and the period for advance warning before the password expires.  Only a level-3 or higher-level administrator can run the command.  * The command applies only to administrators and does not affect other local users. The system prompts the administrator to change the password *n* days before the password expires. * If the administrator does not change the password till the password expires, the administrator is denied access to the device. |
   | Configure the period during which a local user is allowed to log in. | [**local-user**](cmdqueryname=local-user) *user-name* **login-period** *begin-time* **to** *end-time* *begin-day* **to** *end-day* | - |
   | Set the state of a local user. | [**local-user**](cmdqueryname=local-user) *user-name* **state** { **active** | **block** [ **fail-times** *fail-times-value* **interval** *interval-value* ] } | - |
   | Configure alarm and alarm clearance thresholds within a specified period. | [**login-failed threshold-alarm**](cmdqueryname=login-failed+threshold-alarm) **upper-limit** *report-times* **lower-limit** *resume-times* **period** *period* | - |
5. Run **quit**
   
   
   
   Return to the system view.
6. Run [**local-aaa-server**](cmdqueryname=local-aaa-server)
   
   
   
   The local AAA server view is displayed.
7. Perform the following configurations in the local AAA view to improve user security as required.
   
   
   
   **Table 2** Configurations to improve user security in the local AAA view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Enable password complexity check for local users. | [**user-password complexity-check**](cmdqueryname=user-password+complexity-check) | - |
   | Configure the minimum password length for local users. | [**user-password min-len**](cmdqueryname=user-password+min-len) *min-length* | This command applies to passwords in plain text only. |
   | Configure the function to prompt a local administrator to change the initial password upon the next login. | [**user-password change**](cmdqueryname=user-password+change) | - |
   | Set the password validity period and the period for advance warning before the password expires. | [**user-password expire**](cmdqueryname=user-password+expire) *expire-days* **prompt** *prompt-days* | - |
   | Set the state of a local user to blocked. | [**user**](cmdqueryname=user) *username* **block** [ **fail-times** *fail-times-value* **interval** *interval-value* ] | - |
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

You can run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** *configuration-type* command to view the configuration.