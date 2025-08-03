Example for Configuring Unicast UDP Encapsulation for 1588v2 (PTP) Devices in BC Mode
=====================================================================================

Example for Configuring Unicast UDP Encapsulation for 1588v2 (PTP) Devices in BC Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512839394__fig_dc_cfg_ptp_003401), all devices are located on a Layer 3 network and support 1588v2, with DeviceA and DeviceB connected to two different PTP clock sources. After the grandmaster clock is determined between DeviceA and DeviceB through dynamic BMC selection, it transmits 1588v2 time signals to the entire network.

**Figure 1** Networking diagram of clock synchronization  
![](figure/en-us_image_0000001921223346.png)
![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable 1588v2 globally and set the device type to BC.
2. Configure 1588v2 devices to import time signals from PTP clock sources.
3. Enable 1588v2 on interfaces.
4. As interface IP addresses are known on a Layer 3 network, configure 1588v2 devices to transmit 1588v2 packets in unicast UDP encapsulation mode.

#### Procedure

1. Enable 1588v2 globally and set the device type to BC.
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ptp enable
   [*DeviceA] ptp device-type bc
   [*DeviceA] commit
   ```
2. Configure 1588v2 devices to import time signals from PTP clock sources.# Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA.
   ```
   [~DeviceA] clock source ptp synchronization enable
   [*DeviceA] clock source ptp priority 1
   [*DeviceA] commit
   ```
3. Enable 1588v2 on interfaces, and set the encapsulation mode of 1588v2 packets to unicast UDP encapsulation.
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] ptp enable
   [*DeviceA-100GE1/0/1] ptp udp-egress source-ip 10.1.0.1 destination-ip 10.1.0.2
   [*DeviceA-100GE1/0/1] ptp udp-egress destination-mac 00e0-fc22-2211
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] ptp enable
   [*DeviceA-100GE1/0/2] ptp udp-egress source-ip 10.0.0.1 destination-ip 10.0.0.2
   [*DeviceA-100GE1/0/2] ptp udp-egress destination-mac 00e0-fc00-1122
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] ptp enable
   [*DeviceA-100GE1/0/3] ptp udp-egress source-ip 10.3.0.1 destination-ip 10.3.0.2
   [*DeviceA-100GE1/0/3] ptp udp-egress destination-mac 00e0-fc22-3311
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check that DeviceC and DeviceD can trace the time of DeviceA and DeviceB. The configuration on DeviceC is used as an example. Run the **display ptp all** command to check the PTP status of DeviceC.

```
[~DeviceC] display ptp all
```
```
  Device config info                                                            
  ------------------------------------------------------------------------------
  PTP state         :enabled            Domain  value      :0                 
  Slave only        :no                   Device type        :BC                
  Set port state    :no                   Local clock ID     :00259e1000000001  
  Acl               :no                   Virtual clock ID   :no               
  Acr               :no                   Time lock success  :yes               
  Asymmetry measure :disable              Passive measure    :disable           
                                                                                
  BMC run info                                                                  
  ------------------------------------------------------------------------------
  Grand clock ID    :00259e1000000002                                           
  Receive number    :100GE1/0/2                                                  
  Parent clock ID   :00259e1000000002                                           
  Parent portnumber :4126                                                       
  Priority1         :110                 Priority2           :110               
  Step removed      :1                   Clock accuracy      :0x31              
  Clock class       :6                   Time Source         :0xa0              
  UTC Offset        :35                  UTC Offset Valid    :False             
  Timescale         :ARB                 Time traceable      :False             
  Leap              :None                Frequency traceable :False             
  Offset scaled     :0xffff                                                     
                                                                                
  Port info                                                                     
  Name                        State        Delay-mech Ann-timeout Type   Domain 
  ------------------------------------------------------------------------------
  100GE1/0/1                   master       delay      4           BC     0      
  100GE1/0/2                   slave        delay      4           BC     0      
                                                                                  
  Time Performance Statistics(ns): Slot 1  Card 0  Port 1                       
  ------------------------------------------------------------------------------
  Realtime(T2-T1)   :140                     Pathdelay     :0                   
  Max(T2-T1)        :3510286792100                                              
  Min(T2-T1)        :-5715158684                                                
                                                                                
  Clock source info                                                             
  Clock       Pri1 Pri2 Accuracy Class TimeSrc Signal Switch Direction In-Status
  ------------------------------------------------------------------------------
  local       128  128  0x31     187   0xa0    -      -      -         -        
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  ptp enable
  ptp device-type bc
  #
  interface 100GE1/0/1
   ptp enable
   ptp udp-egress source-ip 10.1.0.1 destination-ip 10.1.0.2
   ptp udp-egress destination-mac 00e0-fc22-2211
  #
  interface 100GE1/0/2
   ptp enable
   ptp udp-egress source-ip 10.0.0.1 destination-ip 10.0.0.2
   ptp udp-egress destination-mac 00e0-fc00-1122
  #
  interface 100GE1/0/3
   ptp enable
   ptp udp-egress source-ip 10.3.0.1 destination-ip 10.3.0.2
   ptp udp-egress destination-mac 00e0-fc22-3311
  #
  return
  
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  ptp enable
  ptp device-type bc
  #
  interface 100GE1/0/1
   ptp enable
   ptp udp-egress source-ip 10.0.0.2 destination-ip 10.0.0.1
   ptp udp-egress destination-mac 00e0-fc00-1111
  #
  interface 100GE1/0/2
   ptp enable
   ptp udp-egress source-ip 10.2.0.1 destination-ip 10.2.0.2
   ptp udp-egress destination-mac 00e0-fc22-2233
  #
  interface 100GE1/0/3
   ptp enable
   ptp udp-egress source-ip 10.5.0.1 destination-ip 10.5.0.2
   ptp udp-egress destination-mac 00e0-fc22-3322
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  ptp enable
  ptp device-type bc
  #
  interface 100GE1/0/1
   ptp enable
   ptp udp-egress source-ip 10.6.0.1 destination-ip 10.6.0.2
   ptp udp-egress destination-mac 00e0-fc22-5511
  #
  interface 100GE1/0/2
   ptp enable
   ptp udp-egress source-ip 10.1.0.2 destination-ip 10.1.0.1
   ptp udp-egress destination-mac 00e0-fc00-1111
  #
  return 
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  ptp enable
  ptp device-type bc
  #
  interface 100GE1/0/1
   ptp enable
   ptp udp-egress source-ip 10.2.0.2 destination-ip 10.2.0.1
   ptp udp-egress destination-mac 00e0-fc00-1122
  #
  interface 100GE1/0/2
   ptp enable
   ptp udp-egress source-ip 10.7.0.1 destination-ip 10.7.0.2
   ptp udp-egress destination-mac 00e0-fc22-5522
  #
  return  
  ```