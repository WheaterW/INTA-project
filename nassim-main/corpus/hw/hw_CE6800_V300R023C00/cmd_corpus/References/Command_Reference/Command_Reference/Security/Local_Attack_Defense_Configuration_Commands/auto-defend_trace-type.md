auto-defend trace-type
======================

auto-defend trace-type

Function
--------



The **auto-defend trace-type** command configures an attack source tracing mode.

The **undo auto-defend trace-type** command deletes an attack source tracing mode.



By default, attack source tracing is based on source MAC addresses and source IP addresses.


Format
------

**auto-defend trace-type** { **source-mac** | **source-ip** | **source-portvlan** } \*

**undo auto-defend trace-type** { **source-mac** | **source-ip** | **source-portvlan** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-mac** | Configures attack source tracing based on source MAC addresses so that the device classifies and collects statistics based on the source MAC address and identifies the attack source. | - |
| **source-ip** | Configures attack source tracing based on source IP addresses so that the device classifies and collects statistics based on the source IP address and identifies the attack source. | - |
| **source-portvlan** | Configures attack source tracing based on source ports+VLANs so that the device classifies and collects statistics based on the source port and VLAN and identifies the attack source. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After enabling attack source tracing, you can specify one or more attack source tracing modes. The device then uses the specified modes to trace attack sources.The device supports the following attack source tracing modes:

* Source IP address-based tracing: defends against Layer 3 attack packets.
* Source MAC address-based tracing: defends against attack packets with a fixed source MAC address.
* Source port+VLAN based tracing: defends against attack packets with different source MAC addresses.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Precautions**

After the attack source tracing function is enabled on the device, you can run the display auto-defend attack-source command to view attack source tracing information if an attack occurs.If the attack source tracing function is enabled by using the **auto-defend enable** command, you cannot run the undo auto-defend trace-type command to delete all source tracing modes.When the following trace types are configured on the device, trace types take effect in the following order of priority (highest to lowest): source mac > source ip > source·portvlan.


Example
-------

# Configure attack source tracing based on source MAC addresses.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend trace-type source-mac

```