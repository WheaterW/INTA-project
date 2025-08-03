Example for Configuring Storm Control
=====================================

Example for Configuring Storm Control

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001512689334__fig_dc_cfg_storm_001101), DeviceA connects a Layer 2 network to a Layer 3 device. Storm control needs to be configured on DeviceA so as to limit the number of broadcast packets, unknown multicast packets, and unknown unicast packets forwarded at Layer 2, preventing broadcast storms.

**Figure 1** Networking diagram of storm control![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512848934.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure storm control in the view of 100GE1/0/1 to prevent broadcast storms caused by broadcast packets, unknown multicast packets, and unknown unicast packets forwarded at Layer 2.
* Enable the device to record logs during storm control to remind a network administrator to take measures to protect the device.


#### Procedure

1. Enter the interface view.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   ```
2. Configure the upper and lower thresholds for broadcast packets, unknown multicast packets, and unknown unicast packets. When the average rate at which an interface receives one of these types of packets is greater than 2000 pps within the storm detection interval, storm control is performed on the packets of the corresponding type on the interface. When the average rate drops below 1000 pps, the interface starts to forward packets of the corresponding type again.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm control broadcast min-rate 1000 max-rate 2000
   [*DeviceA-100GE1/0/1] storm control multicast min-rate 1000 max-rate 2000
   [*DeviceA-100GE1/0/1] storm control unknown-unicast min-rate 1000 max-rate 2000
   ```
3. Set the storm control action to **block**.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm control action block
   ```
4. Set the storm detection interval to 90s.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm control interval 90
   ```
5. Enable the device to record logs during storm control.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm control enable log
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the storm control configuration.

```
[~DeviceA] display storm control interface 100ge 1/0/1
--------------------------------------------------------------------------------
NOTE:
BC = Broadcast; MC = Multicast; UUC = Unknown Unicast
Int = Interval value (unit: seconds)
--------------------------------------------------------------------------------
PortName     Type   MaxRate Mode Action    Punish-   Trap Log  Int Last
                                           Status                  Punish-Time
--------------------------------------------------------------------------------
100GE1/0/1   BC        2000 Pps  Block     Normal    Off  On    90 --
100GE1/0/1   MC        2000 Pps  Block     Normal    Off  On    90 --
100GE1/0/1   UUC       2000 Pps  Block     Normal    Off  On    90 --
```

The **Punish-Status** field displays the packet status on the current interface, and the **Last Punish-Time** field displays the time when the storm control penalty was last implemented. The preceding output shows that the broadcast packets, unknown multicast packets, and unknown unicast packets on 100GE1/0/1 of DeviceA are normal and that no storm control penalty is performed. This indicates that the average rate of these packets within the detection interval does not exceed the specified value and the network runs properly.


#### Configuration Scripts

DeviceA

```
#                                                                                                                                   
sysname DeviceA                                                                                                                     
# 
interface 100GE1/0/1
 storm control broadcast min-rate 1000 max-rate 2000
 storm control multicast min-rate 1000 max-rate 2000
 storm control unknown-unicast min-rate 1000 max-rate 2000
 storm control interval 90
 storm control action block
 storm control enable log
#
return
```