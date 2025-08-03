tcp window
==========

tcp window

Function
--------



The **tcp window** command sets the size of the sending/receiving buffer of the connection-oriented socket.

The **undo tcp window** command restores the default size of the buffer.



By default, the size of the packet sending/receiving buffer of the connection-oriented socket is 8K bytes.


Format
------

**tcp window** *window-size*

**undo tcp window**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *window-size* | Specifies the size of the packet sending/receiving buffer of the connection-oriented Socket. | The value is an integer ranging from 1 to 32, in KBytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Running the tcp window command changes the TCP window size that is used for setting up a TCP session.



**Precautions**



If this command is configured for several times in the same view, only the last configuration takes effect.You are recommended to configure the parameters under the guidance of the technical personnel.




Example
-------

# Configure the size of the packet sending/receiving buffer of the connection-oriented socket to 3K bytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp window 3

```