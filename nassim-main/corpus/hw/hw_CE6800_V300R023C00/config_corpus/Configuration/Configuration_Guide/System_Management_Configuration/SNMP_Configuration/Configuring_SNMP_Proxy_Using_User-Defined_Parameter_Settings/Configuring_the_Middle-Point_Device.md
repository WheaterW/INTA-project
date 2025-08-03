Configuring the Middle-Point Device
===================================

Configuring the Middle-Point Device

#### Prerequisites

Before configuring a device to communicate with an NMS using SNMP proxy, complete the following tasks:

* Configure a routing protocol to ensure that there are reachable routes between the NMS and the middle-point device and between the middle-point device and the managed device.

#### Context

This section describes how to use user-defined parameter settings to configure Simple Network Management Protocol (SNMP) proxy on the middle-point device.

In this type of SNMP proxy configuration, you must configure SNMP on the managed device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the minimum SNMP password length.
   
   
   ```
   [snmp-agent password min-length](cmdqueryname=snmp-agent+password+min-length) min-length
   ```
   
   After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.
3. Configure SNMP proxy on the middle-point device.
   
   
   
   **Table 1** SNMP proxy configuration tasks
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a proxy rule for SNMP messages. | * If the SNMP message type is GetRequest, SetRequest, or Trap, run the [**snmp-agent proxy rule**](cmdqueryname=snmp-agent+proxy+rule) *rule-name* { **read** | **trap** | **write** } **remote-engineid** *remote-engineid* **target-host** *target-host-name* **params-in** **securityname** { *security-name* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-text* { **v1** | **v2c** } } command to configure a proxy rule for SNMP messages. * If the SNMP message type is Inform, run the [**snmp-agent proxy rule**](cmdqueryname=snmp-agent+proxy+rule) *rule-name* **inform** **remote-engineid** *remote-engineid* **target-host** *target-host-name* **params-in** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-text* **v2c** } command to configure a proxy rule for SNMP messages. | In order for an NMS to effectively manage a managed device, configure attributes for the NMS to receive SNMP proxy messages. This allows the middle-point device to filter out SNMP messages that do not match the specified attributes. You must configure correct proxy rules for SNMP messages and ensure that these proxy rules are unique on the middle-point device.  If you specify neither **authentication** nor **privacy**, SNMPv3 messages are neither authenticated nor encrypted. |
   | Create an SNMP proxy community. | [**snmp-agent proxy community**](cmdqueryname=snmp-agent+proxy+community) { *community-name* | **cipher** *cipher-name* } **remote-engineid** *remote-engineid* [ **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \* | A community is a set of an NMS and SNMP agents and is identified using a community name. The community name acts like a password to regulate access to a managed device. An NMS can access a managed device only if the community name carried in the SNMP request sent by the NMS is the same as that configured on the managed device.  After the weak password dictionary maintenance function is enabled, the value of *community-name* cannot be any password defined in the weak password dictionary. (You can run the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command to view the passwords defined in the weak password dictionary.)  This operation applies only to SNMPv1 and SNMPv2c. |
   | Configure attributes of the target hosts for receiving SNMP proxy messages. | Run one of following commands as needed: * On an IPv4 network, run the [**snmp-agent proxy target-host**](cmdqueryname=snmp-agent+proxy+target-host) *target-host-name* **address** **udp-domain** *ip-address* **udp-port** *port-number* [ { **source** { *interface-type interface-number* | **interface-name** } | { **vpn-instance** *vpn-instance-name* | **public-net** } } | { **timeout** *timeout-value* } ]\* **params** **securityname** { *security-name* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-text* { **v1** | **v2c** } } command to configure attributes for the target host to receive SNMP proxy messages. * On an IPv6 network, run the [**snmp-agent proxy target-host**](cmdqueryname=snmp-agent+proxy+target-host) *target-host-name* **ipv6 address udp-domain** *ipv6-address* **udp-port** *port-number* [ { **source** { *interface-type* *interface-number* | *interface-name* } | { **vpn-instance** *vpn-name* | **public-net** } } | { **timeout** *timeout-value* } ] \* **params securityname** { *security-string* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *security-string-cipher* { **v1** | **v2c** } } command to configure attributes for the target host to receive SNMP proxy messages. | This operation enables the middle-point device to forward SNMP requests from the NMS to the managed device and forward responses from the managed device to the NMS.  * The target host may be either the NMS or the managed device. * You can run the command multiple times with different parameters set to configure a middle-point device to send SNMP proxy messages to multiple NMSs. * The default number of the destination UDP port is 162, a well-known port number. If you want to change this number to a non-well-known port number, ensure that the new UDP port number is the same as that on the NMS. * If you specify neither **authentication** nor **privacy**, SNMPv3 messages are neither authenticated nor encrypted. * If the NMS and managed device need to communicate over a virtual private network (VPN), use the **vpn-instance** *vpn-instance-name* parameter. |
   | Create an SNMP proxy user. | [**snmp-agent**](cmdqueryname=snmp-agent) **remote-engineid** *engine-Id* | SNMPv1 and SNMPv2c use community names for authentication, whereas SNMPv3 uses usernames for authentication.  Unlike SNMPv1 or SNMPv2c, SNMPv3 can implement access control, identity authentication, and data encryption using the local processing model and User-based Security Model (USM). SNMPv3 achieves higher security and confidentiality and is applicable to a wider range than SNMPv1 and SNMPv2c.  This operation applies only to SNMPv3 networking. |
   | Configure the priority of SNMP messages. | [**snmp-agent packet-priority**](cmdqueryname=snmp-agent+packet-priority) { **snmp** | **trap** } *priority-level* | Change the priority of SNMP messages in the following scenarios if necessary: * Increase the priority of notifications to ensure that the NMS receives them. * Increase the priority of GetResponse and SetResponse messages to facilitate management operations performed on the MIB of a managed device by the NMS. * Reduce the priority of SNMP messages (including GetResponse, SetResponse, Trap, and Inform messages) to prevent frequent message sending when network congestion occurs. The default priority of SNMP messages is 6. |
4. Configure the SNMP proxy to receive and respond to requests from the managed device.
   
   
   
   **Table 2** Configuring the SNMP proxy to receive and respond to requests from the managed device
   | Operation | Command | Description |
   | --- | --- | --- |
   | Specify the source interface for the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-status) { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* } | N/A |
   | Enable all IPv4 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status) | N/A |
   | Specify the source IPv6 address for the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+source-status) *ip-address* [ **vpn-instance** *vpn-instance-name* ] | N/A |
   | Enable all IPv6 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status) | N/A |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```