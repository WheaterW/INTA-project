als restart pulse
=================

als restart pulse

Function
--------



The **als restart pulse** command sets the ALS pulse width or interval of a laser of an optical module.

The **undo als restart pulse** command restores the ALS pulse width or interval of the laser to the default value.



By default, the ALS pulse width of the laser is 2s, the ALS pulse interval of the laser is 100s.


Format
------

**als restart pulse** { **interval** *interval-value* | **width** *width-value* }

**undo als restart pulse interval** [ *interval-value* ]

**undo als restart pulse width** [ *width-value* ]

**undo als restart pulse**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-value* | Specifies the ALS pulse interval of the laser. | The value is an integer that ranges from 100 to 20000, in seconds. |
| **width** *width-value* | Specifies the ALS pulse width of the laser. | The value is an integer that ranges from 2 to 200, in seconds. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The light emitting time of the laser is the width of the probe light pulse sent by the laser. A smaller width helps save energy but cannot detect fiber link recovery in a timely manner. A bigger width helps detect fiber link recovery in a timely manner but consumes more energy.In automatic restart mode, the laser pulse interval affects the frequency of detecting LOS on an interface. A longer interval helps save energy but cannot detect fiber link recovery in a timely manner. A shorter interval helps detect fiber link recovery in a timely manner but cannot save energy.ALS is supported only when an optical module is pre-configured, an optical interface has an optical module installed, or a combo interface works in optical mode. Electrical interfaces do not support ALS.


Example
-------

# Set the ALS pulse width on 100GE1/0/1 to 3s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] als restart pulse width 3

```

# Set the ALS pulse interval of lasers on 100GE1/0/1 to 150s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] als restart pulse interval 150

```