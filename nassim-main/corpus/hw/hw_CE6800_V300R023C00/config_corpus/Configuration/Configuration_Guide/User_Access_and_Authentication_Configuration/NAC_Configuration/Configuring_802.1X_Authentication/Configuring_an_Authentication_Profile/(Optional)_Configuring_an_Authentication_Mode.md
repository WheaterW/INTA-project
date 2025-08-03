(Optional) Configuring an Authentication Mode
=============================================

(Optional) Configuring an Authentication Mode

#### Context

[Table 1](#EN-US_TASK_0000001512681054__en-us_task_0000001563880209_table1245113532551) lists the NAC authentication modes that can be configured on interfaces. Administrators can configure the NAC authentication mode based on user access requirements.

**Table 1** NAC authentication modes
| Authentication Mode | Description | Application Scenario |
| --- | --- | --- |
| multi-authen | Indicates that the device authenticates each access user on an interface. If a user passes the authentication, the device grants independent network access rights to that user. If the user goes offline, other users are not affected. | This mode applies when multiple data terminals need to be connected to the network through an interface and high security is required.  This authentication mode enables you to configure the maximum number of access users on the interface based on the actual user quantity, preventing users on other interfaces from failing to go online due to malicious users occupying a large amount of device resources. |
| single-terminal | Indicates that the device allows only one user to go online on an interface. | This mode applies when only one data terminal needs to be connected to the network through an interface. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the authentication profile view.
   
   
   ```
   [authentication-profile](cmdqueryname=authentication-profile) name authentication-string
   ```
3. Configure an authentication mode.
   
   
   ```
   [authentication mode](cmdqueryname=authentication+mode) { single-terminal | multi-authen [ max-user max-user-number [ dot1x | none ] * ] }
   ```
   
   By default, the access authentication mode of an interface is **multi-authen**.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```