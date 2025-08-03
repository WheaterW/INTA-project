Configuration Example for Data Plane Fast Recovery
==================================================

Configuration Example for Data Plane Fast Recovery

#### Networking Requirements

An enterprise has high-performance database access services, which require DCNs to provide high performance and reliability. In this case, DPFR can be deployed to implement local or remote fast fault convergence based on the data plane, without affecting services.

In [Figure 1](#EN-US_TOPIC_0000001688535109__fig_dc_vrp_feature_new_ipfpm_000702), service traffic is normally forwarded along the path Spine1 -> Leaf1 -> Server1. If the link between Leaf1 and Server1 fails, the enterprise expects the fault to be rapidly detected and service traffic be quickly switched to the backup link. In this case, DPFR can be configured. Once Leaf1 detects that interface1 fails and no redundant path to Server1 is available, it generates a fault advertisement packet and forwards the packet to the adjacent upstream device Spine1. Spine1 provides a redundant path to Server1 so that subsequent service traffic is switched to the standby link and forwarded along the path Spine1 -> Leaf2 -> Server1.

**Figure 1** Network diagram of DPFR![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001724254074.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable DPFR globally, and set the sampling rate and aging time of entries in the fault table.
2. Configure fault detection on an interface for DPFR.

#### Procedure

1. Configure DPFR on a device. The following uses Leaf1 as an example. The configurations of other devices are similar. For details, see the configuration script.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] interface 100ge1/0/1
   [*Leaf1-100GE1/0/1] undo portswitch
   [*Leaf1-100GE1/0/1] ip address 10.1.1.1 24
   [*Leaf1-100GE1/0/1] quit
   [*Leaf1] commit
   [~Leaf1] dpfr enable sampler 1024 aging-time 10
   [*Leaf1] interface 100ge1/0/1
   [*Leaf1-100GE1/0/1] dpfr enable
   ```

![](public_sys-resources/note_3.0-en-us.png) 

Only the interfaces enabled with fault detection can detect faults. You can configure fault detection on the corresponding interfaces as required. The following uses interface1 as an example.



#### Verifying the Configuration

If Leaf1 fails and fault convergence is implemented after the preceding configurations are complete, you can check information about the fault table for DPFR on the device.

# Display detailed information about the fault table for DPFR.
```
[~Leaf1] display dpfr cache slot 1
ChipId: 0
------------------------------------------------------------------                                  
Protocol     DestinationIPv4     Interface    Time             
------------------------------------------------------------------
IPv4         1.1.1.1             100GE1/0/1   2022-10-10 19:49:13
------------------------------------------------------------------
```

# Display the fault table statistics about DPFR.
```
[~Leaf1] display dpfr cache statistics slot 1
ChipId: 0
---------------------------------------------------------
Protocol          Current           Aged          Created
---------------------------------------------------------
IPv4                    1               0               1
---------------------------------------------------------
```

# Display the event logs of DPFR.

```
[~Leaf1] display dpfr event-log slot 1
Recover     : Data plane fast failover event.    
ResourceFail: Resource failures causes DPFR function to fail. 
PortStatus  : Port down event.
--------------------------------------------------------------------------------
EventType      Log
--------------------------------------------------------------------------------
recover        DIP:1.1.1.1,srcPort:100GE1/0/2,dstPort:100GE1/0/1
               recover: 2000/12/12 12:00:00 
--------------------------------------------------------------------------------
```

#### Configuration Scripts

* Leaf1
  ```
  #
  sysname Leaf1
  #
  dpfr enable sampler 1024 aging-time 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   dpfr enable
  ```
* Spine1
  ```
  #
  sysname Spine1
  #
  dpfr enable sampler 1024 aging-time 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   dpfr enable
  ```