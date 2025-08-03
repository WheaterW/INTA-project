Example for Configuring the Device to Output Debugging Messages to the Console
==============================================================================

Example for Configuring the Device to Output Debugging Messages to the Console

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563999645__fig11654113023015), the PC is connected to DeviceA through the console port. Users want to view debugging information about the ARP module on DeviceA on a PC to locate faults.

**Figure 1** Networking diagram of outputting debugging messages to the console  
![](figure/en-us_image_0000001564119561.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the IM function.
2. Configure a channel and rule for outputting debugging messages to the console.
3. Enable the terminal display function and debugging message display function.
4. Enable the debugging of the ARP module.

#### Procedure

1. Enable the IM function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [~HUAWEI] commit
   [~DeviceA] info-center enable
   ```
2. Configure a channel and rule for outputting debugging messages to the console.
   
   
   
   # Specify channel 0 to output debugging messages to the console.
   
   ```
   [~DeviceA] info-center console channel 0
   [~DeviceA] commit
   ```
   
   # Configure a rule for outputting debugging messages to the information channel, allow the debugging messages of the ARP module to be output on the console, and set the severity level to debugging.
   
   ```
   [~DeviceA] info-center source arp channel console debug level debugging
   [~DeviceA] commit
   [~DeviceA] quit
   ```
3. Enable the terminal display function and debugging message display function.
   
   
   ```
   <DeviceA> terminal monitor
   <DeviceA> terminal debugging
   ```
4. Enable the debugging of the ARP module.
   
   
   ```
   <DeviceA> debugging arp packet
   ```

#### Verifying the Configuration

# Display the channel information.

```
<DeviceA> display info-center channel 0
channel number:0, channel name:console
ModuID   Name          Enable LogLevel      Enable TrapLevel     Enable DebugLevel   
ffffffff default       Y      warning       Y      debugging     Y      debugging    
00000859 ARP           Y      warning       Y      debugging     Y      debugging   
```

#### Configuration Scripts

```
#
sysname DeviceA
#
info-center console channel 0
info-center source arp channel console debug level debugging
#
return
```