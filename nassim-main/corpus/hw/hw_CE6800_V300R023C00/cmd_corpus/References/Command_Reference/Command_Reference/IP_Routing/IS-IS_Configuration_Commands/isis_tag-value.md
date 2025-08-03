isis tag-value
==============

isis tag-value

Function
--------



The **isis tag-value** command configures an administrative tag value for an interface.

The **undo isis tag-value** command deletes the configured administrative tag value.



By default, no administrative tag value is configured on an interface.


Format
------

**isis tag-value** *tag* [ **level-1** | **level-2** ]

**undo isis tag-value** [ *tag* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tag* | Specifies an administrative tag value for the interface. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Indicates the administrative tag value of the Level-1 interface. | - |
| **level-2** | Indicates the administrative tag value of the Level-2 interface. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An administrative tag carries administrative information about IP address prefixes. Administrative tags can advertise IP address prefixes in the IS-IS area to control routes, simplifying management.The **isis tag-value** command is used to configure an administrative tag value for an interface, and the tag can be used to filter out unwanted routes.

**Prerequisites**



An IS-IS process has been created using the **isis** command.



**Precautions**



Only when the IS-IS cost type is wide, wide-compatible, or compatible, an advertised LSP carries the administrative tag value. The cost type can be configured using the **cost-style** command.The administrative tag value set using the **isis tag-value** command takes precedence over the one set using the **circuit default-tag** command.




Example
-------

# Set the administrative tag value of 100GE1/0/1 to 77.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis tag-value 77

```