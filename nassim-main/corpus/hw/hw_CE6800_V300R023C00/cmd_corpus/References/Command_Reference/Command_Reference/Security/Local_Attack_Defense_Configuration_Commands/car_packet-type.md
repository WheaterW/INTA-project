car packet-type
===============

car packet-type

Function
--------



The **car packet-type** command sets the rate limit for packets sent to the CPU.

The **undo car packet-type** command restores the default rate limit for packets sent to the CPU.



By default, You can run the display cpu-defend configuration command to check the rate limit for protocol packets.


Format
------

**car packet-type** *packet-type* **pps** *pps-value*

**undo car packet-type** *packet-type*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-type* | Specifies the type of packets.  When a packet type is specified, the CAR value takes effect on this type of packets and these packets are put into an independent queue. | The packet type information displayed on the device prevails. You can run the display cpu-defend configuration command to check the supported packet types and rate limit. |
| **pps** *pps-value* | Specifies the rate limit. | The value is an integer that ranges from 25 to 100,00, in pps. The value for the different packets maybe different. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The switch has default CPCAR values for each type of protocol packet. You can adjust CPCAR values for specified types of protocol packets based on services and network environment. After an attack defense policy is created, you can limit the rate of protocol packets using the policy:

* Reduce the CAR values in the following situation: When a network undergoes an attack, reduce the CAR values of the corresponding protocol, to reduce impact on the system CPU.
* Increase the CAR values in the following situation: When service traffic volume on the network increases, a large number of protocol packets need to be sent to the CPU. Increase the CAR values of the corresponding protocols to meet service requirements.

**Precautions**



CPCAR limits the rate of protocol packets sent to the control plane to ensure control plane security. The device has default CPCAR values for each type of protocol packets. You can adjust the CPCAR values for specified types of protocol packets based on the actual service scale and network environment. For example, when a large number of IPv6 user hosts are connected to a device, the default CPCAR value of ND packets may not meet the requirements of protocol packet exchange. As a result, a large number of ND packets are discarded, and ND neighbor entries cannot be learned. To prevent the CPU from running with heavy load, set a proper CPCAR value. An improper CPCAR value affects network services. Therefore, you are advised to contact technical support personnel if the CPCAR value of ND packets needs to be adjusted. If both the deny and car commands are configured for a specified type of packets to be sent to the CPU, the command configured later takes effect.



The CAR value of said-ping packets ranges from 25 to 5000, which is different from that of other protocol packets.




Example
-------

# Configure the CAR in the attack defense policy named test and set the rate limit of FTP packets to 6400 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] car packet-type ftp pps 6400

```