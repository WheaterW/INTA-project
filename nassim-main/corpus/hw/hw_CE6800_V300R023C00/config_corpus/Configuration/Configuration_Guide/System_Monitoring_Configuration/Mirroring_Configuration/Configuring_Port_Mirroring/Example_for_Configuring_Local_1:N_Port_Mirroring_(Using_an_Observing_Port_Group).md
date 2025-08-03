Example for Configuring Local 1:N Port Mirroring (Using an Observing Port Group)
================================================================================

Example for Configuring Local 1:N Port Mirroring (Using an Observing Port Group)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001563766669__fig047813711184), hosts access the Internet through DeviceA, which is directly connected to three monitoring devices: ServerA, ServerB, and ServerC. Internet access traffic of the hosts needs to be mirrored to different servers for monitoring and analysis purposes.

**Figure 1** Networking diagram of local port mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, 3, and 4 indicate 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001513046350.png)

#### Procedure

1. Configure an observing port group on DeviceA and add 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4 to the observing port group.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port group 1
   [*DeviceA-observe-port-group-1] group-member 100ge 1/0/2 to 100ge 1/0/4
   [*DeviceA-observe-port-group-1] quit
   [*DeviceA] commit
   ```
2. Configure 100GE 1/0/1 on DeviceA as a mirrored port to copy incoming traffic to observing port group 1.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-mirroring observe-port group 1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the configuration of the observing port group.

```
[~DeviceA] display observe-port
  GroupId    MemberPorts
  -----------------------------------------------------------------------------
        1    100GE1/0/2            100GE1/0/3            100GE1/0/4
  -----------------------------------------------------------------------------
```

# Check the mirroring configuration.

```
[~DeviceA] display port-mirroring
  Observe port group mirroring:
  -----------------------------------------------------------------------------
  MirroringPort         Direction        ObserveGroup
  -----------------------------------------------------------------------------
  100GE1/0/1            Inbound                     1
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port group 1
 group-member 100GE1/0/2
 group-member 100GE1/0/3
 group-member 100GE1/0/4
#
interface 100GE1/0/1
 port-mirroring observe-port group 1 inbound
#
return
```