radius-attribute check
======================

radius-attribute check

Function
--------

The **radius-attribute check** command enables the device to check the specified attributes in the received RADIUS Access-Accept packets.

The **undo radius-attribute check** command disables the device from checking the specified attributes in the received RADIUS Access-Accept packets.

By default, the device does not check whether a RADIUS Access-Accept packet contains the specified attributes.



Format
------

**radius-attribute check** *attribute-name*

**undo radius-attribute check** [ *attribute-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *attribute-name* | Specifies the name of the RADIUS attribute. If this parameter is specified, the RADIUS Access-Accept packets are checked based on attribute names. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After the radius-attribute check command is executed, the device checks whether the received RADIUS Access-Accept packets contain the specified attributes. If yes, the device considers that authentication was successful; if not, the device considers that authentication failed and discards the packet. For example, after the radius-attribute check filter-id command is executed, the device checks the filter-id attribute in the received RADIUS Access-Accept packets. If a RADIUS packet does not contain this attribute, authentication fails.

**Precautions**

* When you use the undo radius-attribute check command with parameters, the device checks the specified attributes in the RADIUS Access-Accept packets. When you use the undo radius-attribute check command without any parameter, the device does not check RADIUS Access-Accept packets.
* The display radius-attribute can display RADIUS attribute names.


Example
-------

# Check whether the RADIUS Access-Accept packets contain the framed-protocol attribute.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-attribute check framed-protocol

```