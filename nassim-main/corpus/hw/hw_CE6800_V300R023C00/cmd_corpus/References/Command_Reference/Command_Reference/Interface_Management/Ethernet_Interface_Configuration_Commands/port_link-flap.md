port link-flap
==============

port link-flap

Function
--------



The **port link-flap** command sets the link flapping detection interval and maximum number of link flapping events on an interface.

The **undo port link-flap** command restores the default link flapping detection interval and maximum number of link flapping events on an interface.



By default, the link flapping detection interval on an interface is 10s and the maximum number of link flapping events is 5.The threshold configuration for the second group of link flapping does not take effect.


Format
------

**port link-flap** { **interval** *interval-value* [ **threshold** *threshold-value* ] | **threshold** *threshold-value* } [ **second-interval** *second-interval-value* **second-threshold** *second-threshold-value* ]

**undo port link-flap** { **interval** *interval-value* **threshold** *threshold-value* **second-interval** *second-interval-value* **second-threshold** *second-threshold-value* }

**undo port link-flap** { **threshold** [ *threshold-value* ] }

**undo port link-flap** { **interval** [ *interval-value* ] **threshold** [ *threshold-value* ] }

**undo port link-flap** { **interval** [ *interval-value* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-value* | Specifies the link flapping detection interval on an interface. | The·value·is·an·integer·that·ranges·from·5·to·86400,·in·seconds.·The·default·value·is·10. |
| **threshold** *threshold-value* | Specifies the maximum number of link flapping events on an interface. | The value is 0 or an integer that ranges from 2 to 1200. The default value is 5.  If the value is 0, link flapping protection is disabled on the interface. |
| **second-interval** *second-interval-value* | Specifies the second link flapping detection interval on an interface. You can configure two link flapping detection intervals and two maximum numbers of link flapping events. An alarm is generated when either group of the intervals and maximum numbers is reached. | The value is an integer that ranges from 5 to 86400. |
| **second-threshold** *second-threshold-value* | Specifies the second maximum number of link flapping events on an interface. You can configure two link flapping detection intervals and two maximum numbers of link flapping events. An alarm is generated when either group of the intervals and maximum numbers is reached. | The value is an integer that ranges from 2 to 1200. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After link flapping protection is enabled on the device, you can set the link flapping detection interval and maximum number of link flapping events on an interface. When the device receives an interface Up/Down message, the device checks the number of interface flapping events that occur within the specified link flapping detection interval. If the number of interface flapping events reaches the maximum value, the device sets the status of the interface to Error-Down.

**Precautions**

This command must be used together with the **port link-flap trigger error-down** command. After an Ethernet interface is enabled to transit to the Error-Down state due to link flapping using the **port link-flap trigger error-down** command, run the **port link-flap** command to set the link flapping detection time and number of link flappings on the interface.


Example
-------

# Set the link flapping interval to 50 seconds and the number of link flapping times to 6 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port link-flap interval 50 threshold 6

```

**Table 1** Description of the **port link-flap** command output
| Item | Description |
| --- | --- |
| port link-flap interval | Link flapping interval. |