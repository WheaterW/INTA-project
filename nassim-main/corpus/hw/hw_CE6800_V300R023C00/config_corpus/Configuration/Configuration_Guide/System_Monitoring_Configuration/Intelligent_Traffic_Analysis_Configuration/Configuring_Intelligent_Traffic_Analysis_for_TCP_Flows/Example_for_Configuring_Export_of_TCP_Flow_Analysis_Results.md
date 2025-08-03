Example for Configuring Export of TCP Flow Analysis Results
===========================================================

Example for Configuring Export of TCP Flow Analysis Results

#### Networking Requirements

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support intelligent traffic analysis for TCP flows.

In [Figure 1](#EN-US_TASK_0000001512693824__fig_dc_cfg_traffic-analysis_001501), packets of a TCP flow between the client with the IP address 10.1.1.1 and the server with the IP address 10.1.2.1 traverse the same path in both directions. DeviceA on the path can be configured with intelligent traffic analysis for the TCP flow to analyze the flow and export the flow analysis results to the FabricInsight analyzer.

**Figure 1** Network diagram of intelligent traffic analysis for the TCP flow![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001512853444.png)

#### Procedure

1. Configure an advanced ACL rule.
   
   
   
   # Configure an advanced ACL rule to match the TCP flow transmitted between the client with IP address 10.1.1.1 and the server with the IP address 10.1.2.1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] acl number 3055
   [*DeviceA-acl4-advance-3055] rule 4 permit tcp source 10.1.1.1 0.0.0.0 destination 10.1.2.1 0.0.0.0
   [*DeviceA-acl4-advance-3055] quit
   [*DeviceA] commit
   ```
2. Enable intelligent traffic analysis for the TCP flow.
   
   
   
   # Configure a traffic classifier.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3055
   [*DeviceA-classifier-c1] quit
   [*DeviceA] commit
   ```
   
   # Enable intelligent traffic analysis for the TCP flow on DeviceA.
   
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
   
   # On DeviceA, enable intelligent traffic analysis for unidirectional TCP packets with the sequence numbers or acknowledgment numbers of 0x*XXXXXX*0A (*X* indicates a hexadecimal digit), so that DeviceA can create a unidirectional flow table for these TCP packets.
   
   ```
   [~DeviceA] traffic-analysis tcp one-way sequence 0x0000000A 0x000000FF 
   [*DeviceA] commit
   ```
3. Configure the TCP flow aging function.
   
   
   
   # Set the inactive flow aging time to 100 seconds.
   
   ```
   [~DeviceA] traffic-analysis tcp timeout inactive 100
   [*DeviceA] commit
   ```
4. Configure export of TCP flow analysis results.
   
   
   
   # Set the source IP address to 10.1.3.1, destination IP address to 10.1.3.2, and destination port number to 6000 for the exported packets carrying TCP flow analysis results.
   
   ```
   [~DeviceA] traffic-analysis tcp export source ip 10.1.3.1
   [*DeviceA] traffic-analysis tcp export host ip 10.1.3.2 6000
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display detailed information about intelligent traffic analysis results of TCP flows.

```
[~DeviceA] display traffic-analysis tcp ipv4 cache slot 1
NOTE:  S2C: server to client  C2S: client to server                                                                                 
Traffic analysis cache information:                                                                                                 
-------------------------------------------------------------------------------                                                     
ClientIP            ClientPort          C2S Interface1      C2S Interface2                                                          
ServerIP            ServerPort          S2C Interface1      S2C Interface2                                                          
C2S RTT             C2S Packets         C2S PacketLossUp    C2S PacketLoss                                                          
S2C RTT             S2C Packets         S2C PacketLossUp    S2C PacketLoss                                                          
C2S Vni             S2C Vni             FlowStatus          Time                                                                    
-------------------------------------------------------------------------------  
10.1.1.1            1024                100GE1/0/2           --                                                                
10.1.2.1            24                  --                  --                                                                      
0                   48331               0                   1                                                                   
0                   7788                0                   0                                                                       
--                  --                  ESTABLISH           2019-06-05 19:58:28
-------------------------------------------------------------------------------                                                     
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
acl number 3055
 rule 4 permit tcp source 10.1.1.1 0.0.0.0 destination 10.1.2.1 0.0.0.0
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
traffic-analysis tcp one-way sequence 0x0000000A 0x000000FF
#
traffic-analysis tcp timeout inactive 100
#
traffic-analysis tcp export source ip 10.1.3.1
#
traffic-analysis tcp export host ip 10.1.3.2 6000
#
```