radius-server nas-port-id-format
================================

radius-server nas-port-id-format

Function
--------

The **radius-server nas-port-id-format** command sets the format of the NAS port ID attribute.

The **undo radius-server nas-port-id-format** command restores the default format of the NAS port ID attribute.

By default, the new format of the NAS port ID attribute is used.



Format
------

**radius-server nas-port-id-format** { **new** | **old** | **vendor** *vendor-id* }

**undo radius-server nas-port-id-format**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **new** | Uses the new format of the NAS port ID. | - |
| **old** | Uses the old format of the NAS port ID. | - |
| **vendor** *vendor-id* | Uses the NAS port ID format that is customized by the vendor. | The value is 9. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The NAS port format and the NAS port ID format are developed by Huawei, which are used to ensure connectivity and service cooperation among Huawei devices.

**Precautions**

If the new parameter is selected:

* For Ethernet access users, the NAS port ID format is slot=xx; subslot=xx; port=xxx; VLAN ID=xxxx; interfaceName=port, in which slot ranges from 0 to 15, subslot from 0 to 15, port from 0 to 255, and VLAN ID from 1 to 4094. interfaceName indicates the user access interface, including the interface type and number.
* For ADSL access users, the NAS port ID format is slot=xx; subslot=x; port=x; VPI=xxx; VCI=xxxxx; interfaceName=port, in which slot ranges from 0 to 15, subslot from 0 to 9, port from 0 to 9, VPI from 0 to 255, and VCI from 0 to 65535. interfaceName indicates the user access interface, including the interface type and number.If the old parameter is selected:
* For Ethernet access users, the NAS port ID format is port number (2 characters) + subslot number (2 bytes) + card number (3 bytes) + VLAN ID (9 characters).
* For ADSL access users, the NAS port ID format is port number (2 characters) + subslot number (2 bytes) + card number (3 bytes) + VPI (8 characters) + VCI (16 characters). The fields are prefixed with 0s if they contain fewer bytes than specified.vendor vendor-id: uses the vendor-defined format. Currently, the value of vendor-id can only be 9. The format is interface type+interface number, indicating a user access interface. You can run the **display access-user user-id user-id** command to check the user access interface, which is displayed as the User access Interface field in the command output.



Example
-------

# Set the format of the NAS port ID attribute to new.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server nas-port-id-format new

```