Example for Multiple Users to Perform the Same Configuration for a Service in Two-Phase Validation Mode
=======================================================================================================

This section provides an example for multiple users to perform the same configuration for a service on one Router in two-phase validation mode.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360016__fig_dc_vrp_cfgm_cfg_004201), both user A and user B log in to the Router. After user A configures a service on the Router, user B performs the same configuration for the service on the Router.

**Figure 1** Networking for multiple users to perform the same configuration for a service in two-phase validation mode
  
![](images/fig_dc_vrp_cfgm_cfg_004201.png)  

When the configuration committed by user B is the same as that committed by user A, the system notifies user B that the configuration conflicts with an existing configuration.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Simulate a situation in which user A and user B perform the same configuration for a service.
2. Simulate a situation in which user A commits the configuration.
3. Simulate a situation in which user B commits the configuration.

#### Data Preparation

To complete the configuration, you need an interface IP address.


#### Procedure

1. Simulate a situation in which user A and user B perform the same configuration for a service.
   
   
   * Simulate a situation in which user A sets the IP address of GigabitEthernet 0/1/4 to 10.1.1.1 on the Router.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] interface GigabitEthernet 0/1/4
     ```
     ```
     [~HUAWEI-GigabitEthernet0/1/4] ip address 10.1.1.1 24
     ```
   * Simulate a situation in which user B sets the IP address of GigabitEthernet 0/1/4 to 10.1.1.1 on the Router.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] interface GigabitEthernet 0/1/4
     ```
     ```
     [~HUAWEI-GigabitEthernet0/1/4] ip address 10.1.1.1 24
     ```
2. Simulate a situation in which user A commits the configuration.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
3. Simulate a situation in which user B commits the configuration.
   
   
   
   The system notifies user B that the configuration conflicts with an existing configuration.
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ip address 10.1.1.1 24
   Error: The address already exists.
   
   Commit canceled, the configuration conflicted with other user, you can modify 
   the configuration and commit again.
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
 ip address 10.1.1.1 255.255.255.0
#    
```