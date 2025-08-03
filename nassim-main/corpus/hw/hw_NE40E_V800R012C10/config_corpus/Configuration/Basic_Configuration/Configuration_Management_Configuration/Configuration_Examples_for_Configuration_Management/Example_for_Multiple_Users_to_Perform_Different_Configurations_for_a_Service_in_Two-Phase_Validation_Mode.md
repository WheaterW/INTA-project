Example for Multiple Users to Perform Different Configurations for a Service in Two-Phase Validation Mode
=========================================================================================================

This section provides an example for multiple users to perform different configurations for a service on one Router.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360019__fig_dc_vrp_cfgm_cfg_003401), both user A and user B log in to the Router. After user A configures a service on the Router, user B performs a different configuration for the service on the router. For example, user A and user B configure different IP addresses on the same interface.

**Figure 1** Networking for multiple users to perform different configurations for a service in two-phase validation mode
  
![](images/fig_dc_vrp_cfgm_cfg_003401.png)  

The configuration committed by user B overwrites that committed by user A.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Simulate a situation in which user A and user B perform different configurations for a service.
2. Simulate a situation in which user A commits the configuration.
3. Simulate a situation in which user B commits the configuration.

#### Data Preparation

To complete the configuration, you need different interface IP addresses.


#### Procedure

1. Simulate a situation in which user A and user B perform different configurations for a service.
   
   
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
   * Simulate a situation in which user B sets the IP address of GigabitEthernet 0/1/4 to 10.1.1.2 on the Router.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] interface GigabitEthernet 0/1/4
     ```
     ```
     [~HUAWEI-GigabitEthernet0/1/4] ip address 10.1.1.2 24
     ```
2. Simulate a situation in which user A commits the configuration.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
3. Simulate a situation in which user B commits the configuration.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
   
   The following command output indicates that the configuration committed by user B has overwritten that committed by user A.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/4] display this
   #
   interface GigabitEthernet0/1/4
    undo shutdown
    ip address 10.1.1.2 255.255.255.0
   return 
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
 ip address 10.1.1.2 255.255.255.0
#    
```