(Optional) Configuring Accounting Packet Merging for Value-added Services
=========================================================================

This section describes how to configure accounting packet merging for value-added services to reduce the number of packets sent to a RADIUS accounting server.

#### Context

When a large number of users go online and each user applies for many value-added services, a large number of accounting packets are generated. The processing capability of a RADIUS accounting server is limited. To prevent the number of accounting packets from exceeding the processing capability of a RADIUS accounting server, the number of accounting packets sent by a device to a RADIUS accounting server must be reduced to relieve the pressure on the RADIUS accounting server.


#### Procedure

1. Enable accounting packet merging for value-added services.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain view is displayed.
   4. Run [**value-added-service accounting-merge**](cmdqueryname=value-added-service+accounting-merge) **edsg** { **stop** | **interim** **interval** *interval* [ **hash** ] }
      
      
      
      Accounting packet merging is enabled for value-added services.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. (Optional) Set the maximum length of a post-merging accounting packet for value-added services.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      
      
      The RADIUS server group view is displayed.
   3. Run [**radius-server accounting-merge max-length**](cmdqueryname=radius-server+accounting-merge+max-length) *length*
      
      
      
      The maximum length is set for a post-merging accounting packet for value-added services.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Enable a post-merging accounting packet that fails to be sent for value-added services to enter the accounting packet cache.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**value-added-service accounting-merge cache enable**](cmdqueryname=value-added-service+accounting-merge+cache+enable)
      
      
      
      A post-merging accounting packet that fails to be sent for value-added services is enabled to enter the accounting packet cache.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.