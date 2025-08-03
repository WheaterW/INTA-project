if-match source-mac
===================

if-match source-mac

Function
--------



The **if-match source-mac** command configures a matching rule based on the source MAC address in a traffic classifier.

The **undo if-match source-mac** command deletes a matching rule based on the source MAC address in a traffic classifier.



By default, a matching rule based on the source MAC address is not configured in a traffic classifier.


Format
------

**if-match source-mac** *mac-address* [ *mac-address-mask* ]

**undo if-match source-mac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a source MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| *mac-address-mask* | Specifies the mask of the source MAC address.  Similar to the mask of the IP address, the mask of the MAC address determines a group of MAC addresses. The device can accurately match certain bits in the source MAC address using the mask of the MAC address. In practice, you can set these bits to F in the mask of the source MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match source-mac** command to classify packets based on the source MAC address so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

If you run the **if-match source-mac** command in the same traffic classifier view multiple times, only the latest configuration takes effect.


Example
-------

# Configure a matching rule based on the source MAC address of 00e0-fc12-3456 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match source-mac 00e0-fc12-3456

```