Configuring GTSM for RIP
========================

Generalized TTL Security Mechanism (GTSM) defends against
attacks by checking the TTL value.

#### Context

During network attacks, attackers may simulate RIP packets
and continuously send them to a router. If the packets are destined
for the router, it directly forwards them to the control plane for
processing without validating them. As a result, the increased processing
workload on the control plane results in high CPU usage. Generalized
TTL Security Mechanism (GTSM) defends against attacks by checking
whether the time to live (TTL) value in each IP packet header is within
a pre-defined range.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip valid-ttl-hops**](cmdqueryname=rip+valid-ttl-hops) *valid-ttl-hops-value* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   GTSM is configured
   for RIP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The valid TTL range of the detected
   packets is [ 255 -*valid-ttl-hops-value* + 1, 255
   ].
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.
4. Set the default action for packets that do not match the GTSM
   policy.
   
   
   
   GTSM only checks the TTL values of packets that match the
   GTSM policy. Packets that do not match the GTSM policy can be allowed
   or dropped.
   
   You can enable the log function to record packet
   drop for troubleshooting.
   
   Perform the following configurations
   on the GTSM-enabled Router:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**gtsm default-action**](cmdqueryname=gtsm+default-action) { **drop** | **pass** } command to set a default action for the messages that do not match the GTSM policy.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the default action is configured but no GTSM policy is configured, GTSM does not take effect.
      
      This command is supported only on the Admin-VS and cannot be configured in other VSs. This command takes effect on all VSs.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.