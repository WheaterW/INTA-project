Example for Configuring Local 1:1 Port Mirroring
================================================

Example for Configuring Local 1:1 Port Mirroring

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001563766665__fig17397105751518), the administration department of an enterprise accesses the Internet through DeviceA, and the Server acting as a monitoring device is directly connected to DeviceA. Internet access traffic of the administration department needs to be monitored through the Server.

**Figure 1** Networking diagram of local port mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, and 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001564006585.png)

#### Procedure

1. Configure 100GE1/0/2 on DeviceA as a local observing port.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port 1 interface 100ge 1/0/2
   [*DeviceA] commit
   ```
2. On DeviceA, configure 100GE1/0/1 as a mirrored port to monitor the packets sent by the administration department.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-mirroring observe-port 1 inbound
   [*DeviceA-100GE1/0/1] quit
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
  100GE1/0/1            Inbound                    1 : 100GE1/0/2
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port 1 interface 100GE1/0/2
#
interface 100GE1/0/1
 port-mirroring observe-port 1 inbound
#
return
```