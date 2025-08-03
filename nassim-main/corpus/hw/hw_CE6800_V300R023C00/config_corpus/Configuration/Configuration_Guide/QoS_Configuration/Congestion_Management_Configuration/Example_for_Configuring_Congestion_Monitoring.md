Example for Configuring Congestion Monitoring
=============================================

Example for Configuring Congestion Monitoring

#### Networking Requirements

Servers store information about voice, video, and data services, and users obtain data from the servers through DeviceB. When a large amount of data is transmitted from the servers to hosts, the total rate of inbound interfaces is higher than the rate of the outbound interface. As a result, congestion may occur on the outbound interface of DeviceB.

When packet loss occurs on the outbound interface of DeviceB due to queue congestion, the administrator needs to know the buffer usage of each queue and information about the packets that cause congestion to determine subsequent network traffic planning and adjustment.

**Figure 1** Network diagram for configuring congestion monitoring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000002010525957.png)
![](public_sys-resources/note_3.0-en-us.png) 

This example is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.



#### Procedure

1. Configure VLANs for each interface so that devices can communicate with each other at the link layer.
   
   
   
   # Configure 100GE 1/0/3 on DeviceB as a trunk interface. Add 100GE 1/0/1 to VLAN 100, 100GE 1/0/2 to VLAN 200, and 100GE 1/0/3 to VLAN 100 and VLAN 200.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 100 200
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port default vlan 100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port default vlan 200
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 100 200
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
2. Enable congestion monitoring. Use the default lower and upper buffer thresholds.
   
   
   ```
   [~DeviceB] interface 100ge 1/0/3
   [~DeviceB-100GE1/0/3] qos buffer-monitoring enable
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check real-time congestion monitoring information about queues on 100GE 1/0/3.

```
<DeviceB> display qos buffer-monitoring result interface 100ge 1/0/3
Queue Time                        BufferUsage(Bytes)     Percent(%)  
--------------------------------------------------------------------      
0 2015-11-04 09:46:27.095                      0              0      
1 2015-11-04 09:46:27.101                      0              0      
2 2015-11-04 09:46:27.107                      0              0      
3 2015-11-04 09:46:27.113                1598064            100      
4 2015-11-04 09:46:27.118                      0              0      
5 2015-11-04 09:46:27.124                      0              0      
6 2015-11-04 09:46:27.130                      0              0      
7 2015-11-04 09:46:27.136                      0              0  
-------------------------------------------------------------------- 
```

#### Configuration Scripts

DeviceB

```
#
sysname DeviceB
#
vlan batch 100 200
#
interface 100GE1/0/1
 port default vlan 100
#
interface 100GE1/0/2
 port default vlan 200
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 100 200
 qos buffer-monitoring enable
#
return
```