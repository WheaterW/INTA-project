Configuring IGMP Snooping Querier
=================================

Configuring IGMP Snooping Querier

#### Context

By listening to IGMP messages exchanged between an IGMP querier and user hosts, a Layer 2 device on which IGMP snooping is enabled can dynamically create Layer 2 multicast forwarding entries to implement Layer 2 multicast. However, such a device cannot dynamically create these entries in the following situations:

* The interfaces on the upstream Layer 3 multicast device do not run IGMP. Instead, static multicast groups are configured on them.
* The multicast source is located on the same Layer 2 network as user hosts, and no Layer 3 multicast device is required.

In these situations, you can configure the IGMP snooping querier function on the Layer 2 multicast device so that this device sends IGMP Query messages to user hosts on behalf of the Layer 3 multicast device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Enable the IGMP snooping querier function.
   
   
   ```
   [igmp snooping querier enable](cmdqueryname=igmp+snooping+querier+enable)
   ```
   
   
   
   After the IGMP snooping querier function is enabled, the device periodically broadcasts IGMP Query messages to all the interfaces (including the router ports) in the BD. This may result in the reelection of the IGMP querier if one already exists on the multicast network. In this case, you are advised not to configure the IGMP snooping querier function. However, if this function must be configured, ensure that the source IP address of the General Query messages sent by the device is larger than the IP address of the upstream IGMP querier.
   
   IGMP snooping querier and IGMP snooping proxy cannot both be enabled in the same BD.
4. (Optional) Configure the querier election function.
   
   
   ```
   [igmp snooping querier-election](cmdqueryname=igmp+snooping+querier-election)
   ```
   
   
   
   If the querier function is enabled on multiple devices in the same BD, the querier election function needs to be enabled. After one of these devices is elected as the querier, it sends Query messages to user hosts on behalf of the upstream device.
5. (Optional) Set querier parameters.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When setting parameters, ensure that the maximum time for the response to IGMP Query messages is shorter than the interval for sending IGMP General Query messages.
   
   
   **Table 1** Setting querier parameters
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set an interval for sending General Query messages. | [**igmp snooping query interval**](cmdqueryname=igmp+snooping+query+interval) *QueryIntervalValue* | The querier sends General Query messages at the specified interval to maintain group memberships in the BD. |
   | Configure an IGMP robustness variable. | [**igmp snooping robust-count**](cmdqueryname=igmp+snooping+robust-count) *robust-count-value* | The robustness variable defines the following values: * Number of times a querier sends General Query messages after startup. The interval for sending such messages in this case is 1/4 of the interval for sending General Query messages. * Number of times a querier sends IGMP Group-Specific Query messages after a Leave message is received. The interval for sending such messages in this case is the same as that for sending IGMP Group-Specific Query messages. |
   | Set the maximum time for response to IGMP Query messages. | [**igmp snooping query max-response-time**](cmdqueryname=igmp+snooping+query+max-response-time) *QueryRspIntValue* | When receiving an IGMP Report message from a host, the device determines the aging time of the member port as follows: Interval for sending General Query messages x IGMP robustness variable + Maximum response time.  After a multicast group member receives an IGMP Query message, it must send a Report message before the maximum response time expires if it still requires the traffic of the multicast group. This command is not supported in IGMPv1. |
   | Configure an interval for sending Group-Specific Query messages. | [**igmp snooping query lastmember-queryinterval**](cmdqueryname=igmp+snooping+query+lastmember-queryinterval) *LastMemQIValue* | When receiving a Leave message from a host, the device determines the aging time of the member port as follows: Interval for sending Group-Specific Query messages x IGMP robustness variable. The device continuously sends Group-Specific Query messages (for the number of times specified by the IGMP robustness variable) to check whether the multicast group has other members. This command is not supported in IGMPv1. |
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. (Optional) Configure a source IP address for IGMP General Query messages.
   
   
   ```
   [igmp snooping send-query source-address](cmdqueryname=igmp+snooping+send-query+source-address) ip-source-address
   ```
   
   
   
   By default, the source IP address of General Query messages sent by the IGMP snooping querier is 192.168.0.1. If this address is already in use on the network, use this command to set a different address.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```