Starting a Test Instance
========================

After a test instance is started, test results are periodically recorded in files.

#### Context

Perform the following operations on the NQA client.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
   
   
   
   The NQA view is displayed.
3. Run [**test-type**](cmdqueryname=test-type) { **icmp** | **icmpjitter** | **jitter** | **udp** }
   
   
   
   A test instance type is set.
4. Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
   
   
   
   A destination address is configured.
5. (Optional) Run [**destination-port**](cmdqueryname=destination-port) *port-number*
   
   
   
   A destination port number is configured.
6. Run [**start**](cmdqueryname=start)
   
   
   
   An NQA test instance is started.
   
   
   
   An NQA test instance can be started immediately, at a specified time, or after a specified delay.
   
   * Run [**start**](cmdqueryname=start) **now** [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ]
     
     The test instance is started immediately.
   * Run [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ]
     
     The test instance is started at a specified time.
   * Run [**start**](cmdqueryname=start) **delay** { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ]
     
     The test instance is started after a specified delay.
   * Run [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** { *yyyy*/*mm*/*dd* | *yyyy-mm-dd* } ] [ **begin** { *yyyy*/*mm*/*dd* | *yyyy-mm-dd* } ]
     
     The test instance is started at a specified time every day.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.