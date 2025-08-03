Example for Configuring PFC Deadlock Prevention
===============================================

Example for Configuring PFC Deadlock Prevention

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001563888441__fig19978171395514) shows a typical Layer 2 Clos network using the spine-leaf architecture. A lossless service is deployed on Host1 and Host2. It is planned that the service is carried by a queue with priority 3 and the DSCP value of packets is 24. To ensure lossless transmission of the lossless service, PFC is configured for the queue with priority 3.

To prevent PFC deadlocks, configure PFC deadlock prevention on Leaf1 and Leaf2. As described in [Table 1](#EN-US_TASK_0000001563888441__table485617561830), configure lossless backup queue 4 and lossy backup queue 2 for lossless service packets with the DSCP value 24. When the system detects that the service flow with the DSCP value 24 becomes a hook-shaped flow, the system switches the service from the original queue to lossless backup queue 4 and changes the DSCP value to 32. If the service flow with the DSCP value 32 becomes a hook-shaped flow after the switchover, the system switches the service flow to lossy backup queue 2 and changes the DSCP value to 16.

**Table 1** Data plan for PFC deadlock prevention
| Queue Information | Packets of the Original Lossless Service | Service Packets After the First Switchover | Service Packets After the Second Switchover |
| --- | --- | --- | --- |
| Queue priority | 3 | 4 | 2 |
| DSCP value | 24 | 32 | 16 |
| Queue type | Lossless queue | Lossless queue | Lossy queue |


**Figure 1** Network diagram of PFC deadlock prevention![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001513048494.png)

#### Procedure

1. Configure PFC.
   
   
   
   # Configure PFC for queues with priorities 3 and 4 on interfaces of Leaf1 to ensure lossless transmission of the lossless service. The configuration on Leaf2 is similar.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
   [*Leaf1] dcb pfc
   [*Leaf1-dcb-pfc-default] priority 3 4
   [*Leaf1-dcb-pfc-default] quit
   [*Leaf1] port-group all_using   
   [*Leaf1-port-group-all_using] group-member 100ge 1/0/1 to 100ge 1/0/2
   [*Leaf1-port-group-all_using] dcb pfc enable mode manual
   [*Leaf1-port-group-all_using] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf1 to implement PFC based on the priority after DSCP mapping. The configuration on Leaf2 is similar. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
   
   ```
   [~Leaf1] dcb pfc dscp-mapping enable slot 1
   [*Leaf1] commit
   ```
   
   # In this example, the DSCP value of lossless service packets is 24. Configure the DiffServ domain **ds1** on Leaf1 to map the DSCP value 24 of lossless service packets to priority 3, and apply the DiffServ domain to interfaces. The configuration on Leaf2 is similar.
   
   ```
   [~Leaf1] diffserv domain ds1 
   [*Leaf1-dsdomain-ds1] ip-dscp-inbound 24 phb af3 green
   [*Leaf1-dsdomain-ds1] quit 
   [*Leaf1] port-group all_using
   [*Leaf1-port-group-all_using] trust dscp
   [*Leaf1-port-group-all_using] trust upstream ds1
   [*Leaf1-port-group-all_using] quit
   [*Leaf1] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the preceding PFC configurations are complete, queues 3 and 4 with priorities 3 and 4 respectively are lossless queues.
2. Configure PFC deadlock prevention.
   
   
   
   # On Leaf1, create a PFC uplink interface group named **myuplink**, and add interfaces connected to Spine1 and Spine2 to the PFC uplink interface group. The configuration on Leaf2 is similar.
   
   ```
   [~Leaf1] dcb pfc uplink group myuplink
   [*Leaf1-dcb-pfc-uplink-group-myuplink] group-member interface 100ge 1/0/1 to 100ge 1/0/2 
   [*Leaf1-dcb-pfc-uplink-group-myuplink] quit
   [*Leaf1] commit
   ```
   
   
   
   # In the PFC uplink interface group **myuplink**, configure lossless backup queue 4 with the DSCP value 32 and lossy backup queue 2 with the DSCP value 16 for the lossless queue with the DSCP value 24.
   
   ```
   [~Leaf1] dcb pfc uplink group myuplink
   [~Leaf1-dcb-pfc-uplink-group-myuplink] adjust original-dscp 24 to priority 4 dscp 32
   [*Leaf1-dcb-pfc-uplink-group-myuplink] adjust original-dscp 32 to priority 2 dscp 16
   [*Leaf1-dcb-pfc-uplink-group-myuplink] quit
   [*Leaf1] commit
   ```

#### Verifying the Configuration

# Check statistics about PFC deadlock prevention.

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:

```
[~Leaf1] display dcb pfc uplink-group statistics
O/N: Original/New
Slot: 1  Chip: 0
----------------------------------------------------------------------------------------------
Index   PacketType   OutInterface   Priority Dscp                 Count    LastAdjustmentTime
                                    O/N       O/N                                 
----------------------------------------------------------------------------------------------
    0   Layer-3      --             3/4      24/32                 4760    2023-4-13 00:00:00
    1   Layer-3      --             4/2      32/16                   73    2023-4-15 05:00:00
----------------------------------------------------------------------------------------------

```

For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:

```
[~Leaf1] display dcb pfc uplink-group statistics
O/N: Original/New
Slot: 1  Chip: 0
-----------------------------------------------------------------------
Index   NewPriority   Dscp                 Count    LastAdjustmentTime
                       O/N
-----------------------------------------------------------------------
    0             4   24/32                 4760    2023-04-13 00:00:00
    1             2   32/16                   73    2023-04-15 05:00:00
-----------------------------------------------------------------------
```

#### Configuration Scripts

Leaf1

```
#
sysname Leaf1
#
dcb pfc
 priority 3 4
# 
dcb pfc dscp-mapping enable slot 1    //Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
diffserv domain ds1 
 ip-dscp-inbound 24 phb af3 green
#
interface 100GE1/0/1
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
dcb pfc uplink group myuplink
 adjust original-dscp 24 to priority 4 dscp 32
 adjust original-dscp 32 to priority 2 dscp 16 
 group-member interface 100GE1/0/1        
 group-member interface 100GE1/0/2 
#
port-group all_using  
 group-member 100GE1/0/1        
 group-member 100GE1/0/2 
#
return

```

Leaf2

```
#
sysname Leaf2
#
dcb pfc
 priority 3 4
# 
dcb pfc dscp-mapping enable slot 1    //Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.

#
diffserv domain ds1 
 ip-dscp-inbound 24 phb af3 green
#
interface 100GE1/0/1
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
dcb pfc uplink group myuplink
 adjust original-dscp 24 to priority 4 dscp 32
 adjust original-dscp 32 to priority 2 dscp 16
 group-member interface 100GE1/0/1        
 group-member interface 100GE1/0/2 
#
port-group all_using  
 group-member 100GE1/0/1        
 group-member 100GE1/0/2 
#
return

```