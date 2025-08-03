dhcp option82 append vendor-specific
====================================

dhcp option82 append vendor-specific

Function
--------



The **dhcp option82 append vendor-specific** command inserts the Sub9 suboption into Option 82.

The **undo dhcp option82 append vendor-specific** command restores the default configuration.



By default, Sub9 suboption is not inserted into the Option 82 field of DHCP messages.


Format
------

**dhcp option82 append vendor-specific**

**undo dhcp option82 append vendor-specific**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **dhcp option82 append vendor-specific** command is run on a DHCP relay agent, the device will insert the Sub9 suboption into the Option 82 field of a received DHCP message. When this DHCP message is forwarded to the DHCP server, the server obtains the DHCP client location information from the Sub9 suboption.The Sub9 suboption has old and new formats. The old format contains the vendor ID, for example, hwid. The new format does not contain the vendor ID.Both the dhcp option82 append vendor-specific and **dhcp option82 vendor-specific format** commands can insert the Sub9 into the Option 82 field of the DHCP message, except that the Sub9 formats are different:

* dhcp option82 append vendor-specific: inserts the Sub9 of the new format. The new format includes the location information such as the node identifier, system name, node chassis ID, node slot ID, node port number, and user VLAN.
* dhcp option82 vendor-specific format: inserts the Sub9 of the old format.

**Prerequisites**

The global DHCP function has been enabled using the **dhcp enable** command.

**Precautions**

If both the dhcp option82 append vendor-specific and **dhcp option82 vendor-specific format** commands are configured, the **dhcp option82 append vendor-specific** command takes effect.If the insertion mode is set to insert and the packet carries the Option 82 field:When the **dhcp option82 append vendor-specific** command is run, the device performs the following operations:

* If the Option 82 field does not contain suboption 9, the device inserts suboption 9 in the new format.
* If the Option 82 field carries suboption 9 in the new format, the device adds suboption 9 to the original packet. If the Option 82 field carries suboption 9 in the old format, the device does not process the packet.

If the **dhcp option82 vendor-specific format** command is run, the device performs the following operations:

* If the Option 82 field does not contain suboption 9, the device inserts suboption 9 in the old format.
* If the Option 82 field carries suboption 9 in the new format, the device does not process the suboption. If the carried suboption 9 is in the old format and contains the HWID but does not contain the configured subcode, the corresponding subcode is added after the HWID. If the carried suboption 9 is in the old format but does not contain the HWID, the device adds the HWID and the corresponding suboption 9.

If the Option 82 insertion mode is set to rebuild or packets do not carry the Option 82 field:

* If the **dhcp option82 append vendor-specific** command is run, the device replaces or adds suboption 9 in the original packet based on the new format.
* If the **dhcp option82 vendor-specific format** command is run, the device replaces or adds suboption 9 in the original packet according to the old format.

The total length of the Option 82 field cannot exceed 255 bytes.


Example
-------

# Insert the Sub9 suboption into the Option 82 field of DHCP messages in the 100GE 1/0/1 interface view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] dhcp option82 insert enable
[*HUAWEI-100GE1/0/1] dhcp option82 append vendor-specific

```