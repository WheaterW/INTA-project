Configuring an Upper Rate Limit for Multicast Traffic on a Board
================================================================

To prevent multicast traffic bursts from resulting in multicast packet loss, set an upper rate limit for multicast traffic on a specified board.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**multicast shaping**](cmdqueryname=multicast+shaping) *shaping-value*
   
   
   
   An upper rate limit is configured for multicast traffic on the board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.