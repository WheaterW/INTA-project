port identity
=============

port identity

Function
--------



The **port identity** command configures a peer device identity TLV.

The **undo port identity** command deletes a peer device identity TLV.



By default, no peer device identity TLV is configured.


Format
------

**port identity** *identify-para*

**undo port identity** [ *identify-para* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *identify-para* | Specifies a peer device identity TLV. | The value is a string of 1 to 507 case-sensitive characters without the following characters: > $ \* ^ ? | and spaces. When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the Agile Controller is used to automatically deploy network services, the network administrator manually manages a device on the Agile Controller GUI. When multiple devices directly connected to the device go online, the Agile Controller cannot determine which configurations should be delivered to the target devices. You can run this command to configure the identity TLV of the peer device directly connected to the interface and run the **identity enable** command to enable the interface to send LLDP packets carrying the identity TLV. In this way, the directly connected devices can receive the identity TLV and notify the AC of the TLV. The AC then delivers network service configurations to the devices based on the TLV.

**Precautions**

To ensure that the devices to go online on the network have different identities, configure different peer identity TLVs on the interfaces directly connected to these devices.


Example
-------

# Configure identity TLV leaf1-1 for the device directly connected to 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port identity leaf1-1

```