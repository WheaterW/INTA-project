timer lsp-generation (IS-IS view)
=================================

timer lsp-generation (IS-IS view)

Function
--------



The **timer lsp-generation** command sets an LSP generation interval for a specified IS-IS process.

The **undo timer lsp-generation** command restores the default configuration.



By default, the LSP generation interval is 2 seconds.


Format
------

**timer lsp-generation** *max-interval* [ *init-interval* [ *incr-interval* ] ] [ **level-1** | **level-2** ]

**undo timer lsp-generation** [ *max-interval* [ *init-interval* [ *incr-interval* ] ] ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-interval* | Specifies a maximum LSP generation interval. | The value ranges from 1 to 120 seconds. The default value is 2 seconds. |
| *init-interval* | Specifies an initial LSP generation interval. | The value is an integer ranging from 1 to 60000, in milliseconds. By default, this interval is not used. |
| *incr-interval* | Specifies an incremental LSP generation interval. | The value is an integer ranging from 1 to 60000, in milliseconds. By default, this interval is not used. |
| **level-1** | Applies the interval setting to Level-1 LSPs. | - |
| **level-2** | Applies the interval setting to Level-2 LSPs.  If neither Level-1 nor Level-2 is specified, the interval setting applies both to Level-1 and Level-2 LSPs. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For IS-IS, when the local routing information is changed, some new LSPs (or LSP fragments) need to be generated to advertise the change of routes. If the change occurs frequently, immediate generation of LSPs (or LSP fragments) will consume a large number of resources.To speed up network convergence and prevent the system from being affected, use an intelligent timer to control the LSP generation interval. Using the timer, you can adjust the LSP generation interval based on the route change frequency.Before using the**timer lsp-generation** command, note the following:

* When only max-interval is specified, the intelligent timer functions as a one-shot timer.
* If init-interval and incr-interval are specified, init-interval is used as the LSP generation interval for the first time, and incr-interval is used as the LSP generation interval for the second time. From the third time on, the LSP generation interval doubles each time until the interval reaches max-interval. If the local routing information keeps being updated within the max-interval period, the interval remains at max-interval until the time the local routing information is not updated within the max-interval period or the IS-IS process is restarted. Then the interval decreases to init-interval.
* If init-interval is specified, but incr-interval is not, init-interval is used as the LSP generation interval for the first time, and then max-interval is used as the interval. If the local routing information keeps being updated within the max-interval period, the interval remains at max-interval until the time the local routing information is not updated within the max-interval period or the IS-IS process is restarted. Then the interval decreases to init-interval.

**Prerequisites**

An IS-IS process has been created using the **isis** command.

**Configuration Impact**

If the LSP generation interval is too long, the device cannot advertise its changes to neighbors in time, which slows down network convergence.

**Precautions**

When the local routing information does not change within the interval specified by max-interval, the intelligent timer is stopped. When the network topology changes for the first time after the intelligent timer stops, the device immediately generates an LSP to notify the change and then starts the intelligent timer.


Example
-------

# Set the LSP generation interval to 5s.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] timer lsp-generation 5

```

# Set the maximum LSP generation interval to 20s, initial interval to 50 ms, and incremental interval to 2000 ms.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] timer lsp-generation 20 50 2000

```