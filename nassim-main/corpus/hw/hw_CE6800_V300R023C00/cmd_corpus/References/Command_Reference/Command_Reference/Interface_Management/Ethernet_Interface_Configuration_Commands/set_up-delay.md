set up-delay
============

set up-delay

Function
--------



The **set up-delay** command sets the delay after which an interface goes Up.

The **undo set up-delay** command restores the default setting.



By default, the delay after which an interface goes Up is 0 seconds.


Format
------

**set up-delay** *value*

**undo set up-delay** [ *value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the delay after which an interface goes Up. | The value is an integer that ranges from 0 to 3600, in seconds. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The physical status of an Ethernet interface can be Up or Down. When the interface physical status changes, the system notifies upper-layer protocol modules (such as the routing and forwarding modules) of the change to direct packet receiving and forwarding. The system also automatically generates traps and logs to remind users to perform corresponding operations on physical links.After the device restarts or a subcard resets, the physical status of interfaces is Up. However, the upper-layer protocol modules do not meet forwarding requirements. If an interface receives service packets and sends the packets to the upper-layer protocol modules. The services cannot run properly because the upper-layer protocol modules cannot process the service packets. You can run the **set up-delay** command to set the delay after which the interface goes Up. The interface then becomes physically Up after the upper-layer protocol modules meet forwarding requirements, ensuring that packets can be processed.

**Precautions**

If this command is configured, the function of making an interface go Up after a delay takes effect only after the device restarts or the subcard resets.If the delay in reporting the interface Up status does not expire on an interface, and the **set up-delay** command is run to change the delay or the interface restarts, the original delay becomes invalid. Therefore, change the delay when the interface works properly.


Example
-------

# Set the delay after which 100GE1/0/1 goes Up to 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] set up-delay 10

```