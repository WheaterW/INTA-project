redirect observe-port group
===========================

redirect observe-port group

Function
--------



The **redirect observe-port group** command configures an action of redirecting packets to an observing port group in a traffic behavior.

The **undo redirect observe-port group** command deletes the redirection configuration.



By default, the action of redirecting packets to an observing port group is not configured in a traffic behavior.


Format
------

**redirect observe-port group** *group-id*

**undo redirect observe-port group** *group-id*

**undo redirect**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Specifies the ID of an observing port group to which packets are redirected. | The value is an integer ranging from 1 to 128. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can add a device's ports connected to servers or firewalls to an observing port group and run this command to redirect packets to the observing port group, which simplifies configurations. This action takes effect only for packets forwarded at Layer 2.

**Prerequisites**

An observing port group has been created using the **observe-port group** command.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing redirection to an observing port group.

**Precautions**

* A traffic policy that contains the redirection action cannot be used in the outbound direction.
* This command cannot be configured together with deny.

Example
-------

# Configure an action of redirecting packets to observing port group 2 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port group 2
[*HUAWEI-observe-port-group-2] q
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect observe-port group 2

```