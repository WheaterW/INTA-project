Example for Outputting Information to a Remote Terminal
=======================================================

Information can be output to a remote terminal for user query when faults occur on the Device.

#### Networking Requirements

A remote PC user logs in to the Device using Virtual Type Terminal (VTY) or Telnet, as shown in [Figure 1](#EN-US_TASK_0172361203__fig_dc_vrp_logs_cfg_204101). To check the operating status of an ARP module through a remote terminal, you can output debugging information of the ARP module to the remote terminal.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, debugging information is output to a remote terminal.


**Figure 1** Outputting information to a remote terminal  
![](images/fig_dc_vrp_logs_cfg_204101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the information management function.
2. Configure the module of which debugging information is to be output and set rules for outputting debugging information to the information channel.
3. Enable screen display and debugging on the terminal.
4. Enable the debugging of the ARP module.

#### Data Preparation

To complete the configuration, you need the following data:

* Information channel number
* Module and severity of the information to be output

#### Procedure

1. Enable the information center.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] info-center enable
   ```
2. Output debugging information about the ARP module to the remote terminal, and set the severity of information to debugging.
   
   
   ```
   [*Device] info-center source arp channel monitor debug level debugging
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] quit
   ```
3. Enable screen display and debugging.
   
   
   ```
   <Device> terminal monitor
   ```
   ```
   <Device> terminal debugging
   ```
4. Enable the debugging of the ARP module.
   
   
   ```
   <Device> debugging arp packet
   ```
5. Verify the configuration.
   
   
   
   # Display the channel information.
   
   ```
   <Device> display channel 1
   ```
   ```
   channel number:1, channel name:monitor
   ModuID   Name          Enable LogLevel      Enable TrapLevel     Enable DebugLevel   
   ffffffff default       Y      warning       Y      debugging     Y      debugging    
   00000859 ARP           Y      warning       Y      debugging     Y      debugging   
   ```

#### Configuration Files

```
#
sysname Device
#
```
```
info-center source arp channel 1
```
```
#
```
```
return
```