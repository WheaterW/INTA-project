device transceiver
==================

device transceiver

Function
--------

The **device transceiver** command pre-configures the medium type on an optical interface.

The **undo device transceiver** command deletes the pre-configured medium type on an optical interface.

By default, no medium type is pre-configured on an optical interface.



Format
------

**device transceiver** *transceiver-type*

**undo device transceiver** [ *transceiver-type* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *transceiver-type* | Specifies the medium type. | The value can be:   * 1000BASE-X: GE optical module * 1000BASE-T: GE copper module * 10GBASE-FIBER: 10GE optical module * 10GBASE-COPPER: 10GE high-speed cable * 10GBASE-DWDM: 10GE-DWDM colored optical module * 25GBASE-FIBER: 25GE optical module * 25GBASE-COPPER: 25GE high-speed cable * 40GBASE-FIBER: 40GE optical module * 40GBASE-COPPER: 40GE high-speed cable * 50GBASE-COPPER: 50GE high-speed cable * QSFP28-50GBASE-COPPER: QSFP28\_50GE high-speed cable * 100GBASE-DWDM: 100GE-DWDM colored optical module * 100GBASE-FIBER: 100GE optical module * 100GBASE-COPPER: 100GE high-speed cable * 200GBASE-FIBER: 200GE optical module * 200GBASE-COPPER: 200GE high-speed cable * 400GBASE-FIBER: 400GE optical module * 400GBASE-COPPER: 400GE high-speed cable |




Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Pre-configuring the optical interface type helps users to deploy the medium type of the optical interface in advance and configure services on the pre-deployed medium when the optical interface medium is not in position.

After the medium type is pre-configured on an interface, if a medium of the correct type is installed, the interface has the condition to go Up and the configuration on the interface takes effect.If the installed transmission medium type differs from the pre-configured transmission medium type, the installed transmission medium type prevails.

**Prerequisites**

The interface is an optical interface that has no medium installed.

**Precautions**

If a high-speed cable is pre-configured but an optical module is installed, the optical module may be burnt. Ensure that the same type of media is inserted.

If a Huawei-certified optical module is installed, the system can automatically identify the optical module. If an unknown optical module is installed on an interface, the interface can go Up only when the bandwidth of the pre-configured medium type is the same as that of the installed optical module. Otherwise, the interface cannot go Up.To ensure that the interface works properly, you are advised to use Huawei-certified optical modules. The system can automatically identify Huawei-certified optical modules and determine whether the medium type is the same as the pre-configured medium type.

Example
-------

# Pre-configure the medium type on
100GE
1/0/1 as 10GBASE-FIBER.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] device transceiver 10GBASE-FIBER
Warning: This operation will cause all transceiver-related configurations on the port to be lost.
Ensure that the transceiver on the port is consistent with the configuration. Continue? [Y/N]:Y

```