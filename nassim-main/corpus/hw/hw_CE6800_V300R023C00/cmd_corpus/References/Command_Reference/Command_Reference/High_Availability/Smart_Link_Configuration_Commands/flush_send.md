flush send
==========

flush send

Function
--------



The **flush send** command enables a Smart Link group to send Flush packets and specifies the control VLAN ID and password to be carried in the Flush packets.

The **undo flush send** command disables the function.



By default, a Smart Link group does not send Flush packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**flush send control-vlan** *vlan-id* [ **password** { **sha** | **simple** | **hmac-sha256** } *password* ]

**undo flush send**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **password** | Specifies the encryption mode of the password in Flush packets. | - |
| *password* | Specifies a password carried in Flush packets. | * A simple password is a string of 1 to 16 characters. * When the password is encrypted in SHA256 or HMAC SHA256 mode, the value is a string of 48 characters. * If the source version supports a ciphertext password of 24 or 32 characters, the target version also supports a ciphertext password of 24 or 32 characters.   The value is a string of 1 to 16 case-sensitive characters or 24/32/48/108/128 case-sensitive characters. |
| **sha** | Indicates that the password for sending Flush packets uses the SHA256 encryption mode. | - |
| **simple** | Specifies the password of Flush packets is in simple text. | - |
| **hmac-sha256** | Specifies the password of Flush packets is in HMAC-SHA256 encryption mode. | - |
| **control-vlan** *vlan-id* | Specifies the control VLAN ID of Smart Link Flush packets. | The value is an integer that ranges from 1 to 4094. |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a link switchover is performed in a Smart Link group, the existing forwarding entries no longer apply to the new topology. All MAC address entries and Address Resolution Protocol (ARP) entries on the network must be updated. In this situation, you can configure the Smart Link group on a downstream device to send Flush packets to instruct upstream devices to update their MAC address entries and ARP entries.To enable a Smart Link group to send Flush packets and specify the control VLAN ID and password carried in the packets, run the flush send command in the Smart Link group view.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command.

**Follow-up Procedure**

Run the **smart-link flush receive** command to enable an interface on an upstream device to receive Flush packets. The sent and received Flush packets must have the same encryption mode, control VLAN ID, and password.

**Precautions**

* The control VLAN must be an existing static VLAN on the device. If the specified static VLAN does not exist on the device, Flush packets cannot be sent.
* When a link switchover occurs in a Smart Link group, the Smart Link group sends Flush packets to instruct other devices to update their MAC address tables and ARP tables to ensure normal packet forwarding.
* Because the Flush packet format varies with vendors, the Flush packets are used only for communication between Huawei switching devices, and the peer device must be enabled to receive Flush packets.
* After you run this command to configure the encryption mode and password, the original encryption mode and password are deleted.
* If the password is encrypted in SHA256 or HMAC SHA256 mode, the original password cannot be restored after the configuration. If you forget the password, you need to reconfigure it.
* If the password for receiving Flush packets is not specified or the simple password mode is specified, security problems may occur.

Example
-------

# Enable Smart Link group 1 to send Flush packets. Set the control VLAN ID to 100 and password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] flush send control-vlan 100 password sha YsHsjx_202206

```