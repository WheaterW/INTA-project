(Optional) Configuring the MLD Snooping Querier
===============================================

(Optional) Configuring the MLD Snooping Querier

#### Context

A Layer 2 device on which MLD snooping is enabled can dynamically create Layer 2 multicast forwarding entries and provide Layer 2 multicast functions by listening to MLD messages exchanged between an MLD querier and user hosts.

However, an MLD snooping-enabled device cannot listen to MLD messages and therefore cannot create dynamic Layer 2 multicast entries if the following conditions exist:

* The interfaces on the upstream Layer 3 multicast device do not run MLD. Instead, static multicast groups are configured on them.
* The multicast source is located on the same Layer 2 network as user hosts, and no Layer 3 multicast device is required.

If the preceding conditions exist, you can configure the MLD snooping querier function on the Layer 2 multicast device so that it sends MLD Query messages to user hosts on behalf of the Layer 3 multicast device.

![](../public_sys-resources/note_3.0-en-us.png) 

* When configuring MLD snooping in an M-LAG scenario, ensure that the MLD snooping querier configuration is consistent on the active and standby M-LAG devices.
* MLD snooping querier and MLD snooping proxy cannot be enabled in the same VLAN.
* The MLD snooping querier function cannot be enabled in a VLAN if the corresponding Layer 3 VLANIF interface has Layer 3 multicast functions (such as MLD and PIM) enabled.
* After the MLD snooping querier function is enabled in a VLAN, the device periodically broadcasts MLD Query messages to all the interfaces (including the router ports) in the VLAN. This may result in the reelection of the MLD querier if one already exists on the multicast network. In this case, you are advised not to configure the MLD snooping querier function. However, if this function must be configured, ensure that the source IP address of the General Query messages sent by the device is larger than the IP address of the upstream MLD querier.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Enable the MLD snooping querier function.
   
   
   ```
   [mld snooping querier enable](cmdqueryname=mld+snooping+querier+enable)
   ```
4. (Optional) Configure the querier election function.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   When setting querier parameters, ensure that the interval for sending MLD General Query messages is larger than the maximum response time for MLD Query messages.
   
   
   | Querier Parameter | Configuration Command | Parameter Description | Default Setting | Supported Version |
   | --- | --- | --- | --- | --- |
   | Interval for sending General Query messages | [**mld snooping query interval**](cmdqueryname=mld+snooping+query+interval) **query-interval** | This parameter determines the interval at which a querier sends General Query messages to maintain the memberships in a VLAN. | 125 seconds | MLDv1, MLDv2 |
   | MLD robustness variable | [**mld snooping robust-count**](cmdqueryname=mld+snooping+robust-count) *robust-count* | The robustness variable defines the following values: * Number of times a querier sends General Query messages after startup. The interval for sending such messages in this case is 1/4 of the interval for sending General Query messages. * Number of times a querier sends MLD Group-Specific Query messages after a Done message is received. The interval for sending such messages in this case is the same as that for sending MLD Group-Specific Query messages. | 2 | MLDv1, MLDv2 |
   | Maximum response time of MLD Query messages | [**mld snooping query max-response-time**](cmdqueryname=mld+snooping+query+max-response-time) *max-response-time* | When receiving an MLD Report message from a host, the device determines the aging time of the member port as follows: Interval for sending General Query messages x MLD robustness variable + Maximum response time.  After a multicast member receives an MLD Query message, it must send a Report message before the maximum response time expires if it still requires the group's traffic. | 10s | MLDv1, MLDv2 |
   | Interval for sending Group-Specific Query messages | [**mld snooping query last-member-interval**](cmdqueryname=mld+snooping+query+last-member-interval) *l*astmember-queryinterval** | This parameter specifies the interval for sending Group-Specific Query messages. When receiving a Done message from a host, the device determines the aging time of the member port as follows: Interval for sending Group-Specific Query messages x MLD robustness variable. The device continuously sends Group-Specific Query messages (for the number of times specified by the MLD robustness variable) to check whether the multicast group has other members. | 1s | MLDv1, MLDv2 |
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Configure a source IP address for MLD General Query messages.
   
   
   ```
   [mld snooping send-query source-address](cmdqueryname=mld+snooping+send-query+source-address) ip-address
   ```
   
   By default, the source IP address of General Query messages sent by the MLD snooping querier is FE80::. If this address is already in use on the network, use this command to set a different address. If the [**mld-snooping send-query source-address**](cmdqueryname=mld-snooping+send-query+source-address) command is executed in both the system view and VLAN view, the configuration in the VLAN view is preferentially used.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```