(Optional) Configuring a Service Scheme
=======================================

(Optional) Configuring a Service Scheme

#### Context

A service scheme is used to manage user authorization information in a unified manner. When a user needs multiple types of authorization information, you can use a service scheme to authorize the user. This simplifies server settings and facilitates authorization information management. When a service scheme is used for authorization, you only need to set the name of the service scheme on the server. The user obtains the name of the service scheme through server authorization, finds the service scheme with the specified name on the device, and obtains authorization information configured in the service scheme.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create a service scheme and enter the service scheme view.
   
   
   ```
   [service-scheme](cmdqueryname=service-scheme) service-scheme-name
   ```
4. Configure authorization information in the service scheme.
   
   
   
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the privilege level for administrators. | [**admin-user privilege level**](cmdqueryname=admin-user+privilege+level) *level* | The value of *level* ranges from 0 to 3. By default, no privilege level is configured. |
   | Configure a user VLAN. | [**user-vlan**](cmdqueryname=user-vlan) *vlan-id* | By default, no user VLAN is configured in a service scheme. |
   | Set the maximum number of users who are allowed to access the network using the same user name. | [**access-limit user-name max-num**](cmdqueryname=access-limit+user-name+max-num) *number* | By default, the number of users who are allowed to access the network using the same user name is determined by the maximum number of access users supported by the device. |
   | Configure an ACL. | **[**acl-id**](cmdqueryname=acl-id)** *acl-number* | By default, no ACL is bound to a service scheme.  The value of *acl-number* ranges from 3000 to 3999.  NOTE:  * Before running this command, ensure that an ACL has been created using the **acl** or **acl name** command, and ACL rules have been configured using the **rule** command. * The priorities of the following access policies are in descending order: ACL number delivered by the RADIUS server > ACL number configured on the local device > ACL rule or DACL group delivered by the RADIUS server through the HW-Data-Filter attribute numbered 26-82 > UCL group delivered by the RADIUS server > UCL group configured on the local device |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display service-scheme** [ **name** *name* ] command to check the service scheme configuration.