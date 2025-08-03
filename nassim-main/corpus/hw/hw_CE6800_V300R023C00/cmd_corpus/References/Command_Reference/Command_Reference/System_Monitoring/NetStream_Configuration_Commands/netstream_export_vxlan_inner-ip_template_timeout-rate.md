netstream export vxlan inner-ip template timeout-rate
=====================================================

netstream export vxlan inner-ip template timeout-rate

Function
--------



The **netstream export vxlan inner-ip template timeout-rate** command sets the interval at which the template for exporting VXLAN flexible flow statistics in V9 format is refreshed.

The **undo netstream export vxlan inner-ip template timeout-rate** command restores the default setting.



By default, the template is refreshed every 1 minute.


Format
------

**netstream export vxlan inner-ip template timeout-rate** *timeout-interval*

**undo netstream export vxlan inner-ip template timeout-rate** [ *timeout-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeout-interval* | Specifies the interval for refreshing the V9 template. | The value is an integer that ranges from 1 to 3600, in minutes. The default value is 1. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When the export version for VXLAN flexible flow statistics is set to V9, the template must be exported to the NDA. This command sets the interval for refreshing the V9 template.If network traffic is heavy, the template refresh interval should be set to a small value; however, this will generate more traffic on the network. You need to set a proper template refresh interval according to network situation. The default setting is recommended if you do not have special requirement.


Example
-------

# Set the template refresh interval to 50 minutes.
```
<HUAWEI> system-view
[~HUAWEI] netstream export vxlan inner-ip template timeout-rate 50

```