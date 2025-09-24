Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

# Models
```
models/
├── staging/        # Empty/minimal transformation, raw source ingestion
│   ├── sources.yml
│   ├── stg_customers.sql
│   ├── stg_orders.sql
│   └── stg_transactions.sql
│
├── warehouse/            # Snowflake schema, normalized EDW
│   │   ├── edw_customers.sql
│   │   ├── edw_accounts.sql
│   │   └── edw_transactions.sql
│
└── mart/           # Star schema (fact & dimension tables)
    ├── dim_customers.sql
    ├── dim_accounts.sql
    └── fact_transactions.sql
```