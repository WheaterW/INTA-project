Example for Configuring Attack Defense
======================================

Example for Configuring Attack Defense

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563756881__fig2235623203411), if an attacker on the Internet launches a malformed packet attack, a fragmentation attack, or a flood attack on DeviceA, DeviceA may break down. To prevent such issues, the network administrator needs to deploy attack defense measures on DeviceA, so as to secure the network environment and ensure services run as normal.

**Figure 1** Network diagram of defense against malformed packet attacks, fragmentation attacks, and flood attacks  
![](figure/en-us_image_0000001513156610.png)

#### Procedure

1. Configure defense against malformed packet attacks.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] anti-attack abnormal enable
   [*DeviceA] commit
   ```
2. Configure defense against fragmentation attacks and set the rate limit of packet fragments to 15000 bit/s.
   
   
   ```
   [~DeviceA] anti-attack fragment enable
   [*DeviceA] anti-attack fragment car cir 15000
   [*DeviceA] commit
   ```
3. Configure defense against flood attacks.
   
   
   
   # Configure defense against TCP SYN flood attacks and set the rate limit of TCP SYN packets to 15000 bit/s.
   
   ```
   [~DeviceA] anti-attack tcp-syn enable
   [*DeviceA] anti-attack tcp-syn car cir 15000
   [*DeviceA] commit
   ```
   
   # Configure defense against UDP flood attacks to enable the device to discard UDP packets sent from specified ports.
   
   ```
   [~DeviceA] anti-attack udp-flood enable
   [*DeviceA] commit
   ```
   
   # Configure defense against ICMP flood attacks and set the rate limit of ICMP flood packets to 15000 bit/s.
   
   ```
   [~DeviceA] anti-attack icmp-flood enable
   [*DeviceA] anti-attack icmp-flood car cir 15000
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# After the configuration is complete, run the **display anti-attack statistics** command to view attack defense statistics.

```
<DeviceA> display anti-attack statistics
Packets Statistic Information:
-------------------------------------------------------------------------------
AntiAtkType  TotalPacketNum        DropPacketNum         PassPacketNum
             (H)        (L)        (H)        (L)        (H)        (L)          
-------------------------------------------------------------------------------  
Abnormal      0          0          0          0          0          0           
Fragment      0          0          0          0          0          0           
Icmp-flood    0          0          0          0          0          0           
Tcp-syn       0          58         0          0          0          58          
Udp-flood     0          0          0          0          0          0           
------------------------------------------------------------------------------- 
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
anti-attack abnormal enable
anti-attack fragment enable
anti-attack fragment car cir 15000
anti-attack tcp-syn enable
anti-attack tcp-syn car cir 15000
anti-attack udp-flood enable
anti-attack icmp-flood enable
anti-attack icmp-flood car cir 15000
#
return
```