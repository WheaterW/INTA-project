port-security
=============

port-security

Function
--------



The **port-security enable** command enables the port security function and configures the maximum number of MAC addresses that can be learned.

The **undo port-security enable** command disables the port security function or restores the default maximum number of MAC addresses that can be learned.

The **port-security aging-time** command sets the aging time of secure dynamic MAC addresses.

The **undo port-security aging-time** command restores the default aging time of secure dynamic MAC addresses.

The **port-security protect-action** command configures the protection action to be taken when the number of MAC addresses learned by an interface enabled with the port security function reaches the limit.

The **undo port-security protect-action** command restores the default protection action to be taken when the number of MAC addresses learned by an interface enabled with the port security function reaches the limit.

The **port-security mac-address sticky** command enables the sticky MAC function on an interface and adds sticky MAC address entries.

The **undo port-security mac-address sticky** command disables the sticky MAC function on an interface and deletes sticky MAC address entries.



By default, the port security function is disabled on an interface.

By default, the sticky MAC function is disabled.

By default, the aging function of secure dynamic MAC addresses is disabled on an interface.

By default, the maximum number of MAC addresses that can be learned on an interface enabled with the port security function is 1.

By default, the restrict action is taken when the number of MAC addresses learned by an interface enabled with the port security function reaches the limit.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**port-security enable** [ **maximum** *max-number* ]

**port-security mac-address sticky** *mac-address* **vlan** *vlan-id*

**port-security protect-action** { **protect** | **restrict** | **error-down** }

**port-security mac-address sticky**

**port-security aging-time** *time* [ **type** { **absolute** | **inactivity** | **force** } ]

**undo port-security enable** [ **maximum** *max-number* ]

**undo port-security mac-address sticky** *mac-address* **vlan** *vlan-id*

**undo port-security protect-action**

**undo port-security mac-address sticky**

**undo port-security aging-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *max-number* | Specifies the maximum number of MAC addresses that can be learned. | The value is an integer ranging from 1 to 4096. |
| **mac-address** *mac-address* | Specifies a secure static MAC address. | The value is in the H-H-H format, of which H indicates a hexadecimal number of four characters, such as 00e0 and fc01. If less than four characters are entered, the remaining characters are 0s. For example, e0 is displayed as 00e0. |
| **sticky** *mac-address* | Specifies a sticky MAC address. | The value is in the H-H-H format, of which H indicates a hexadecimal number of four characters, such as 00e0 and fc01. If less than four characters are entered, the remaining characters are 0s. For example, e0 is displayed as 00e0. |
| **vlan** *vlan-id* | Specifies a VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **protect** | Indicates that the packets with the source MAC address not contained in the MAC address table are discarded when the number of learned MAC addresses reaches the limit. | - |
| **restrict** | Indicates that the packets with the source MAC address not contained in the MAC address table are discarded and an alarm is generated when the number of learned MAC addresses reaches the limit. | - |
| **error-down** | Indicates that after an error Down event is generated on an interface, the interface is automatically shut down and cannot automatically restore and an alarm is generated. | - |
| **aging-time** *time* | Specifies the aging time of secure dynamic MAC address entries. | The value is an integer that ranges from 1 to 1440, in minutes. |
| **type** | Specifies the aging type of secure dynamic MAC address entries. | - |
| **absolute** | Specifies that the secure dynamic MAC address entries age out based on an absolute time. | - |
| **inactivity** | Specifies that the secure dynamic MAC address entries age out based on a relative time. | - |
| **force** | Indicates that secure dynamic MAC address entries are forcibly aged out based on an absolute time. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Port security is a security function that converts dynamic MAC addresses learned by an interface into secure MAC addresses.After port security is enabled on an interface, the switch converts dynamic MAC addresses learned by the interface into secure MAC addresses. In this case, the dynamic MAC address entries learned by the interface are deleted. When the number of MAC addresses learned by the interface reaches the upper limit, the interface no longer learns new MAC addresses. If the source MAC address of a packet received by an interface does not exist in the MAC address entries, the interface considers the packet as an attack packet and discards the packet, reports an alarm, or shuts down the interface.

**Prerequisites**



You can configure the aging time of secure dynamic MAC addresses only after port security is enabled.When enabling port security, you can set the maximum number of MAC addresses that can be learned.You can configure the protection action after the number of MAC addresses learned by an interface enabled with port security reaches the limit only after port security is enabled.Sticky MAC can be enabled only after port security is enabled. A sticky MAC address entry can be manually added only after the sticky MAC function is enabled.




Example
-------

# Enable the sticky MAC function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security enable
[~HUAWEI-100GE1/0/1] port-security mac-address sticky

```

# Set the maximum number of MAC addresses that can be learned by 100GE1/0/1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security enable maximum 5

```

# Set the aging time of secure dynamic MAC address entries to 6 minutes on 100GE1/0/1 and configure the MAC address entries to be aged out based on the absolute aging time.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security aging-time 6 type absolute

```

# Set the protection action on 100GE1/0/1 to protect.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security enable
[~HUAWEI-100GE1/0/1] port-security protect-action protect

```

# Enable port security on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security enable

```

# Manually add a sticky MAC address entry with the MAC address 1-1-3 and the VLAN ID 10 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port-security enable
[~HUAWEI-100GE1/0/1] port-security mac-address sticky
[~HUAWEI-100GE1/0/1] port-security mac-address sticky 1-1-3 vlan 10

```