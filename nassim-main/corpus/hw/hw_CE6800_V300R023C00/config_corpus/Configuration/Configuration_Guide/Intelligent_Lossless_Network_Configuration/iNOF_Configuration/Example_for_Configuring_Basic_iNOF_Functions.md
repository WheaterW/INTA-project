Example for Configuring Basic iNOF Functions
============================================

Example for Configuring Basic iNOF Functions

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001563763673__fig19978171395514), iNOF can be enabled on DeviceA and DeviceB to better manage connected hosts.

**Figure 1** Networking diagram of basic iNOF functions![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001564003617.png)

#### Precautions

During the configuration, note the following:

* The SNSD function must be enabled for the host and storage array (Host1 and Host2 in [Figure 1](#EN-US_TASK_0000001563763673__fig19978171395514), respectively).

#### Procedure

1. Create VLANs and add interfaces to them.
   
   
   
   # Create VLANs on DeviceA and add interfaces to them.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Create VLANs on DeviceB and add interfaces to them.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 20
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 20
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. Enable the LLDP function.
   
   
   
   # Enable LLDP on DeviceA. The configurations on DeviceB are similar.
   
   ```
   [~DeviceA] lldp enable
   [*DeviceA] commit
   ```
3. Enable the iNOF function.
   
   
   
   # Enable iNOF on DeviceA. The configurations on DeviceB are similar.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] inof
   [*DeviceA-ai-service-inof] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   ```
4. Enable the function for automatically adding hosts to the default zone.
   
   
   
   In an iNOF system, the function for automatically adding hosts to the default zone is enabled by default. When this function is enabled, new hosts are automatically added to the default zone as zone members.

#### Verifying the Configuration

# After the iNOF reflector and client are configured, check information about the iNOF connection established between the local and peer devices.

```
[~DeviceA] display inof configuration zone
IPv4 Info:
Total Zone number: 1
iNOF Default-Zone: Enable

ZoneName: Default
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
10.1.1.1                                  Local
10.1.1.2                                  Local
----------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
lldp enable
# 
vlan batch 10
#
interface 100GE1/0/1
 port link-type trunk  
 port trunk allow-pass vlan 10 
#
interface 100GE1/0/2
 port link-type trunk  
 port trunk allow-pass vlan 10
#
ai-service
 #
 inof
#
return
```

DeviceB

```
#
sysname DeviceB
#
lldp enable
# 
vlan batch 20
#
interface 100GE1/0/1
 port link-type trunk  
 port trunk allow-pass vlan 20 
#
interface 100GE1/0/2
 port link-type trunk  
 port trunk allow-pass vlan 20
#
ai-service
 #
 inof
#
return

```