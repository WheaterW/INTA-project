force transceiver
=================

force transceiver

Function
--------

The **force transceiver** command forcibly configures the medium type for an Ethernet optical interface.

The **undo force transceiver** command cancels the configuration.

By default, no medium type is configured for an Ethernet optical interface.



Format
------

**force transceiver** *transceiver-type*

**undo force transceiver** [ *transceiver-type* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *transceiver-type* | Specifies the medium type. | The options are as follows:   * 1000BASE-X: GE optical module * 1000BASE-T: GE copper module * 10GBASE-FIBER: 10GE optical module * 10GBASE-COPPER: 10GE high-speed cable * 10GBASE-DWDM: 10GE-DWDM colored optical module * 25GBASE-FIBER: 25GE optical module * 25GBASE-COPPER: 25GE high-speed cable * 40GBASE-FIBER: 40GE optical module * 40GBASE-COPPER: 40GE high-speed cable * 50GBASE-COPPER: 50GE high-speed cable * QSFP28-50GBASE-COPPER: QSFP28\_50GE high-speed cable * 100GBASE-DWDM: 100GE-DWDM colored optical module * 100GBASE-FIBER: 100GE optical module * 100GBASE-COPPER: 100GE high-speed cable * 200GBASE-FIBER: 200GE optical module * 200GBASE-COPPER: 200GE high-speed cable * 400GBASE-FIBER: 400GE optical module * 400GBASE-COPPER: 400GE high-speed cable |




Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If the installed medium type is incorrectly identified, you can run this command to forcibly set the medium type to the actual one.



Example
-------

# Forcibly configure the medium type of a
100GE optical module.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] force transceiver 10GBASE-FIBER
Warning: This operation will cause all configurations related with the transceiver on the port to be lost.                                                      
Ensure that the transceiver on the port is consistent with the configuration.   
After the transceiver type is changed, the transceiver may not work properly. Co
ntinue? [Y/N]:Y

```