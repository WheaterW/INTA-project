auto-rp listening enable
========================

auto-rp listening enable

Function
--------



The **auto-rp listening enable** command enables the auto-rendezvous point (auto-RP) listening function.

The **undo auto-rp listening enable** command disables the auto-RP listening function.



By default, auto-RP listening is disabled.


Format
------

**auto-rp listening enable**

**undo auto-rp listening enable**


Parameters
----------

None

Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device communicates with a device that supports Auto-RP, you need to run this command to enable Auto-RP listening. After Auto-RP listening is enabled, the device receives Auto-RP Advertisement and Discovery messages and learns RP information from the Discovery messages.

* The C-RP sends an Announce message to 224.0.1.39.
* The auto-RP mapping agent sends a Discovery message to 224.0.1.40.

**Configuration Impact**

After receiving an auto-RP advertisement message or discovery message, the device analyzes the source address of the message and then performs a reverse path forwarding (RPF) check based on the source address.If the RPF check fails, the device discards the message; if the RPF check succeeds, the device forwards the message to other PIM neighbors.


Example
-------

# Enable auto-RP listening on a device.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] auto-rp listening enable

```