Example for Configuring Priority Mapping
========================================

Example for Configuring Priority Mapping

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563750049__fig_dc_cfg_qos_001301), Host1 and Host2 are connected to DeviceB and DeviceC through DeviceD, and then access the network through DeviceA.

The 802.1p values of packets sent from Host1 and Host2 are both 0. To ensure normal running of low-latency services on Host1, the customer wants to configure the CoS of Host1 to be higher than that of Host2, offering differentiated services for Host1 and Host2.

**Figure 1** Network diagram of priority mapping![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001563869709.png)

#### Procedure

1. Create VLANs and configure interfaces so that DeviceD can communicate with Host1, Host2, DeviceB, and DeviceC.
   
   
   
   # Create VLAN 100 and VLAN 200.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceD] vlan batch 100 200
   ```
   
   # Set the link type of 100GE 1/0/3 and 100GE 1/0/4 on DeviceD to trunk, and add 100GE 1/0/1 to VLAN 100, 100GE 1/0/2 to VLAN 200, and 100GE 1/0/3 and 100GE 1/0/4 to both VLAN 100 and VLAN 200.
   
   ```
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] portswitch
   [*DeviceD-100GE1/0/1] port default vlan 100
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] portswitch
   [*DeviceD-100GE1/0/2] port default vlan 200
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] portswitch
   [*DeviceD-100GE1/0/3] port link-type trunk
   [*DeviceD-100GE1/0/3] port trunk allow-pass vlan 100 200
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] interface 100ge 1/0/4
   [*DeviceD-100GE1/0/4] portswitch
   [*DeviceD-100GE1/0/4] port link-type trunk
   [*DeviceD-100GE1/0/4] port trunk allow-pass vlan 100 200
   [*DeviceD-100GE1/0/4] quit
   [*DeviceD] [commit](cmdqueryname=commit)
   ```
2. Configure interfaces to trust outer 802.1p values in packets.
   
   
   
   # Configure 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4 to trust outer 802.1p values in packets. By default, a Layer 2 interface trusts outer 802.1p values. In this case, skip this step.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] trust 8021p outer
   [~DeviceD-100GE1/0/1] quit
   [~DeviceD] interface 100ge 1/0/2
   [~DeviceD-100GE1/0/2] trust 8021p outer
   [~DeviceD-100GE1/0/2] quit
   [~DeviceD] interface 100ge 1/0/3
   [~DeviceD-100GE1/0/3] trust 8021p outer
   [~DeviceD-100GE1/0/3] quit
   [~DeviceD] interface 100ge 1/0/4
   [~DeviceD-100GE1/0/4] trust 8021p outer
   [~DeviceD-100GE1/0/4] quit
   ```
3. Create DiffServ domains, configure priority mapping in the DiffServ domains, and bind the DiffServ domains to interfaces.
   
   
   
   # Create DiffServ domains **ds1** and **ds2** on DeviceD and map the 802.1p values of packets sent from Host1 and Host2 to different internal priorities.
   
   ```
   [*DeviceD] diffserv domain ds1
   [*DeviceD-dsdomain-ds1] 8021p-inbound 0 phb af4 green
   [*DeviceD-dsdomain-ds1] quit
   [*DeviceD] diffserv domain ds2
   [*DeviceD-dsdomain-ds2] 8021p-inbound 0 phb af2 green
   [*DeviceD-dsdomain-ds2] quit
   ```
   
   
   
   # Bind DiffServ domains **ds1** and **ds2** to 100GE 1/0/1 and 100GE 1/0/2, respectively.
   
   ```
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] trust upstream ds1
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] trust upstream ds2
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Display queue statistics on the outbound interface. If there are packet statistics in queue 2 corresponding to the internal priority AF2, and in queue 4 corresponding to the internal priority AF4, priority mapping is configured successfully.

```
[~DeviceD] display qos queue statistics interface 100ge 1/0/3
 Queue   CIR/PIR              Passed     Pass Rate             Dropped     Drop Rate  Drop Time
        (% or kbps)   (Packets/Bytes)     (pps/bps)     (Packets/Bytes)    (pps/bps)                                                
 ----------------------------------------------------------------------------------------------
     0         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
     1         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
     2         0            11295086         17516                   0             0          -
        10000000           114688668      14573986                   0             0          
 ----------------------------------------------------------------------------------------------
     3         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
     4         0            11511125         19563                   0             0          -
        10000000           112653485      15352321                   0             0          
 ----------------------------------------------------------------------------------------------
     5         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
     6         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
     7         0                   0             0                   0             0          -
        10000000                   0             0                   0             0          
 ----------------------------------------------------------------------------------------------
```
#### Configuration Scripts

DeviceD

```
#
sysname DeviceD
#
vlan batch 100 200
#
diffserv domain ds1
 8021p-inbound 0 phb af4 green
#
diffserv domain ds2
 8021p-inbound 0 phb af2 green
# 
interface 100GE1/0/1
 port default vlan 100
 trust upstream ds1
#
interface 100GE1/0/2
 port default vlan 200
 trust upstream ds2
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 100 200
#
interface 100GE1/0/4
 port link-type trunk
 port trunk allow-pass vlan 100 200
#
return
```