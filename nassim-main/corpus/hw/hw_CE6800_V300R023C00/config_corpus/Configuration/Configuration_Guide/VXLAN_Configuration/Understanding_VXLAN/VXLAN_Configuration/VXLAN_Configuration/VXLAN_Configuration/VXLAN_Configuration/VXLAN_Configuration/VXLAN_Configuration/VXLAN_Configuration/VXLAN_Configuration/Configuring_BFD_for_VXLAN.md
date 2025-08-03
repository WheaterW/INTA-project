Configuring BFD for VXLAN
=========================

Configuring BFD for VXLAN

#### Prerequisites

Before configuring BFD for VXLAN, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

BFD for VXLAN enables a network to quickly detect a primary tunnel fault and switch traffic to a backup tunnel. This ensures normal traffic forwarding and improves network reliability. To implement BFD for a VXLAN tunnel, configure a BFD session for the VXLAN tunnel.

**Application Scenarios**

BFD for VXLAN uses BFD to detect the connectivity of VXLAN tunnels. It implements VXLAN tunnel switching and improves the reliability of services transmitted over VXLAN tunnels.

BFD for VXLAN is typically used when VXLAN gateways interwork with VM simulation devices, as shown in [Figure 1](#EN-US_TASK_0000001176664051__fig116441245164714). On a network where no VM simulation device is deployed, if service traffic of VM3 needs to be forwarded to VM1 and VM2, Device3 directly forwards unicast service traffic to Device1 or Device2. For BUM traffic, Device3 uses ingress replication for multiple traffic copies and sends them to Device1 and Device2. If there are many VMs, ingress replication wastes a lot of resources. To reduce network pressure, deploy the VM simulation device. The VM simulation device uses replicator nodes to perform centralized replication of BUM packets. In this case, each VTEP encapsulates a BUM packet into the replicator tunnel and sends it only to the replicator, which then sends the packet to other VTEPs (except the source VTEP). Replicators can be deployed in clusters (consisting of multiple replicator nodes) to improve network reliability.

**Figure 1** BFD for VXLAN  
![](figure/en-us_image_0000001130624548.png)

**Fundamentals**

[Figure 2](#EN-US_TASK_0000001176664051__fig_dc_vrp_feature_vxlan_105002) shows the format of a BFD for VXLAN packet.

**Figure 2** Format of a BFD for VXLAN packet  
![](figure/en-us_image_0000001130784342.png)
The BFD for VXLAN packet forwarding process is as follows:

* A VTEP establishes multiple VXLAN tunnels, one for each replicator, which back each other up. Only one of them is used to forward BUM traffic. Therefore, the replicator that receives a BUM packet replicates and forwards it to the other replicators.
* A BFD for VXLAN session is deployed between a VXLAN gateway and a replicator cluster to detect the tunnel connectivity between them. If one tunnel fails, traffic is automatically switched to a backup link for forwarding.

Assume that a centralized VXLAN replication group on Device3 has two VXLAN tunnels.

1. The destination VTEPs are Replicator1 and Replicator2 for the two VXLAN tunnels in the centralized replication group on Device3. The tunnel between Device3 and Replicator1 is the primary VXLAN tunnel.
2. Device3 forwards a BUM packet received from VM3 to the primary VXLAN tunnel between Device3 and Replicator1.
3. BFD for VXLAN monitors the primary VXLAN tunnel.
4. If the VXLAN tunnel between Device3 and Replicator1 fails, Device3 detects the fault through BFD, performs fast traffic switching, and selects the backup tunnel. BUM traffic on Device3 is then forwarded through the tunnel between Device3 and Replicator2, ensuring reliable traffic forwarding.

The following procedure uses Device3 to describe how to configure BFD for VXLAN.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
   
   By default, BFD is not enabled globally.
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Create a BFD for VXLAN session and enter the session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) session-name bind vxlan peer-ip peer-ip-address source-ip source-ip-address peer-mac peer-mac-address auto
   ```
   
   By default, no BFD for VXLAN session is created.
5. (Optional) Configure the interval at which BFD packets are sent.
   
   
   ```
   [min-tx-interval](cmdqueryname=min-tx-interval) tx-interval
   ```
   
   The default interval is 1000 milliseconds.
6. (Optional) Configure the interval at which BFD packets are received.
   
   
   ```
   [min-rx-interval](cmdqueryname=min-rx-interval) rx-interval
   ```
   
   The default interval is 1000 milliseconds.
7. (Optional) Configure a local detection multiplier.
   
   
   ```
   [detect-multiplier](cmdqueryname=detect-multiplier) multiplier
   ```
   
   By default, the local detection multiplier is 3.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command to check BFD session information.