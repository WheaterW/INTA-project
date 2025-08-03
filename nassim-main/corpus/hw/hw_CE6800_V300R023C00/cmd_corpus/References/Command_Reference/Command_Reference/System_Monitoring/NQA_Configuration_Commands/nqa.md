nqa
===

nqa

Function
--------



The **nqa** command creates an NQA test instance and displays the NQA test instance view.

The **undo nqa** command deletes an NQA test instance.



By default, no NQA test is created.


Format
------

**nqa test-instance** *admin-name* *test-name*

**undo nqa test-instance** *admin-name* *test-name*

**undo nqa all-test-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *test-name* | Specifies the name of an NQA test instance. | The value is a string of 1 to 32 characters, excluding question marks (?), en dashes (-), a single or consecutive quotation marks ("). |
| **test-instance** *admin-name* | Specifies the administrator of an NQA test instance. | The value is a string of 1 to 32 characters, excluding question marks (?), en dashes (-), a single or consecutive quotation marks ("). |
| **all-test-instance** | Specifies all NQA test instances. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network Quality Analysis (NQA) integrates the network test function on a device. NQA can accurately test the network running status, output statistics, and effectively reduce costs.NQA measures the performance of various protocols running on the network so that carriers can collect network operation indicators in real time, such as the TCP connection delay, packet loss rate, and path MTU.NQA tests the preceding service features by creating test instances. The two ends of an NQA test are called the NQA client and NQA server. An NQA test is initiated by the NQA client. After test instances are configured on the client, NQA places different types of test instances into various test queues. After a test instance is started, the returned packets provide data information about the running status of related protocols. Before sending a test packet, the system reads the system time as the sending time of the test packet, adds a timestamp to the packet, and sends the packet to the destination. After receiving the packet, the destination end returns a response to the source end. After receiving the packet, the source end reads the system time again and adds a timestamp to the packet. This helps calculating the RTT of the packet based on the time when the packets are sent and received.For example, to monitor whether the peer device is reachable, run the **nqa** command to create an NQA test instance, set the test type to ICMP, and then run the **destination-address** command to configure the IP address of the peer device as the destination IP address. After that, you can start the test instance.Then, you can check whether the peer device is reachable by analyzing the received response packet.

**Configuration Impact**



The undo nqa all-test-instance command deletes all the NQA test instances, including the running ones.



**Precautions**

* Before deleting an NQA test instance, delete the services associated to it.
* After all NQA test instances are deleted, associated services are affected.


Example
-------

# Create an NQA test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test

```