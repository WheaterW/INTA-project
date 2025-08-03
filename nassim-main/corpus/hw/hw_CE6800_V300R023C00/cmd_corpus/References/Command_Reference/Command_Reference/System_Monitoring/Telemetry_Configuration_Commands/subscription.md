subscription
============

subscription

Function
--------



The **subscription** command creates a subscription in the Telemetry view and displays the Subscription view.

The **undo subscription** command deletes a subscription created in the Telemetry view.



By default, no subscription is created in the Telemetry view.


Format
------

**subscription** *subscription-name*

**undo subscription** *subscription-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *subscription-name* | Specifies a subscription name. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To create one or more subscriptions in the Telemetry view, run the **subscription** command. A subscription can be associated with destination groups and sampling sensor groups for data sending.

**Precautions**



A maximum of 25 subscriptions can be created.




Example
-------

# Create subscription named A.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription A

```