Configuring the CPCAR Value
===========================

Configuring the CPCAR Value

#### Context

To reduce the total number of packets reaching the CPU, and to mitigate the impact that different types of packets have on one another in order to protect the CPU, the device can rate-limit packets to be sent to the CPU at different levels. This includes CPCAR based on protocol packets, rate limiting on all packets sent to the CPU, and rate limiting based on protocol association.

* Rate limiting based on protocol association has the highest priority and therefore takes precedence over CPCAR based on protocol packets as well as rate limiting on all protocol packets sent to the CPU.
* If only CPCAR based on protocol packets and rate limiting on all protocol packets sent to the CPU are configured, the device rate-limits packets based on the smaller value of the two.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an attack defense policy and enter the attack defense policy view.
   
   
   ```
   [cpu-defend policy](cmdqueryname=cpu-defend+policy) policy-name
   ```
3. Configure the method used to rate-limit packets sent to the CPU.
   
   
   * Set a CPCAR value for protocol packets of a specified type.
     ```
     [car packet-type](cmdqueryname=car+packet-type) packet-type pps pps-value
     ```
   * Set a CPCAR value for all packets sent to the CPU.
     ```
     [car all-packets](cmdqueryname=car+all-packets) pps pps-value
     ```
   * Configure rate limiting based on protocol association.
     1. Enable protocol association.
        ```
        [application-apperceive](cmdqueryname=application-apperceive) { bgp | bgp4plus | isis | ftp | ssh | telnet | tftp | ospf | ospfv3  | m-lag | m-lag-sync } enable
        ```
        
        The CE6885-LL in low latency mode does not support bgp4plus or ospfv3.
     2. Set a CPCAR value for packets of a specific protocol upon the establishment of the protocol connection.
        ```
        [linkup-car](cmdqueryname=linkup-car) packet-type { bgp | bgp4plus | isis | ftp | ssh | telnet | tftp | m-lag | m-lag-sync | ospf | ospfv3  } pps pps-value
        ```
        
        The CE6885-LL in low latency mode does not support bgp4plus or ospfv3.
     3. Configure the penalty ratio threshold for protocol association.
        ```
        [linkup session anti-attack ratio-threshold](cmdqueryname=linkup+session+anti-attack+ratio-threshold) rate-value-percent 
        ```
        
        By default, the threshold is 50%.
4. (Optional) Configure the device to discard packets to be sent to the CPU. 
   
   
   ```
   deny packet-type packet-type
   ```
   
   By default, the device does not discard the packets to be sent to the CPU.
5. (Optional) Configure the description of the attack defense policy.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   By default, no description is configured for an attack defense policy.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Apply the attack defense policy.
   
   
   * Configure attack defense policies in batches.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name batch slot { start-slot [ to end-slot ] } &<1-12>
     ```
   * Configure an attack defense policy separately.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name [ slot slot-id ]
     ```
   
   After an attack defense policy is created, you must apply the policy in the system view. Otherwise, the policy does not take effect.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```