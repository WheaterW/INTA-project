Example for Configuring the Device to Output Traps to an SNMP Agent
===================================================================

Example for Configuring the Device to Output Traps to an SNMP Agent

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563759713__fig4663143481017), DeviceA is connected to the NMS through a network, and reachable routes exist between DeviceA and the NMS. To enable the NMS to monitor the traps of DeviceA in real time and locate faults in a timely manner, configure the device to output traps to the SNMP agent. In this way, the SNMP agent sends the traps to the NMS. In this example, SNMPv3 is used.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


**Figure 1** Networking diagram of outputting traps to the SNMP agent  
![](figure/en-us_image_0000001512839886.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the IM function.
2. Configure a channel and rule for outputting traps to the SNMP agent.
3. Configure the SNMP agent to output traps to the NMS through SNMPv3.

#### Procedure

1. Configure reachable routes between the device and NMS. For details, see Configuration Scripts.
2. Enable the IM function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] info-center enable
   ```
3. Configure a channel and rule for outputting traps to the SNMP agent.
   
   
   
   # Specify the channel used by the device to output traps to an SNMP agent.
   
   ```
   [*DeviceA] info-center snmp channel channel7
   [*DeviceA] commit
   ```
   
   # Configure a rule for outputting traps to a channel.
   
   # Output traps whose severity is informational or higher to channel 7.
   
   ```
   [~DeviceA] info-center source im channel channel7 trap level informational
   [*DeviceA] commit
   ```
4. Output traps to the NMS through the SNMP agent.
   
   
   
   # Enable the SNMP agent function, with the SNMP version of SNMPv3.
   
   ```
   [~DeviceA] snmp-agent sys-info version v3
   [*DeviceA] commit
   ```
   
   # Configure the SNMP agent to send traps.
   
   ```
   [~DeviceA] snmp-agent mib-view include iso iso
   [*DeviceA] snmp-agent group v3 gtest privacy read-view iso write-view iso notify-view iso
   [*DeviceA] snmp-agent usm-user v3 test
   [*DeviceA] snmp-agent usm-user v3 test group gtest
   [*DeviceA] snmp-agent usm-user v3 test authentication-mode md5 cipher ******
   [*DeviceA] snmp-agent usm-user v3 test privacy-mode des56 cipher ******
   [*DeviceA] snmp-agent trap enable
   [*DeviceA] snmp-agent target-host host-name test123 tarp address udp-domain 10.1.1.1 params securityname test v3 privacy private-netmanager
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the channel through which traps are exported to the SNMP agent.

```
[~DeviceA] display info-center
Information Center:enabled
Log host:
Console:
        channel number : 0, channel name : console
Monitor:
        channel number : 1, channel name : monitor
SNMP Agent:
        channel number : 7, channel name : channel7
Log buffer:
        enabled,max buffer size 10240, current buffer size 512,
current messages 10, channel number : 4, channel name : logbuffer
dropped messages 0, overwritten messages 0
Trap buffer:
        enabled,max buffer size 1024, current buffer size 256,
current messages 3, channel number:3, channel name:trapbuffer
dropped messages 0, overwritten messages 0
logfile:
        channel number : 9, channel name : logfile, language : English
Information timestamp setting:
        log - date, trap - date, debug - date millisecond

```

# Display the information output to the SNMP agent through the channel.

```
[~DeviceA] display info-center channel 7
channel number:7, channel name:channel7
ModuID   Name          Enable LogLevel      Enable TrapLevel     Enable DebugLevel   
ffffffff default       Y      debugging     Y      debugging     N      debugging    
00000957 IM            Y      debugging     Y      informational N      debugging  
```

# Display trap information output by the SNMP agent to the NMS.

```
[~DeviceA] display snmp-agent target-host
Target-host NO. 1
-----------------------------------------------------------
  Host-name                        : targetHost_2
  IP-address                       : 10.1.1.1
  Source interface                 : -
  VPN instance                     : -
  Security name                    : %+%#-(}fC-|38%RgqpW$+c^UU"AH()$q#K26fL2X5XK7%+%#
  Port                             : 162
  Type                             : trap
  Version                          : v3
  Level                            : No authentication and privacy
  NMS type                         : HW NMS
  With ext-vb                      : No
  Notification filter profile name : - 
-----------------------------------------------------------
```

#### Configuration Scripts

```
#
sysname DeviceA
#
info-center source im channel 7 trap level informational
info-center snmp channel 7
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.2 255.255.0.0
#
snmp-agent
#
snmp-agent sys-info version v3
snmp-agent mib-view include iso iso
snmp-agent group v3 gtest privacy read-view iso write-view iso notify-view iso
snmp-agent usm-user v3 test
snmp-agent usm-user v3 test group gtest
snmp-agent usm-user v3 test authentication-mode md5 cipher %^%#7%%^p{1$d!X%_YQKZ{;(rPdQHXU.QSi9dw6FO[90%^%#
snmp-agent usm-user v3 test privacy-mode des56 cipher %^%#ntE.+A4@16fmc.<'_D{:ifwI#d''@05kV5[*idr2<%^%#
snmp-agent trap enable
snmp-agent target-host host-name test123 tarp address udp-domain 10.1.1.1 params securityname test v3 privacy private-netmanager
#
snmp-agent trap enable
#
return
```