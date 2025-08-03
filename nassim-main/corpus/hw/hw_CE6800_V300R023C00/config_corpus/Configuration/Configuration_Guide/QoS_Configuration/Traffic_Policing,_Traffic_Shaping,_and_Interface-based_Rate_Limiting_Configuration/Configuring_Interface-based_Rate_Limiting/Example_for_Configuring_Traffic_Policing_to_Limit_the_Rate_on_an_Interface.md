Example for Configuring Traffic Policing to Limit the Rate on an Interface
==========================================================================

Example for Configuring Traffic Policing to Limit the Rate on an Interface

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563770129__fig_dc_cfg_qos_012801), the host sends packets through DeviceA. It is required that the bandwidth of the packets sent by the host should not exceed 100 Mbit/s.

**Figure 1** Networking of interface-based rate limiting![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001513049814.png)![](public_sys-resources/note_3.0-en-us.png) 

This example is not supported by the CE6885-LL (low latency mode).




#### Procedure

1. Configure a CAR profile.
   
   
   
   # On DeviceA, create a CAR profile named **car1** to police traffic from the host.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [~DeviceA] qos car car1 cir 100000
   [*DeviceA] commit
   ```
2. Apply the CAR profile.
   
   
   
   # On DeviceA, apply CAR profile **car1** to the inbound direction of 100GE 1/0/1 to police the traffic from the host.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] qos car inbound car1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the CAR profile configuration.

```
[~DeviceA] display qos car name car1
  ----------------------------------------------------------------
   CAR Name  : car1
   CAR Index : 0
    car cir 100000 kbps cbs 800000 bytes 
   Applied number on behavior  : 0
   Applied number on interface inbound  : 1
    100GE1/0/1
   Applied number on Eth-Trunk inbound  : 0
   Applied number on interface outbound  : 0
   Applied number on Eth-Trunk outbound  : 0
```

# Send packets to 100GE 1/0/1 at the rates of 60000 kbit/s and 110000 kbit/s, respectively, and then run the [**display qos car statistics**](cmdqueryname=display+qos+car+statistics) command to check the traffic statistics. If the configuration is successful, all packets are successfully forwarded when they are sent to 100GE 1/0/1 at 60000 kbit/s; however, some packets are discarded when packets are sent to 100GE 1/0/1 at 110000 kbit/s.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
qos car car1 cir 100000 kbps 
#
interface 100GE1/0/1
 qos car inbound car1
#
return
```