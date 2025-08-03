Verifying the MPAC Configuration
================================

After configuring the Management Plane Access Control (MPAC)
policy, check the configurations.

#### Prerequisites

An MPAC policy has been configured.


#### Procedure

* Run the [**display service-security policy**](cmdqueryname=display+service-security+policy) { **ipv4** | **ipv6** } [ *security-policy-name* [ **slot** *slot-id* ] ] command to check information about all MPAC
  policies.
* Run the [**display service-security binding**](cmdqueryname=display+service-security+binding) { **ipv4** | **ipv6** } [ **interface** *interface-type* *interface-number* [ **slot** *slot-id* ] ] command to
  check information about MPAC policies on interfaces.
* Run the [**display service-security statistics**](cmdqueryname=display+service-security+statistics) { **ipv4** | **ipv6** } [ *security-policy-name* ] command to check statistics about
  all matched MPAC rules.