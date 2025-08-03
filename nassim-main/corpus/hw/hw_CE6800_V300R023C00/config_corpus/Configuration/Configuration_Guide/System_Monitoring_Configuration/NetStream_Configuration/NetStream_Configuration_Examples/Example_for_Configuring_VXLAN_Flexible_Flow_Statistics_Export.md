Example for Configuring VXLAN Flexible Flow Statistics Export
=============================================================

Example for Configuring VXLAN Flexible Flow Statistics Export

#### Networking Requirements

On the VXLAN network shown in [Figure 1](#EN-US_TASK_0000001513161246__fig376535683313), Host1 and Host2 are connected to the VXLAN network through DeviceB and DeviceC, respectively. A VXLAN tunnel is established between DeviceB and DeviceA and between DeviceC and DeviceA. The network administrator wants the NetStream server to collect statistics about VXLAN traffic and the network resources used by Host1 and Host2.

**Figure 1** NetStream networking diagram![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001564001597.png)

#### Procedure

1. Configure IP addresses for interfaces on DeviceA according to [Figure 1](#EN-US_TASK_0000001513161246__fig376535683313).
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.1.3.1 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. Configure a VXLAN flexible flow statistics template.
   
   
   
   # Create a flexible flow statistics template named **VXLAN-record** to aggregate flows based on the source and destination addresses of inner packets in VXLAN packets, and configure the exported packets to include the number of bytes and packets.
   
   ```
   [~DeviceA] netstream record VXLAN-record vxlan inner-ip
   [*DeviceA-netstream-record-vxlan-VXLAN-record] match inner-ip destination-address
   [*DeviceA-netstream-record-vxlan-VXLAN-record] match inner-ip source-address
   [*DeviceA-netstream-record-vxlan-VXLAN-record] collect counter bytes
   [*DeviceA-netstream-record-vxlan-VXLAN-record] collect counter packets
   [*DeviceA-netstream-record-vxlan-VXLAN-record] quit
   [*DeviceA] commit
   ```
3. Configure NetStream sampling.
   
   
   
   # Configure NetStream sampling for the incoming and outgoing traffic on 100GE 1/0/1 and 100GE 1/0/2, and set the sampling rate to 8192.
   
   ```
   [~DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] netstream sampler random-packets 8192 inbound
   [*DeviceA-100GE1/0/1] netstream sampler random-packets 8192 outbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] netstream sampler random-packets 8192 inbound
   [*DeviceA-100GE1/0/2] netstream sampler random-packets 8192 outbound
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure VXLAN flexible flow statistics export.
   
   
   
   # Set the source IP address of the exported packets carrying VXLAN flexible flow statistics to 10.1.3.1, destination IP address to 10.1.3.2, destination port number to 6000, and DSCP value to 0.
   
   ```
   [~DeviceA] netstream export vxlan inner-ip source 10.1.3.1
   [*DeviceA] netstream export vxlan inner-ip host 10.1.3.2 6000 dscp 0
   [*DeviceA] commit
   ```
5. Enable VXLAN flexible flow statistics collection on interfaces.
   
   
   
   # Enable VXLAN flexible flow statistics collection for incoming packets on 100GE 1/0/1 and 100GE 1/0/2, and apply the VXLAN flexible flow statistics template to the interfaces.
   
   ```
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] netstream record VXLAN-record vxlan inner-ip
   [*DeviceA-100GE1/0/1] netstream inbound ip
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] netstream record VXLAN-record vxlan inner-ip
   [*DeviceA-100GE1/0/2] netstream inbound ip
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
6. Verify the configuration.
   
   
   
   # View flow statistics.
   
   ```
   [~DeviceA] display netstream statistics vxlan inner-ip slot 1
    Last time when statistics were cleared: -
    -------------------------------------------------------------------------------
    Packet Length    : Number
    -------------------------------------------------------------------------------
    1      ~    64   : 0
    65     ~    128  : 3480368
    129    ~    256  : 0
    257    ~    512  : 0
    513    ~    1024 : 0
    1025   ~    1500 : 0
    longer than 1500 : 0
    -------------------------------------------------------------------------------
    StreamType
         Current           Aged        Created       Exported       Exported
         (streams)         (streams)   (streams)     (streams)      (Packets)
    -------------------------------------------------------------------------------
    VXLAN-record
               0             60             60             60              6
    -------------------------------------------------------------------------------
   ```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA 
#
netstream export vxlan inner-ip source 10.1.3.1
netstream export vxlan inner-ip host 10.1.3.2 6000 dscp 0
#
netstream record VXLAN-record vxlan inner-ip
 collect counter bytes
 collect counter packets
 match inner-ip destination-address
 match inner-ip source-address
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 255.255.255.0
 netstream inbound ip
 netstream sampler random-packets 8192 inbound
 netstream sampler random-packets 8192 outbound
 netstream record VXLAN-record vxlan inner-ip
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.2.1 255.255.255.0
 netstream inbound ip
 netstream sampler random-packets 8192 inbound
 netstream sampler random-packets 8192 outbound
 netstream record VXLAN-record vxlan inner-ip
#
interface 100GE1/0/3
 undo portswitch
 ip address 10.1.3.1 255.255.255.0
#
return
```