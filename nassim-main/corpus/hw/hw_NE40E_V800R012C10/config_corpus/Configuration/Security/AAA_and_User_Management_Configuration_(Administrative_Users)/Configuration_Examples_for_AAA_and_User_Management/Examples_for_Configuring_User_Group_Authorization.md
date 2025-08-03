Examples for Configuring User Group Authorization
=================================================

This section provides an example for configuring user group authentication on a network so that the user groups **network** and **service** in the domain **huawei** can manage the routing module and service module respectively.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371839__fig_dc_vrp_aaa_cfg_102101), two administrators (**adminA** and **adminB**) simultaneously manage the Device. To normalize the operations, **adminA** and **adminB** are required to manage the route module and MPLS module, respectively. In addition, they have no permission to operate each other's module.

**Figure 1** User group authorization  
![](images/fig_dc_vrp_aaa_cfg_102101.png)  


#### Precautions

During the configuration, note the following:

* **adminA** and **adminB** must belong to different user groups.
* The user groups to which **adminA** and **adminB** belong cannot overlap on routes or MPLS permissions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure task groups and add task instances of the corresponding modules.
2. Configure user groups and add corresponding task groups.
3. Configure users and specify user groups for them.

#### Data Preparation

To complete the configuration, you need the following data:

* Task group names
* User group names
* Domain name
* Local authentication for users

#### Procedure

1. Configure task groups.
   
   
   
   # Configure a task group for the routing module.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] task-group route
   ```
   ```
   [*Device-aaa-task-group-route] task ospf read write
   ```
   ```
   [*Device-aaa-task-group-route] task isis read write
   ```
   ```
   [*Device-aaa-task-group-route] task bgp read write
   ```
   ```
   [*Device-aaa-task-group-route] commit
   ```
   ```
   [~Device-aaa-task-group-route] quit
   ```
   
   # Configure a task group for the MPLS module.
   
   ```
   [~Device-aaa] task-group mpls
   [*Device-aaa-task-group-mpls] task mpls-base read write
   [*Device-aaa-task-group-mpls] task mpls-ldp read write
   [*Device-aaa-task-group-mpls] task mpls-te read write
   [*Device-aaa-task-group-mpls] commit
   [~Device-aaa-task-group-mpls] quit
   ```
2. Configure user groups.
   
   
   
   # Configure the user group **groupA**.
   
   ```
   [~Device-aaa] user-group groupA
   [*Device-aaa-user-group-groupa] task-group route
   [*Device-aaa-user-group-groupa] commit
   [~Device-aaa-user-group-groupa] quit
   ```
   
   # Configure the user group **groupB**.
   
   ```
   [~Device-aaa] user-group groupB
   [*Device-aaa-user-group-groupb] task-group mpls
   [*Device-aaa-user-group-groupb] commit
   [~Device-aaa-user-group-groupb] quit
   ```
3. Configure users.
   
   
   
   Configure the user **adminA**.
   
   ```
   [~Device-aaa] local-user adminA password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   [*Device-aaa] local-user adminA user-group groupA
   [*Device-aaa] commit
   ```
   
   Configure the user **adminB**.
   
   ```
   [~Device-aaa] local-user adminB password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   [*Device-aaa] local-user adminB user-group groupB
   [*Device-aaa] commit
   ```
4. Verify the configuration.
   
   
   
   After the preceding configurations are complete, run the [**display task-group**](cmdqueryname=display+task-group) [ *task-group-name* ] command to check the user group information.
   
   ```
   <Device> display task-group route
   -----------------------------------------------------------
   Task group name     : route
   -----------------------------------------------------------
   
   Task authorization
   -----------------------------------------------------------
   TaskName                          Authorization            
   -----------------------------------------------------------
   ospf                              read write               
   bgp                               read write               
   interface-mgr                     read write execute       
   config                            read write execute       
   vlan                              read write execute       
   isis                              read write               
   shell                             read write execute       
   cli                               read execute             
   -----------------------------------------------------------
   Total 8, 8 printed
   ```

#### Configuration Files

```
#
diffserv domain default
#
admin
#
user-interface con 0
#
 aaa
 #
 authentication-scheme default
 #
 authorization-scheme default
 #
 accounting-scheme default
 #
 task-group route
  task ospf read write
  task bgp read write
  task isis read write
 #
 task-group mpls
  task mpls-base read write
  task mpls-ldp read write
  task mpls-te read write
 #
 user-group groupa
  task-group route
 #
 user-group groupb
  task-group mpls
 #
 domain default
 local-user admina password cipher %^%#pPgn;|W90$J72.Ak$Y,IQ:gqIfPBTLjqW%,N`M_~%^%#
 local-user admina user-group groupa
 local-user adminb password cipher %^%#pPgn4@^7&QB*OY_,UMTLjqW%D0PV(YTLjqW%O1!!%^%#
 local-user adminb user-group groupb
 #
 task defaultTask1
 #
 task defaultTask2
return  
```