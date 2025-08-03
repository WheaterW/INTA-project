(Optional) Configuring IGMP Snooping Querier
============================================

(Optional) Configuring IGMP Snooping Querier

#### Context

A Layer 2 device on which IGMP snooping is enabled can dynamically create Layer 2 multicast forwarding entries and provide Layer 2 multicast functions by listening to IGMP messages exchanged between an IGMP querier and user hosts.

However, an IGMP snooping-enabled device cannot listen to IGMP messages and therefore cannot create dynamic Layer 2 multicast entries if the following conditions exist:

* The interfaces on the upstream Layer 3 multicast device have static multicast groups configured and do not run IGMP.
* The multicast source is located on the same Layer 2 network as user hosts, and no Layer 3 multicast device is deployed.

If the preceding conditions exist, you can configure the IGMP snooping querier function on the Layer 2 multicast device so that it sends IGMP Query messages to user hosts on behalf of the Layer 3 multicast device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Enable the IGMP snooping querier function.
   
   
   ```
   [igmp snooping querier enable](cmdqueryname=igmp+snooping+querier+enable)
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * The IGMP snooping querier function cannot be enabled in a VLAN if the corresponding Layer 3 VLANIF interface has Layer 3 multicast functions (such as IGMP and PIM) enabled.
   * After the IGMP snooping querier function is enabled in a VLAN, the device periodically broadcasts IGMP Query messages to all the interfaces (including the router ports) in the VLAN. This may result in the reelection of the IGMP querier if one already exists on the multicast network. In this case, you are advised not to configure the IGMP snooping querier function. However, if this function must be configured, ensure that the source IP address of the General Query messages sent from the device is larger than the IP address of the upstream IGMP querier.
   * IGMP snooping querier and IGMP snooping proxy cannot both be enabled in the same VLAN.
4. (Optional) Configure the querier election function.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   When setting the querier parameters, ensure that the interval for sending IGMP Query messages is larger than the maximum response time for IGMP Query messages.
   
   
   | Querier Parameter | Configuration Command | Parameter Description | Default Setting | Supported Version |
   | --- | --- | --- | --- | --- |
   | Interval for sending IGMP General Query messages | [**igmp snooping query interval**](cmdqueryname=igmp+snooping+query+interval) *QueryIntervalValue* | This parameter determines the interval at which a querier sends IGMP General Query messages to maintain the memberships in a VLAN. | 60 seconds | IGMPv1, IGMPv2, and IGMPv3 |
   | IGMP robustness variable | [**igmp snooping robust-count**](cmdqueryname=igmp+snooping+robust-count) *robust-count-value* | This parameter defines the following values: * Number of times a querier sends General Query messages after startup. The interval for sending messages is 1/4 of the interval for sending General Query messages. * Number of times a querier sends Group-Specific Query messages after a Leave message is received. The interval for sending messages is the same as that for sending IGMP Group-Specific Query messages. | 2 | IGMPv1, IGMPv2, and IGMPv3 |
   | Maximum response time for IGMP Query messages | [**igmp snooping query max-response-time**](cmdqueryname=igmp+snooping+query+max-response-time) *QueryRspIntValue* | When receiving an IGMP Report message from a host, the device determines the aging time of the member port as follows: General Query interval x IGMP robustness variable + Maximum response time.  After a multicast member receives an IGMP Query message, it must send a Report message before the maximum response time expires if it still requires the group's traffic. | 10 seconds | IGMPv2 and IGMPv3 |
   | Interval for sending Group-Specific Query messages | [**igmp snooping query last-member-interval**](cmdqueryname=igmp+snooping+query+last-member-interval) *LastMemQIValue* | This parameter specifies the interval for sending Group-Specific Query messages. When receiving a Leave message from a host, the device determines the aging time of the member port as follows: Group-Specific Query interval x IGMP robustness variable. The device continuously sends Group-Specific Query messages (the number of which is specified by the IGMP robustness variable) to check whether the multicast group has other members. | 1 second | IGMPv2 and IGMPv3 |
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Configure a source IP address for IGMP General Query messages.
   
   
   * Perform the configuration in the system view:
     ```
     [igmp snooping send-query source-address](cmdqueryname=igmp+snooping+send-query+source-address) ip-source-address
     ```
   * Perform the configuration in the VLAN view:
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [igmp snooping send-query source-address](cmdqueryname=igmp+snooping+send-query+source-address) ip-source-address
     [quit](cmdqueryname=quit)
     ```
   
   By default, the source IP address of General Query messages sent by the IGMP snooping querier is 192.168.0.1. If this address is already in use on the network, use this command to set a different address. If the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) command is run in both the system view and VLAN view, the configuration in the VLAN view is preferentially used.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```