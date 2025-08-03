(Optional) Configuring Whitelist Session-CAR for gRPC
=====================================================

You can modify bandwidth parameters of whitelist session-CAR for gRPC to properly allocate bandwidth resources for sessions.

#### Procedure

1. Run **[**system-view**](cmdqueryname=system-view)**
   
   
   
   The system view is displayed.
2. Run **[**grpc**](cmdqueryname=grpc)**
   
   
   
   The gRPC view is displayed.
3. Run [**whitelist session-car grpc**](cmdqueryname=whitelist+session-car+grpc) { **cir** *sessionCarCir* | **cbs** *sessionCarCbs* | **pir** *sessionCarPir* | **pbs** *sessionCarPbs* } \*
   
   
   
   Whitelist session-CAR bandwidth parameters are set for gRPC.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring whitelist session-CAR for gRPC, you can verify the configuration.

* For IPv4:
  
  Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **grpc** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for gRPC on a specified interface board.
  
  To view new statistics, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **grpc** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for gRPC on a specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **grpc** **statistics** **slot** *slot-id* command.
* For IPv6:
  
  Run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **grpcv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for gRPC on a specified interface board.
  
  To view new statistics, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **grpcv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for gRPC on a specified interface board, and then run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **grpcv6** **statistics** **slot** *slot-id* command.