Configuring a Local Access User
===============================

Configuring a Local Access User

#### Context

When an access user uses local authentication and authorization, you need to configure a local access user.

![](public_sys-resources/note_3.0-en-us.png) 

After the permissions (such as the password and access type) of a local account are changed, the permissions of online users remain unchanged, and new users obtain new permissions when they go online.

Access users are supported only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S. Therefore, only these device models support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create a local access user and configure the password and access type for the user.
   
   
   1. Create a local access user and enter the local access user view.
      ```
      [local-access-user](cmdqueryname=local-access-user) user-name
      ```
   2. Configure the password for the local access user.
      ```
      [password](cmdqueryname=password) cipher password
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      * For device security purposes, change the password periodically.
      * A secure password must consist of at least two types of the following, uppercase letters, lowercase letters, digits, and special characters. In addition, the password cannot repeat or reverse the user name.
      * After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command) defined in the weak password dictionary cannot be specified in this command.
   3. Configure an access type for the local access user.
      ```
      [service-type](cmdqueryname=service-type) { none | dot1x  }
      ```
4. (Optional) Configure other information about the local access user as required.
   
   
   
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the state of the local access user. | [**state**](cmdqueryname=state) { **active** | **block** } | By default, a local access user is in active state.  The following describes how the device handles authentication requests of users in active or block state:  * active state: The device accepts the authentication request of the user and performs further processing. * block state: The device rejects the authentication request of the user. |
   | Configure the validity period of the local access user account. | [**expire-date**](cmdqueryname=expire-date) *expire-date* | By default, a local access account is valid permanently. |
   | Configure an access time range for the local access user. | [**time-range**](cmdqueryname=time-range) *time-name* | By default, no access time range is configured for local access users. In this case, local access users are allowed access to the network anytime. |
5. (Optional) Configure a password policy for the local access user.
   
   
   1. Enable the password policy for the local access user and enter the local access user password policy view.
      ```
      [local-aaa-user password policy access-user](cmdqueryname=local-aaa-user+password+policy+access-user)
      ```
      
      By default, the password policy for local access users is disabled. To clear the historical passwords of a local access user, run the [**reset local-access-user**](cmdqueryname=reset+local-access-user) *user-name* **[**password history record**](cmdqueryname=password+history+record)** command.
   2. Set the maximum number of historical passwords recorded for each user.
      ```
      [password history record number](cmdqueryname=password+history+record+number) number
      ```
      
      By default, a maximum of five historical passwords are recorded for each user.
   3. Return to the AAA view.
      ```
      [quit](cmdqueryname=quit)
      ```
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **[**display local-access-user**](cmdqueryname=display+local-access-user)** [ **domain** *domain-name* | **username** *user-name* | **state** { **active** | **block** } ] \* command to check the attributes of local access users.
* Run the **[**display local-aaa-user password policy**](cmdqueryname=display+local-aaa-user+password+policy)** **access-user** command to check the password policy of local access users.
* Run the **[**display local-access-user expire-time**](cmdqueryname=display+local-access-user+expire-time)** command to check the expiry time of local access users.