parity
======

parity

Function
--------



The **parity** command sets the check bit of a user interface.

The **undo parity** command restores the default check bit of a user interface.



By default, no check is performed.


Format
------

**parity** *paritytype*

**undo parity**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *paritytype* | Specifies the transmission check bit. | The value is an enumerated type, which can be:   * even: Sets the transmission check bit to even parity. * mark: Sets the transmission check bit to mark check. * none: Sets the transmission check bit to no check. * odd: Sets the transmission check bit to odd parity. * space: Sets the transmission check bit to space check. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, no transmission check is performed. To prevent transmission errors, run the parity command to configure the check bit of the specified user interface to improve data transmission correctness.


Example
-------

# Set the transmission check bit on the console port to odd parity.
```
<HUAWEI> system-view
[~HUAWEI] user-interface  console 0
[~HUAWEI-ui-console0] parity odd

```