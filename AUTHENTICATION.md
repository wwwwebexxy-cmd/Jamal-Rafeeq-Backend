# Authentication and deployment

The public Jamal Rafeeq storefront is catalogue-only. Customers browse
products and send WhatsApp enquiries; the public UI does not provide customer
registration, Google login, password reset, cart, checkout, wishlist, profile,
or order-history flows.

The protected Super Admin dashboard still uses the existing email/password
login and HttpOnly JWT cookies:

- `POST /login/` with `login_type=super_admin`
- `GET /auth/session/` to restore the dashboard session
- `POST /logout/` to clear the session cookies
- `POST /token/refresh/` to rotate the access cookie

For the AWS deployment, set:

```dotenv
DEBUG=False
ENABLE_CUSTOMER_COMMERCE=False
STOREFRONT_ORIGINS=https://your-storefront.example
SITE_URL=https://your-storefront.example
```

With `ENABLE_CUSTOMER_COMMERCE=False`, legacy customer account, cart,
wishlist, checkout, profile, order-history, coupon, and welcome-bonus routes
are not added to Django's URL table. Their database models and migrations are
kept temporarily so existing data and the admin workspace remain safe; remove
those tables only as a separate, approved data migration after confirming that
no historical records are required.

Google OAuth, SMTP password reset, Stripe checkout, and the related environment
variables are only needed if the legacy customer-commerce flag is enabled for
a future rollout. They are not required by the current catalogue + WhatsApp
storefront deployment.

Never commit the Django secret key, database password, Google credentials,
SMTP app password, Stripe keys, or JWT values.
