ntp disable
===========

ntp disable

Function
--------



The **ntp disable** command disables IPv4 NTP.

The **undo ntp disable** command enables IPv4 NTP.



By default, NTP services are enabled.


Format
------

**ntp** [ **ipv6** ] **disable**

**undo ntp** [ **ipv6** ] **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Specifies the NTP IPv6 service. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To disable NTP, run the ntp-service disable command in the system view.Disabling the NTP function does not delete the existing configuration.This command can be used in the following scenarios:

* The device does not need to synchronize its clock with the clock of an external server or peer.
* The device does not need to provide a reference clock source for external clients.

Example
-------

# Disable IPv4 NTP services.
```
<HUAWEI> system-view
[~HUAWEI] ntp disable

```