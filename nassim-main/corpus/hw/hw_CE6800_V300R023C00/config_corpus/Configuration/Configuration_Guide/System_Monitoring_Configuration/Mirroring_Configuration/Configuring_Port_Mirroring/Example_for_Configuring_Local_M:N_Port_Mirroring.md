Example for Configuring Local M:N Port Mirroring
================================================

Example for Configuring Local M:N Port Mirroring

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001512687182__fig1881622112817), hosts access the Internet through DeviceA, which is directly connected to monitoring devices ServerA and ServerB. Internet access traffic of the hosts needs to be mirrored to ServerA and ServerB for monitoring and analysis purposes.

**Figure 1** Networking diagram of local port mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, 3, 4, and 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5 respectively.


  
![](figure/en-us_image_0000001564126417.png)

#### Procedure

1. Configure an observing port group on DeviceA, and add 100GE 1/0/4 and 100GE 1/0/5 to the observing port group.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port group 1
   [*DeviceA-observe-port-group-1] group-member 100ge 1/0/4 to 100ge 1/0/5
   [*DeviceA-observe-port-group-1] quit
   [*DeviceA] commit
   ```
2. Configure 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 on DeviceA as mirrored ports to copy incoming traffic to observing port group 1.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-mirroring observe-port group 1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port-mirroring observe-port group 1 inbound
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] port-mirroring observe-port group 1 inbound
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the configuration of the observing port group.

```
[~DeviceA] display observe-port
  -----------------------------------------------------------------------------
  Index    : 1
  Interface: 100GE1/0/1
  -----------------------------------------------------------------------------
  Index    : 2
  Interface: 100GE1/0/5
  -----------------------------------------------------------------------------
  GroupId    MemberPorts
  -----------------------------------------------------------------------------
        1    100GE1/0/4            100GE1/0/5
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
  100GE1/0/2            Inbound                     1
  100GE1/0/3            Inbound                     1
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port group 1
 group-member 100GE1/0/4
 group-member 100GE1/0/5
#
interface 100GE1/0/1
 port-mirroring observe-port group 1 inbound
#
interface 100GE1/0/2
 port-mirroring observe-port group 1 inbound
#
interface 100GE1/0/3
 port-mirroring observe-port group 1 inbound
#
return
```