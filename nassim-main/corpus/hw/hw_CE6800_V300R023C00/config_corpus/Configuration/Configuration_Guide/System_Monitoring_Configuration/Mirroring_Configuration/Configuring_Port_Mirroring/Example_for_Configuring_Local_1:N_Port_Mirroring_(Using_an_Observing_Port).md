Example for Configuring Local 1:N Port Mirroring (Using an Observing Port)
==========================================================================

Example for Configuring Local 1:N Port Mirroring (Using an Observing Port)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564006581__fig086114617300), hosts access the Internet through DeviceA, which is directly connected to three monitoring devices: ServerA, ServerB, and ServerC. Internet access traffic of the hosts needs to be mirrored to different servers for monitoring and analysis purposes.

**Figure 1** Networking diagram of local port mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, 3, and 4 indicate 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001564006593.png)

#### Procedure

1. Configure 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4 on DeviceA as observing ports.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port 1 interface 100ge 1/0/2
   [*DeviceA] observe-port 2 interface 100ge 1/0/3
   [*DeviceA] observe-port 3 interface 100ge 1/0/4
   [*DeviceA] commit
   ```
2. Configure 100GE 1/0/1 on DeviceA as a mirrored port to copy incoming traffic to observing ports 1, 2, and 3.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-mirroring observe-port 1 inbound
   [*DeviceA-100GE1/0/1] port-mirroring observe-port 2 inbound
   [*DeviceA-100GE1/0/1] port-mirroring observe-port 3 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the observing port configuration.

```
[~DeviceA] display observe-port
  -----------------------------------------------------------------------------
  Index    : 1
  Interface: 100GE1/0/2
  -----------------------------------------------------------------------------
  Index    : 2
  Interface: 100GE1/0/3
  -----------------------------------------------------------------------------
  Index    : 3
  Interface: 100GE1/0/4
  -----------------------------------------------------------------------------
```

# Check the mirroring configuration.

```
[~DeviceA] display port-mirroring
  Observe port mirroring:
  -----------------------------------------------------------------------------
  MirroringPort         Direction        ObservePort : Interface
  -----------------------------------------------------------------------------
  100GE1/0/1            Inbound                    1 : 100GE1/0/2
                        Inbound                    2 : 100GE1/0/3
                        Inbound                    3 : 100GE1/0/4
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port 1 interface 100GE1/0/2
observe-port 2 interface 100GE1/0/3
observe-port 3 interface 100GE1/0/4
#
interface 100GE1/0/1
 port-mirroring observe-port 1 inbound
 port-mirroring observe-port 2 inbound
 port-mirroring observe-port 3 inbound
#
return
```