Configuring OSPF Delay Advertisement
====================================

With OSPF delay advertisement, intra-domain link delay information can be collected and flooded.

#### Usage Scenario

Traditional path computation algorithms compute the optimal path to a destination address based on costs. However, the path computed in this way may not have the minimum delay. For services that have stringent requirements on delay, path computation can be performed based on the delay rather than on the cost to ensure that service traffic is transmitted along the path with the minimum delay. After OSPF delay advertisement is configured, OSPF collects and floods intra-domain link delay information and reports the information to the controller through BGP-LS. The controller then computes paths on the P2P network based on delay constraints.


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
     4. Run [**test-session**](cmdqueryname=test-session) *session-id* **sender-ip** *sender-ip-address* **reflector-ip** *reflector-ip-address* **sender-port** *sender-port* **reflector-port** *reflector-port* [ **dscp** *dscp-value* | **padding** *padding-length* | **padding-type** *padding-type* | **description** *description* ] \*
        
        A measurement session is created on the initiator.
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
  4. Run [**test-session**](cmdqueryname=test-session) *session-id* **local-ip** *local-ip-address* **remote-ip** *remote-ip-address* **local-port** *local-port* **remote-port** *remote-port* **interface** { *interface-type* *interface-number* | *interface-name* } [ **anti-loop-on** ] [ **description** *description* ]
     
     A measurement session is created on the responder.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

For details about how to configure TWAMP Light, see [TWAMP Light](dc_vrp_cfg_twamp-light_0001.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   An OSPF process is created, and the OSPF view is displayed.
   
   
   
   *process-id* specifies an OSPF process. If the *process-id* parameter is not specified, the system creates process 1 by default.
3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
   
   
   
   The Opaque capability is enabled on the device.
4. Run **[**metric-delay**](cmdqueryname=metric-delay)**[ **average** | **variation** ] **advertisement enable**
   
   
   
   Delay advertisement is enabled.
5. (Optional) Run [**metric-delay normalize**](cmdqueryname=metric-delay+normalize) **interval** *interval-value* [ **offset** *offset-value* ]
   
   
   
   The link delay normalization function is configured for the OSPF process.
   
   
   
   For the delay-based path computation algorithm, the delay differences of links are different, and the differences may be small. However, even if the delay differences are small, only one optimal path can be generated according to the existing SPF algorithm, and load balancing cannot be implemented within a certain delay tolerance range. As a result, link resources on the network cannot be fully utilized. To resolve this problem to the greatest extent, normalization processing may be performed on the link delays with a small difference or a difference within an acceptable range so that load balancing can be implemented and link resources on the network can be fully utilized.
6. (Optional) Run **[**metric-delay suppress**](cmdqueryname=metric-delay+suppress)** **timer** **time-value** ****percent-threshold**** **percent-value** ****absolute-threshold**** **absolute-value**
   
   
   
   The delay advertisement suppression function is configured.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the **[**display ospf interface**](cmdqueryname=display+ospf+interface) **verbose**** command to view information about OSPF-enabled interfaces.