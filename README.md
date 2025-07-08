# Document Access Control Demo

This project demonstrates a chatbot application that enforces document access control using Oso Cloud authorization. The chatbot allows users to query documents while respecting their access permissions based on their role and department.

## Features

- Role-based access control (Manager, Member)
- Department-based document access
- Document similarity search using embeddings
- Interactive chat interface
- Public document access

## Prerequisites

- Python 3.12+
- PostgreSQL database with pgvector extension
- Oso Cloud account
- OpenAI API key

## Setup

1. Clone this repository

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:
   ```
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   OSO_URL=https://cloud.osohq.com
   OSO_API_KEY=your_api_key # make sure you use an environment without an active policy
   OPENAI_API_KEY=your_openai_key
   ```

4. Initialize the database:
   ```bash
   python main.py
   ```

## Usage

Run the chatbot:
   ```bash
   python main.py
   ```

The chatbot will display a list of available users and their roles. Select a user by entering their name.

You can then:
- Enter prompts to query documents the user has access to
- Type "set_user" to switch to a different user
- Type "exit" to quit

## Access Control Rules

- Managers can read all documents in their department
- Members can only read documents they created
- All users can read public documents

Example users:
- Jane (Engineering Manager)
- Jerry (Engineering Member) 
- George (HR Manager)
- Karen (HR Member)

## Example Queries

Try these queries with different users to see how access control works:

- "What project is Jerry working on?"
- "Are Jerry and Karen dating?"
- "When is George's birthday?" (Public document)
- "How old is Karen?"

The responses will vary based on the user's permissions.