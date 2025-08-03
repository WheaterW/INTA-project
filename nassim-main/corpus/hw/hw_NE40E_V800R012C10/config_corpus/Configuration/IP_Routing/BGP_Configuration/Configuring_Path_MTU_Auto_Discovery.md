Configuring Path MTU Auto Discovery
===================================

Path MTU auto discovery allows BGP to discover the smallest MTU value on a path so that BGP messages are transmitted based on the path MTU. This function improves transmission efficiency and BGP performance.

#### Usage Scenario

The link-layer MTUs of different networks that a communication path traverses may vary. The smallest MTU on the path is the most important factor that influences the communication between the two ends of the path. The smallest MTU on the communication path is called the path MTU.

The path MTU varies with the selected path and therefore may change. In addition, the path MTU in one direction may be inconsistent with that in the reverse direction. Enabling path MTU auto discovery allows a device to discover the path MTU from the transmit end to the receive end. TCP encapsulates IP packets based on the path MTU when transmitting BGP messages.

In [Figure 1](#EN-US_TASK_0172366235__fig_dc_vrp_bgp_cfg_305401), path MTU auto discovery is not enabled, and a BGP peer relationship is established between Device A and Device C. After Device A sends 9000-byte BGP messages to Device C, Device B fragments the messages upon reception by adding one IP header, one Layer 2 frame header, and one Layer 2 frame trailer in each fragment, which reduces transmission efficiency. If a fragment of a message is lost, the message becomes invalid.

**Figure 1** Network without path MTU auto discovery  
![](images/fig_dc_vrp_bgp_cfg_305401.png)  

In [Figure 2](#EN-US_TASK_0172366235__fig_dc_vrp_bgp_cfg_305402), path MTU auto discovery is enabled, and a BGP peer relationship is established between Device A and Device C. Device A sends 9000-byte BGP messages to Device C, and the path MTU is 6000 bytes. In this case, Device B does not fragment the messages upon reception, which improves transmission efficiency.

**Figure 2** Network with path MTU auto discovery  
![](images/fig_dc_vrp_bgp_cfg_305402.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) Enabling path MTU auto discovery affects TCP MSS calculation.

* When path MTU auto discovery is not enabled:
  
  + For the sender, the TCP MSS is calculated using the following formula: **MSS = MIN { CFGMSS, MTU-40 }**
  + For the receiver:
    
    When the device supports SYN Cookie, the MSS is calculated using the following formula: **MSS = MIN { MIN { CFGMSS, MTU-40 } , internally-defined MSS value }**
    
    If the device does not support SYN Cookie, the MSS is calculated using the following formula: **MSS = MIN { CFGMSS, MTU-40 }**
* When path MTU auto discovery is enabled:
  
  + The sender updates the local MSS only when it sends a packet with the MSS greater than the path MTU. The TCP MSS is calculated using the following formula: **MSS = MIN { MIN { CFGMSS, MTU-40 } , PMTU-40 }**
  + For the receiver:
    
    If the device supports SYN Cookie, the TCP MSS is calculated using the following formula: **MSS = MIN { MIN { MIN { CFGMSS, MTU-40 } , internally-defined MSS value } , PMTU-40 }**
    
    If the device does not support SYN Cookie, the TCP MSS is calculated using the following formula: **MSS = MIN { MIN { CFGMSS, MTU-40 } , PMTU-40 }**

Parameters in the formula are described as follows:

* CFGMSS: **MIN { APPMSS, CLICFGMSS }**
  + APPMSS: MSS value configured using the [**peer tcp-mss**](cmdqueryname=peer+tcp-mss) command
  + CLICFGMSS: maximum MSS value configured using the [**tcp max-mss**](cmdqueryname=tcp+max-mss) *mss-value* command
* MTU-40: interface MTU minus 40
* PMTU-40: path MTU minus 40
* internally-defined MSS value: MSS value, including 216, 460, 952, 1400, 2900, 4900, 7900, and 9500. Upon receipt of a packet, the receive-end device uses the internally-defined MSS value which is smaller than but closest to the MSS of the received packet.



#### Pre-configuration Tasks

Before configuring path MTU auto discovery, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+path-mtu+auto-discovery) { *group-name* | *ipv4-address* } **path-mtu auto-discovery**
   
   
   
   Path MTU auto discovery is enabled.
   
   
   
   After the command is run, a BGP peer learns the path MTU, preventing BGP messages from being fragmented during transmission.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The forward and return transmission paths between two BGP peers may be different. Therefore, running this command on both ends is recommended so that the two BGP peers can send messages based on the path MTU.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**tcp timer pathmtu-age**](cmdqueryname=tcp+timer+pathmtu-age) *age-time*
   
   
   
   The aging time is set for an IPv4 path MTU.
   
   The path MTUs vary with the path. If there are multiple routes between two communication hosts and the routes selected for packet transmission change frequently, configure the path MTU aging time so that the system updates path MTUs based on the path MTU aging time, increasing the transmission efficiency.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After performing all configurations related to path MTU auto discovery, you can run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to check whether path MTU auto discovery is successfully configured in the detailed BGP peer information.