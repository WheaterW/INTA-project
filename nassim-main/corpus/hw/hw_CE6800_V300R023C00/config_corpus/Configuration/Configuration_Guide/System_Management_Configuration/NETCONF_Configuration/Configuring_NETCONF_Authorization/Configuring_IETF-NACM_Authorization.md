Configuring IETF-NACM Authorization
===================================

Configuring IETF-NACM Authorization

#### Context

NACM authorization is an IETF-defined, more flexible authorization mode. NACM authorization rules allow you to define NACM authorization rules to control specific users' permissions to perform NETCONF operations and access NETCONF resources.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the NETCONF user interface view.
   
   
   ```
   [netconf](cmdqueryname=netconf)
   ```
3. Enter the NACM view.
   
   
   ```
   [nacm](cmdqueryname=nacm)
   ```
4. Enable the NACM function.
   
   
   ```
   [nacm enable](cmdqueryname=nacm+enable)
   ```
5. (Optional) Configure the operation permissions of a user as required.
   
   
   
   **Table 1** A user's operation permissions
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the user's permission on query operations. | [**read-default permit**](cmdqueryname=read-default+permit) | By default, the user's permission on query operations is disabled. |
   | Configure the user's permission on configuration operations. | [**write-default permit**](cmdqueryname=write-default+permit) | By default, a user's permission on configuration operations is disabled. |
   | Configure the user's default execution permission on RPC operations. | [**execute-default permit**](cmdqueryname=execute-default+permit) | By default, the user's permission on RPC operations is enabled. |
6. Create an NACM user group and enter the NACM user group view.
   
   
   ```
   [group-name](cmdqueryname=group-name) group-name
   ```
7. Create a user in the NACM user group.
   
   
   ```
   [user-name](cmdqueryname=user-name) user-name
   ```
8. Exit the NACM user group view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
10. Create a NACM authorization rule list and enter the NACM authorization rule list view.
    
    
    ```
    [rule-list-name](cmdqueryname=rule-list-name) list-name
    ```
11. Associate the NACM user group with the NACM authentication rule list.
    
    
    ```
    [group](cmdqueryname=group) group-name
    ```
12. Configure an NACM authorization rule name in the NACM authorization rule list view.
    
    
    ```
    [rule-name](cmdqueryname=rule-name) rule-name action { permit | deny }
    ```
13. (Optional) Configure a description for the NACM authorization rule list.
    
    
    ```
    [description](cmdqueryname=description) description
    ```
14. Configure the name of a feature module allowed for access.
    
    
    ```
    [module-name](cmdqueryname=module-name) module-name
    ```
    
    By default, the feature module name is an asterisk (\*), indicating all features.
15. Configure an NACM authorization rule type.
    
    
    ```
    [rule-type](cmdqueryname=rule-type) { rpc-name rpc-name | notification-name notification-name | path path }
    ```
16. Configure protocol operations.
    
    
    ```
    [access-operation](cmdqueryname=access-operation) { { create | read | update | delete | exec } * | * }
    ```
17. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```