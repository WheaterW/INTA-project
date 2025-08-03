Example for Configuring CPU Attack Defense
==========================================

Example for Configuring CPU Attack Defense

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564116661__fig_dc_cfg_LocalAttackDefense_002501), a large number of users access the Internet through DeviceA. The administrator determines that an attacker is sending a significant number of ARP Request packets to DeviceA, which impacts normal operation of the device's CPU. As such, the administrator must alleviate any adverse impact of ARP packets on the CPU.

**Figure 1** Networking diagram of local attack defense![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001513156710.png)

#### Procedure

1. Configure an attack defense policy.
   
   
   
   # Create an attack defense policy.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] cpu-defend policy test1
   ```
   
   # Set the rate limit of ARP Request packets sent to the CPU.
   
   ```
   [*DeviceA-cpu-defend-policy-test1] car packet-type arp-request pps 128
   [*DeviceA-cpu-defend-policy-test1] quit
   [*DeviceA] commit
   ```
2. Apply the attack defense policy globally.
   
   
   ```
   [~DeviceA] cpu-defend-policy test1
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the configured attack defense policy.
```
[~DeviceA] display cpu-defend policy test1
==============================================
Policy name: test1
Policy applies on slot: <1> 
Car packet-type arp-request(pps) : 128
==============================================    
```

# Check the CAR setting.
```
[~DeviceA] display cpu-defend configuration all
Car configurations on slot 1 :
----------------------------------------------------------------------
PacketType            Status      Current(pps) Default(pps)      Queue
----------------------------------------------------------------------
arp-miss              Enabled             1536         1536         13
arp-reply             Enabled             2048         2048         23
arp-request           Enabled             128          2048         23
arp-request-uc        Enabled             2048         2048         23
...
```


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
cpu-defend policy test1
 car packet-type arp-request pps 128
#
cpu-defend-policy test1
# 
return 
```