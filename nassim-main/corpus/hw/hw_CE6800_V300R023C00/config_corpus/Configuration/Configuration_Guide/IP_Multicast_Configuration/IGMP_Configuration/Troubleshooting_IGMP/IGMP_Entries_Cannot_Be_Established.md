IGMP Entries Cannot Be Established
==================================

IGMP Entries Cannot Be Established

#### Fault Symptom

After IGMP is configured, a host requests data from multicast group G. However, the last-hop multicast device does not generate any IGMP entries.


#### Possible Causes

1. The group address requested by the host has been reserved by the protocol.
2. The interface connected to the host's network segment is down.
3. IP multicast routing is disabled.
4. IGMP is disabled on the interface that is directly connected to the host.
5. The IGMP configuration on the interface is incorrect.

#### Procedure

1. Check whether the group address requested by the host has been reserved by the protocol.
   
   
   
   The reserved group addresses range from 224.0.0.1 to 224.0.0.255. The device does not generate an IGMP entry for an IGMP Report message with one of these group addresses as the destination address. If the group address requested has been reserved by the protocol, change the group address to one that has not been reserved.
2. Check whether the interface connected to the host's network segment is up.
   
   
   ```
   [display interface](cmdqueryname=display+interface) interface-type interface-number
   ```
   
   
   
   If the interface is down, the possible causes are: the interface is not correctly connected; the [**shutdown**](cmdqueryname=shutdown) command has been run on the interface; the IP address configured on the interface is incorrect. In this case, rectify the fault according to the corresponding cause.
3. Check whether IP multicast routing is enabled.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration)
   ```
   
   
   
   If the command output does not contain "multicast routing-enable," run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command in the system view to enable IP multicast routing.
4. Check whether IGMP is enabled on the interface that is directly connected to the host.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration) interface interface-type interface-number
   ```
   
   
   
   If the command output does not contain "igmp enable," IGMP is not enabled. Run the [**igmp enable**](cmdqueryname=igmp+enable) command in the interface view to enable IGMP.
5. Check whether the IGMP configuration on the interface is correct.
   
   
   ```
   [display igmp](cmdqueryname=display+igmp) [ vpn-instance vpn-instance-name | all-instance ] interface interface-type interface-number
   ```
   
   
   
   If the IGMP version displayed in "Current IGMP version" is earlier than the IGMP version used by the host, run the **igmp version** command to change the IGMP version to the one used by the host or later.
   
   If "IGMP group policy" displays an ACL rule, check whether the multicast group address is rejected by the ACL rule. If so, modify the ACL rule to allow the device to receive Report messages from this multicast group.