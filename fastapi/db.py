# Initializes database tables on startup
CREATE_TABLES_SQL = [
    """
    CREATE TABLE IF NOT EXISTS repositories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL UNIQUE,
        description TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS branches (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        repo_id INTEGER REFERENCES repositories(id) ON DELETE CASCADE,
        UNIQUE (repo_id, name)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS issues (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        repo_id INTEGER REFERENCES repositories(id) ON DELETE CASCADE,
        branch_id INTEGER REFERENCES branches(id) ON DELETE SET NULL,
        status VARCHAR(50) DEFAULT 'open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS user_issues (
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        issue_id INTEGER REFERENCES issues(id) ON DELETE CASCADE,
        assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, issue_id)
    );
    """
]