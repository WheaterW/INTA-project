min-tx-interval
===============

min-tx-interval

Function
--------



The **min-tx-interval** command sets the interval between sending BFD packets.

The **undo min-tx-interval** command restores the default value.



By default, the interval is 1000 milliseconds.


Format
------

**min-tx-interval** *tx-interval*

**undo min-tx-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tx-interval* | Specifies the interval between sending BFD packets. | The value is an integer that ranges from 3 to 1000, in milliseconds. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can increase or decrease the interval between transmitting BFD packets according to the actual network environment.If no BFD packet is received within a configured detection period, the link that the BFD session detects is regarded as failed, and the BFD session status is set to Down. To reduce the usage of system resources, when detecting that the BFD session is Down, the system adjusts the interval between transmitting BFD packets to a random value greater than 1000 ms. After the BFD session becomes Up, the configured interval is restored.Asynchronous mode: Detection period = Received Detect Mult of the remote system x Max (Local RMRI, Received DMTI)where

* DMTI: indicates the desired minimum interval between sending BFD packets on the local end.
* RMRI: indicates the supported minimum interval between receiving BFD packet on the local end.
* Detect Mult: indicates the detection multiplier.

Example
-------

# Set the interval between transmitting BFD packets to 500 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session] quit
[*HUAWEI] bfd session
[*HUAWEI-bfd-session-session] min-tx-interval 500

```