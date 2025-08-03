Example for Managing Configuration Files
========================================

This example shows you how to save configurations and set the configuration file to be loaded at the next startup.

#### Networking Requirements

As shown in[Figure 1](#EN-US_TASK_0172360028__fig_dc_vrp_cfgm_cfg_003601), the user logs in to the device to manage configuration files.

**Figure 1** Managing configuration files  
![](images/fig_dc_vrp_cfgm_cfg_003601.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Modify configurations.
2. Save configurations in a configuration file.
3. Specify the configuration file to be loaded at the next startup.
4. After a system upgrade, compare the current running configurations with those defined in the configuration file to be loaded at the next startup to check whether configurations are lost.

#### Procedure

1. Modify configurations.
   
   
   
   For example, enable the SFTP server function.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sftp server enable
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] quit
   ```
2. Save configurations to the configuration file **vrpcfg.cfg**.
   
   
   ```
   <HUAWEI> save vrpcfg.cfg
   ```
   ```
   Warning: Are you sure to save the configuration to vrpcfg.cfg? [Y/N]: y
   ```
3. Specify the configuration file to be loaded at the next startup.
   
   
   ```
   <HUAWEI> startup saved-configuration vrpcfg.cfg
   ```
4. After a system upgrade, compare the current running configurations with those defined in the configuration file to be loaded at the next startup to check whether configurations are lost.
   
   
   ```
   <HUAWEI> compare configuration
   ```
   ```
   The current configuration is the same as the next startup configuration file.
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
sftp server enable
```