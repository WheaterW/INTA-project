Example for Configuring Attack Source Tracing
=============================================

Example for Configuring Attack Source Tracing

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563996785__fig_dc_cfg_LocalAttackDefense_002501), users on different network segments access the Internet through DeviceA. Because there are a large number of access users, DeviceA often processes a large number of ARP packets, leading to a high CPU usage and hence affecting services.

The administrator requires that the device analyze the ARP packets sent to the CPU, identify the packets whose rate exceeds the threshold as attack packets, find out the attack source user or source interface, and send logs and alarms to notify the administrator so that the administrator can take security measures to protect the CPU. Users on Net2 are fixed authorized users, so the administrator needs to ensure that ARP packets of these users can be sent to the CPU.

**Figure 1** Networking diagram of attack source tracing![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001512677510.png)

#### Procedure

1. Configure an attack defense policy.
   
   
   
   # Create an attack defense policy.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] cpu-defend policy test1
   ```
   
   # Enable attack source tracing.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend enable
   ```
   
   # Set the attack source tracing threshold to 100 pps.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend threshold 100
   ```
   
   # Set the sampling ratio for attack source tracing to 7. That is, one packet is sampled in every seven packets.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] [auto-defend attack-packet sample 7](cmdqueryname=auto-defend+attack-packet+sample+7)
   ```
   
   # Set the packet type for attack source tracing to ARP packets.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend protocol arp
   ```
   
   # Set the attack source tracing mode to source tracing based on source MAC addresses and source IP addresses.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend trace-type source-mac source-ip
   ```
   
   # Enable the event reporting function for attack source tracing.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend alarm enable
   ```
   
   # Configure a punishment action for attack source tracing: When the device is attacked, it discards packets from the attack source for 360s. Configure the punishment action when you confirm that the device is under attack; otherwise, the device may discard a lot of valid protocol packets, affecting services.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] auto-defend action deny timeout 360
   [*DeviceA-cpu-defend-policy-test1] commit
   [~DeviceA-cpu-defend-policy-test1] quit
   ```
   
   # Configure a whitelist for attack source tracing.
   
   ```
   [~DeviceA] acl number 2001
   [*DeviceA-acl-basic-2001] rule permit source 10.2.2.0 0.0.0.255
   [*DeviceA-acl-basic-2001] quit
   [*DeviceA] cpu-defend policy test1
   [*DeviceA-cpu-defend-policy-test1] auto-defend whitelist 1 acl 2001
   [*DeviceA-cpu-defend-policy-test1] quit
   ```
2. Apply the attack defense policy.
   
   
   ```
   [*DeviceA] cpu-defend-policy test1
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the configuration of attack source tracing.
```
[~DeviceA] display auto-defend configuration cpu-defend policy test1                                                                 
-----------------------------------------------------------------------                                                             
 Name  : test1                                                                                                                      
 Related slot : ***                                                                                                          
 auto-defend                      : enable                                                                                          
 auto-defend threshold            : 100 (pps)                                                                                       
 auto-defend attack-packet sample : 7 (pps)                                                                                         
 auto-defend alarm                : enable                                                                                          
 auto-defend alarm threshold      : 128 (pps)                                                                                       
 auto-defend action               : deny timer: 360 (second)                                                                        
 auto-defend trace-type           : source-mac source-ip                                                                            
 auto-defend protocol             : arp                                                                                             
 auto-defend whitelist 1          : acl number 2001                                                                                 
-----------------------------------------------------------------------     
```


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
cpu-defend policy test1                                                                                                             
 auto-defend enable
 auto-defend threshold 100  
 auto-defend attack-packet sample 7 
 auto-defend protocol arp
 auto-defend trace-type source-mac source-ip
 auto-defend alarm enable                                                                                                           
 auto-defend action deny timeout 360                                                                                              
 auto-defend whitelist 1 acl 2001
#
cpu-defend-policy test1
#
acl number 2001
 rule 5 permit source 10.2.2.0 0.0.0.255
# 
return 
```