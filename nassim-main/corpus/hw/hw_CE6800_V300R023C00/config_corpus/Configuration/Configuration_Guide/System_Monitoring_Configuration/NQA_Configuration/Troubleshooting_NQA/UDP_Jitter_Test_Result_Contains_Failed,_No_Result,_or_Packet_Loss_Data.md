UDP Jitter Test Result Contains Failed, No Result, or Packet Loss Data
======================================================================

UDP Jitter Test Result Contains Failed, No Result, or Packet Loss Data

#### Fault Symptom

The [**display nqa results**](cmdqueryname=display+nqa+results) command output shows the following information:

* The value of **Completion** is **failed**.
* The value of **Completion** is **no result**.
* The value of **Lost packet ratio** is not **0%**.

![](../public_sys-resources/note_3.0-en-us.png) 

Unless otherwise specified, the following commands are run in the NQA test instance view.



#### Possible Causes

* The value of the statistical item **drop** in the UDP jitter test result is not 0.
* The value of the statistical item **busy** in the UDP jitter test result is not 0.
* The value of the statistical item **timeout** in the UDP jitter test result is not 0.
* TTL timeout occurs.
* The **frequency** parameter is incorrectly set.
* The **fail-percent** parameter is incorrectly set.

#### Procedure

1. Check whether the TTL value is configured for test packets in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * Ensure that the TTL value is 255. If the fault persists, go to step 2.
     ```
     [ttl](cmdqueryname=ttl) ttlValue
     ```
2. Check whether the **frequency** parameter is configured in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If so, compare the time required for a single NQA test (packet interval x number of packets sent in a single probe x number of probes in a test) with the NQA test execution interval (specified by **frequency**). If the time required for a single NQA test is longer than the NQA test execution interval, increase the value of **frequency** to ensure that the NQA test execution interval is longer than the time required for a single NQA test so that the test can properly end.
     ```
     [frequency](cmdqueryname=frequency) frequencyValue
     ```
   * If **frequency** is not configured or the fault persists after a proper value is configured, go to step 3.
3. Check whether the **fail-percent** parameter is configured in the NQA test instance view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If **fail-percent** is configured, cancel the configuration. If the fault persists after the configuration is cancelled, go to Step 4.
     ```
     [undo fail-percent](cmdqueryname=undo+fail-percent)
     ```
   * If **fail-percent** is not specified, go to Step 4.
4. Contact technical support and provide the following information:
   
   
   * Results of the preceding troubleshooting procedure
   * Configuration, log, and trap information
5. End.