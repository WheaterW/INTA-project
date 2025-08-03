Example for Configuring Flexible Flow Statistics Export
=======================================================

Example for Configuring Flexible Flow Statistics Export

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001512841718__fig376535683313), Host1 and Host2 communicate with DeviceA through DeviceB. To support network planning, the network administrator wants the NetStream server to collect statistics about the traffic transmitted between the hosts and DeviceA.

**Figure 1** NetStream networking diagram![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000002135713857.png)

#### Procedure

1. Configure IP addresses for interfaces on DeviceB according to [Figure 1](#EN-US_TASK_0000001512841718__fig376535683313).
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] commit
   [~DeviceB] vlan 110
   [*DeviceB-vlan110] quit
   [*DeviceB] interface vlanif 110
   [*DeviceB-Vlanif110] ip address 10.1.1.1 24
   [*DeviceB-Vlanif110] quit
   [*DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk pvid vlan 110
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 110
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] vlan 120
   [*DeviceB-vlan120] quit
   [*DeviceB] interface vlanif 120
   [*DeviceB-Vlanif120] ip address 10.1.2.1 24
   [*DeviceB-Vlanif120] quit
   [*DeviceB] interface 100ge1/0/2
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk pvid vlan 120
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 120
   [*DeviceB-100GE1/0/2] quit
   ```
2. Configure a flexible flow statistics template.
   
   
   
   # Create a flexible flow statistics template named **record1** to aggregate flows based on source and destination addresses, and configure the exported packets to include the number of bytes and packets.
   
   ```
   [*DeviceB] netstream record record1 ip
   [*DeviceB-netstream-record-ipv4-record1] match ip destination-address
   [*DeviceB-netstream-record-ipv4-record1] match ip source-address
   [*DeviceB-netstream-record-ipv4-record1] collect counter bytes
   [*DeviceB-netstream-record-ipv4-record1] collect counter packets
   [*DeviceB-netstream-record-ipv4-record1] quit
   ```
3. Configure NetStream sampling.
   
   
   
   # Configure NetStream sampling for the incoming and outgoing traffic on 100GE 1/0/1 and set the sampling rate to 1024.
   
   ```
   [*DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] netstream sampler random-packets 1024 inbound
   [*DeviceB-100GE1/0/1] netstream sampler random-packets 1024 outbound
   [*DeviceB-100GE1/0/1] quit
   ```
4. Configure NetStream flexible flow statistics export.
   
   
   
   # Set the source IP address of the exported packets carrying flexible flow statistics to 10.1.2.1, destination IP address to 10.1.2.2, destination port number to 6000, and DSCP value to 0.
   
   ```
   [*DeviceB] netstream export ip source 10.1.2.1
   [*DeviceB] netstream export ip host 10.1.2.2 6000 dscp 0
   ```
5. Enable flexible flow statistics collection on an interface.
   
   
   
   # Enable flexible flow statistics collection for incoming and outgoing packets on 100GE 1/0/1, and apply the flexible flow statistics template to the interface.
   
   ```
   [*DeviceB] interface 100ge1/0/1 
   [*DeviceB-100GE1/0/1] netstream record record1 ip
   [*DeviceB-100GE1/0/1] netstream inbound ip
   [*DeviceB-100GE1/0/1] netstream outbound ip 
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
6. Verify the configuration.
   
   
   
   # View flow statistics.
   
   ```
   [~DeviceB] display netstream statistics ip slot 1
    Last time when statistics were cleared: -
    -------------------------------------------------------------------------------
    Packet Length    : Number
    -------------------------------------------------------------------------------
    1      ~    64   : 15
    65     ~    128  : 14
    129    ~    256  : 1
    257    ~    512  : 0
    513    ~    1024 : 0
    1025   ~    1500 : 0
    longer than 1500 : 0
    -------------------------------------------------------------------------------
    StreamType
         Current           Aged        Created       Exported       Exported
         (streams)         (streams)   (streams)     (streams)      (Packets)
    -------------------------------------------------------------------------------
    origin
               0              0              0              0              0
    ------------------------------------------------------------------------------- 
    record1
               2              2              4              2              2
   -------------------------------------------------------------------------------
   ```

#### Configuration Scripts

DeviceB

```
#                                                                               
sysname DeviceB 
# 
vlan batch 110 120 
# 
netstream export ip source 10.1.2.1
netstream export ip host 10.1.2.2 6000 dscp 0
#
netstream record record1 ip
 collect counter bytes
 collect counter packets
 match ip destination-address
 match ip source-address
#    
interface Vlanif110                                                             
 ip address 10.1.1.1 255.255.255.0 
#                                                                               
interface Vlanif120                                                             
 ip address 10.1.2.1 255.255.255.0 
# 
interface 100GE1/0/1        
 port link-type trunk                                                           
 port trunk pvid vlan 110                                                       
 port trunk allow-pass vlan 110 
 netstream inbound ip 
 netstream outbound ip 
 netstream sampler random-packets 1024 inbound
 netstream sampler random-packets 1024 outbound
 netstream record record1 ip
# 
interface 100GE1/0/2                                                  
 port link-type trunk                                                           
 port trunk pvid vlan 120                                                       
 port trunk allow-pass vlan 120
# 
return
```