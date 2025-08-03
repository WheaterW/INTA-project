Example for Outputting Information to an SNMP Agent
===================================================

After information is output to an SNMP agent, the NMS can receive the information from the Device through an SNMP agent.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361209__fig_dc_vrp_logs_cfg_204401), a Device is connected to the NMS. To monitor the Device operation in real time or collect important information about the Device operation, you can output traps to an SNMP agent. The SNMP agent forwards the information to an NMS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, traps are output to a remote terminal.


**Figure 1** Outputting traps to an SNMP agent  
![](images/fig_dc_vrp_logs_cfg_204401.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE 0/1/0.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the information management function.
2. Configure the channel through which traps are output to an SNMP agent and the module of which traps are to be output.
3. Output traps to an SNMP agent.
4. Output traps to an NMS through an SNMP agent.

#### Data Preparation

To complete the configuration, you need the following data:

* Information channel number
* Module and severity of the traps to be output

#### Procedure

1. Configure available routes between the Router and the NMSs. Details for the configuration procedure are not provided here.
2. Enable the information management function.
   
   
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
3. Configure the channel through which traps are output to an SNMP agent and the module of which traps are to be output.
   
   
   
   # Output traps whose severity is informational or higher to channel 7.
   
   ```
   [*Device] info-center source im channel channel7 trap level informational
   ```
4. Output traps to an SNMP agent.
   
   
   ```
   [*Device] info-center snmp channel channel7
   ```
5. Output traps to the NMS through an SNMP agent.
   
   
   
   # Enable the SNMP agent function, with the SNMP version of SNMPv3.
   
   ```
   [*Device] snmp-agent sys-info version v3
   ```
   
   # Enable the SNMP agent to send traps.
   
   ```
   [*Device] snmp-agent trap enable
   ```
   ```
   [*Device] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname cipher public
   ```
   ```
   [*Device] commit
   ```
6. Verify the configuration.
   
   
   
   # Display the channel used by the SNMP agent to output traps.
   
   ```
   [~Device] display info-center
   ```
   ```
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
   [~Device] display channel 7
   ```
   ```
   channel number:7, channel name:channel7
   ModuID   Name          Enable LogLevel      Enable TrapLevel     Enable DebugLevel   
   ffffffff default       Y      debugging     Y      debugging     N      debugging    
   00000957 IM            Y      debugging     Y      informational N      debugging  
   ```
   
   # Display trap information output by the SNMP agent to the NMS.
   
   ```
   [~Device] display snmp-agent target-host
   Target-host NO. 1
   -----------------------------------------------------------
     Host-name                        : targetHost_2
     IP-address                       : 10.1.1.1
     Source interface                 : -
     VPN instance                     : -
     Security name                    : %^%#-(}fC-|38%RgqpW$+c^UU"AH()$q#K26fL2X5XK7%^%#
     Port                             : 162
     Type                             : trap
     Version                          : v3
     Level                            : No authentication and privacy
     NMS type                         : HW NMS
     With ext-vb                      : No
     Notification filter profile name : -  
   -----------------------------------------------------------
   ```

#### Configuration Files

```
#
sysname Device
#
info-center source im channel 7 trap level informational
info-center snmp channel 7
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 10.1.1.2 255.255.255.0
#
snmp-agent
#
snmp-agent sys-info version v3
snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname cipher %^%#-(}fC-|38%RgqpW$+c^UU"AH()$q#K26fL2X5XK7%^%#
#
snmp-agent trap enable
#
return
```