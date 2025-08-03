Example for Configuring DCB
===========================

Example for Configuring DCB

#### Networking Requirements

During deployment of a converged data center network, DCB is used to build lossless Ethernet, meeting QoS requirements on the converged data center network.

DeviceA carries common Ethernet traffic and the server cluster's IPC traffic, and the 802.1p priority of IPC traffic is 7. The QoS requirements of these types of traffic are as follows:

* IPC traffic requires low latency.
* Common Ethernet traffic is transmitted in BE mode.

**Figure 1** Networking diagram of a data center![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001563869645.png)

#### Precautions

This example applies to the following models: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.

The CE6885-LL (low-latency mode) supports only PFC. It does not support ETS, DCBX, or specifying the PFC working to auto.


#### Configuration Roadmap

To meet QoS requirements in the preceding scenario, configure DCB on DeviceA.

The configuration roadmap is as follows:

1. If the peer DCBX version is **intel-oui**, switch the DCBX version on DeviceA.
2. Configure DCBX on DeviceA to implement automatic DCB capability negotiation at both ends of a link.
3. Configure PFC on DeviceA to ensure lossless transmission of SAN traffic.
4. Configure ETS on DeviceA to ensure low latency of IPC traffic and bandwidth of SAN traffic.


#### Procedure

1. Switch the DCBX version.
   
   
   
   # The default DCBX version is **IEEE DCBX**. If the DCBX version of the peer device is **intel-oui**, switch the DCBX version on 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] dcb compliance intel-oui
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] dcb compliance intel-oui
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] dcb compliance intel-oui
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. Configure DCBX.
   
   
   ```
   [~DeviceA] lldp enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] lldp tlv-enable dcbx
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] lldp tlv-enable dcbx
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] lldp tlv-enable dcbx
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
3. Configure PFC.
   
   
   
   # Enable PFC globally and enable PFC in queues with priority 3. By default, PFC is enabled globally, and PFC is enabled in queues with priority 3. Therefore, skip this step.
   
   
   
   ```
   [~DeviceA] qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] dcb pfc enable mode auto
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] dcb pfc enable mode auto
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] dcb pfc enable mode auto
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
4. Configure ETS.
   
   
   
   # Create an ETS profile.
   
   ```
   [~DeviceA] dcb ets-profile ets1
   ```
   
   
   
   # Map queue 3 to PG1, queue 7 to PG15, and other queues to PG0. Queue 3 maps PG1, and queues 6 and 7 map PG15 by default, so you only need to add queue 6 to PG0.
   
   ```
   [*DeviceA-ets-ets1] priority-group 0 queue 6
   ```
   
   
   
   # Configure flow control based on the priority group and set DRR weights of PG0 and PG1 to 60% and 40% respectively.
   
   ```
   [*DeviceA-ets-ets1] priority-group 0 drr weight 60
   [*DeviceA-ets-ets1] priority-group 1 drr weight 40
   [~DeviceA-ets-ets1] quit
   ```
   
   
   
   # Apply the ETS profile on 100GE1/0/1 and 100GE1/0/2.
   
   ```
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] dcb ets enable ets1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] dcb ets enable ets1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the ETS profile configuration.

```
[~DeviceA] display dcb ets-profile ets1
ETS Profile: ets1                                                               
------------------------------------------------------------------------------- 
PG(RN)  Q  SCH    Weight              CIR/PIR(kbps)            CBS/PBS(kbytes)  
------------------------------------------------------------------------------- 
 0(0)   -  DRR    60(60)                -/-                      -/-            
        0  PQ          -                -/-                      -/-            
        1  PQ          -                -/-                      -/-            
        2  PQ          -                -/-                      -/-            
        4  PQ          -                -/-                      -/-            
        5  PQ          -                -/-                      -/-            
        6  PQ          -                -/-                      -/-            
 1(1)   -  DRR    40(40)                -/-                      -/-            
        3  PQ          -                -/-                      -/-            
15(15)  -  PQ          -                -/-                      -/-            
        7  PQ          -                -/-                      -/-            
------------------------------------------------------------------------------- 
```

# Check the DCB configuration and negotiation status.

Run the **display dcb** command to check the DCB configuration and negotiation status. If the DCB configuration is correct, the following negotiation result is displayed:

```
[~DeviceA] display dcb
M:Manual;    A:Auto                                                             
------------------------------------------------------------------------------- 
Interface         PFC Name     PFC Status  ETS Name    ETS Status App-Profile   
------------------------------------------------------------------------------- 
100GE1/0/1        default      ENABLE(A)   ets1        SUCCEED     -             
100GE1/0/2        default      ENABLE(A)   ets1        SUCCEED     -             
100GE1/0/3        default      ENABLE(A)   -           -            -             
-------------------------------------------------------------------------------
```
#### Configuration Scripts

```
#
sysname DeviceA
#
dcb pfc                                                                         
#                                                                               
dcb ets-profile default                                                         
#                                                                               
dcb ets-profile ets1                                                            
 priority-group 0 drr weight 60                                                 
 priority-group 1 drr weight 40                                                 
 priority-group 0 queue 0 to 2 4 to 6                                           
 priority-group 15 queue 7                                                      
#                                                                               
dcb app-profile default
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#                                                                               
interface 100GE1/0/1
 lldp tlv-enable dcbx                                                           
 dcb compliance intel-oui                                                       
 dcb ets enable ets1                                                            
 dcb pfc enable mode auto 
#
interface 100GE1/0/2
 lldp tlv-enable dcbx                                                           
 dcb compliance intel-oui                                                       
 dcb ets enable ets1                                                            
 dcb pfc enable mode auto
#
interface 100GE1/0/3 
 lldp tlv-enable dcbx                                                           
 dcb compliance intel-oui                                                       
 dcb pfc enable mode auto
#
lldp enable                                                                     
#
return
```