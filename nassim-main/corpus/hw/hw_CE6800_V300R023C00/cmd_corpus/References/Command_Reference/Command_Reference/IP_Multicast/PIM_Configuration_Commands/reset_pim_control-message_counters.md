reset pim control-message counters
==================================

reset pim control-message counters

Function
--------



The **reset pim control-message counters** command deletes statistics about PIM control messages.




Format
------

**reset pim control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**reset pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Indicates all instances. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To re-collect statistics about PIM control messages, run the reset pim control-message counters command to delete existing statistics about PIM control messages.

**Configuration Impact**

Deleted statistics about PIM control messages cannot be restored, but the deletion does not affect PIM running.


Example
-------

# Reset the statistics about PIM control messages on all interfaces in the public network instance.
```
<HUAWEI> reset pim control-message counters

```

# Clear statistics about PIM control messages on 100GE1/0/1 in the public network instance.
```
<HUAWEI> reset pim control-message counters interface 100GE 1/0/1

```