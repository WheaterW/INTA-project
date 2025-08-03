stp enable
==========

stp enable

Function
--------



The **stp enable** command enables STP/RSTP/MSTP on a device.

The **stp disable** command disables STP/RSTP/MSTP on a device.

The **undo stp enable** command cancels the stp enable command configuration.

The **undo stp disable** command cancels the stp disable command configuration.



By default, STP/RSTP/MSTP is enabled on a device.


Format
------

**stp** { **enable** | **disable** }

**undo stp** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables STP/RSTP/MSTP. | - |
| **disable** | Disables STP/RSTP/MSTP. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On a complex Layer 2 network, STP/RSTP/MSTP can be configured on devices to prevent or break loops.
* To enable STP/RSTP/MSTP, run the **stp enable** command. The devices running STP/RSTP/MSTP exchange information to discover loops on the network and block some interfaces to trim the ring topology into a loop-free tree topology. This prevents packet replication and circular propagation and device performance deterioration.
* Spanning tree calculation consumes system resources. Therefore, run the **stp disable** command to disable STP/RSTP/MSTP on devices or interfaces that do not need to participate in spanning tree calculation.

**Prerequisites**

After STP/RSTP/MSTP is enabled on a ring network, STP/RSTP/MSTP immediately calculates spanning trees on the network. Configurations on a device, such as the device priority, port priority, and port path cost, will affect spanning tree calculation. Any change of the configurations may cause network flapping. Therefore, ensure that basic configurations have been complete before enabling STP/RSTP/MSTP. For example:

* The working mode of the device has been configured using the stp mode { mstp | rstp | stp } command.
* The priority of the device on a spanning tree has been set using the **stp priority** command
* The priority of an interface on a spanning tree instance has been configured using the **stp port priority** command.
* The device has been set as the primary root bridge of a spanning tree using the **stp root primary** command.
* The device has been set as a secondary root bridge of a spanning tree using the **stp root secondary** command.
* The path cost of an interface on a spanning tree instance has been set using the stp cost cost command.
* If the spanning tree protocol is MSTP, an MST region has been configured using the **region-name**, **instance vlan** and **revision-level** commands.Other configurations are completed as required.

**Precautions**

* Running the **undo stp enable** or **stp disable** command in the system view disables STP, RSTP, or MSTP globally, which may cause loops.
* STP, RSTP, or MSTP must be enabled on all interfaces that participate in spanning tree calculation. Otherwise, network loops may occur.
* For security purposes, after the **configuration re-authentication enable** command is configured, you need to enter the password and pass the authentication to make the STP disabling configuration take effect.


Example
-------

# Enable STP/RSTP/MSTP on a device.
```
<HUAWEI> system-view
[~HUAWEI] stp enable

```