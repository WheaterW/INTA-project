Understanding the Function of Adding Option 82 to a DHCP Message
================================================================

Understanding the Function of Adding Option 82 to a DHCP Message

#### Overview

In conventional DHCP-based dynamic IP address allocation mode, a DHCP server cannot obtain the physical location of a DHCP client based on a DHCP request message. As a result, DHCP clients in the same VLAN have the same rights to obtain IP addresses. Because the network administrator cannot control the access of specific DHCP clients in the same VLAN to network resources, this threatens the security control of the network.

RFC 3046 defines the DHCP Relay Agent Information Option (Option 82) to record the location of a DHCP client. A DHCP snooping-enabled device or a DHCP relay agent adds Option 82 to a DHCP request message to send the accurate location of a DHCP client to the DHCP server. This enables the DHCP server to allocate a proper IP address and other configurations to the DHCP client, implementing security control on the DHCP client.

Option 82 contains two common sub-options: Circuit ID and Remote ID. The Circuit ID sub-option identifies a client's information such as the VLAN ID and interface number, whereas the Remote ID sub-option identifies the device to which a client connects. Typically, the Remote ID sub-option identifies the MAC address of the device.

When the device functions as a DHCP relay agent, it supports Option 82 regardless of whether DHCP snooping is enabled or disabled. However, if the device functions as an access device on a Layer 2 network, Option 82 can be used only after DHCP snooping is enabled.


#### Implementation

The device supports Option 82 when it functions as a DHCP relay agent or an access device on a Layer 2 network and has DHCP snooping enabled. Option 82 can be enabled in two modes: Insert and Rebuild. The device processes DHCP request messages differently in each of the modes.

* Insert mode: If a received DHCP request message does not contain Option 82, the device inserts it into the message. If the message contains Option 82, the device checks whether the option contains the Remote ID sub-option. If so, the device keeps the option unchanged; if not, the device inserts the Remote ID sub-option.
* Rebuild mode: If a received DHCP request message does not contain Option 82, the device inserts it into the message. If the message contains Option 82, the device deletes this option and inserts Option 82 configured by the administrator.

The device processes a reply message from the DHCP server in the same way regardless of whether the Insert or Rebuild mode is used.

* When the DHCP reply message contains Option 82:
  + If the received DHCP request message does not contain Option 82, the device deletes this option from the DHCP reply message, and then forwards the message to the DHCP client.
  + If the received DHCP request message contains Option 82, the device changes the Option 82 format in the DHCP reply message to that in the DHCP request message, and then forwards the message to the DHCP client.
* When the DHCP reply message does not contain Option 82, the device directly forwards the message.