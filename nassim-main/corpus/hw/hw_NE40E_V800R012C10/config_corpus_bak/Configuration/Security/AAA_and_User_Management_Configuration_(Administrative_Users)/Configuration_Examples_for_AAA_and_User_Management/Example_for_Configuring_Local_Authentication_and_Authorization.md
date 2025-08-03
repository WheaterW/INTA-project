Example for Configuring Local Authentication and Authorization
==============================================================

This section provides an example for configuring local authentication and authorization on a network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371842__fig_dc_vrp_aaa_cfg_102201), the administrator **admin@aaa** logs in to the Router through Telnet, and local authentication and authorization are used. This user can run all AAA commands and view ACL commands, but cannot configure ACL commands.

**Figure 1** Configuring local authentication and authorization  
![](images/fig_dc_vrp_aaa_cfg_102201.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a task group and add the task instance of the corresponding module.
2. Configure a user group, bind the user group to the corresponding task group, and bind the user group to a domain.
3. Configure a user and specify a user group for the user.
4. Configure authentication and authorization modes.

#### Data Preparation

To complete the configuration, you need the following data:

* Task group name
* User group name
* Domain name
* Local authentication is performed for users on the device.

#### Procedure

1. Configure a task group.
   
   
   
   # Create a task group.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] task-group admin
   ```
   
   # Add the AAA read and write task and ACL read-only task to the task group.
   
   ```
   [*HUAWEI-aaa-task-group-admin] task aaa execute write read
   ```
   ```
   [*HUAWEI-aaa-task-group-admin] task acl read
   ```
   ```
   [*HUAWEI-aaa-task-group-admin] task config read write execute debug
   ```
   ```
   [*HUAWEI-aaa-task-group-admin] commit
   ```
   ```
   [~HUAWEI-aaa-task-group-admin] quit
   ```
2. Create a user group, bind the user group to a domain, and bind the task group to the user group.
   
   
   
   # Create a user group.
   
   ```
   [~HUAWEI-aaa] user-group admin
   ```
   
   # Bind the task group to the user group.
   
   ```
   [*HUAWEI-aaa-user-group-admin] task-group admin
   ```
   ```
   [*HUAWEI-aaa-user-group-admin] commit
   ```
   ```
   [~HUAWEI-aaa-user-group-admin] quit
   ```
3. Configure authentication and authorization schemes for the user.
   
   
   
   # Configure a local authentication scheme.
   
   ```
   [~HUAWEI-aaa] authentication-scheme localtype
   ```
   ```
   [*HUAWEI-aaa-authen-localtype] authentication-mode local
   ```
   ```
   [*HUAWEI-aaa-authen-localtype] commit
   ```
   ```
   [~HUAWEI-aaa-authen-localtype] quit
   ```
   
   # Configure a local authorization scheme.
   
   ```
   [~HUAWEI-aaa] authorization-scheme localtype
   ```
   ```
   [*HUAWEI-aaa-author-localtype] authorization-mode local
   ```
   ```
   [*HUAWEI-aaa-author-localtype] commit
   ```
   ```
   [~HUAWEI-aaa-author-localtype] quit
   ```
   
   # Apply the authentication and authorization schemes to a domain.
   
   ```
   [~HUAWEI-aaa] domain aaa
   ```
   ```
   [*HUAWEI-aaa-domain-aaa] authentication-scheme localtype
   ```
   ```
   [*HUAWEI-aaa-domain-aaa] authorization-scheme localtype
   ```
   ```
   [*HUAWEI-aaa-domain-aaa] commit
   ```
   ```
   [~HUAWEI-aaa-domain-aaa] quit
   ```
4. Create a local user.
   
   
   ```
   [~HUAWEI-aaa] local-user admin@aaa password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*HUAWEI-aaa] local-user admin@aaa user-group admin
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   ```
   [~HUAWEI] telnet server enable
   ```
   ```
   [*HUAWEI] commit
   ```
5. Verify the configuration.
   
   
   
   After completing the preceding configurations, the user goes online through Telnet. It is found that the user can run AAA commands and view ACL commands but cannot configure ACL commands.
   
   ```
   [~HUAWEI] acl 3000
   ```
   ```
   Error: No permission to run the command.
   ```

#### Configuration Files

```
#
aaa
 local-user admin@aaa password cipher %^%#pPgn;|W90$J72.Ak$Y,IQ:gqIfPBTLjqW%,N`M_~%^%#
 local-user admin@aaa user-group admin
 #
 authentication-scheme default
 #
 authentication-scheme localtype
 #
 authorization-scheme default
 #
 authorization-scheme localtype
 #
 accounting-scheme default
 #
 domain default
 #
 domain aaa
  authentication-scheme localtype
  authorization-scheme localtype
 #
 task-group admin
  task acl read  
  task aaa read write execute  
  task config read write execute debug
 #
 user-group admin
  task-group admin 
#
interface GigabitEthernet0/3/0
 undo shutdown
 ip address 10.137.217.251 255.255.254.0
#
ip route-static 0.0.0.0 0.0.0.0 10.137.216.1
#
user-interface vty 0 4
 authentication-mode aaa
return
```