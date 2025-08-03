SRv6 Trusted Domain
===================

SRv6 Trusted Domain

#### Security Policy

SRv6 forwards IPv6 data packets on a network based on source routing. It inherits the security risks of source routing, IPv6 security risks, and SDN risks caused by centralized management and control, and also faces a series of attacks initiated when attackers modify packet headers to manipulate traffic paths. As such, SRv6 divides the network into a trusted domain and an untrusted network outside the domain. Traffic filtering is performed on the edge nodes of the trusted domain to prevent attackers from sending attack packets to nodes in the trusted domain by means of packet forging.

The SRv6 trusted domain is defined according to the following security requirements:

1. A clear border is defined for the SRv6 trusted domain to distinguish networks inside and outside the SRv6 trusted domain.
2. Traffic filtering is performed on the edge nodes of the SRv6 trusted domain in order to discard packets whose source or destination addresses are in the SID range of the SRv6 trusted domain.
3. Nodes in the SRv6 trusted domain discard packets whose destination addresses are local SIDs and source addresses are not within the SRv6 trusted domain.

#### Configuration and Maintenance Methods

SRv6 improves security by filtering traffic on the edge nodes of the SRv6 trusted domain and discarding packets that do not meet the preceding security requirements.

1. Configure ACL6 policies on the edge nodes of the SRv6 trusted domain in order to discard packets whose destination addresses are in the SID range of the SRv6 trusted domain.
   ```
   <HUAWEI> system-view
   [~HUAWEI] acl ipv6-pool srv6_deny_destination_address
   [*HUAWEI-acl-ipv6-pool-srv6_deny_destination_address] ipv6 address 2001:DB8:: 32
   [*HUAWEI-acl-ipv6-pool-srv6_deny_destination_address] quit
   [*HUAWEI] acl ipv6-pool srv6_deny_source_address
   [*HUAWEI-acl-ipv6-pool-srv6_deny_source_address] ipv6 address 2001:DB8:: 32
   [*HUAWEI-acl-ipv6-pool-srv6_deny_source_address] quit
   [*HUAWEI] acl ipv6 3200
   [*HUAWEI-acl6-advance-3200] rule 10 deny ipv6 source-pool srv6_deny_source_address destination-pool srv6_deny_destination_address
   [*HUAWEI-acl6-advance-3200] quit
   [*HUAWEI] commit
   ```
2. Configure a traffic policy.
   ```
   [~HUAWEI] traffic classifier tcSrv6TrustDomain operator or 
   [*HUAWEI-classifier-tcSrv6TrustDomain] if-match ipv6 acl 3200
   [*HUAWEI-classifier-tcSrv6TrustDomain] quit
   [*HUAWEI] traffic behavior tbSrv6TrustDomain 
   [*HUAWEI-behavior-tbSrv6TrustDomain] quit
   [*HUAWEI] traffic policy tpSrv6TrustDomain 
   [*HUAWEI-trafficpolicy-tpSrv6TrustDomain] share-mode 
   [*HUAWEI-trafficpolicy-tpSrv6TrustDomain] statistics enable 
   [*HUAWEI-trafficpolicy-tpSrv6TrustDomain] classifier tcSrv6TrustDomain behavior tbSrv6TrustDomain precedence 1 
   [*HUAWEI-trafficpolicy-tpSrv6TrustDomain] quit
   [*HUAWEI] commit
   ```
3. Apply the traffic policy to the inbound direction of the upstream interface.
   ```
   [*HUAWEI] interface GigabitEthernet1/0/0 
   [*HUAWEI-GigabitEthernet1/0/0] undo shutdown 
   [*HUAWEI-GigabitEthernet1/0/0] traffic-policy tpSrv6TrustDomain inbound
   [*HUAWEI-GigabitEthernet1/0/0] quit
   [*HUAWEI] commit
   ```

#### Checking the Security Hardening Result

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **acl-ipv6-pool** command to check the configured IPv6 address pool.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **acl6-adv** command to check the global ACL6 configuration.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **segment-routing-ipv6** command to check SRv6 configurations.
* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check interface traffic information.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) **interface** *interface-type* *interface-number* [ .*sub-interface* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics about the specified interface.