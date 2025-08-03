Example for Configuring Service Diagnosis
=========================================

Example for Configuring Service Diagnosis

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564117285__en-us_task_0200327165_fig168713817385), DeviceA connects to a user through interface 1 and to a log server through interface 2.

Maintenance personnel want to diagnose services for the online user with the MAC address of 00e0-fc12-3456 and export diagnostic information to the log server.

**Figure 1** Network diagram of service diagnosis![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 indicate 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001933979028.png)

#### Procedure

1. Configure a device name.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   ```
2. Enable the service diagnosis function.
   
   
   ```
   [~DeviceA] trace enable
   ```
3. Create a diagnosis object and export diagnostic information to a log server.
   
   
   ```
   [~DeviceA] trace object mac-address 00e0-fc12-3456 output syslog-server 10.10.20.2
   ```
4. Configure 100GE 1/0/2 as the source interface from which diagnostic information is exported to the log server.
   
   
   ```
   [~DeviceA] trace syslog source 100ge 1/0/2
   ```

#### Verifying the Configuration

* Run the [**display trace information**](cmdqueryname=display+trace+information) command to check information about service diagnosis.
  ```
  [~DeviceA] [display trace information](cmdqueryname=display+trace+information)
  Trace Information:                                                              
  ------------------------------------------------------------                    
  Trace Enable                            : Enable                                
  Debug info level                        : Detail                                
  Debug fill-instance                     : Off                                   
  Debug quit-instance                     : Off                                   
  Debug output information                : Off                                   
  Syslog Source IP Address                : 10.10.20.1                               
  
  The sum of all the instances            : 0                                     
  The startID of the instance table       : -                                     
  Alloc instance times                    : 32                                    
  Free instance times                     : 32                                    
  The sum of all the objects              : 1                                     
  ------------------------------------------------------------    
  ```
* Run the [**display trace instance**](cmdqueryname=display+trace+instance) command to check information about service diagnosis instances on the device.
  ```
  [~DeviceA] [display trace instance mac-address 00e0-fc12-3456](cmdqueryname=display+trace+instance+mac-address+00e0-fc12-3456)
  Trace Instance:
  ------------------------------------------------------------
    ID             : 0
    MAC Address    : 00e0-fc12-3456
    IP Flag        : -
    Session ID     : -
    IP Address     : -
    VRF Index      : -
    CID            : -
    User Name      : -
    Interface      : -
    QinQ VLAN ID   : -
    User VLAN ID   : -
    Access Mode    : -
    Modules online : EAPoL  :0 WEBS   :0 WEB    :0 WEBMNG :0 AAA    :0
                     CM     :0 TM     :0 SAM    :0 RADIUS :0
                     DHCPS  :1 DHCPC  :0 DHCPR  :0 DHCPP  :0
                     TACACS :0 AM     :0 SAVI   :0 WLAN_AC:0
                     L2TP   :0 LNS    :0 PPP    :0 PPPOE  :0
                     PPPOLNS:0
                     AD     :0
                     LDAP   :0
   ------------------------------------------------------------
    Total 1, 1 printed
  ```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
return
```