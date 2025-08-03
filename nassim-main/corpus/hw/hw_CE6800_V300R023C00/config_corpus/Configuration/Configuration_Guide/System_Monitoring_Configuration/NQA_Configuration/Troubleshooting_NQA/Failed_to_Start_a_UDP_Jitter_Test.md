Failed to Start a UDP Jitter Test
=================================

Failed to Start a UDP Jitter Test

#### Fault Symptom

A UDP jitter test cannot be started.

![](../public_sys-resources/note_3.0-en-us.png) 

Unless otherwise specified, the commands provided in "Procedure" are run in the NQA test instance view.



#### Possible Causes

Mandatory parameters of the NQA test instance are incorrectly configured.


#### Procedure

1. Check whether the type of the test instance type is UDP jitter in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If so, go to step 2.
   * If not, set the test instance type to jitter.
     ```
     [test-type](cmdqueryname=test-type) jitter
     ```
     + If the fault is rectified, go to step 5.
     + If the fault persists, go to step 2.
2. Check whether a destination IP address is configured in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If so, go to step 3.
   * If not, configure a destination IP address.
     ```
     [destination-address](cmdqueryname=destination-address) ipv4 destAddress
     ```
     + If the fault is rectified, go to step 5.
     + If the fault persists, go to step 3.
3. Check whether a destination port number is configured in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If so, go to step 4.
   * If not, configure a destination port number.
     ```
     [destination-port](cmdqueryname=destination-port) port-number
     ```
     + If the fault is rectified, go to step 5.
     + If the fault persists, go to step 4.
4. Contact technical support and provide the following information:
   
   
   * Results of the preceding troubleshooting procedure
   * Configuration, log, and trap information
5. End.