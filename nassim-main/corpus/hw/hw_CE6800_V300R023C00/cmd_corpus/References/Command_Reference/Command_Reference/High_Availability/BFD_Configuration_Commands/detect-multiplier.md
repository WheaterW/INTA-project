detect-multiplier
=================

detect-multiplier

Function
--------



The **detect-multiplier** command sets the local detection multiplier of a BFD session.

The **undo detect-multiplier** command restores the default value.



The default local detection multiplier of a BFD session is 3.


Format
------

**detect-multiplier** *multiplier*

**undo detect-multiplier** [ *multiplier* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *multiplier* | Specifies the local detection multiplier of a BFD session.   * For a stable link, you can set a large detection multiplier to prevent frequent link detections. * For an unstable link, a small detection multiplier may cause the BFD session to flap. Therefore, it is recommended that you set the detection multiplier to a large value. | The value is an integer ranging from 3 to 50. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can increase or decrease the local detection multiplier of a BFD session according to the networking environment.If no BFD packets are received within a detection period, the link that a BFD session detects is regarded as failed, and the BFD session status is set to Down. To reduce the usage of system resources, when detecting that the BFD session is Down, the system adjusts the interval between receiving BFD packets to a random value larger than 1000, in ms. After the BFD session becomes Up, the configured interval is restored.The local detection multiplier of a BFD session determines the detection period on the remote end of the BFD session.Asynchronous mode: Detection period = Received Detect Mult of the remote system x Max (Local RMRI, Received DMTI)where

* Desired Min Tx Interval (DMTI): indicates the desired minimum interval between sending BFD packets on the local end.
* Required Min Rx Interval (RMRI): indicates the supported minimum interval between receiving BFD packet on the local end.
* Detect Mult: indicates the detection multiplier.

**Prerequisites**

A BFD session has been created.

**Configuration Impact**

If BFD is applied to other protocols, setting a large BFD detection multiplier causes BFD to detect a link in a long period. If a fault is detected on the link, traffic can be switched to a standby link only after the detection period expires. In this period, packets may be dropped. Therefore, exercise caution when running the detect-multiplier command.

**Precautions**

You can configure different detection multipliers on both ends of a BFD session as required. During the establishment of a BFD session, the detection multipliers do not need to be negotiated.


Example
-------

# Set the local detection multiplier of the BFD session named session to 10.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session1 bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session1] quit
[*HUAWEI] bfd session1
[*HUAWEI-bfd-session-session1] detect-multiplier 10

```