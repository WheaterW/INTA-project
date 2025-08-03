Configuring OSPF Sham Hello
===========================

Configuring OSPF Sham Hello

#### Prerequisites

Before configuring OSPF sham hello, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

With OSPF sham hello configured, a device can maintain OSPF neighbor relationships not only through Hello packets, but also through LSU and LSAck packets. This allows for agile detection of OSPF neighbors and improves the stability of neighbor relationships.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Configure OSPF sham hello.
   
   
   ```
   [sham-hello enable](cmdqueryname=sham-hello+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf)[ *process-id* ] **brief** command to check brief OSPF information.