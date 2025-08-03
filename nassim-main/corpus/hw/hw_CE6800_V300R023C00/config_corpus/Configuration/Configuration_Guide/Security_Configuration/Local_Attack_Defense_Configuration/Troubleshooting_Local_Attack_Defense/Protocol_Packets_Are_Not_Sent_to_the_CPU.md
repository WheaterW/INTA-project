Protocol Packets Are Not Sent to the CPU
========================================

Protocol Packets Are Not Sent to the CPU

#### Fault Symptom

Protocol packets are not sent to the CPU after CPU attack defense is configured.


#### Possible Causes

Possible causes are as follows:

* A deny rule is configured to discard specified protocol packets to be sent to the CPU.
* The CPU is attacked by illegitimate packets.


#### Procedure

1. Check whether a deny rule has been configured to discard specified protocol packets to be sent to the CPU.
   1. Run the **display current-configuration** command in the system view to check the configured attack defense policy.
   2. Run the [**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy) [ *policy-name* ] command to check whether the deny rule is configured in the attack defense policy for the protocol packets to be sent to the CPU.
      
      If so, run the [**car**](cmdqueryname=car) command in the attack defense policy view to set the rate limit for the protocol packets sent to the CPU.
      
      If not, go to the next step.
2. Check statistics on the packets sent to the CPU.
   
   Run the [**display cpu-defend statistics**](cmdqueryname=display+cpu-defend+statistics) command to check statistics on the packets sent to the CPU. If a large number of protocol packets are discarded, check whether these are attack packets (identified using the attack source tracing function, for example). If so, use a filter or traffic policy to prevent such packets from being sent to the CPU.