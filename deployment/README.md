# Production edge configuration

Terminate TLS at either an AWS Application Load Balancer or Nginx.  In both
cases, listen publicly only on HTTPS and redirect HTTP with a permanent 301.

For an EC2 Nginx deployment, adapt `nginx/eehook-api.conf.example`, install a
valid certificate (for example, Certbot), and proxy only to Gunicorn on
`127.0.0.1:8000`.  Do not expose Gunicorn's port in the EC2 security group.

For an ALB deployment, configure an HTTP:80 listener whose only action is a
redirect to HTTPS:443; configure the HTTPS listener to forward to a private
target group.  The load balancer must overwrite `X-Forwarded-Proto` with
`https`.  Keep the instance security group limited to the ALB security group.

Set `STOREFRONT_ORIGINS` to every exact HTTPS browser origin allowed to send
credentialed requests. This must include the deployed dashboard origin
(`https://eehook-frondent-web.vercel.app`) as well as any custom storefront
domains. For a same-origin storefront `/api` proxy, keep
`JWT_COOKIE_SAMESITE=Lax`; only use `None` when the browser calls a genuinely
cross-site API origin directly.

The current storefront is catalogue-only and sends enquiries to WhatsApp. Set
`ENABLE_CUSTOMER_COMMERCE=False` in the AWS environment so unused customer
registration, cart, wishlist, checkout, profile, and order-history routes are
not exposed. Keep it enabled only for local legacy checkout testing or a
future checkout rollout.
