dhcp option82 enable
====================

dhcp option82 enable

Function
--------



The **dhcp option82 enable** command enables a device to insert the Option 82 field to a DHCP message.

The **undo dhcp option82 enable** command disables a device from inserting the Option 82 field to a DHCP message.



By default, a device does not insert the Option 82 field to a DHCP message.


Format
------

**dhcp option82** { **insert** | **rebuild** } **enable**

**undo dhcp option82** { **insert** | **rebuild** } **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **insert** | Enables a device to insert the Option 82 field to a DHCP message. | - |
| **rebuild** | Enables a device to forcibly insert the Option 82 field to a DHCP message. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Option 82 field records the location of the DHCP client. By adding the Option 82 field to a DHCP request message, the device can send the location information of the DHCP client to the DHCP server. The DHCP server can assign an appropriate IP address and other configuration parameters to the DHCP client based on the Option 82 field to implement security control on the client.The function of adding the Option 82 field to DHCP messages can be enabled in Insert or Rebuild mode. The device processes DHCP messages in different modes.Insert: When the device receives a DHCP request message that does not contain the Option 82 field, the device inserts the Option 82 field into the message. If the packet contains the Option 82 field, the device checks whether the Option 82 field contains the remote ID. If yes, the device retains the Option 82 field. If no, the device inserts the remote ID into the Option 82 field.Rebuild mode: When a device receives a DHCP request message without the Option 82 field, the device inserts the Option 82 field into the message. If the DHCP request message contains the Option 82 field, the device deletes the Option 82 field and inserts the Option 82 field configured by the administrator into the message.

When the device receives a response message from the DHCP server in Insert or Rebuild mode, the device processes the message in the same way.The DHCP response message contains the Option 82 field.

* If the DHCP request message received by the device does not contain the Option 82 field, the device deletes the Option 82 field from the DHCP response message and forwards the message to the DHCP client.
* If the DHCP request message received by the device contains the Option 82 field, the device restores the Option 82 field format in the DHCP response message to that in the DHCP request message and forwards the DHCP request message to the DHCP client.

If the DHCP response message does not contain the Option 82 field, the device directly forwards the message.

**Prerequisites**

The device has been configured as a DHCP relay agent.

**Precautions**

* When receiving a DHCP Request message, the device checks whether the field GIADDR in the packet is 0. If so, the **dhcp option82 enable** command takes effect; if not, this command does not take effect.
* DHCP Option 82 must be configured on the user-side of a device; otherwise, the DHCP messages sent to the DHCP server will not carry Option 82.

Example
-------

# Enable the device to insert the Option 82 field to DHCP messages on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] dhcp option82 insert enable

```