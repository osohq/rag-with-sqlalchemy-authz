Current sprint
x Define schema
x Define authz

x Psuedo-code app
x get writes, models and tests working with SQLite
x Set up Postgres (docker)
x Set up vector
x Modfiy database manager
x Test semantic search

x Publish policy
x Insert facts
x Configure local authorization
x Get local authz working

- Reach parity with Neon
  - Get models, tests working with Neon
    - Project setup
    - Branch and data seeding
    - Test semantic search

- Set up and tear down for Oso Cloud
- Write demo situations

- Integrate Oso SQLAlchemy adapter
- Refactor for readability and simplicity

- Set up docker


functions:
- run_demo()
- setup_db(openai) -> db
- setup_oso(db) -> oso
- run_query(db, prompt, user_id) -> result
- print_results(results)


**Output**

A command line interface where the user selects an identity and can issue queries that return authorized responses.

**Tools**

- Python
- Postgres and pgvector
- Oso SQLAlchemy Integration
- Docker

JS demo structure

- authorization
    
    data.yaml: local authz query mapping
    
    policy.polar: policy
    
- data
    
    facts.js: facts for app to insert into Oso
    
- primsa
    schema.prisma: models

- supabase
    seed.sql: DDL and initial inserts
    config.toml: DB configuration
    - migrations

app.js: import getAuthzFilter, getAuthzBlocks, and generatEmbedding, generateChatbotResponse
- handlePrompt: takes user, prompt and threshold, generates embedding, gets filter, passes to getAuthorizedBlocks
cli.js: component that handles user input
- askQuestionsAndRespond(user) {}
- async function start()
- init CLI, defines methods that call start and initialize
data.js: functions for I/O to database
- getAuthorizedBlocks(promptEmbedding, authorizationFilter, threshold) -> Authorized Blocks
- addVectorEmbeddings(): inserts vector embeddings

llm.js: create OpenAI client
- generateEmbedding(prompt)
- generateChatbotResponse