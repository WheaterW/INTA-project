car (traffic behavior view)
===========================

car (traffic behavior view)

Function
--------



The **car** command configures traffic policing in a traffic behavior.

The undo car command deletes traffic policing from a traffic behavior.



By default, traffic policing is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**undo car**

**car** { **cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] [ **pir** *pir-value* [ **kbps** | **mbps** | **gbps** ] ] } [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] **pbs** *pbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] [ **share** ] [ **mode** { **color-blind** | **color-aware** } ] [ **green** **pass** [ **service-class** *class* **color** *color* ] | **yellow** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the guaranteed average transmission rate. | The value is an integer in the range from 24 to 400000000. |
| **kbps** | Indicates that the rate is expressed in kbit/s. | - |
| **mbps** | Indicates that the rate is expressed in Mbit/s. | - |
| **gbps** | Indicates that the rate is expressed in Gbit/s. | - |
| **pir** *pir-value* | Specifies the peak information rate (PIR), which is the maximum rate of traffic that can pass through an interface. | The value is an integer that ranges from 1 to 400000000. |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the average volume of burst traffic that can pass through an interface. | The value is an integer that ranges from 1 to 33554432. |
| **bytes** | Indicates that the CBS is expressed in bytes. | - |
| **kbytes** | Indicates that the CBS is expressed in kbytes. | - |
| **mbytes** | Indicates that the CBS is expressed in mbytes. | - |
| **pbs** *pbs-value* | Specifies the peak burst size (PBS), which is the maximum volume of burst traffic that can pass through an interface. | The value is an integer that ranges from 1 to 33554432. |
| **share** | Indicates the level-1 shared CAR. If a traffic behavior is bound to a traffic classifier that contains multiple matching rules, all traffic matching the traffic classifier is restricted by the level-1 shared CAR. | - |
| **mode** | Specifies the color mode for traffic policing. | - |
| **color-blind** | Specifies the color-blind mode. In color-blind mode, the original packet color does not affect the traffic policing action. | - |
| **green** | Specifies the action taken for packets if the packet rate is less than or equal to the CIR value. | The default value is pass. |
| **pass** | Allows packets to pass through. | - |
| **yellow** | Specifies the action taken for packets if the packet rate is greater than the CIR value and less than or equal to the PIR value. | The default value is pass. |
| **discard** | Discards packets. | - |
| **red** | Specifies the action taken for packets if the packet rate is greater than the PIR value. | The default value is discard. |
| **color-aware** | Specifies the color-aware mode. In color-aware mode, the original packet color affects the traffic policing action. | - |
| **service-class** *class* | Specifies the class of service (CoS).   * Assured Forwarding (AF): applies to key data services that require guaranteed bandwidth and low delay. Provides forwarding quality assurance for the traffic that does not exceed the bandwidth limit, and lowers the CoS for the traffic that exceeds the bandwidth limit and forwards the traffic instead of discarding the traffic. * Best-Effort (BE): applies to best-effort services that do not require strict QoS guarantee. BE focuses only on reachability and does not have any requirements on other aspects. For example, traditional IP packet transmission is in BE mode. * Expedited Forwarding (EF): indicates the highest QoS on a DiffServ network. It is used for services with low packet loss rate, low delay, and high bandwidth. In any case, the information traffic can obtain a rate equal to or higher than the configured rate. * Class Selector (CS): indicates the class selection code. The CoS represented by CS is the same as that represented by IP Precedence. | The value can be af1, af2, af3, af4, be, cs6, cs7, or ef. |
| **color** *color* | Specifies the color corresponding to the CoS. | The value can be:   * red * green * yellow |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Flow-based traffic policing controls traffic that matches traffic classification rules and discards the excess traffic to limit traffic within a proper range and to protect network resources.When data is sent from a high-speed link to a low-speed link, the bandwidth on the interface of the low-speed link is insufficient. As a result, a large number of packets are discarded. To solve this problem, configure traffic policing for outgoing traffic on the interface of the high-speed link. The interface then discards the packets whose rate exceeds the traffic policing rate so that the outgoing traffic rate is limited within a proper range. You can also configure traffic policing for incoming traffic on the interface of the low-speed link. The interface then discards the received packets whose rate exceeds the traffic policing rate.Traffic policing based on traffic policies controls rates of packets of different types.

**Precautions**

* When a traffic policy containing traffic policing actions is applied, you do not need to run the **undo traffic-policy** command to unbind the traffic policy if you need to modify traffic policing parameters.
* It is recommended that the CIR be greater than 2 Mbit/s.
* If the class of service (CoS) of a packet is re-marked as EF, BE, CS6, or CS7, the packet can be re-marked only green.
* If you run this command multiple times in the same traffic behavior view, only the latest configuration takes effect.
* The relationships between CIR, PIR, CBS, and PBS in this command are as follows:
* It is recommended that the PIR be greater than the configured CIR.
* It is recommended that the CBS be greater than the configured CIR.
* It is recommended that the PBS be greater than the configured PIR.
* The following is recommended: PBS â¥ CBS = CIR/8 x (1-1.5) x 1000
* If a DiffServ domain is bound to the inbound interface, traffic policing is configured, and the CBS value and PBS value are set:
* If the color-blind mode is used in traffic policing, the packet color is determined by the packet color defined in traffic policing, regardless of the packet color defined in the DiffServ domain.
* If the color-aware mode is used in traffic policing and the two color marking rules conflict and take effect for the same packet, the packet color complies with the following rules:
* If the packet color defined in the DiffServ domain is green and that defined in traffic policing is yellow, the final packet color is yellow.
* If the packet color defined in the DiffServ domain is green and that defined in traffic policing is red, the final packet color is red.
* If the packet color defined in the DiffServ domain is yellow and that defined in traffic policing is green, the final packet color is yellow.
* If the packet color defined in the DiffServ domain is yellow and that defined in traffic policing is red, the final packet color is red.
* If the packet color defined in the DiffServ domain is red and that defined in traffic policing is green, the final packet color is red.
* If the packet color defined in the DiffServ domain is red and that defined in traffic policing is yellow, the final packet color is red.
* If a CoS is specified for packets with a specified color and the color corresponding to the CoS is specified, the final packet color is determined by the color corresponding to the CoS.


Example
-------

# Configure traffic policing in the traffic behavior b1 as follows: Set the CIR to 200000 kbit/s and the PIR to 2500000 kbit/s. Then apply the traffic policy p1 containing the traffic behavior to the inbound direction of 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match any
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] car cir 200000 kbps pir 2500000 kbps
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] traffic-policy p1 inbound

```