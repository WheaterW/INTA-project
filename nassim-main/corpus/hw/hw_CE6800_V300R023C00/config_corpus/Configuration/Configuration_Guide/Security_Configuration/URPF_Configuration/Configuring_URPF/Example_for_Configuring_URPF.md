Example for Configuring URPF
============================

Example for Configuring URPF

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563990981__fig_dc_s_cfg_10017301), DeviceA is connected to the ISP device through interface1 and connected to a user network through interface2. The administrator requires DeviceA to defend against source address spoofing attacks. If DeviceA cannot provide this function, unauthorized users will occupy an excessive amount of service resources by sending valid service requests, thereby preventing authorized users from communicating with each other due to a lack of response from the server.

**Figure 1** Network diagram of URPF configuration![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001563990989.png)

#### Configuration Roadmap

Configure URPF on the user-side interface 100GE1/0/2 of DeviceA to prevent source IP address spoofing attacks from users.

![](public_sys-resources/note_3.0-en-us.png) 

Route symmetry is ensured in this example, so the URPF strict check is used.



#### Procedure

1. Configure the URPF check mode on the interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip urpf enable
   [*DeviceA-100GE1/0/2] ip urpf strict
   [*DeviceA-100GE1/0/2] commit
   [~DeviceA-100GE1/0/2] quit
   ```

#### Verifying the Configuration

# Check the URPF configuration on 100GE1/0/2.
```
[~DeviceA-100GE1/0/2] display this
#
interface 100GE1/0/2
 undo portswitch
 ip urpf enable
 ip urpf strict
#
return
```
#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
interface 100GE1/0/2
 undo portswitch
 ip urpf enable
 ip urpf strict
#
return
```