Configuring RIP GTSM
====================

Configuring RIP GTSM

#### Context

You can configure the generalized time to live security mechanism (GTSM) to improve the security of a RIP network. Attackers can simulate RIP messages and continuously send them to a routing device. In such cases, these messages are destined for the routing device, which directly forwards them to the control plane for processing without validation. As a result, the increased processing workload on the control plane causes high CPU usage. A routing device enabled with GTSM defends against such attacks by checking whether the TTL value in each IP packet header is within a pre-defined range.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure RIP GTSM.
   
   
   ```
   [rip valid-ttl-hops](cmdqueryname=rip+valid-ttl-hops) valid-ttl-hops-value [ vpn-instance vpn-instance-name ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The valid TTL range of the detected messages is [255â*valid-ttl-hops-value*+1, 255].
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```