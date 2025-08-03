Example for Configuring Services in Immediate Validation Mode
=============================================================

This section describes how to configure services on a Router in immediate validation mode.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360010__fig_dc_vrp_cfgm_cfg_004001), the Router is connected to the PC.

**Figure 1** Configuring services in immediate validation mode
  
![](images/fig_dc_vrp_cfgm_cfg_004001.png)  

To enable services to take effect immediately after they are configured, configure the services in immediate validation mode.

After you enter a command and press **Enter**, the system performs a syntax check. If the check is successful, the configuration immediately takes effect.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the immediate validation mode.
2. Configure a service.

#### Data Preparation

To complete the configuration, you need an interface IP address.


#### Procedure

1. Configure the immediate validation mode.
   
   
   ```
   <HUAWEI> system-view immediately
   ```
2. Configure a service.
   
   
   
   # Set the IP address of GigabitEthernet 0/1/4 to 10.1.1.1 on the Router.
   
   ```
   [HUAWEI] interface GigabitEthernet 0/1/4
   ```
   ```
   [HUAWEI-GigabitEthernet0/1/4] ip address 10.1.1.1 24
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