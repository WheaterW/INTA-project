interface l2
============

interface l2

Function
--------



The **interface l2** command displays the view of an existing interface, or creates a Layer 2 sub-interface and displays the Layer 2 sub-interface view.

The **undo interface** command deletes a Layer 2 sub-interface.



By default, this type of port is not created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**interface** { *interface-name* | *interface-type* *interface-number* } { *mode* **l2** }

**undo interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of an interface. | The value is of the enumerated type. |
| *interface-number* | Specifies an interface number. | - |
| *mode* | Specifies an interface mode. Currently, the value of this parameter is fixed to mode. mode and l2 are used together to indicate the Layer 2 sub-interface mode. | The value is a string of characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Ethernet virtual connection (EVC) module defines Layer 2 sub-interfaces as service access points. Only Layer 2 sub-interface provides access services. To create a Layer 2 sub-interface, run the interface mode l2 command.The Virtual eXtensible Local Area Network (VXLAN) module defines Layer 2 sub-interfaces as service access points. Only Layer 2 sub-interface provide access services. To create a Layer 2 sub-interface, run the interface mode l2 command.



**Precautions**

After a logical interface is deleted using the **undo interface** command, all the configurations on the interface are automatically deleted. These configurations cannot be restored even if you create an interface same as the one deleted.Layer 2 sub-interfaces can only send access packets to bridge domains, not Layer 3 networks. Each Layer 2 sub-interface can be added to only one BD.


Example
-------

# Create a Layer 2 sub-interface 100GE 1/0/1.1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2

```