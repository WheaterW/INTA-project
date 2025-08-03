mac-address flapping periodical trap
====================================

mac-address flapping periodical trap

Function
--------



The **mac-address flapping periodical trap enable** command enables the function to periodically report MAC address flapping traps.

The **undo mac-address flapping periodical trap enable** command disables the function to periodically report MAC address flapping traps.

The **mac-address flapping periodical trap interval** command sets the interval at which MAC address flapping traps are reported.

The **undo mac-address flapping periodical trap interval** command restores the default value.



By default, the function to periodically report MAC address flapping traps is disabled, the interval at which MAC address flapping traps are reported is 2 minutes.


Format
------

**mac-address flapping periodical trap enable**

**mac-address flapping periodical trap interval** *interval*

**undo mac-address flapping periodical trap enable**

**undo mac-address flapping periodical trap interval** [ *interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval* | Specifies the interval at which MAC address flapping traps are reported. | The value is an integer ranging from 2 to 30, in minutes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Configuring global MAC address flapping detection helps to check whether MAC addresses flap. If MAC address flapping occurs, a trap is generated. By default, a trap is reported every 30 minutes. To timely check whether MAC address flapping occurs, run the **mac-address flapping periodical trap enable** command to enable the function to periodically report MAC address flapping traps.To timely check whether MAC address flapping occurs, run the **mac-address flapping periodical trap interval interval** command to set the interval at which MAC address flapping traps are reported.



**Follow-up Procedure**



Run the **mac-address flapping periodical trap interval interval** command to set the interval at which MAC address flapping traps are reported.




Example
-------

# Set the interval at which MAC address flapping traps are reported to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping periodical trap interval 5

```

# Enable the function to periodically report MAC address flapping traps.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping periodical trap enable

```