Example for Configuring Local N:1 Port Mirroring
================================================

Example for Configuring Local N:1 Port Mirroring

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564126409__fig10214753171312), the marketing department, R&D department, and administration department of an enterprise access the Internet through DeviceA, and the Server acting as a monitoring device is directly connected to DeviceA. Internet access traffic of the three departments needs to be monitored through the Server.

**Figure 1** Networking diagram of local port mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, 3, 4, and 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5 respectively.


  
![](figure/en-us_image_0000001564126421.png)

#### Procedure

1. Configure 100GE1/0/4 on DeviceA as a local observing port.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port 1 interface 100ge 1/0/4
   [*DeviceA] commit
   ```
2. On DeviceA, configure 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3 as mirrored ports to copy the received packets to the local observing port.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-mirroring observe-port 1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port-mirroring observe-port 1 inbound
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] port-mirroring observe-port 1 inbound
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the mirroring configuration

```
[~DeviceA] display port-mirroring
  Observe port mirroring:
  -----------------------------------------------------------------------------
  MirroringPort         Direction        ObservePort : Interface
  -----------------------------------------------------------------------------
  100GE1/0/1            Inbound                    1 : 100GE1/0/4
  100GE1/0/2            Inbound                    1 : 100GE1/0/4
  100GE1/0/3            Inbound                    1 : 100GE1/0/4
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port 1 interface 100GE1/0/4
#
interface 100GE1/0/1
 port-mirroring observe-port 1 inbound
#
interface 100GE1/0/2
 port-mirroring observe-port 1 inbound
#
interface 100GE1/0/3
 port-mirroring observe-port 1 inbound
#
return
```