Resetting the RSVP Process
==========================

Resetting the RSVP process triggers a node to re-establish all RSVP CR-LSPs or verify the RSVP process.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting the RSVP process causes all RSVP CR-LSPs to be torn down and re-established.



#### Procedure

1. In the user view, run [**reset mpls rsvp-te**](cmdqueryname=reset+mpls+rsvp-te) [ **lsp-id** *lspId-value* ] [ **tunnel-id** *tunnelId-value* ] [ **ingress-id** *ingressId-value* ] [ **egress-id** *egressId-value* ] [ **name** *name-value* ]
   
   
   
   The RSVP-TE process is restarted.