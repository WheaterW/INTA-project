Configuring OSPFv3 Delay Advertisement
======================================

With OSPFv3 delay advertisement, intra-domain link delay information can be collected and flooded.

#### Usage Scenario

Traditional path computation algorithms compute the optimal path to a destination address based on costs. However, the path computed in this way may not have the minimum delay. For services that have stringent requirements on delay, path computation can be performed based on the delay rather than on the cost to ensure that service traffic is transmitted along the path with the minimum delay. After OSPFv3 delay advertisement is configured, OSPFv3 collects and floods intra-domain link delay information and reports the information to the controller through BGP-LS. The controller then computes paths on the P2P network based on delay constraints.


#### Pre-configuration Tasks

Before configuring delay advertisement, configure TWAMP Light to detect delay information. The configuration is as follows:

* Configure the TWAMP Light controller function on the local end.
  1. Configure the TWAMP Light client function, and create a test session.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**nqa twamp-light**](cmdqueryname=nqa+twamp-light)
        
        The TWAMP Light view is displayed.
     3. Run [**client**](cmdqueryname=client)
        
        The TWAMP Light client function is enabled, and the TWAMP Light client view is displayed.
     4. Run [**test-session**](cmdqueryname=test-session) *session-id* [**sender-ipv6**](cmdqueryname=sender-ipv6) *sender-address-v6* [**reflector-ipv6**](cmdqueryname=reflector-ipv6) *reflector-address-v6* **sender-port** *sender-port* **reflector-port** *reflector-port* [ **dscp** *dscp-value* | **padding** *padding-length* | **padding-type** *padding-type* | **description** *description* ] \*
        
        A test session is created on the initiator.
     5. Run [**quit**](cmdqueryname=quit)
        
        Return to the TWAMP Light view.
  2. Configure the TWAMP Light Sender and start the TWAMP Light performance test.
     1. Run [**sender**](cmdqueryname=sender)
        
        The TWAMP Light Sender function is enabled, and the TWAMP Light Sender view is displayed.
     2. Run [**test start-continual**](cmdqueryname=test+start-continual) **test-session** *session-id* [ **period** { **10** | **100** | **1000** | **30000** } ] [ **time-out** *time-out* ]
        
        Continual measurement is started.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
* Configure the TWAMP Light Responder on the peer end.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nqa twamp-light**](cmdqueryname=nqa+twamp-light)
     
     The TWAMP Light view is displayed.
  3. Run [**responder**](cmdqueryname=responder)
     
     The TWAMP Light Responder function is enabled, and the TWAMP Light Responder view is displayed.
  4. Run [**test-session**](cmdqueryname=test-session) *session-id* [**local-ipv6**](cmdqueryname=local-ipv6) *local-ipv6-address* [**remote-ipv6**](cmdqueryname=remote-ipv6) *remote-ipv6-address* **local-port** *local-port* **remote-port** *remote-port* **interface** { *interface-type* *interface-number* | *interface-name* } [ **anti-loop-on** ] [ **description** *description* ]
     
     A test session is created on the reflector.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

For details about how to configure TWAMP Light, see [TWAMP Light](dc_vrp_cfg_twamp-light_0001.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   An OSPFv3 process is created, and the OSPFv3 view is displayed.
   
   
   
   *process-id* specifies an OSPFv3 process. If *process-id* is not specified, the default process ID 1 is used.
3. Run [**router-id**](cmdqueryname=router-id) *router-id*
   
   
   
   A router ID is configured.
   
   
   
   A router ID uniquely identifies an OSPFv3 process in an AS. If no router ID is configured, the OSPFv3 process cannot run.
4. Run **[**metric-delay**](cmdqueryname=metric-delay)**[ **average** | **variation** ] **advertisement enable**
   
   
   
   OSPFv3 delay advertisement is configured.
5. (Optional) Run [**metric-delay normalize**](cmdqueryname=metric-delay+normalize) **interval** *interval-value* [ **offset** *offset-value* ]
   
   
   
   The link delay tolerance in the OSPFv3 process is configured.
   
   
   
   For the delay-based path computation algorithm, the delay differences of links are different, and the differences may be small. However, even if the delay differences are small, only one optimal path can be generated according to the existing SPF algorithm, and load balancing cannot be implemented within a certain delay tolerance range. As a result, link resources on the network cannot be fully utilized. To resolve this problem to the greatest extent, normalization processing may be performed on the link delays with a small difference or a difference within an acceptable range so that load balancing can be implemented and link resources on the network can be fully utilized.
6. (Optional) Run [**metric-delay suppress**](cmdqueryname=metric-delay+suppress) **timer** **timer-value** ****percent-threshold**** **percent-value** ****absolute-threshold**** **absolute-value**
   
   
   
   Delay advertisement suppression is configured.
   
   
   
   If delay variation occurs frequently, the delay-based route calculation changes frequently. As a result, routing information is flooded and reported repeatedly. In this case, you can configure this function to suppress delay advertisement.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the **display ospfv3 traffic-eng** command to check the delay information advertised by OSPFv3.