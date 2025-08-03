Maintaining MQC
===============

Maintaining MQC

#### Context

Before re-collecting statistics on packets matching a traffic policy, clear all existing statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

Traffic statistics cannot be restored after being cleared. Exercise caution when you use this command.



#### Procedure

* Clear statistics on packets matching a traffic policy.
  
  
  
  For the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, and CE6885-SAN:
  
  ```
  [reset traffic-policy statistics](cmdqueryname=reset+traffic-policy+statistics) { global [ slot slot-id ] | interface { interface-type interface-number | interface-name } | vlan vlan-id | vpn-instance vpn-instance-name | qos group group-id | bridge-domain bd-id } [ policy-name ] [ inbound | outbound ] [ classifier-base classifier-name ] [ history ] 
  ```
  
  For the CE6820H, CE6820H-K, and CE6820S:
  
  ```
  [reset traffic-policy statistics](cmdqueryname=reset+traffic-policy+statistics) { global [ slot slot-id ] | interface { interface-type interface-number | interface-name } | vlan vlan-id | vpn-instance vpn-instance-name | qos group group-id } [ policy-name ] [ inbound | outbound ] [ classifier-base classifier-name ] [ history ] 
  ```
  
  For the CE6885-LL (low latency mode):
  
  ```
  [reset traffic-policy statistics](cmdqueryname=reset+traffic-policy+statistics) { global [ slot slot-id ] | interface { interface-type interface-number | interface-name } | vlan vlan-id | vpn-instance vpn-instance-name | qos group group-id } [ policy-name ] [ inbound ] [ classifier-base classifier-name ] [ history ] 
  ```