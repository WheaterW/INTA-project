import-source
=============

import-source

Function
--------



The **import-source** command configures a policy for filtering active sources that can be advertised using source active (SA) messages.

The **undo import-source** command restores the default configuration.



By default, all active sources can be advertised using SA messages.


Format
------

**import-source acl** { *acl-number* | *acl-name* }

**import-source**

**undo import-source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL or an advanced ACL. | The value is an integer ranging from 2000 to 3999.   * ACLs numbered 2000 to 2999 are basic ACLs. A basic ACL defines a range of source addresses, so that only (S, G) entries that contain a source address in the defined range can be advertised using SA messages. * ACLs numbered 3000 to 3999 are advanced ACLs. An advanced ACL defines both ranges of source and group addresses, so that only (S, G) entries that contain source and group addresses in the defined ranges can be advertised using SA messages. If the ACL is not specified, no multicast sources can be advertised. |
| *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl** | Specifies the ACL rule for advertisement. | - |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **import-source** command is run, Multicast Source Discovery Protocol (MSDP) filters (S, G) forwarding entries to be advertised based on source addresses when creating SA messages, implementing control over the transmission of multicast source information.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **import-source** command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, configure an MSDP peer to advertise only (S, G) entries with source addresses on the network segment 10.10.0.0/16 and group address 225.1.0.0/16 using SA messages.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3101
[*HUAWEI-acl4-advance-3101] rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3101] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] import-source acl 3101

```