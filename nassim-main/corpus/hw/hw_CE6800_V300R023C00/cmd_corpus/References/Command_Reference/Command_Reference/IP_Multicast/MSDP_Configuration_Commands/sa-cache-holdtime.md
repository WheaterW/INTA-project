sa-cache-holdtime
=================

sa-cache-holdtime

Function
--------



The **sa-cache-holdtime holdtime** command configures the lifetime of (S, G) entries in locally cached SA messages.

The undo sa-cache-holdtime command restores the default lifetime of (S, G) entries in locally cached SA messages.



By default, the lifetime of (S, G) entries in locally cached SA messages is 360 seconds.


Format
------

**sa-cache-holdtime** *holdtime*

**undo sa-cache-holdtime** [ *holdtime* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdtime* | Specifies the lifetime of (S, G) entries in locally cached SA messages. | The value is an integer ranging from 150 to 3600, in seconds. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A router configured with the SA cache lifetime can locally save the (S, G) entries contained in SA messages and start the lifetime timer for the entries. To adjust the lifetime of the (S, G) entries in SA messages, run this command. When the device receives a new SA message, the (S, G) cache timeout interval is set to the value specified by this command.

**Prerequisites**

The **multicast routing-enable** command has been run for the public network or VPN instance.


Example
-------

# Change the lifetime of (S, G) entries in locally cached SA messages for the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] sa-cache-holdtime 600

```