Example for One User to Configure Services After Another User Locks Configurations in Two-Phase Validation Mode
===============================================================================================================

This section provides an example for one user to configure services on a Router after another user locks configurations.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360013__fig_dc_vrp_cfgm_cfg_004101), both user A and user B log in to the Router. After user A locks configurations on the Router, user B attempts to configure services on the Router.

**Figure 1** Networking for one user to configure services after another user locks configurations in two-phase validation mode
  
![](images/fig_dc_vrp_cfgm_cfg_004101.png)  

To use the running database exclusively, lock configurations on the router to prevent other users from configuring services or committing configurations. In this case, the system displays a message indicating that the configuration is locked by a user when other users attempt to perform configurations. Other users can configure services in the running database only after you unlock configurations.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Simulate a situation in which user A locks configurations.
2. Simulate a situation in which user B configures a service.

#### Data Preparation

To complete the configuration, you need an interface IP address.


#### Procedure

1. Simulate a situation in which user A locks configurations.
   
   
   ```
   <HUAWEI> configuration exclusive
   ```
2. Simulate a situation in which user B configures a service.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/4
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/4] ip address 10.1.1.1 24
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
   ```
   Error: The configuration is locked by other user. [Session ID = 407]
   ```

#### Configuration Files

```
# 
```
```
sysname HUAWEI 
```
```
# 
```
```
interface GigabitEthernet0/1/4
 undo shutdown
#    
```