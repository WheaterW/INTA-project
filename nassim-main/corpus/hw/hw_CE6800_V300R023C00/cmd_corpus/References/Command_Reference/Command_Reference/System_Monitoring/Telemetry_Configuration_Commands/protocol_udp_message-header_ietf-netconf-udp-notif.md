protocol udp message-header ietf-netconf-udp-notif
==================================================

protocol udp message-header ietf-netconf-udp-notif

Function
--------



The **protocol udp message-header ietf-netconf-udp-notif** command configures a device to use the UDP header in draft-ietf-netconf-udp-notif-08 format.

The **undo protocol udp message-header** command restores the default configuration.



By default, the UDP header in draft-ietf-netconf-udp-pub-channel-01 format is used.


Format
------

**protocol udp message-header ietf-netconf-udp-notif**

**undo protocol udp message-header** [ **ietf-netconf-udp-notif** ]


Parameters
----------

None

Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Telemetry provides the capability of specifying the packet header format. Currently, the draft-ietf-netconf-udp-pub-channel-01 format is used by default. You can switch the format to draft-ietf-netconf-udp-notif-08 as required.


Example
-------

# Configure Telemetry to use the UDP packet header in draft-ietf-netconf-udp-notif-08 format.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] protocol udp message-header ietf-netconf-udp-notif

```