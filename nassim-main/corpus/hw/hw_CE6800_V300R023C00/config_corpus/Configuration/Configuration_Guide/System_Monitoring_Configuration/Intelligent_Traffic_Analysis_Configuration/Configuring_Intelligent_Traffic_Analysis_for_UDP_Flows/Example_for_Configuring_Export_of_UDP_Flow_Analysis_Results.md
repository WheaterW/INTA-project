Example for Configuring Export of UDP Flow Analysis Results
===========================================================

Example for Configuring Export of UDP Flow Analysis Results

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001512853440__fig_dc_cfg_traffic-analysis_001501), the client with the IP address 10.1.1.1 sends UDP packets to the server with the IP address 10.1.2.1 and UDP port number 3300. DeviceA on the path can be configured with intelligent traffic analysis for the UDP flow to analyze the flow and export the flow analysis results to the FabricInsight analyzer.

**Figure 1** Network diagram of intelligent traffic analysis for UDP flows![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001564013217.png)

#### Procedure

1. Configure an advanced ACL rule.
   
   
   
   # Configure an advanced ACL rule to match the UDP flow transmitted between the client with the IP address 10.1.1.1 and the server with the IP address 10.1.2.1 and port number 3300.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] acl number 3055
   [*DeviceA-acl4-advance-3055] rule 4 permit udp source 10.1.1.1 0.0.0.0 destination 10.1.2.1 0.0.0.0 destination-port eq 3300 
   [*DeviceA-acl4-advance-3055] quit
   [*DeviceA] commit
   ```
2. Enable intelligent traffic analysis for the UDP flow.
   
   
   
   # Configure a traffic classifier.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3055
   [*DeviceA-classifier-c1] quit
   [*DeviceA] commit
   ```
   
   # Enable intelligent traffic analysis for the UDP flow on DeviceA.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] traffic-analysis enable
   [*DeviceA-behavior-b1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure a traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] commit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~DeviceA] traffic-policy p1 global inbound
   [*DeviceA] commit
   ```
   
   # Set the number of blocks in the UDP flow to be intelligently analyzed to 128 on DeviceA.
   
   ```
   [~DeviceA] traffic-analysis udp identification block 128
   [*DeviceA] commit
   ```
3. Configure UDP flow aging.
   
   
   
   # Set the inactive flow aging time to 100 seconds.
   
   ```
   [~DeviceA] traffic-analysis udp timeout inactive 100
   [*DeviceA] commit
   ```
4. Configure export of UDP flow analysis results.
   
   
   
   # Set the source IP address to 10.1.3.1, destination IP address to 10.1.3.2, and destination port number to 6000 for the exported packets carrying UDP flow analysis results.
   
   ```
   [~DeviceA] traffic-analysis udp export source ip 10.1.3.1
   [*DeviceA] traffic-analysis udp export host ip 10.1.3.2 6000
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display detailed information about intelligent traffic analysis results of UDP flows.

```
[~DeviceA] display traffic-analysis udp cache slot 1
Source IP          : 10.1.1.1 
Destination IP     : 10.1.2.1
Source Port        : 1024
Destination Port   : 3300
Direction          : InBound
Interface          : 100GE1/0/1
Flow Start Time    : 2023-06-16 19:47:07
VNI                : --
----------------------------------------------------------------------------------
Status        Block Id      Block Timestamp    Receive Packets      Receive Bytes 
----------------------------------------------------------------------------------
Previous           154           1516680000                 20               1640 
Current            206           3368361000                 49               4018 
----------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
acl number 3055
 rule 4 permit udp source 10.1.1.1 0.0.0.0 destination 10.1.2.1 0.0.0.0 destination-port eq 3300
#
traffic classifier c1
 if-match acl 3055 
#
traffic behavior b1
 traffic-analysis enable
#
traffic policy p1
 classifier c1 behavior b1
#
traffic-policy p1 global inbound
#
traffic-analysis udp identification block 128
#
traffic-analysis udp timeout inactive 100
#
traffic-analysis udp export source ip 10.1.3.1
#
traffic-analysis udp export host ip 10.1.3.2 6000
#
```