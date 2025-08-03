Example for Configuring the Device to Output Logs to a Log File
===============================================================

Example for Configuring the Device to Output Logs to a Log File

#### Networking Requirements

Information can be saved as files on a device. If a fault occurs on the device, log files can be exported and used for fault locating. As shown in [Figure 1](#EN-US_TASK_0000001513039378__fig3344141161119), log information can be saved in the log file of DeviceA. If there are a large number of log files, you can configure the device to send them to an external server (for example, an SFTP server) to reduce storage resource consumption and implement unified maintenance. DeviceA is connected to the SFTP server through a network, and there are reachable routes between DeviceA and the SFTP server. Maintenance personnel can view logs generated on DeviceA on the SFTP server to query the running status of DeviceA.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


**Figure 1** Network diagram of outputting logs to a log file  
![](figure/en-us_image_0000001513159418.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the AAA authentication mode.
2. Enable the IM function.
3. Configure a channel and a rule for outputting logs to a log file.
4. Configure the device to send log files to the SFTP server.

#### Procedure

1. Configure a routing protocol to ensure that there are reachable routes between the device and SFTP server. For details, see Configuration Scripts.
2. Configure the SFTP server function and parameters, create an SSH user, and set the authentication mode to AAA authentication.
3. Enable the IM function.
   
   
   ```
   <HUAWEI> system-view
   [*HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] info-center enable
   ```
4. Configure a channel and a rule for outputting logs to a log file.
   
   
   
   # Specify a channel through which logs are output to a log file.
   
   ```
   [*DeviceA] info-center logfile channel channel8
   [*DeviceA] commit
   ```
   
   
   
   # Configure a rule for outputting logs to an information channel, allowing the output of IM information and information with a severity level higher than warning.
   
   ```
   [~DeviceA] info-center source im channel channel8 log level warning
   [*DeviceA] commit
   [~DeviceA] quit
   ```
5. Configure the device to send the log file to the SFTP server.
   
   
   
   # Switch to the save path of the log file.
   
   ```
   <DeviceA> cd flash:
   ```
   
   # Log in to the SFTP server.
   
   ```
   <DeviceA> system-view
   [~DeviceA] ssh client first-time enable
   [*DeviceA] commit
   [~DeviceA] sftp 10.2.1.2 
   Trying 10.2.1.2 ...
   Press CTRL+K to abort
   Connected to 10.2.1.2 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it? [Y/N]:y
   The keyname:10.2.1.2 already exists. Update it? [Y/N]:n  
   
   Please input the username: admin123
   Enter password:
   sftp-client>
   ```
   
   # Configure the device to transfer the log file to the SFTP server.
   
   ```
   sftp-client> put log_17_20110504041811.log
   sftp-client> quit
   ```

#### Verifying the Configuration

# View the logs output through the channel.

```
<DeviceA> display info-center
Information Center:enabled
Log host:
        10.0.0.1, channel number 2, channel name loghost,
language English , host facility local7
Console:
        channel number : 0, channel name : console
Monitor:
        channel number : 1, channel name : monitor
SNMP Agent:
        channel number : 5, channel name : snmpagent
Log buffer:
        enabled,max buffer size 10240, current buffer size 512,
current messages 10, channel number : 4, channel name : logbuffer
dropped messages 0, overwritten messages 0
Trap buffer:
        enabled,max buffer size 1024, current buffer size 256,
current messages 3, channel number:3, channel name:trapbuffer
dropped messages 0, overwritten messages 0
logfile:
        channel number : 8, channel name : channel8, language : English
Information timestamp setting:
        log - date, trap - date, debug - date millisecond
```

#### Configuration Scripts

```
#
sysname DeviceA
info-center enable
#
info-center logfile channel channel8
info-center source im channel channel8 log level warning
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.2.1.1 255.255.0.0
#
ssh client first-time enable 
# 
return
```