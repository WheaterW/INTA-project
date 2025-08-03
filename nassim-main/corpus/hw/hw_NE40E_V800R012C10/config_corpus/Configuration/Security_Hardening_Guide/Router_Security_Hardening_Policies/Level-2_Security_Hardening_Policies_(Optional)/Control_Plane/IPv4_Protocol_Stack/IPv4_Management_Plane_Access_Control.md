IPv4 Management Plane Access Control
====================================

IPv4 Management Plane Access Control

#### Security Policy

Management Plane Access Control (MPAC) enhances system security by protecting devices against Denial of Service (DoS) attacks.

In a common deployment scenario, the Router may run multiple services at the same time, such as Layer 2 services MSTP, RRPP, routing services OSPF and BGP, MPLS services LDP and RSVP, system services, and diagnostic functions ping and tracert.

This enables attackers to send various attack packets to the Router. Unless protective features such as MPAC are enabled, the Router sends packets destined for its interfaces (including the loopback interface) directly to the CPU without any filtering. As a result, CPU and system resources are wasted and the system comes under DoS attacks.

To prevent such attacks, define an MPAC policy to filter packets.

The NE40E supports definitions of MPAC policies that can be applied to sub-interfaces, to interfaces, or globally on the NE40E.

After you define the rules for an MPAC policy, the device filters packets destined for the CPU If no such policy is defined, the CPU remains vulnerable to attacks.


#### Attack Methods

To prevent an attacker from sending various types of TCP/IP attack packets to paralyze Device A, MPAC is deployed on Device A, as shown in [Figure 1](#EN-US_CONCEPT_0000001134623476__fig_dc_vrp_sec_maintenance_009701).

**Figure 1** MPAC networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is GE 0/1/0.


  
![](figure/en-us_image_0000001180503163.png)

#### Configuration and Maintenance Methods

Configure IPv4 MPAC on Device A.

```
<DeviceA> system-view
```
```
[~DeviceA] service-security policy ipv4 test
```
```
[*DeviceA-service-sec-test] rule 10 deny protocol ip source-ip 10.10.1.1 0
```
```
[*DeviceA-service-sec-test] step 10
```
```
[*DeviceA-service-sec-test] description rule 10 is deny ip packet which from 10.10.1.1
```
```
[*DeviceA-service-sec-test] commit
```
```
[~DeviceA-service-sec-test] quit
```
```
[~DeviceA] service-security global-binding ipv4 test
```
```
[*DeviceA] commit
```
```
[~DeviceA] interface gigabitethernet 0/1/0
```
```
[~DeviceA-GigabitEthernet0/1/0] service-security binding ipv4 test
```
```
[*DeviceA-GigabitEthernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

None.


#### Verifying the Security Hardening Result

* Run the **display service-security policy** **ipv4** [ *security-policy-name* [ **slot** *slot-id* ] ] command to check information about all MPAC policies on the device.
* Run the **display service-security binding** **ipv4** [ **interface** *interface-type* *interface-number* [ **slot** *slot-id* ] ] command to check information about MPAC policies on interfaces.
* Run the **display service-security statistics** **ipv4** [ *security-policy-name* ] command to check statistics that matched MPAC policies.