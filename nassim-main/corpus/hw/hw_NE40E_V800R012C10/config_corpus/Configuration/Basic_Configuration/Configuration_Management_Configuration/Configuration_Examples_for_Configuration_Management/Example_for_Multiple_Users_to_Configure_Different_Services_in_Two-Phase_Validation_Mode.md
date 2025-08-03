Example for Multiple Users to Configure Different Services in Two-Phase Validation Mode
=======================================================================================

This section provides an example for multiple users to configure different services on a Router.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360022__fig_dc_vrp_cfgm_cfg_003501), both user A and user B log in to the Router. User A and user B configure different services on the Router.

**Figure 1** Networking for multiple users to configure different services in two-phase validation mode  
![](images/fig_dc_vrp_cfgm_cfg_003501.png)  

The configurations committed by user A and user B both take effect.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Simulate a situation in which user A and user B configure different services.
2. Simulate a situation in which user A commits the configuration.
3. Simulate a situation in which user B commits the configuration.

#### Data Preparation

To complete the configuration, you need an interface IP address.


#### Procedure

1. Simulate a situation in which user A and user B configure different services.
   
   
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
   * Simulate a situation in which user B enables the SFTP server function.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sftp server enable
     ```
2. Simulate a situation in which user A commits the configuration.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
3. Simulate a situation in which user B commits the configuration.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/4] commit
   ```
   
   The following command output indicates that the configuration committed by user B has been added to the configuration file.
   
   ```
   <HUAWEI> display current-configuration
   #
   sftp server enable
   #
   interface GigabitEthernet0/1/4
    undo shutdown
    ip address 10.1.1.1 255.255.255.0
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
```
sftp server enable
```
```
#
```
```
return
```