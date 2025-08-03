MLD Entries Cannot Be Established
=================================

MLD Entries Cannot Be Established

#### Fault Symptom

After MLD is configured, a host requests data from multicast group G. However, the last-hop multicast device does not generate any MLD entries.


#### Possible Causes

1. The group address requested by the host has been reserved by the protocol.
2. The interface connected to the host's network segment is down.
3. IPv6 multicast routing is disabled.
4. MLD is disabled on the interface that is directly connected to the host.
5. The MLD configuration on the interface is incorrect.

#### Procedure

1. Check whether the group address requested by the host has been reserved by the protocol.
   
   
   
   The reserved group address range is FF0x::. The device does not generate an MLD entry for an MLD Report message with one of these group addresses as the destination address. If the group address requested has been reserved by the protocol, change the group address to one that has not been reserved.
2. Check whether the interface connected to the host's network segment is up.
   
   
   ```
   [display interface](cmdqueryname=display+interface) interface-type interface-number
   ```
   
   
   
   If the interface is down, the possible causes are as follows: the interface is not correctly connected; the [**shutdown**](cmdqueryname=shutdown) command has been run on the interface; or the IPv6 address configured on the interface is incorrect. In this case, rectify the fault according to the corresponding cause.
3. Check whether IPv6 multicast routing is enabled.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration)
   ```
   
   
   
   If the command output does not contain "multicast ipv6 routing-enable," run the [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable) command in the system view to enable IPv6 multicast routing.
4. Check whether MLD is enabled on the interface that is directly connected to the host.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration) interface interface-type interface-number
   ```
   
   
   
   If the command output does not contain "mld enable," MLD is not enabled. Run the [**mld enable**](cmdqueryname=mld+enable) command in the interface view to enable MLD.
5. Check whether the MLD configuration on the interface is correct.
   
   
   ```
   [display mld interface](cmdqueryname=display+mld+interface) [ interface-type interface-number ] [ verbose ]
   ```
   
   
   
   If the MLD version displayed in "Current MLD version" is earlier than that used by the host, run the **mld version** command to change the version to the one used by the host or a later version.
   
   If "MLD group policy" displays an ACL6 rule, check whether the multicast group address is rejected by the ACL6 rule. If it is, modify the ACL6 rule to allow the device to receive Report messages from this multicast group.