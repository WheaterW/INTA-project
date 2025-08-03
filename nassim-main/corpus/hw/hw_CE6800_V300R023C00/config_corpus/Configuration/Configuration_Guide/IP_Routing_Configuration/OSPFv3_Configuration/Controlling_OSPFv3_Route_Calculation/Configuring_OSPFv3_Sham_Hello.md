Configuring OSPFv3 Sham Hello
=============================

Configuring OSPFv3 Sham Hello

#### Prerequisites

Before configuring OSPFv3 sham hello, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

With OSPFv3 sham hello configured, a device can maintain OSPFv3 neighbor relationships not only through Hello packets, but also through LSU and LSAck packets. This allows for agile detection of OSPFv3 neighbors and strengthens the stability of neighbor relationships.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure OSPFv3 sham hello.
   
   
   ```
   [sham-hello enable](cmdqueryname=sham-hello+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3)[ *process-id* ] command to check brief OSPFv3 information.