Configuring IPsec QoS
=====================

Configure the IPsec packet format or forwarding behavior to implement QoS for IPsec packets.

#### Context

IPsec QoS is used to back up session table status information between the active and standby devices.

Fragmentation before encryption can be configured globally or locally:

* Global configuration
  
  The global configuration is valid to all created IPsec policies (except for policies in which this is separately configured). You can use the global configuration to improve efficiency. If a large number of IPsec policies need to use this function, you do not need to run the [**ipsec df-bit clear**](cmdqueryname=ipsec+df-bit+clear) command to manually configure this function for IPsec policies one by one.
* Local configuration
  
  For a specific IPsec policy, you can run the [**ipsec df-bit clear**](cmdqueryname=ipsec+df-bit+clear) command to separately configure this function. The local configuration takes precedence over the global configuration.

#### Procedure

* Global configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Globally enable the device to fragment IPsec packets and then encrypt them.
     
     
     1. Run the [**ipsec global df-bit clear**](cmdqueryname=ipsec+global+df-bit+clear) command to clear the DF flag to allow IPsec packet fragmentation.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        You can run the [**ipsec global fragmentation**](cmdqueryname=ipsec+global+fragmentation+aging-time) **aging-time** *aging-time* command to set the aging time of IPsec packet fragments. The default aging time is 5000 ms.
     2. Run the [**ipsec global fragmentation before-encryption**](cmdqueryname=ipsec+global+fragmentation+before-encryption) command to enable the device to fragment and then encrypt IPsec packets.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Local configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure IPsec QoS in the IPsec policy or IPsec policy template based on actual requirements.
     
     
     
     **Table 1** Configuring IPsec QoS
     | Step/Item | IPsec Policy | IPsec Policy Template |
     | --- | --- | --- |
     | Enter the IPsec policy view or IPsec policy template view. | [**ipsec policy**](cmdqueryname=ipsec+policy+isakmp) *policy-name* *sequence-number* **isakmp** | [**ipsec policy-template**](cmdqueryname=ipsec+policy-template) *template-name* *sequence-number* |
     | Set a rate limit. | Run the [**speed-limit**](cmdqueryname=speed-limit) { **inbound** | **outbound** } *speed-limit* [ **ike** ] [ **payload** ] command to set a rate limit.  When multiple tunnels are established on the device, traffic conflict occurs in case of heavy traffic. By running the [**speed-limit**](cmdqueryname=speed-limit) command, you can limit the traffic on each IPsec tunnel. The traffic beyond the limit is discarded. In this manner, traffic on each tunnel can be transmitted. | |
     | Configure the device to fragment and then encrypt IPsec packets. | 1. Run the [**ipsec df-bit clear**](cmdqueryname=ipsec+df-bit+clear) command to clear the DF flag to allow IPsec packet fragmentation. 2. Run the [**ipsec fragmentation before-encryption**](cmdqueryname=ipsec+fragmentation+before-encryption) command to configure the device to fragment and then encrypt IPsec packets.  NOTE:  For the IPsec policies, the [**ipsec df-bit clear**](cmdqueryname=ipsec+df-bit+clear) command takes precedence over the [**ipsec global df-bit clear**](cmdqueryname=ipsec+global+df-bit+clear) command in the system view. | |
     | Configure the priority re-marking function. | + Run the [**set dscp**](cmdqueryname=set+dscp+af11+af12+af13+af21+af22+af23+af31+af32+af33+af41+af42) { *dscp-value* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } { **inbound** | **outbound** } command to set the DSCP value of IPv4 packets. + Run the [**set service-class**](cmdqueryname=set+service-class+af1+af2+af3+af4+be+cs6+cs7+ef+inbound+outbound) { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } { **inbound** | **outbound** } command to set the internal service class corresponding to the EXP value in MPLS headers.  After a packet enters an MPLS network, both the DSCP value of IP headers and EXP value of MPLS headers in the packets are mapped to service classes by default. To allow only the EXP value of MPLS headers to be modified, run this command to set the internal service class.  To enable the EXP value in an MPLS packet header to inherit the DSCP value in the plaintext packet header, run the [**set service-class**](cmdqueryname=set+service-class+inherit-plain+inbound) **inherit-plain** **inbound** command. | |
     | Define a policy template. | - | [**ipsec policy**](cmdqueryname=ipsec+policy+isakmp+template) *policy-name* *seq-number* **isakmp** [ **template** *template-name* ]  After the IPsec policy template is bound to the IPsec policy, you can apply the IPsec policy to the interface to enable functions of the IPsec policy template.  NOTE:  In an IPsec policy group, only one IPsec policy can quote the IPsec policy template.  The names of the IPsec policy template and the IPsec policy must be different. |
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.