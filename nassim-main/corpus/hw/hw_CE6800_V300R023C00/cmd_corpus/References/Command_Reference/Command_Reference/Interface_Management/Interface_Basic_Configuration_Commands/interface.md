interface
=========

interface

Function
--------



The **interface** command displays the view of an existing interface or creates a logical interface and displays the view of the logical interface.

The **undo interface** command deletes a logical interface.



By default, this type of port is not created.


Format
------

**interface** { *interface-name* | *interface-type* *interface-number* }

**undo interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | Enumerated type, depending on the interface type supported by the device. |
| *interface-number* | Specifies the number of an interface. | The value is a string of characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A physical interface cannot be created. You can run the **interface** command to enter the interface view directly.A logical interface can be created. You can run the **interface** command to create a logical interface and enter the view of the logical interface.



**Precautions**



Sub-interfaces cannot be configured on Layer 2 interfaces.




Example
-------

# Create VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1

```

# Create VBDIF 1.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 1
[*HUAWEI-bd1] quit
[*HUAWEI-bd1] interface Vbdif 1
[*HUAWEI-Vbdif1]

```

# Create Loopback 1.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 1
[*HUAWEI-LoopBack1]

```

# Create Tunnel 1.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 1
[*HUAWEI-Tunnel1]

```

# Create NVE 1.
```
<HUAWEI> system-view
[~HUAWEI] interface Nve 1
[*HUAWEI-Nve1]

```